
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor, Utils):  
    global_envi = [] 
    classMap = {}
    constFlag = False
    classFlag = "-None-"
    methodFlag = "-None-"
    inLoop = 0
    hasMain = False
    
    def __init__(self,ast):
        self.classMap = {}
        self.constFlag = False
        self.class_Flag = "-None-"
        self.methodFlag = "-None-"
        self.inLoop = 0
        self.hasMain = False
        self.ast = ast

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)
    
    def searchTheFamily(self, starter, claimed):
        if self.classMap[starter[1:]]["-parent"] == 'None':
            return False
        if claimed[1:] == self.classMap[starter[1:]]["-parent"]:
            return True
        else:
            self.searchTheFamily("-" + self.classMap[starter]["-parent"], claimed)
    
    def compareType(self, left, right):
        if len(left) == 1 and len(right) == 1:
            if left[0][0] == "-" and right[0][0] == "-":
                if left == right: return True
                return self.searchTheFamily(right[0], left[0])
            elif left == right:
                return True
            else:
                if left[0] == 'Float' and right[0] == 'Int':
                    return True
                return False
        elif len(left) == len(right):
            left_arr = left[:-1]
            right_arr = right[:-1]
            if left_arr == right_arr and self.compareType([left[-1]], [right[-1]]):
                return True
            return False
        else:
            return False
    
    def searchId(self, ctx, o): 
        local_scope = o[:-2]
        for i in local_scope:
            if ctx.name in i:
                return i[ctx.name]['type'], i[ctx.name]['var']
        return None, None
    
    # Class Scope
    def visitProgram(self, ctx, o): 
        #print(str(ctx.decl[0]))
        o = []
        for decl_i in ctx.decl:
            self.visit(decl_i, o)
            self.class_Flag = "-None-"
        if not self.hasMain:
            raise NoEntryPoint()
        # print(self.classMap)
        return []
        
    def visitClassDecl(self, ctx, o): 
        name = (ctx.classname.name)
        if name in self.classMap.keys():
            raise Redeclared(Class(), name)
        self.class_Flag = (name)
        #print(self.class_Flag)
        self.classMap[name] = {}
        if ctx.parentname is not None:
            if ctx.parentname.name not in self.classMap.keys():
                raise Undeclared(Class(), ctx.parentname.name)
            o = [self.classMap[ctx.parentname.name]] + o
            self.classMap[name]["-parent"] = ctx.parentname.name
        else:
            o = [{}] + o
            self.classMap[name]["-parent"] = "-None-"
        o = [{}] + o   
        for mem in ctx.memlist:
            self.visit(mem, o)
        if ctx.parentname is not None:
            for mem in self.classMap[ctx.parentname.name].keys():
                if(mem in o[0].keys()):
                    continue
                else:
                    if mem != "-parent":
                        self.classMap[ctx.classname.name][mem] = self.classMap[ctx.parentname.name][mem] 
        o.pop();
        o.pop();
    
    def visitAttributeDecl(self, ctx, o): 
        cname = list(self.classMap.keys())[-1]
        name, dic, err = self.visit(ctx.decl, o)
        if err:
            raise Redeclared(Attribute(), name)
        self.classMap[cname]["&" + name] = dic
     
    def visitMethodDecl(self, ctx, o):
        print(self.classMap)
        cname = list(self.classMap.keys())[-1]
        self.classMap[cname]["*" + ctx.name.name] = {}
        if ctx.name.name in o[0].keys():
            raise Redeclared(Method(), ctx.name.name)
        o[0][ctx.name.name] = 'func'
        o = [{}] + o
        kind = self.visit(ctx.kind, o)
        if(self.class_Flag == "Program" and ctx.name.name == "main" and kind == "S"):
            self.hasMain = True
            self.methodFlag = "-main"
        else:
            self.methodFlag = ctx.name.name
        
        # Append param to Newest Scope
        param = []
        for i in ctx.param:
            name, dic, err = self.visit(i, o)
            if err:
                raise Redeclared(Parameter(), name)  # Redeclared Param
            param += [dic['type']]
            o[0][name] = {'type': dic['type'], 'var': True}
        
        # Visit body
        o[0]['Return'] = []
        self.visit(ctx.body, o)
        if(self.class_Flag == "Program" and ctx.name.name == "main" and kind == "S"):
            param += ["Special"]
        else:
            if o[0]['Return'] != []:
                param += o[0]['Return']
            else:
                param += [['Void']]
        self.classMap[cname]["*" + ctx.name.name]['type'] = param
        self.classMap[cname]["*" + ctx.name.name]['kind'] = kind
        self.methodFlag = "-None-"
        o.pop()
    
    # Stmt
    def visitVarDecl(self, ctx, o): 
        err = False
        if ctx.variable.name in o[0].keys():
            err = True
            return ctx.variable.name, None, err
        typ = self.visit(ctx.varType, o)
        if(ctx.varInit is not None):
            val_typ, val_err = self.visit(ctx.varInit, o)
            if not self.compareType(left=typ, right=val_typ):
                raise TypeMismatchInStatement(ctx) 
        o[0][ctx.variable.name] = {'type': typ, 'var': True}
        return ctx.variable.name, {'type': typ, 'var': True}, err
     
    def visitConstDecl(self, ctx, o):
        flg = False
        ini_flg = {}
        err = False
        if ctx.constant.name in o[0].keys():
            err = True
            return ctx.variable.name, None, err
        typ = self.visit(ctx.constType, o)
        if ctx.value is None:
            raise IllegalConstantExpression(None)
        self.constFlag = True
        val_typ, val_err = self.visit(ctx.value, o)
        self.constFlag = False
        if val_err:
            raise IllegalConstantExpression(None)
        if not self.compareType(left=typ, right=val_typ):
            raise TypeMismatchInConstant(ctx)
        o[0][ctx.constant.name] = {'type': typ, 'var': False}
        return ctx.constant.name, {'type': typ, 'var': False}, err
        
    def visitBlock(self, ctx, o):
        for inst in ctx.inst:
            self.visit(inst, o)
    
    def visitAssign(self, ctx, o): 
        lhs, lerr = self.visit(ctx.lhs, o)
        if lerr != True:
            raise CannotAssignToConstant(ctx)
        rhs, rerr = self.visit(ctx.exp, o)
        if not self.compareType(lhs, rhs):
            raise TypeMismatchInStatement(ctx)

    def visitIf(self, ctx, o): 
        typ, err = self.visit(ctx.expr, o)
        if typ != ['Bool']:
            raise TypeMismatchInStatement(ctx)
        o = [{}] + o
        self.visit(ctx.thenStmt, o)
        o.pop()
        if ctx.elseStmt is not None:
            o = [{}] + o
            self.visit(ctx.elseStmt, o)
            o.pop()
    
    def visitFor(self, ctx, o): 
        val1, err1 = self.visit(ctx.expr1, o)
        val2, err2 = self.visit(ctx.expr2, o)
        if val1 != ['Int'] or val2 != ['Int']:
            raise TypeMismatchInStatement(ctx)
        if ctx.expr3 is not None:
            val3, err3 = self.visit(ctx.expr3, o)
            if val3 != ['Int']:
                raise TypeMismatchInStatement(ctx)   
        self.inLoop += 1
        o  = [{ctx.id.name: {'type': ['Int'], 'var': True}}] + o
        self.visit(ctx.loop, o)
        o.pop()
        self.inLoop -= 1
    
    def visitBreak(self, ctx, o): 
        if self.inLoop <= 0:
            raise MustInLoop(ctx)
     
    def visitContinue(self, ctx, o): 
        if self.inLoop <= 0:
            raise MustInLoop(ctx)
     
    def visitReturn(self, ctx, o): 
        typ = []
        if ctx.expr:
            if self.methodFlag == "-main" or self.methodFlag == "Constructor" or self.methodFlag == "Destructor":
                raise TypeMismatchInStatement(ctx)
            val_typ, err = self.visit(ctx.expr, o)
            typ = val_typ
        else:
            typ = ['Void']
        if o[-3]["Return"] == []:
            o[-3]["Return"] = [typ]
        else:
            if o[-3]["Return"] != [typ]:
                raise TypeMismatchInStatement(ctx)
     
    def visitCallStmt(self, ctx, o): 
        if ctx.method.name[0] == "$":
            if type(ctx.obj) != type(Id('2')):
                raise IllegalMemberAccess(FieldAccess(ctx.obj, ctx.method))
            else:
                cname = ctx.obj.name
                if self.classMap[cname] is None:
                    raise Undeclared(Class, cname)
                else:
                    if "*" + ctx.method.name not in self.classMap[cname]:
                        raise Undeclared(Method, ctx.method.name)
                    if (self.classMap[cname]["*" + ctx.method.name][-1] != ['Void']):
                        raise TypeMismatchInStatement(ctx)
                    else:
                        p = []
                        for i in ctx.param:
                            typ, err = self.visit(i, o)
                            p += [typ]
                        expected = self.classMap[cname]["*" + ctx.method.name]['type'][:-1]
                        if len(p) == len(expected):
                            for i in range(0, len(p)):
                                if not self.compareType(expected[i], p[i]):
                                    raise TypeMismatchInStatement(ctx)
                            return
                        raise TypeMismatchInStatement(ctx)                   
        else:
            typ, err = self.visit(ctx.obj, o)
            cname = typ[0][1:]
            if self.classMap[cname] is None:
                raise Undeclared(Class(), cname)
            else:
                if "*" + ctx.method.name not in self.classMap[cname]:
                    raise Undeclared(Method(), ctx.method.name)
                if (self.classMap[cname]["*" + ctx.method.name]['type'][-1] != ['Void']):
                    raise TypeMismatchInStatement(ctx)
                else:
                    p = []
                    for i in ctx.param:
                        typ, err = self.visit(i, o)
                        p += [typ]
                    expected = self.classMap[cname]["*" + ctx.method.name]['type'][:-1]
                    if len(p) == len(expected):
                        for i in range(0, len(p)):
                            if not self.compareType(expected[i], p[i]):
                                raise TypeMismatchInStatement(ctx)
                        return
                    raise TypeMismatchInStatement(ctx)
                            
    # Expression
    def visitBinaryOp(self, ctx, o): 
        left, lerr = self.visit(ctx.left, o)
        right, rerr  = self.visit(ctx.right, o)
        if ctx.op in ["+", "-", "*", "/"]:
            if left == ['Int'] and right == ['Int']:
                return ["Int"], (lerr and rerr)
            elif left in [["Int"], ["Float"]] and right in [["Int"], ["Float"]]:
                return ['Float'], (lerr and rerr)
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in [">", "<", ">=", "<="]:
            if left in [["Int"], ["Float"]] and right in [["Int"], ["Float"]]:
                return ['Bool'], (lerr and rerr)
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op == "%":
            if left == ["Int"] and right == ["Int"]:
                return ["Int"], (lerr and rerr)
            else: 
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ["!=", "=="]:
            if (left == ['Int'] and right == ['Int']) or (left == ['Bool'] and right == ['Bool']):
                return ['Bool'], (lerr and rerr)
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['&&', '||']:
            if left == ['Bool'] and right == ['Bool']:
                return ['Bool'], (lerr and rerr)
            else: 
                raise TypeMismatchInExpression(ctx)
        elif ctx.op == '==.':
            if left == ['String'] and right == ['String']:
                return ['Bool'], (lerr and rerr)
            else: 
                raise TypeMismatchInExpression(ctx)
        else: # ctx.op == '+.':
            if left == ['String'] and right == ['String']:
                return ['String'], (lerr and rerr)
            else: 
                raise TypeMismatchInExpression(ctx)
     
    def visitUnaryOp(self, ctx, o): 
        typ, err = self.visit(ctx.body, o) 
        if ctx.op == "-":
            if typ in [["Int"], ["Float"]]:
                return typ, err
            else:
                raise TypeMismatchInExpression(ctx)
        else: # ctx.op == "!":
            if typ == ['Bool']:
                return typ, err
            else:
                raise TypeMismatchInExpression(ctx)
    
    def visitCallExpr(self, ctx, o): 
        if ctx.method.name[0] == "$":
            if type(ctx.obj) != type(Id('2')):
                raise IllegalMemberAccess(FieldAccess(ctx.obj, ctx.method))
            else:
                cname = ctx.obj.name
                if cname not in self.classMap.keys():
                    raise Undeclared(Class, cname)
                else:
                    if "*" + ctx.method.name not in self.classMap[cname]:
                        raise Undeclared(Method, ctx.method.name)
                    if (self.classMap[cname]["*" + ctx.method.name][-1] == ['Void']):
                        raise TypeMismatchInStatement(ctx)
                    else:
                        p = []
                        for i in ctx.param:
                            typ, err = self.visit(i, o)
                            p += [typ]
                        expected = self.classMap[cname]["*" + ctx.method.name]['type'][:-1]
                        if len(p) == len(expected):
                            for i in range(0, len(p)):
                                if not self.compareType(expected[i], p[i]):
                                    raise TypeMismatchInStatement(ctx)
                            return self.classMap[cname]["*" + ctx.method.name]['type'][-1], False
                        raise TypeMismatchInStatement(ctx)                   
        else:
            typ, err = self.visit(ctx.obj, o)
            cname = typ[0][1:]
            
            if cname not in self.classMap.keys():
                raise Undeclared(Class(), cname)
            else:
                if "*" + ctx.method.name not in self.classMap[cname]:
                    raise Undeclared(Method(), ctx.method.name)
                if (self.classMap[cname]["*" + ctx.method.name]['type'][-1] == ['Void']):
                    raise TypeMismatchInStatement(ctx)
                else:
                    p = []
                    for i in ctx.param:
                        typ, err = self.visit(i, o)
                        p += [typ]
                    expected = self.classMap[cname]["*" + ctx.method.name]['type'][:-1]
                    if len(p) == len(expected):
                        for i in range(0, len(p)):
                            if not self.compareType(expected[i], p[i]):
                                raise TypeMismatchInStatement(ctx)
                        print(self.classMap[cname]["*" + ctx.method.name]['type'][-1], False)
                        return self.classMap[cname]["*" + ctx.method.name]['type'][-1], False
                    raise TypeMismatchInStatement(ctx)
     
    def visitNewExpr(self, ctx, o): 
        if ctx.classname.name in self.classMap.keys() and self.class_Flag != ctx.classname.name:
            if "*Constructor" in self.classMap[ctx.classname.name].keys():
                pr = []
                expected = self.classMap[ctx.classname.name]["*Constructor"]['type'][:-1]
                for expr in ctx.param:
                    typ, var = self.visit(expr, o)
                    pr += [typ]
                if len(pr) == len(expected):
                    for i in range(0, len(pr)):
                        if not self.compareType(expected[i], pr[i]):
                            raise TypeMismatchInExpression(ctx)
                    return ["-" + ctx.classname.name], False
                raise TypeMismatchInExpression(ctx)
            else:
                if len(ctx.param) == 0:
                    return ["-" + ctx.classname.name], False
                raise TypeMismatchInExpression(ctx) 
        else:
            Undeclared(Class(), ctx.classname.name)
     
    def visitIntLiteral(self, ctx, o): 
        return ['Int'], False
    
    def visitFloatLiteral(self, ctx, o): 
        return ['Float'], False
    
    def visitStringLiteral(self, ctx, o): 
        return ['String'], False
    
    def visitBooleanLiteral(self, ctx, o): 
        return ['Bool'], False
     
    def visitNullLiteral(self, ctx, o): 
        return ['Void'], False
    
    def visitSelfLiteral(self, ctx, o): 
        return ['-' + self.class_Flag], False
    
    def visitId(self, ctx, o): 
        local_scope = o[:-2]
        for i in local_scope:
            if ctx.name in i:
                return i[ctx.name]['type'], i[ctx.name]['var']
        raise Undeclared(Identifier(), ctx.name)
        
    def visitArrayLiteral(self, ctx, o): 
        if len(ctx.value) == 0: # Array();
            return [0, 'Int'], False
        typ, err = self.visit(ctx.value[0], o)
        for literal in ctx.value:
            val_typ, err = self.visit(literal, o)
            if val_typ != typ:
                raise IllegalArrayLiteral(ctx)
        return [len(ctx.value)] + typ, False
            
    def visitArrayCell(self, ctx, o): 
        aname, aerr = self.visit(ctx.arr, o)
        if len(aname) - 1 < len(ctx.idx):
            raise TypeMismatchInExpression(ctx)
        for i in range(0, len(ctx.idx)):
            t, e = self.visit(ctx.idx[i], o)
            if t != ['Int']:
                raise TypeMismatchInExpression(ctx)
        return aname[len(ctx.idx):], aerr
            
    def visitFieldAccess(self, ctx, o): 
        if ctx.fieldname.name[0] == '$': # Static Field
            if type(ctx.obj) is not type(Id("2")):
                raise IllegalMemberAccess(ctx)
            else:
                if ctx.obj.name not in self.classMap.keys():
                    raise Undeclared(Class(), ctx.obj.name)
                else:
                    if ("&" + ctx.fieldname.name) not in self.classMap[ctx.obj.name].keys():
                        if ctx.obj.name == self.class_Flag and self.classMap[ctx.obj.name]["-parent"] != "-None-":
                            par_name = self.classMap[ctx.obj.name]["-parent"]
                            if ("&" + ctx.fieldname.name) in self.classMap[par_name]:
                                return self.classMap[par_name]["&" + ctx.fieldname.name]['type'], self.classMap[par_name]["&" + ctx.fieldname.name]['var']
                        raise Undeclared(Attribute(), ctx.fieldname.name)
                    return self.classMap[ctx.obj.name]["&" + ctx.fieldname.name]['type'], self.classMap[ctx.obj.name]["&" + ctx.fieldname.name]['var']
        else: # Instance Field
            if type(ctx.obj) is type(Id("2")): # Previous Stuff is an ID
                idtype, isvar = self.searchId(ctx.obj, o)
                if isvar is None: # Undeclared: No ID like that
                    if ctx.obj.name in self.classMap.keys():
                        raise IllegalMemberAccess(ctx)
                    else:
                        raise Undeclared(Identifier(), ctx.obj.name)
                else: # There is a Variable/Const
                    if len(idtype) != 1: # Type is An Array
                        raise TypeMismatchInExpression(ctx)
                    else: # Type is Not An Array
                        t = idtype[0][1:]
                        if t == self.class_Flag: # This Class
                            if self.classMap[t]["&" + ctx.fieldname.name] is None:
                                par_name = self.classMap[t]["-parent"]
                                if par_name != "-None-":
                                    if self.classMap[par_name]["&" + ctx.fieldname.name] is None:
                                        raise IllegalMemberAccess(ctx)
                                    else:
                                        return self.classMap[par_name]["&" + ctx.fieldname.name]['type'], self.classMap[par_name]["&" + ctx.fieldname.name]['var']
                                else:
                                    raise IllegalMemberAccess(ctx)
                            else:
                                return self.classMap[t]["&" + ctx.fieldname.name]['type'], self.classMap[t]["&" + ctx.fieldname.name]['var']
                        else: # Other Classes
                            if ("&" + ctx.fieldname.name) not in self.classMap[t].keys():
                                raise Undeclared(Attribute(), ctx.fieldname.name)
                            else:
                                return self.classMap[t]["&" + ctx.fieldname.name]['type'], self.classMap[t]["&" + ctx.fieldname.name]['var']
            elif ctx.obj == SelfLiteral(): # Previous Stuff is a Self
                t = self.class_Flag
                if ("&" + ctx.fieldname.name) not in self.classMap[t].keys():
                    par_name = self.classMap[t]["-parent"]
                    if par_name != "-None-":
                        if self.classMap[par_name]["&" + ctx.fieldname.name] is None:
                            raise IllegalMemberAccess(ctx)
                        else:
                            return self.classMap[par_name]["&" + ctx.fieldname.name]['type'], self.classMap[par_name]["&" + ctx.fieldname.name]['var']
                    else:
                        raise Undeclared(Attribute(), ctx.fieldname.name)
                else:
                    return self.classMap[t]["&" + ctx.fieldname.name]['type'], self.classMap[t]["&" + ctx.fieldname.name]['var']
            else: # Previous Stuff is an Expr
                expr_type, expr_state = self.visit(ctx.obj, o)
                if len(expr_type) != 1: # Type is An Array
                    raise TypeMismatchInExpression(ctx)
                else: # Type is Not An Array
                    t = expr_type[0][1:]
                    if t == self.class_Flag: # This Class
                        if self.classMap[t]["&" + ctx.fieldname.name] is None:
                            par_name = self.classMap[t]["-parent"]
                            if par_name != "-None-":
                                if self.classMap[par_name]["&" + ctx.fieldname.name] is None:
                                    raise IllegalMemberAccess(ctx)
                                else:
                                    return self.classMap[par_name]["&" + ctx.fieldname.name]['type'], self.classMap[par_name]["&" + ctx.fieldname.name]['var']
                            else:
                                raise IllegalMemberAccess(ctx)
                        else:
                            return self.classMap[t]["&" + ctx.fieldname.name]['type'], self.classMap[t[1:]]["&" + ctx.fieldname.name]['var']
                    else: # Other Classes
                        if self.classMap[t]["&" + ctx.fieldname.name] is None:
                            raise IllegalMemberAccess(ctx)
                        else:
                            return self.classMap[t]["&" + ctx.fieldname.name]['type'], self.classMap[t[1:]]["&" + ctx.fieldname.name]['var']
                
    # Data Type
    def visitIntType(self, ctx, o): 
        return ['Int']
     
    def visitFloatType(self, ctx, o): 
        return ['Float']
     
    def visitBoolType(self, ctx, o): 
        return ['Bool']
     
    def visitStringType(self, ctx, o): 
        return ['String']
     
    def visitArrayType(self, ctx, o): 
        return [ctx.size] + self.visit(ctx.eleType, o)
     
    def visitClassType(self, ctx , o): 
        if ctx.classname.name not in self.classMap.keys():
            raise Undeclared(Class(), ctx.classname.name)
        return ["-" + ctx.classname.name]
    
    # Instance vs Static
    def visitInstance(self, ctx, o): 
        return "I"
     
    def visitStatic(self, ctx, o): 
        return "S"
     
    
    

