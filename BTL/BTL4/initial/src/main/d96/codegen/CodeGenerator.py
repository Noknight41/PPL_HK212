'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Utils import *
from StaticCheck import *
from StaticError import *
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod

class CodeGenerator(Utils):
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [Symbol("getInt", MType(list(), IntType()), CName(self.libName)),
                    Symbol("putInt", MType([IntType()], VoidType()), CName(self.libName)),
                    Symbol("putIntLn", MType([IntType()], VoidType()), CName(self.libName))
                    
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
    def accept(self, v, param):
        return None

class ArrayPointerType(Type):
    def __init__(self, ctype):
        #cname: String
        self.eleType = ctype

    def __str__(self):
        return "ArrayPointerType({0})".format(str(self.eleType))

    def accept(self, v, param):
        return None
    
class ClassType(Type):
    def __init__(self,cname):
        self.cname = cname
    def __str__(self):
        return "Class({0})".format(str(self.cname))
    def accept(self, v, param):
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
        self.className = "D96Class"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    # Class Scope
    def visitProgram(self, ctx, o): 
        pass
        
    def visitClassDecl(self, ctx, o): 
        pass
    
    def visitAttributeDecl(self, ctx, o): 
        pass
     
    def visitMethodDecl(self, ctx, o):
        pass
    
    # Stmt
    def visitVarDecl(self, ctx, o): 
        pass
     
    def visitConstDecl(self, ctx, o):
        pass
        
    def visitBlock(self, ctx, o):
        pass
    
    def visitAssign(self, ctx, o): 
        pass

    def visitIf(self, ctx, o): 
        pass
    
    def visitFor(self, ctx, o): 
        pass
    
    def visitBreak(self, ctx, o): 
        pass
     
    def visitContinue(self, ctx, o): 
        pass
     
    def visitReturn(self, ctx, o): 
        pass
     
    def visitCallStmt(self, ctx, o): 
        pass
                            
    # Expression
    def visitBinaryOp(self, ctx, o): 
        pass
     
    def visitUnaryOp(self, ctx, o): 
        pass
    
    def visitCallExpr(self, ctx, o): 
        pass
     
    def visitNewExpr(self, ctx, o): 
        pass
     
    def visitIntLiteral(self, ctx, o): 
        return self.emit.emitPUSHICONST(ctx.value, o.frame), IntType()
    
    def visitFloatLiteral(self, ctx, o): 
        return self.emit.emitPUSHFCONST(str(ctx.value), o.frame), FloatType()
    
    def visitStringLiteral(self, ctx, o): 
        return self.emit.emitPUSHCONST(ctx.value, StringType(), o.frame), StringType()
    
    def visitBooleanLiteral(self, ctx, o): 
        return self.emit.emitPUSHICONST(str(ctx.value), o.frame), BoolType()
     
    def visitNullLiteral(self, ctx, o): 
        pass
    
    def visitSelfLiteral(self, ctx, o): 
        pass
    
    def visitId(self, ctx, o): 
        pass
        
    def visitArrayLiteral(self, ctx, o): 
        pass
            
    def visitArrayCell(self, ctx, o): 
        pass
            
    def visitFieldAccess(self, ctx, o): 
        pass
                
    # Data Type
    def visitIntType(self, ctx, o): 
        return 'I'
     
    def visitFloatType(self, ctx, o): 
        return 'F'
     
    def visitBoolType(self, ctx, o): 
        return 'Z'
     
    def visitStringType(self, ctx, o): 
        return 'StringType'
     
    def visitArrayType(self, ctx, o): 
        return "[" + self.visit(ctx.eleType, o)
     
    def visitClassType(self, ctx , o): 
        return ctx.name
    
    # Instance vs Static
    def visitInstance(self, ctx, o): 
        return "I"
     
    def visitStatic(self, ctx, o): 
        return "S"
     
    
    

    
