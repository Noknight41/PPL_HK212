# Nguyen Thi Nhu Y - 1614246

from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
import functools

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"
        self.curFunc = Symbol("null", MType([], VoidType()), CName("MPClass"))

    def init(self):
        return [    Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("getFloat", MType([], FloatType()), CName(self.libName)),
                    Symbol("putFloat", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putFloatLn", MType([FloatType()], VoidType()), CName(self.libName)),
                    Symbol("putBool", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putBoolLn", MType([BoolType()], VoidType()), CName(self.libName)),
                    Symbol("putString", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putStringLn", MType([StringType()], VoidType()), CName(self.libName)),
                    Symbol("putLn", MType([], VoidType()), CName(self.libName)),
                    ]

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)
        
class StringType(Type):
    def __str__(self):
        return "StringType"
    def accept(self, v, c):
       return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, c):
        return None
        
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, c):
        return None
        
class SubBody():
    def __init__(self, frame, sym):
        #frame: Frame
        #sym: List[Symbol]

        self.frame = frame
        self.sym = sym

class Access():
    def __init__(self, frame, sym, isLeft, isFirst):
        #frame: Frame
        #sym: List[Symbol]
        #isLeft: Boolean
        #isFirst: Boolean

        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft
        self.isFirst = isFirst
      
class Val(ABC):
    pass

class Index(Val):
    def __init__(self, value):
        #value: Int

        self.value = value

class CName(Val):
    def __init__(self, value):
        #value: String

        self.value = value

class CodeGenVisitor(BaseVisitor, Utils):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MPClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")
        self.curFunc = Symbol("null", MType([],VoidType()), CName(self.className))
        
    def varGlobal(self, ast, c):
        _ctxt = c
        _name = ast.variable.name
        _type = ast.varType

        self.emit.printout(self.emit.emitATTRIBUTE(_name, _type, False, ""))    

        _symbol = Symbol(_name, _type, CName (self.className))
        _ctxt.append(_symbol)
        return _ctxt

    def funcGlobal(self, ast, c):
        _ctxt = c
        _name = ast.name.name
        _type = MType([x.varType for  x in ast.param], ast.returnType)
        _symbol = Symbol(_name, _type, CName (self.className))
        _ctxt.append(_symbol)
        return _ctxt     
        
    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
       
        _lstVarDecl = list(filter(lambda x: type(x) is VarDecl, ast.decl))
        _lstFunc = list(filter(lambda x: type(x) is FuncDecl, ast.decl))
        _lstVarArray = list(filter(lambda x: type(x.varType) is ArrayType, _lstVarDecl))
        

        for x in ast.decl:
            self.env = self.varGlobal(x, self.env) if type(x) is VarDecl else self.funcGlobal(x, self.env)

        for x in _lstFunc:
            self.visit(x, SubBody(None, self.env))
        
        # generate default constructor
        self.genMETHOD(FuncDecl(Id("<init>"), list(), list(), list(),None), c, Frame("<init>", VoidType))
        
        if _lstVarArray:
            self.emit.printout(self.emit.emitCLINIT(self.className, _lstVarArray, Frame("<clinit>", VoidType())))

        self.emit.emitEPILOG()
        return c
     
    def genMETHOD(self, consdecl, o, frame):
        isInit = consdecl.returnType is None
        isMain = consdecl.name.name.lower() == "main" and len(consdecl.param) == 0 and type(consdecl.returnType) is VoidType
        returnType = VoidType() if isInit else consdecl.returnType
        # methodName = "<init>" if isInit else consdecl.name.name.lower()
        methodName = ""
        if isInit:
            methodName = "<init>"
        elif isMain:
            methodName = "main"
        else:
            methodName = consdecl.name.name
            
        intype = [ArrayPointerType(StringType())] if isMain else [x.varType for x in consdecl.param]
        
        mtype = MType(intype, returnType)
        
        self.emit.printout(self.emit.emitMETHOD(methodName, mtype, not isInit, frame))
        
        frame.enterScope(True)
        
        glenv = o
        
        # Generate code for parameter declarations
        if isInit:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "this", ClassType(self.className), frame.getStartLabel(), frame.getEndLabel(), frame))
        if isMain:
            self.emit.printout(self.emit.emitVAR(frame.getNewIndex(), "args", ArrayPointerType(StringType()), frame.getStartLabel(), frame.getEndLabel(), frame))
            
        glSubBody = SubBody(frame, glenv)
        if (isMain is False) and (intype != []):
            for x in consdecl.param:
                glSubBody = self.visit(x, glSubBody)

        for x in consdecl.local:
            glSubBody = self.visit(x, glSubBody)
        
        lsArrVarDecl = [i for i in consdecl.local if type(i.varType) is ArrayType]
        self.emit.printout(self.emit.emitLABEL(frame.getStartLabel(), frame))
        
        for x in lsArrVarDecl:
            self.arrayTypeDecl(x, glSubBody)

        if isInit:
            self.emit.printout(self.emit.emitREADVAR("this", ClassType(self.className), 0, frame))
            self.emit.printout(self.emit.emitINVOKESPECIAL(frame))

        returnStmt = list(filter(lambda x:type(x) is Return, consdecl.body))
        
        list(map(lambda x: self.visit(x, glSubBody), consdecl.body))
          
        self.emit.printout(self.emit.emitLABEL(frame.getEndLabel(), frame))
        if (type(returnType) is VoidType) or (not returnStmt):
            self.emit.printout(self.emit.emitRETURN(VoidType(), frame))
        
        self.emit.printout(self.emit.emitENDMETHOD(frame))
        
        frame.exitScope()
    
    def visitVarDecl(self, ast, c):
        _env = c.sym if type(c) is SubBody else []
        _frame = c.frame
        _idx = c.frame.getNewIndex()
        self.emit.printout(self.emit.emitVAR(_idx, ast.variable.name, ast.varType, _frame.getStartLabel(), _frame.getEndLabel(), _frame))
        
        return SubBody(_frame, [Symbol(ast.variable.name, ast.varType, Index(_idx))] + _env)
  
    def arrayTypeDecl(self, ast, c):
        _sym = c.sym
        _frame = c.frame
        _idx = (self.lookup(ast.variable.name.lower(), _sym, lambda x: x.name.lower())).value.value
        self.emit.printout(self.emit.emitNEWARRAY(ast.varType, _frame))
        self.emit.printout(self.emit.emitWRITEVAR(ast.variable.name, ast.varType, _idx, _frame))
        return SubBody(_frame, _sym)
   
    def visitFuncDecl(self, ast, c):
        _sym = c.sym
        _frame = Frame(ast.name.name, ast.returnType )
        self.curFunc = self.lookup(ast.name.name.lower(), _sym, lambda x: x.name.lower())
        self.genMETHOD(ast, _sym, _frame)
        return c
    
    def genCodeBinExpr(self, frame, leftCode, leftType, rightCode, rightType, reqFloat = False):
        if type(leftType) is FloatType and type(rightType) is IntType:
            return leftCode + rightCode + self.emit.emitI2F(frame), FloatType()
        if type(leftType) is IntType and type(rightType) is FloatType:
            return leftCode + self.emit.emitI2F(frame) + rightCode , FloatType()
        if reqFloat and type(leftType) is IntType:
            return leftCode + self.emit.emitI2F(frame) + rightCode + self.emit.emitI2F(frame), FloatType() 
        return leftCode + rightCode, leftType

    def visitBinaryOp(self, ast, c):
        _frame = c.frame
        _sym = c.sym
        _op = ast.op.lower()

        leftCode, leftType = self.visit(ast.left, Access(_frame, _sym, False, True))
        rightCode, rightType = self.visit(ast.right, Access(_frame, _sym, False, True))
                
        if _op == '/':
            _code, _type = self.genCodeBinExpr (_frame, leftCode, leftType, rightCode, rightType, True)
            _code += self.emit.emitMULOP(_op, FloatType(), _frame)
            return _code, _type
        
        _code, _type = self.genCodeBinExpr (_frame, leftCode, leftType, rightCode, rightType, False)
                
        if _op in ['andthen', 'orelse']:
            _code = self.emit.emitAND_OR_SHORT_CIRCUIT(_op, leftCode, rightCode, _frame)
            return _code, _type

        if _op in ['+','-']:
            _code += self.emit.emitADDOP(_op, _type, _frame)
        elif _op == '*':
            _code += self.emit.emitMULOP(_op, _type, _frame)
        elif _op == 'div':
            _code += self.emit.emitMULOP('/', _type, _frame)
        elif _op == 'mod':
            _code += self.emit.emitMOD(_frame)
        elif _op == 'and':
            _code += self.emit.emitANDOP(_frame)
            _type = BoolType()
        elif _op == 'or':
            _code += self.emit.emitOROP(_frame)
            _type = BoolType()
        elif _op in ["<", "<=", ">", ">=",'=','<>']:
            _code += self.emit.emitREOP(_op, _type, _frame)
            _type = BoolType()
        return _code, _type

    def visitUnaryOp(self, ast, c):
        _frame = c.frame
        _sym = c.sym
        
        _code, _type = self.visit(ast.body, Access(_frame, _sym, False, True) )
        if ast.op.lower() == 'not':
            return _code + self.emit.emitNOT(BoolType(), _frame), BoolType()
        elif ast.op == '-':
            return _code + self.emit.emitNEGOP(_type, _frame), _type
       
    def visitCallStmt(self, ast, c):
        _frame = c.frame
        _nenv = c.sym
        _sym = self.lookup(ast.method.name.lower(), _nenv, lambda x: x.name.lower())
        _cname = _sym.value.value
        _ctype = _sym.mtype
        
        checkList = []
        for i in range(len(_ctype.partype)):
            checkList.append((ast.param[i], _ctype.partype[i]))
        
        in_ = ("", list())
        
        for x in checkList:
            (_code, _type) = self.visit(x[0], Access(_frame, _nenv, False, True))
            if type(x[1]) is ArrayType:
                _code += self.emit.emitCLONE(_type) + self.emit.emitCHECKCAST(_type)
            if type(_type) is IntType and type(x[1]) is FloatType:
                in_ = (in_[0] + _code + self.emit.emitI2F(_frame), in_[1] + [_type])
            else:
                in_ = (in_[0] + _code, in_[1] + [_type])

        self.emit.printout(in_[0])
        self.emit.printout(self.emit.emitINVOKESTATIC(_cname + "/" + _sym.name, _ctype, _frame))
        return None
        
    def visitCallExpr(self, ast, c):
        _ctxt = c
        _frame = _ctxt.frame
        _nenv = _ctxt.sym
        _sym = self.lookup(ast.method.name.lower(), _nenv, lambda x: x.name.lower())
        _cname = _sym.value.value
        _ctype = _sym.mtype
        _returnType = _ctype.rettype
        
        if _ctxt.isLeft and not _ctxt.isFirst:
            return self.emit.emitWRITEVAR2(ast.method.name, _returnType, _frame), _returnType
            
        checkList = []
        for i in range(len(_ctype.partype)):
            checkList.append((ast.param[i], _ctype.partype[i]))
            
        in_ = ("", [])
        
        for x in checkList:
            (_code, _type) = self.visit(x[0], Access(_frame, _nenv, False, True))
            if type(x[1]) is ArrayType:
                _code += self.emit.emitCLONE(_type) + self.emit.emitCHECKCAST(_type)
            if type(_type) is IntType and type(x[1]) is FloatType:
                in_ = (in_[0] + _code + self.emit.emitI2F(_frame), in_[1] + [_type])
            else:
                in_ = (in_[0] + _code, in_[1] + [_type])
                
        return in_[0] + self.emit.emitINVOKESTATIC(_cname + "/" + _sym.name, _ctype, _frame), _returnType
    
    def visitId(self, ast, c):
        _sym = self.lookup(ast.name.lower(), c.sym, lambda x: x.name.lower())
        if type(c) != SubBody:

            _code = ""             

            if c.isLeft is True and c.isFirst is True:
                pass
            elif c.isLeft is True and c.isFirst is False:
                if type(_sym.mtype) is ArrayType or type(_sym.mtype) is ArrayPointerType:
                    _code = self.emit.emitWRITEVAR2(ast.name, _sym.mtype, c.frame)
                else:
                    if type(_sym.value) is CName:
                        _code = self.emit.emitPUTSTATIC(_sym.value.value + "." + ast.name, _sym.mtype, c.frame) 
                    elif type(_sym.value) is Index:
                        _code = self.emit.emitWRITEVAR(ast.name, _sym.mtype, _sym.value.value, c.frame)   
            elif c.isLeft is False:
                if type(_sym.value) is CName:
                    _code = self.emit.emitGETSTATIC(_sym.value.value + "." + _sym.name, _sym.mtype, c.frame) 
                elif type(_sym.value) is Index:
                    _code = self.emit.emitREADVAR(ast, _sym.mtype, _sym.value.value, c.frame)
            return _code, _sym.mtype
        else:
            return ("", _sym.mtype)

            
    def visitArrayCell(self, ast, c):
        _frame = c.frame
        _sym = c.sym

        if type(c) != SubBody:
            
            arrt = self.lookup(ast.arr.method.name.lower() if type(ast.arr) is CallExpr else ast.arr.name.lower(), _sym, lambda x: x.name.lower())
            _lower = int(arrt.mtype.rettype.lower) if type(arrt.mtype) is MType else int(arrt.mtype.lower)

            if c.isLeft is True and c.isFirst is True:
                (_code, _type) = self.visit(ast.arr, Access(_frame, _sym, False, True))
                if _lower >= 0:
                    (_codeIdx, _typeIdx) = self.visit(BinaryOp("-", ast.idx, IntLiteral(_lower)), Access(_frame, _sym, False, True))
                else:
                    (_codeIdx, _typeIdx) = self.visit(BinaryOp("+", ast.idx, IntLiteral(- _lower)), Access(_frame, _sym, False, True))
                return (_code + _codeIdx, _type.eleType)
            
            elif c.isLeft is True and c.isFirst is False:
                (_code, _type) = self.visit(ast.arr, Access(_frame, _sym, True, False))
                return (_code, _type)
            
            elif c.isLeft is False:
                (_code, _type) = self.visit(ast.arr, Access(_frame, _sym, False, True))
                if _lower >= 0:
                    (_codeIdx, _typeIdx) = self.visit(BinaryOp("-", ast.idx, IntLiteral(_lower)), Access(_frame, _sym, False, True))
                else:
                    (_codeIdx, _typeIdx) = self.visit(BinaryOp("+", ast.idx, IntLiteral(- _lower)), Access(_frame, _sym, False, True))
                
                if type(_type) is ArrayType:
                    arrayType = _type.eleType
                    aload = self.emit.emitALOAD(arrayType, _frame)
                    return (_code + _codeIdx + aload, arrayType)
                elif type(_type) is ArrayPointerType:
                    arrayPointerType = _type.eleType
                    aload = self.emit.emitALOAD(arrayPointerType, _frame)
                    return (_code + _codeIdx + aload, arrayPointerType)
        else:            
            (_code, _type) = self.visit(ast.arr, Access(_frame, _sym, False, True))
            arrType = _type.eleType
            return ("", arrayType)
        return None
    
    def visitAssign (self, ast, c):        
        _frame = c.frame
        _env = c.sym       
        _code = ""
        _code_I2F = ""

        leftCode, leftType = self.visit(ast.lhs, Access(_frame, _env, True, True))
        print(type(ast.lhs))
        rightCode, rightType = self.visit(ast.exp, Access(_frame, _env, False, True))

        if type(leftType) is FloatType and type(rightType) is IntType:
            _code_I2F = self.emit.emitI2F(_frame)
        
        leftCode_2, leftType_2 = self.visit (ast.lhs, Access(_frame, _env, True, False))
             
        _code = leftCode + rightCode + _code_I2F + leftCode_2
        
        _type = leftType_2
        self.emit.printout(_code)
        return _code, _type
    
    def visitWith(self, ast, c):
        _frame = c.frame
        _nenv = c.sym

        _frame.enterScope(False)

        _varEnv = functools.reduce (lambda x, y: self.visit(y, x), ast.decl, SubBody(_frame, _nenv))

        _lstVarArray = filter(lambda x: type(x.varType) is ArrayType, ast.decl)
        self.emit.printout (self.emit.emitLABEL(_frame.getStartLabel(),_frame))
        list(map(lambda x: self.arrayTypeDecl(x, _varEnv), _lstVarArray))
        list(map(lambda x: self.visit(x, _varEnv), ast.stmt))
        self.emit.printout(self.emit.emitLABEL(_frame.getEndLabel(), _frame))
        _frame.exitScope()
        return None
    
    def visitIf(self, ast, c):
        _frame = c.frame
        _env = c.sym

        _code, _type = self.visit(ast.expr, Access (_frame, _env, False, True))
        _falseLb = _frame.getNewLabel()

        self.emit.printout(_code + self.emit.emitIFFALSE(_falseLb, _frame))
        [self.visit(i, c) for i in ast.thenStmt]
        if not ast.elseStmt:
            self.emit.printout(self.emit.emitLABEL(_falseLb, _frame))
        else:
            _trueLb = _frame.getNewLabel()
            self.emit.printout(self.emit.emitGOTO(_trueLb, _frame))
            self.emit.printout(self.emit.emitLABEL(_falseLb, _frame))
            [self.visit(i, c) for i in ast.elseStmt]
            self.emit.printout(self.emit.emitLABEL(_trueLb, _frame))
        return None

    def visitFor(self, ast, c):
        _frame = c.frame
        _env = c.sym

        _loopLb = _frame.getNewLabel()
        _frame.enterLoop()

        self.visit(Assign(ast.id, ast.expr1), SubBody(_frame, _env))
        
        self.emit.printout(self.emit.emitLABEL(_loopLb, _frame))
        
        _code, _type = self.visit(BinaryOp("<=" if ast.up else ">=" , ast.id, ast.expr2), Access(_frame, _env, False, True) )           
        self.emit.printout(_code)            
        self.emit.printout(self.emit.emitIFFALSE(_frame.getBreakLabel(), _frame))
        [self.visit(i, c) for i in ast.loop]
        self.emit.printout(self.emit.emitLABEL(_frame.getContinueLabel(), _frame))
        self.visit(Assign(ast.id, BinaryOp("+" if  ast.up else  "-", ast.id, IntLiteral(1))), c)
        self.emit.printout(self.emit.emitGOTO(_loopLb, _frame))
        self.emit.printout(self.emit.emitLABEL(_frame.getBreakLabel(),_frame))
        _frame.exitLoop()
        return None
    
    def visitContinue(self, ast, c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))
        return None
    
    def visitBreak(self, ast, c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getBreakLabel(), c.frame))
        return None
    
    def visitReturn (self, ast, c):
        _frame = c.frame
        _env = c.sym

        if ast.expr:
            _code, _type = self.visit(ast.expr, Access(_frame, _env, False, True))
            _typeFunc = self.curFunc.mtype.rettype
            if type(_typeFunc) is FloatType and type(_type) is IntType:
                self.emit.printout(_code + self.emit.emitI2F(_frame) + (self.emit.emitRETURN(FloatType(), _frame)))
            else:
                self.emit.printout(_code + (self.emit.emitRETURN(_type, _frame)))
        else:
            self.emit.printout(self.emit.emitRETURN(VoidType(), _frame))
        return None
    
    def visitWhile(self, ast, c):
        _frame = c.frame
        _env = c.sym

        _loopLb = _frame.getNewLabel()
        _frame.enterLoop()
        _code, _type = self.visit(ast.exp, Access(_frame, _env, False, True))

        self.emit.printout(self.emit.emitLABEL(_loopLb, _frame))
        self.emit.printout(_code)
        self.emit.printout(self.emit.emitIFFALSE(_frame.getBreakLabel(), _frame))
        
        [self.visit (i, c) for i in ast.sl]

        self.emit.printout(self.emit.emitLABEL(_frame.getContinueLabel(), _frame))
        self.emit.printout(self.emit.emitGOTO(_loopLb, _frame))
        self.emit.printout(self.emit.emitLABEL(_frame.getBreakLabel(), _frame))
        _frame.exitLoop()
        return None
    
    def visitIntLiteral(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(ast.value, frame), IntType()
    
    def visitFloatLiteral(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        return self.emit.emitPUSHFCONST(str(ast.value), frame), FloatType()
    
    def visitBooleanLiteral(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        return self.emit.emitPUSHICONST(str(ast.value), frame), BoolType()
    
    def visitStringLiteral(self, ast, c):
        ctxt = c
        frame = ctxt.frame
        return self.emit.emitPUSHCONST(ast.value, StringType(), frame), StringType()
        