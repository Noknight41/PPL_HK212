import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):    
    def test_301(self):
        input = """
        Class Program{
            Var a,b : Int;
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])"""
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_302(self):
        input = """
        Class Program{
            Var t: Float = 1.00;
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(t),FloatType,FloatLit(1.0)))])])"""
        self.assertTrue(TestAST.test(input,expect,302))
    
    def test_303(self):
        input = """
        Class Program{
            hello(){
                Val d: Int =  1;
                d = 2;
                If(d > 2){
                    Val s: Int;
                    d = d + 1;
                }
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(hello),Instance,[],Block([ConstDecl(Id(d),IntType,IntLit(1)),AssignStmt(Id(d),IntLit(2)),If(BinaryOp(>,None,IntLit(2)),Block([ConstDecl(Id(s),IntType,None),AssignStmt(Id(d),BinaryOp(+,None,IntLit(1)))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,303))
    
    def test_304(self):
        input = """
        Class Sum{
            Val x : Int = 1;
            Constructor(x : Int){
                Self.x = x;
            }
        }
        
        Class Program{
            hello(){
                Val d: Int =  1;
                d = 2;
                If(d > 2){
                    d = d + 1;
                }
            }
        }"""
        expect = """Program([ClassDecl(Id(Sum),[AttributeDecl(Instance,ConstDecl(Id(x),IntType,IntLit(1))),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(x)),None)]))]),ClassDecl(Id(Program),[MethodDecl(Id(hello),Instance,[],Block([ConstDecl(Id(d),IntType,IntLit(1)),AssignStmt(Id(d),IntLit(2)),If(BinaryOp(>,None,IntLit(2)),Block([AssignStmt(Id(d),BinaryOp(+,None,IntLit(1)))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,304))
    
    def test_305(self):
        input = """
        Class Program {
            Var a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
                c = Array();
                d = Array("1", "2", "3");
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(100,StringType))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(c),[]),AssignStmt(Id(d),[StringLit(1),StringLit(2),StringLit(3)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,305))
    
    def test_306(self):
        input = """
        Class Program {
            Var a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
                d = Array("1", "2", "3");
                Var e: Array[Array[Array[Int,3],2],2] = Array(
                    Array(Array(1,3,4), Array(1,5,6)),
                    Array(Array(1,7,8), Array(1,9,10))
                );
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(100,StringType))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(d),[StringLit(1),StringLit(2),StringLit(3)]),VarDecl(Id(e),ArrayType(2,ArrayType(2,ArrayType(3,IntType))),[[[IntLit(1),IntLit(3),IntLit(4)],[IntLit(1),IntLit(5),IntLit(6)]],[[IntLit(1),IntLit(7),IntLit(8)],[IntLit(1),IntLit(9),IntLit(10)]]])]))])])"""
        self.assertTrue(TestAST.test(input,expect,306))
   
    def test_307(self):
        input = """
        Class Program {
            Var _Fool, _Magician: Array[Int, 5];
            main(){
                
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(_Fool),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(_Magician),ArrayType(5,IntType))),MethodDecl(Id(main),Instance,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,307))
    
    def test_307(self):
        input = """
        Class Program {
            Val c: Int = 0x413EFFAB;
            main(){
                Val c: Int = 0x413EFFAB;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(1094647723))),MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(c),IntType,IntLit(1094647723))]))])])"""
        self.assertTrue(TestAST.test(input,expect,307))