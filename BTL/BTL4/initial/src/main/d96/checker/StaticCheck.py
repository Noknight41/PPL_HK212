
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
    class_Flag = "-None-"
    methodFlag = "-None-"
    inLoop = 0
    hasMain = False
    returnType = []
    passingParam = {}
    
    def __init__(self,ast):
        self.classMap = {}
        self.constFlag = False
        self.class_Flag = "-None-"
        self.methodFlag = "-None-"
        self.inLoop = 0
        self.hasMain = False
        self.ast = ast
        self.returnType = []
        self.passingParam = {}

    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)
    
    def compareType(self, left, right):
        if len(left) == 1 and len(right) == 1:
            if left == right:
                return True
            else:
                if left[0] == 'Float' and right[0] == 'Int':
                    return True
                if left[0][0] == "-" and right[0] == 'Null':
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
        o = []
        for decl_i in ctx.decl:
            self.visit(decl_i, o)
            self.class_Flag = "-None-"
        if not self.hasMain:
            raise NoEntryPoint()
        return []
        
    def visitClassDecl(self, ctx, o): 
        name = (ctx.classname.name)
        if name in self.classMap.keys():
            raise Redeclared(Class(), name)
        self.class_Flag = (name)
        self.classMap[name] = {}
        if ctx.parentname is not None:
            if ctx.parentname.name not in self.classMap.keys() or self.class_Flag == ctx.parentname.name:
                raise Undeclared(Class(), ctx.parentname.name)
            o = [self.classMap[ctx.parentname.name]] + o
            self.classMap[name]["-parent"] = ctx.parentname.name
        else:
            o = [{}] + o
            self.classMap[name]["-parent"] = "-None-"
        o = [{}] + o   
        for mem in ctx.memlist:
            self.visit(mem, o)
        o.pop()
        o.pop()
    
    def visitAttributeDecl(self, ctx, o): 
        cname = self.class_Flag
        name, dic, err = self.visit(ctx.decl, o)
        if err:
            raise Redeclared(Attribute(), name)
        self.classMap[cname]["&" + name] = dic
     
    def visitMethodDecl(self, ctx, o):
        cname = list(self.classMap.keys())[-1]
        if ('*' + ctx.name.name) in self.classMap[cname].keys():
            raise Redeclared(Method(), ctx.name.name)
        self.classMap[cname]["*" + ctx.name.name] = {}
        kind = self.visit(ctx.kind, o)
        if(self.class_Flag == "Program" and ctx.name.name == "main" and kind == "S"):
            self.hasMain = True
            self.methodFlag = "-main"
        else:
            self.methodFlag = ctx.name.name
        
        # Append param to Newest Scope
        param = []
        o = [{}] + o
        for i in ctx.param:
            name, dic, err = self.visit(i, o)
            if err:
                raise Redeclared(Parameter(), name)  # Redeclared Param
            param += [dic['type']]
            self.passingParam[name] = {'type': dic['type'], 'var': True}
        o = o[1:]
        
        # Visit body
        self.returnType = []
        self.visit(ctx.body, o)
        if(self.class_Flag == "Program" and ctx.name.name == "main" and kind == "S"):
            param += ["Special"]
        else:
            if self.returnType != []:
                param += self.returnType
            else:
                param += [['Void']]
        self.classMap[cname]["*" + ctx.name.name]['type'] = param
        self.classMap[cname]["*" + ctx.name.name]['kind'] = kind
        self.methodFlag = "-None-"
    
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
        err = False
        if ctx.constant.name in o[0].keys():
            err = True
            return ctx.constant.name, None, err
        typ = self.visit(ctx.constType, o)
        if ctx.value is None:
            raise IllegalConstantExpression(None)
        val_typ, val_err = self.visit(ctx.value, o)
        if val_err:
            raise IllegalConstantExpression(ctx.value)
        if not self.compareType(left=typ, right=val_typ):
            raise TypeMismatchInConstant(ctx)
        o[0][ctx.constant.name] = {'type': typ, 'var': False}
        return ctx.constant.name, {'type': typ, 'var': False}, err
        
    def visitBlock(self, ctx, o):
        o = [self.passingParam] + o
        self.passingParam = {}
        for inst in ctx.inst:
            if isinstance(inst, VarDecl):
                name, typ, err = self.visit(inst, o)
                if err:
                    raise Redeclared(Variable(), name)
            elif isinstance(inst, ConstDecl):
                name, typ, err = self.visit(inst, o)
                if err:
                    raise Redeclared(Constant(), name)
            else:
                self.visit(inst, o)
        o.pop()
    
    def visitAssign(self, ctx, o): 
        rhs, risvar = self.visit(ctx.exp, o)
        lhs, lisvar = self.visit(ctx.lhs, o)
        if lisvar != True:
            raise CannotAssignToConstant(ctx)
        if not self.compareType(lhs, rhs):
            raise TypeMismatchInStatement(ctx)

    def visitIf(self, ctx, o): 
        typ, err = self.visit(ctx.expr, o)
        if typ != ['Bool']:
            raise TypeMismatchInStatement(ctx)
        self.visit(ctx.thenStmt, o)
        if ctx.elseStmt is not None:
            self.visit(ctx.elseStmt, o)
    
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
        vartype, isvar = self.visit(ctx.id, o)
        if vartype != ["Int"]:
            raise TypeMismatchInStatement(ctx)
        if isvar != True:
            raise CannotAssignToConstant(Assign(ctx.id, ctx.expr1))
        self.visit(ctx.loop, o)
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
        if self.returnType == []:
            self.returnType = [typ]
        else:
            if self.returnType != [typ]:
                raise TypeMismatchInStatement(ctx)
     
    def visitCallStmt(self, ctx, o): 
        if ctx.method.name[0] == "$":
            if type(ctx.obj) != type(Id('2')):
                raise IllegalMemberAccess(ctx)
            else:
                type1, err1 = self.searchId(ctx.obj, o)
                if type1 != None:
                    if len(type1) != 1:
                        raise TypeMismatchInStatement(ctx)
                    if type1[0][1:] not in self.classMap.keys():
                        raise TypeMismatchInStatement(ctx)
                    if "*" + ctx.method.name in self.classMap[type1[0][1:]]:
                        raise IllegalMemberAccess(ctx)
                cname = ctx.obj.name
                if cname not in self.classMap.keys():
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
        else:
            if self.methodFlag[0] == "$":
                if type(ctx.obj) is type(SelfLiteral()):
                    raise IllegalMemberAccess(ctx)
            typ, err = self.visit(ctx.obj, o)
            if typ[0][0] != "-":
                raise TypeMismatchInStatement(ctx)
            cname = typ[0][1:]
            if cname not in self.classMap.keys():
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
        left, lisvar = self.visit(ctx.left, o)
        right, risvar  = self.visit(ctx.right, o)
        if ctx.op in ["+", "-", "*", "/"]:
            if left == ['Int'] and right == ['Int']:
                return ["Int"], (lisvar or risvar)
            elif left in [["Int"], ["Float"]] and right in [["Int"], ["Float"]]:
                return ['Float'], (lisvar or risvar)
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in [">", "<", ">=", "<="]:
            if left in [["Int"], ["Float"]] and right in [["Int"], ["Float"]]:
                return ['Bool'], (lisvar or risvar)
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op == "%":
            if left == ["Int"] and right == ["Int"]:
                return ["Int"], (lisvar or risvar)
            else: 
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ["!=", "=="]:
            if (left == ['Int'] and right == ['Int']) or (left == ['Bool'] and right == ['Bool']):
                return ['Bool'], (lisvar or risvar)
            else:
                raise TypeMismatchInExpression(ctx)
        elif ctx.op in ['&&', '||']:
            if left == ['Bool'] and right == ['Bool']:
                return ['Bool'], (lisvar or risvar)
            else: 
                raise TypeMismatchInExpression(ctx)
        elif ctx.op == '==.':
            if left == ['String'] and right == ['String']:
                return ['Bool'], (lisvar or risvar)
            else: 
                raise TypeMismatchInExpression(ctx)
        else: # ctx.op == '+.':
            if left == ['String'] and right == ['String']:
                return ['String'], (lisvar or risvar)
            else: 
                raise TypeMismatchInExpression(ctx)
     
    def visitUnaryOp(self, ctx, o): 
        typ, isvar = self.visit(ctx.body, o) 
        if ctx.op == "-":
            if typ in [["Int"], ["Float"]]:
                return typ, isvar
            else:
                raise TypeMismatchInExpression(ctx)
        else: # ctx.op == "!":
            if typ == ['Bool']:
                return typ, isvar
            else:
                raise TypeMismatchInExpression(ctx)
    
    def visitCallExpr(self, ctx, o): 
        if ctx.method.name[0] == "$":
            if type(ctx.obj) != type(Id('2')):
                raise IllegalMemberAccess(ctx)
            else:
                type1, err1 = self.searchId(ctx.obj, o)
                if type1 != None:
                    if len(type1) != 1:
                        raise TypeMismatchInExpression(ctx)
                    if type1[0][1:] not in self.classMap.keys():
                        raise TypeMismatchInExpression(ctx)
                    if "*" + ctx.method.name in self.classMap[type1[0][1:]]:
                        raise IllegalMemberAccess(ctx)
                cname = ctx.obj.name
                if cname not in self.classMap.keys():
                    raise Undeclared(Class(), cname)
                else:
                    if "*" + ctx.method.name not in self.classMap[cname]:
                        raise Undeclared(Method(), ctx.method.name)
                    if (self.classMap[cname]["*" + ctx.method.name]['type'][-1] == ['Void']):
                        raise TypeMismatchInExpression(ctx)
                    else:
                        p = []
                        for i in ctx.param:
                            typ, err = self.visit(i, o)
                            p += [typ]
                        expected = self.classMap[cname]["*" + ctx.method.name]['type'][:-1]
                        if len(p) == len(expected):
                            for i in range(0, len(p)):
                                if not self.compareType(expected[i], p[i]):
                                    raise TypeMismatchInExpression(ctx)
                            return self.classMap[cname]["*" + ctx.method.name]['type'][-1], False
                        raise TypeMismatchInExpression(ctx)                   
        else:
            if self.methodFlag[0] == "$":
                if type(ctx.obj) is type(SelfLiteral()):
                    raise IllegalMemberAccess(ctx)
            typ, err = self.visit(ctx.obj, o)
            if typ[0][0] != "-":
                raise TypeMismatchInExpression(ctx)
            cname = typ[0][1:]
            if cname not in self.classMap.keys():
                raise Undeclared(Class(), cname)
            else:
                if "*" + ctx.method.name not in self.classMap[cname]:
                    raise Undeclared(Method(), ctx.method.name)
                if (self.classMap[cname]["*" + ctx.method.name]['type'][-1] == ['Void']):
                    raise TypeMismatchInExpression(ctx)
                else:
                    p = []
                    for i in ctx.param:
                        typ, err = self.visit(i, o)
                        p += [typ]
                    expected = self.classMap[cname]["*" + ctx.method.name]['type'][:-1]
                    if len(p) == len(expected):
                        for i in range(0, len(p)):
                            if not self.compareType(expected[i], p[i]):
                                raise TypeMismatchInExpression(ctx)
                        return self.classMap[cname]["*" + ctx.method.name]['type'][-1], False
                    raise TypeMismatchInExpression(ctx)
     
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
            raise Undeclared(Class(), ctx.classname.name)
     
    def visitIntLiteral(self, ctx, o): 
        return ['Int'], False
    
    def visitFloatLiteral(self, ctx, o): 
        return ['Float'], False
    
    def visitStringLiteral(self, ctx, o): 
        return ['String'], False
    
    def visitBooleanLiteral(self, ctx, o): 
        return ['Bool'], False
     
    def visitNullLiteral(self, ctx, o): 
        return ['Null'], False
    
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
        if type(ctx.obj) is type(NullLiteral()):
            raise TypeMismatchInExpression(ctx)
        if ctx.fieldname.name[0] == '$': # Static Field
            if type(ctx.obj) is not type(Id("2")):
                raise IllegalMemberAccess(ctx)
            else:
                if ctx.obj.name not in self.classMap.keys():
                    idtype, isvar = self.searchId(ctx.obj, o)
                    if idtype is not None and idtype[0][0] == "-":
                        if ("&" + ctx.fieldname.name) in self.classMap[idtype[0][1:]].keys():
                            raise IllegalMemberAccess(ctx)
                    raise Undeclared(Class(), ctx.obj.name)
                else:
                    if ("&" + ctx.fieldname.name) not in self.classMap[ctx.obj.name].keys():
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
                            if "&" + ctx.fieldname.name not in self.classMap[t].keys():
                                raise IllegalMemberAccess(ctx)
                            else:
                                return self.classMap[t]["&" + ctx.fieldname.name]['type'], self.classMap[t]["&" + ctx.fieldname.name]['var']
                        else: # Other Classes
                            if ("&" + ctx.fieldname.name) not in self.classMap[t].keys():
                                raise Undeclared(Attribute(), ctx.fieldname.name)
                            else:
                                return self.classMap[t]["&" + ctx.fieldname.name]['type'], self.classMap[t]["&" + ctx.fieldname.name]['var']
            elif type(ctx.obj) is type(SelfLiteral()): # Previous Stuff is a Self
                if self.methodFlag[0] == "$":
                    raise IllegalMemberAccess(ctx)
                t = self.class_Flag
                if ("&" + ctx.fieldname.name) not in self.classMap[t].keys():
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
                        if "&" + ctx.fieldname.name not in self.classMap[t].keys():
                            raise IllegalMemberAccess(ctx)
                        else:
                            return self.classMap[t]["&" + ctx.fieldname.name]['type'], self.classMap[t]["&" + ctx.fieldname.name]['var']
                    else: # Other Classes
                        if "&" + ctx.fieldname.name not in self.classMap[t].keys():
                            raise IllegalMemberAccess(ctx)
                        else:
                            return self.classMap[t]["&" + ctx.fieldname.name]['type'], self.classMap[t]["&" + ctx.fieldname.name]['var']
                
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
     
    
    

