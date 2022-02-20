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
                Foreach(i In 1 .. 2){
                    s = s + i;
                    Out.print("2346", i);
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
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(52))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(5))),MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([VarDecl(Id(s),IntType,IntLit(3)),None,Call(Self(),Id(notMain),[]),Return(Id(s))])),MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(sdf),ArrayType(4,ArrayType(3,FloatType))),Call(Self(),Id(notMain),[BooleanLit(True),Id(sdf)]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 310))
    
    def test_simple_program_401(self):
        """ Simple program with nothing
            First testcase from BKEL """
        input = """
        Class Program{

        }
        """
        expect = """Program([ClassDecl(Id(Program),[])])"""
        self.assertTrue(TestAST.test(input, expect, 401))

    def test_simple_program_402(self):
        """ Simple program with nothing
        Second testcase from BKEL """
        input = "Class Rectangle : Shape {}"
        expect = """Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"""
        self.assertTrue(TestAST.test(input, expect, 402))

    def test_simple_program_403(self):
        """ Simple program with nothing
        Third testcase from BKEL """
        input = """
        Class Rectangle {
            Var length: Int;
        }"""
        expect = """Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"""
        self.assertTrue(TestAST.test(input, expect, 403))
        
    def test_simple_program_404(self):
        """Simple program, with few class members"""
        input = """
        Class Rectangle {
            Var b, c, $d, $e, _f: Float = 10, -20.1, 30.2, 40.3, 50.4 - 1;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(10))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,UnaryOp(-,FloatLit(20.1)))),AttributeDecl(Static,VarDecl(Id($d),FloatType,FloatLit(30.2))),AttributeDecl(Static,VarDecl(Id($e),FloatType,FloatLit(40.3))),AttributeDecl(Instance,VarDecl(Id(_f),FloatType,BinaryOp(-,FloatLit(50.4),IntLit(1))))])])"
        self.assertTrue(TestAST.test(input, expect, 404))

    def test_simple_program_405(self):
        """Simple program, with few class members"""
        input = """
        Class Program{
            Var x, $y, z: Int;
            Val t: Float = 3.108;
            Var f: Float;
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Static,VarDecl(Id($y),IntType)),AttributeDecl(Instance,VarDecl(Id(z),IntType)),AttributeDecl(Instance,ConstDecl(Id(t),FloatType,FloatLit(3.108))),AttributeDecl(Instance,VarDecl(Id(f),FloatType))])])"""
        self.assertTrue(TestAST.test(input, expect, 405))

    def test_simple_program_406(self):
        """Simple program, with nothing but inheritance and many classes"""
        input = """
        Class Program : Parent{}
        Class Subprogram{}
        """
        expect = """Program([ClassDecl(Id(Program),Id(Parent),[]),ClassDecl(Id(Subprogram),[])])"""
        self.assertTrue(TestAST.test(input, expect, 406))

    def test_simple_program_407(self):
        """Simple program, with an array attribute member"""
        input = """
        Class Program{
            Var arr: Array[Array[Float, 2], 1];
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1,ArrayType(2,FloatType))))])])"""
        self.assertTrue(TestAST.test(input, expect, 407))
    
    def test_simple_program_408(self):
        """Simple program, with few assigned array attribute member"""
        input = """
        Class Program{
            Var arr, brr: Array[Int, 3] = Array(1, 2, 3), Array(5, -4, 1);
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(3,IntType),[IntLit(1),IntLit(2),IntLit(3)])),AttributeDecl(Instance,VarDecl(Id(brr),ArrayType(3,IntType),[IntLit(5),UnaryOp(-,IntLit(4)),IntLit(1)]))])])"""
        self.assertTrue(TestAST.test(input, expect, 408))

    def test_simple_program_409(self):
        """Simple program, with assigned member that are expression"""
        input = """
        Class Program{
            Val a: Int = 4 + 5;
            Var $b: Float = a + 2.3;
            Val c, d: Int = 0x413EFFAB, 0B0;
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(4),IntLit(5)))),AttributeDecl(Static,VarDecl(Id($b),FloatType,BinaryOp(+,Id(a),FloatLit(2.3)))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(1094647723))),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(0)))])])"""
        self.assertTrue(TestAST.test(input, expect, 409))

    def test_simple_program_410(self):
        """Simple program, with an assigned array attribute member that is nested array (mtd_array)"""
        input = """
        Class Program{
            Val arr, $brr: Array[Array[Float, 2], 3] = Array(Array(2.1, -1.3), Array(0.1, 3.1e3), Array(-0.00001, 123.321E-123)), Array(Array(1.2, 0.132), Array(0.9931, 10.1e3), Array(0.00001111, 1111111119.332321e-2));
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(arr),ArrayType(3,ArrayType(2,FloatType)),[[FloatLit(2.1),UnaryOp(-,FloatLit(1.3))],[FloatLit(0.1),FloatLit(3100.0)],[UnaryOp(-,FloatLit(1e-05)),FloatLit(1.23321e-121)]])),AttributeDecl(Static,ConstDecl(Id($brr),ArrayType(3,ArrayType(2,FloatType)),[[FloatLit(1.2),FloatLit(0.132)],[FloatLit(0.9931),FloatLit(10100.0)],[FloatLit(1.111e-05),FloatLit(11111111.19332321)]]))])])"""
        self.assertTrue(TestAST.test(input, expect, 410))

    ## Wrong
    def test_simple_program_411(self):
        """Simple program, with an attribute and a method with variable"""
        input = """
        Class Program {
            Val $c: Int = 0x413EFFAB;
            main(){
                Var f: Int = 0x413EFFAB;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($c),IntType,IntLit(1094647723))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(f),IntType,IntLit(1094647723))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 411))

    def test_method_412(self):
        """Simple program, with a param-passed method with variable"""
        input = """
        Class Program{
            notMain(f: Boolean; arr: Array[Array[Float, 3], 4]){
                Val a, b, c: Int = 500, 600, 700;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([ConstDecl(Id(a),IntType,IntLit(500)),ConstDecl(Id(b),IntType,IntLit(600)),ConstDecl(Id(c),IntType,IntLit(700))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 412))

    def test_simple_program_413(self):
        """Simple program, with a param-passed method with variable"""
        input = """
        Class Program{
            notMain(f: Boolean){
                Val a, b: Array[Int, 4] = Array(1, 0B101011, 03132, 0x123), Array(-4, 31, 0xEFFE, 5);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType)],Block([ConstDecl(Id(a),ArrayType(4,IntType),[IntLit(1),IntLit(43),IntLit(1626),IntLit(291)]),ConstDecl(Id(b),ArrayType(4,IntType),[UnaryOp(-,IntLit(4)),IntLit(31),IntLit(61438),IntLit(5)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 413))