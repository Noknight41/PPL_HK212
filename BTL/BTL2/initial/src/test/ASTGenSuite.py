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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(hello),Instance,[],Block([ConstDecl(Id(d),IntType,IntLit(1)),AssignStmt(Id(d),IntLit(2)),If(BinaryOp(>,Id(d),IntLit(2)),Block([ConstDecl(Id(s),IntType,None),AssignStmt(Id(d),BinaryOp(+,Id(d),IntLit(1)))]))]))])])"""
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
        expect = """Program([ClassDecl(Id(Sum),[AttributeDecl(Instance,ConstDecl(Id(x),IntType,IntLit(1))),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(x)),Id(x))]))]),ClassDecl(Id(Program),[MethodDecl(Id(hello),Instance,[],Block([ConstDecl(Id(d),IntType,IntLit(1)),AssignStmt(Id(d),IntLit(2)),If(BinaryOp(>,Id(d),IntLit(2)),Block([AssignStmt(Id(d),BinaryOp(+,Id(d),IntLit(1)))]))]))])])"""
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
    
    def test_308(self):
        input = """
        Class Program{
            notMain(f: Boolean; arr: Array[Array[Float, 3], 4]){
                Val a, b, c: Int = 500, 600, 700;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([ConstDecl(Id(a),IntType,IntLit(500)),ConstDecl(Id(b),IntType,IntLit(600)),ConstDecl(Id(c),IntType,IntLit(700))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    
    def test_309(self):
        input = """
        Class Program{
            Var a, $b : Int;
            Val c, $d : Boolean;
            Var e, $f : Int = 023, 0x45;
            Val w, $x : Float = 0.01, .3e2;
            notMain(f: Boolean; arr: Array[Array[Float, 3], 4]){
                Var a : Int;
                Val c : Boolean;
                Var e, f : Int = 023, 0x45;
                Val w, x : Float = 0.01, .3e2;
                Return a + c + e + w;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType)),AttributeDecl(Instance,ConstDecl(Id(c),BoolType,None)),AttributeDecl(Static,ConstDecl(Id($d),BoolType,None)),AttributeDecl(Instance,VarDecl(Id(e),IntType,IntLit(19))),AttributeDecl(Static,VarDecl(Id($f),IntType,IntLit(69))),AttributeDecl(Instance,ConstDecl(Id(w),FloatType,FloatLit(0.01))),AttributeDecl(Static,ConstDecl(Id($x),FloatType,FloatLit(30.0))),MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([VarDecl(Id(a),IntType),ConstDecl(Id(c),BoolType,None),VarDecl(Id(e),IntType,IntLit(19)),VarDecl(Id(f),IntType,IntLit(69)),ConstDecl(Id(w),FloatType,FloatLit(0.01)),ConstDecl(Id(x),FloatType,FloatLit(30.0)),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),Id(c)),Id(e)),Id(w)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 309))
    
    def test_310(self):
        input = """
        Class Program{
            Var a, $b : Int = 0x34, 0b101;
            notMain(f: Boolean; arr: Array[Array[Float, 3], 4]){
                Var s : Int = 3;
                For(i In 1 .. 2){
                    s = s + i;
                    print("2346", i);
                    Continue;
                    Break;
                }
                Self.notMain();
                Return s;
            }
            main(){
                Var sdf :  Array[Array[Float, 3], 4];
                Self.notMain(True, sdf);
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType)),AttributeDecl(Instance,ConstDecl(Id(c),BoolType,None)),AttributeDecl(Static,ConstDecl(Id($d),BoolType,None)),AttributeDecl(Instance,VarDecl(Id(e),IntType,IntLit(19))),AttributeDecl(Static,VarDecl(Id($f),IntType,IntLit(69))),AttributeDecl(Instance,ConstDecl(Id(w),FloatType,FloatLit(0.01))),AttributeDecl(Static,ConstDecl(Id($x),FloatType,FloatLit(30.0))),MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([VarDecl(Id(a),IntType),ConstDecl(Id(c),BoolType,None),VarDecl(Id(e),IntType,IntLit(19)),VarDecl(Id(f),IntType,IntLit(69)),ConstDecl(Id(w),FloatType,FloatLit(0.01)),ConstDecl(Id(x),FloatType,FloatLit(30.0)),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),Id(c)),Id(e)),Id(w)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 309))