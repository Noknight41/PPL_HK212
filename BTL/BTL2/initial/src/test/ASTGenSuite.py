import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):    
    # def test_301(self):
    #     input = """
    #     Class Program{
    #         Var a,b : Int;
    #     }"""
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])"""
    #     self.assertTrue(TestAST.test(input,expect,301))
    
    # def test_302(self):
    #     input = """
    #     Class Program{
    #         Var t: Float = 1.00;
    #     }"""
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(t),FloatType,FloatLit(1.0)))])])"""
    #     self.assertTrue(TestAST.test(input,expect,302))
    
    # def test_303(self):
    #     input = """
    #     Class Program{
    #         hello(){
    #             Val d: Int =  1;
    #             d = 2;
    #             If(d > 2){
    #                 Val s: Int;
    #                 d = d + 1;
    #             }
    #         }
    #     }"""
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(hello),Instance,[],Block([ConstDecl(Id(d),IntType,IntLit(1)),AssignStmt(Id(d),IntLit(2)),If(BinaryOp(>,Id(d),IntLit(2)),Block([ConstDecl(Id(s),IntType,None),AssignStmt(Id(d),BinaryOp(+,Id(d),IntLit(1)))]))]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,303))
    
    # def test_304(self):
    #     input = """
    #     Class Sum{
    #         Val x : Int = 1;
    #         Constructor(x : Int){
    #             Self.x = x;
    #         }
    #     }
        
    #     Class Program{
    #         hello(){
    #             Val d: Int =  1;
    #             d = 2;
    #             If(d > 2){
    #                 d = d + 1;
    #             }
    #         }
    #     }"""
    #     expect = """Program([ClassDecl(Id(Sum),[AttributeDecl(Instance,ConstDecl(Id(x),IntType,IntLit(1))),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(x)),Id(x))]))]),ClassDecl(Id(Program),[MethodDecl(Id(hello),Instance,[],Block([ConstDecl(Id(d),IntType,IntLit(1)),AssignStmt(Id(d),IntLit(2)),If(BinaryOp(>,Id(d),IntLit(2)),Block([AssignStmt(Id(d),BinaryOp(+,Id(d),IntLit(1)))]))]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,304))
    
    # def test_305(self):
    #     input = """
    #     Class Program {
    #         Var a, b: Array[Int, 5];
    #         Var c: Array[String, 10_0];
    #         main() {
    #             c = Array();
    #             d = Array("1", "2", "3");
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(100,StringType))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(c),[]),AssignStmt(Id(d),[StringLit(1),StringLit(2),StringLit(3)])]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,305))
    
    # def test_306(self):
    #     input = """
    #     Class Program {
    #         Var a, b: Array[Int, 5];
    #         Var c: Array[String, 10_0];
    #         main() {
    #             d = Array("1", "2", "3");
    #             Var e: Array[Array[Array[Int,3],2],2] = Array(
    #                 Array(Array(1,3,4), Array(1,5,6)),
    #                 Array(Array(1,7,8), Array(1,9,10))
    #             );
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(100,StringType))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(d),[StringLit(1),StringLit(2),StringLit(3)]),VarDecl(Id(e),ArrayType(2,ArrayType(2,ArrayType(3,IntType))),[[[IntLit(1),IntLit(3),IntLit(4)],[IntLit(1),IntLit(5),IntLit(6)]],[[IntLit(1),IntLit(7),IntLit(8)],[IntLit(1),IntLit(9),IntLit(10)]]])]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,306))
   
    # def test_307(self):
    #     input = """
    #     Class Program {
    #         Var _Fool, _Magician: Array[Int, 5];
    #         main(){
                
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(_Fool),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(_Magician),ArrayType(5,IntType))),MethodDecl(Id(main),Static,[],Block([]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,307))
    
    # def test_307(self):
    #     input = """
    #     Class Program {
    #         Val c: Int = 0x413EFFAB;
    #         main(){
    #             Val c: Int = 0x413EFFAB;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(1094647723))),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(c),IntType,IntLit(1094647723))]))])])"""
    #     self.assertTrue(TestAST.test(input,expect,307))
    
    # def test_308(self):
    #     input = """
    #     Class Program{
    #         notMain(f: Boolean; arr: Array[Array[Float, 3], 4]){
    #             Val a, b, c: Int = 500, 600, 700;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([ConstDecl(Id(a),IntType,IntLit(500)),ConstDecl(Id(b),IntType,IntLit(600)),ConstDecl(Id(c),IntType,IntLit(700))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 308))
    
    # def test_309(self):
    #     input = """
    #     Class Program{
    #         Var a, $b : Int;
    #         Val c, $d : Boolean;
    #         Var e, $f : Int = 023, 0x45;
    #         Val w, $x : Float = 0.01, .3e2;
    #         notMain(f: Boolean; arr: Array[Array[Float, 3], 4]){
    #             Var a : Int;
    #             Val c : Boolean;
    #             Var e, f : Int = 023, 0x45;
    #             Val w, x : Float = 0.01, .3e2;
    #             Return a + c + e + w;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType)),AttributeDecl(Instance,ConstDecl(Id(c),BoolType,None)),AttributeDecl(Static,ConstDecl(Id($d),BoolType,None)),AttributeDecl(Instance,VarDecl(Id(e),IntType,IntLit(19))),AttributeDecl(Static,VarDecl(Id($f),IntType,IntLit(69))),AttributeDecl(Instance,ConstDecl(Id(w),FloatType,FloatLit(0.01))),AttributeDecl(Static,ConstDecl(Id($x),FloatType,FloatLit(30.0))),MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([VarDecl(Id(a),IntType),ConstDecl(Id(c),BoolType,None),VarDecl(Id(e),IntType,IntLit(19)),VarDecl(Id(f),IntType,IntLit(69)),ConstDecl(Id(w),FloatType,FloatLit(0.01)),ConstDecl(Id(x),FloatType,FloatLit(30.0)),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),Id(c)),Id(e)),Id(w)))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 309))
    
    # def test_310(self):
    #     input = """
    #     Class Program{
    #         Var a, $b : Int = 0x34, 0b101;
    #         notMain(f: Boolean; arr: Array[Array[Float, 3], 4]){
    #             Var s : Int = 3;
    #             Foreach(i In 1 .. 2){
    #                 s = s + i;
    #                 Out.print("2346", i);
    #                 Continue;
    #                 Break;
    #             }
    #             Self.notMain();
    #             Return s;
    #         }
    #         main(){
    #             Var sdf :  Array[Array[Float, 3], 4];
    #             Self.notMain(True, sdf);
    #             Return;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(52))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(5))),MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([VarDecl(Id(s),IntType,IntLit(3)),None,Call(Self(),Id(notMain),[]),Return(Id(s))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(sdf),ArrayType(4,ArrayType(3,FloatType))),Call(Self(),Id(notMain),[BooleanLit(True),Id(sdf)]),Return()]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 310))
    
    def test_311(self):
        input = """
        Class Any{
            Var x, y: Float = .15e-2, .e4;
            Constructor(z, t : Float; z: String){
                Foreach(csalar In 0b10101 .. 0x2A){
                    If (!(z ==. "2")){
                        z = z +. "3";
                        Continue;
                        Self.x = Self.x + z - 2.0 * t;
                        Self.y = Self.y + t - 2.0 * z;
                    }
                    Else{
                        Self.x = Self.x + t;
                        Self.y = Self.y + z;
                        Break;
                    }
                }
            }
            Destructor(){
                Self.x = .e1;
                Self.y = .e1;
            }
            getAny(){
                Out.print(Self.x);
            }
        }
        Class Value : Any{
            Var stem: Array[Float, 0xA];
            Constructor(x : Int; y: Float; d: Any){
                Self.x = d.x;
                Self.y = d.y;
                Foreach(i In 1 .. x){
                    Self.stem[i] = Self.x + y + i;
                    If((Self.stem[i] + Self.x > Self.y) && (Self.stem[i] > Self.stem[i+1])){
                        Break;
                    }
                }
            }
            Destructor(){
                Var d: Any = Null;
                d = New Any(2.4,3.5,"2");
            }
        }
        Class Variable : Value{
            main(){
                Self.stem[2] = 1e-25;
                Return Self.stem;
            }
        }
        Class Program{
            main(){
               Val d: Any = New Any(1.0, 3.0, "23");
               Val c: Value = New Value(14,0.5,d);
               Var b: Variable = New Variable(13,0.5,d);
               Var a: Array[Float, 0xF] = b.main();
               b.getAny();
            }
        }
        """
        expect = """Program([ClassDecl(Id(Any),[AttributeDecl(Instance,VarDecl(Id(x),FloatType,FloatLit(0.0015))),AttributeDecl(Instance,VarDecl(Id(y),FloatType,FloatLit(0.0))),MethodDecl(Id(Constructor),Instance,[param(Id(z),FloatType),param(Id(t),FloatType),param(Id(z),StringType)],Block([For(Id(csalar),IntLit(21),IntLit(42),IntLit(1),Block([If(UnaryOp(!,BinaryOp(==.,Id(z),StringLit(2))),Block([AssignStmt(Id(z),BinaryOp(+.,Id(z),StringLit(3))),Continue,AssignStmt(FieldAccess(Self(),Id(x)),BinaryOp(-,BinaryOp(+,FieldAccess(Self(),Id(x)),Id(z)),BinaryOp(*,FloatLit(2.0),Id(t)))),AssignStmt(FieldAccess(Self(),Id(y)),BinaryOp(-,BinaryOp(+,FieldAccess(Self(),Id(y)),Id(t)),BinaryOp(*,FloatLit(2.0),Id(z))))]),Block([AssignStmt(FieldAccess(Self(),Id(x)),BinaryOp(+,FieldAccess(Self(),Id(x)),Id(t))),AssignStmt(FieldAccess(Self(),Id(y)),BinaryOp(+,FieldAccess(Self(),Id(y)),Id(z))),Break]))])])])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(x)),FloatLit(0.0)),AssignStmt(FieldAccess(Self(),Id(y)),FloatLit(0.0))])),MethodDecl(Id(getAny),Instance,[],Block([Call(Id(Out),Id(print),[FieldAccess(Self(),Id(x))])]))]),ClassDecl(Id(Value),Id(Any),[AttributeDecl(Instance,VarDecl(Id(stem),ArrayType(10,FloatType))),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),FloatType),param(Id(d),ClassType(Id(Any)))],Block([AssignStmt(FieldAccess(Self(),Id(x)),FieldAccess(Id(d),Id(x))),AssignStmt(FieldAccess(Self(),Id(y)),FieldAccess(Id(d),Id(y))),For(Id(i),IntLit(1),Id(x),IntLit(1),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(stem)),[Id(i)]),BinaryOp(+,BinaryOp(+,FieldAccess(Self(),Id(x)),Id(y)),Id(i))),If(BinaryOp(&&,BinaryOp(>,BinaryOp(+,ArrayCell(FieldAccess(Self(),Id(stem)),[Id(i)]),FieldAccess(Self(),Id(x))),FieldAccess(Self(),Id(y))),BinaryOp(>,ArrayCell(FieldAccess(Self(),Id(stem)),[Id(i)]),ArrayCell(FieldAccess(Self(),Id(stem)),[BinaryOp(+,Id(i),IntLit(1))]))),Block([Break]))])])])),MethodDecl(Id(Destructor),Instance,[],Block([VarDecl(Id(d),ClassType(Id(Any)),NullLiteral()),AssignStmt(Id(d),NewExpr(Id(Any),[FloatLit(2.4),FloatLit(3.5),StringLit(2)]))]))]),ClassDecl(Id(Variable),Id(Value),[MethodDecl(Id(main),Instance,[],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(stem)),[IntLit(2)]),FloatLit(1e-25)),Return(FieldAccess(Self(),Id(stem)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(d),ClassType(Id(Any)),NewExpr(Id(Any),[FloatLit(1.0),FloatLit(3.0),StringLit(23)])),ConstDecl(Id(c),ClassType(Id(Value)),NewExpr(Id(Value),[IntLit(14),FloatLit(0.5),Id(d)])),VarDecl(Id(b),ClassType(Id(Variable)),NewExpr(Id(Variable),[IntLit(13),FloatLit(0.5),Id(d)])),VarDecl(Id(a),ArrayType(15,FloatType),CallExpr(Id(b),Id(main),[])),Call(Id(b),Id(getAny),[])]))])])""" 
        self.assertTrue(TestAST.test(input, expect, 311))
    
    # def test_simple_program_401(self):
    #     """ Simple program with nothing
    #         First testcase from BKEL """
    #     input = """
    #     Class Program{

    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[])])"""
    #     self.assertTrue(TestAST.test(input, expect, 401))

    # def test_simple_program_402(self):
    #     """ Simple program with nothing
    #     Second testcase from BKEL """
    #     input = "Class Rectangle : Shape {}"
    #     expect = """Program([ClassDecl(Id(Rectangle),Id(Shape),[])])"""
    #     self.assertTrue(TestAST.test(input, expect, 402))

    # def test_simple_program_403(self):
    #     """ Simple program with nothing
    #     Third testcase from BKEL """
    #     input = """
    #     Class Rectangle {
    #         Var length: Int;
    #     }"""
    #     expect = """Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(length),IntType))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 403))
        
    # def test_simple_program_404(self):
    #     """Simple program, with few class members"""
    #     input = """
    #     Class Rectangle {
    #         Var b, c, $d, $e, _f: Float = 10, -20.1, 30.2, 40.3, 50.4 - 1;
    #     }"""
    #     expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(10))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,UnaryOp(-,FloatLit(20.1)))),AttributeDecl(Static,VarDecl(Id($d),FloatType,FloatLit(30.2))),AttributeDecl(Static,VarDecl(Id($e),FloatType,FloatLit(40.3))),AttributeDecl(Instance,VarDecl(Id(_f),FloatType,BinaryOp(-,FloatLit(50.4),IntLit(1))))])])"
    #     self.assertTrue(TestAST.test(input, expect, 404))

    # def test_simple_program_405(self):
    #     """Simple program, with few class members"""
    #     input = """
    #     Class Program{
    #         Var x, $y, z: Int;
    #         Val t: Float = 3.108;
    #         Var f: Float;
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Static,VarDecl(Id($y),IntType)),AttributeDecl(Instance,VarDecl(Id(z),IntType)),AttributeDecl(Instance,ConstDecl(Id(t),FloatType,FloatLit(3.108))),AttributeDecl(Instance,VarDecl(Id(f),FloatType))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 405))

    # def test_simple_program_406(self):
    #     """Simple program, with nothing but inheritance and many classes"""
    #     input = """
    #     Class Program : Parent{}
    #     Class Subprogram{}
    #     """
    #     expect = """Program([ClassDecl(Id(Program),Id(Parent),[]),ClassDecl(Id(Subprogram),[])])"""
    #     self.assertTrue(TestAST.test(input, expect, 406))

    # def test_simple_program_407(self):
    #     """Simple program, with an array attribute member"""
    #     input = """
    #     Class Program{
    #         Var arr: Array[Array[Float, 2], 1];
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(1,ArrayType(2,FloatType))))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 407))
    
    # def test_simple_program_408(self):
    #     """Simple program, with few assigned array attribute member"""
    #     input = """
    #     Class Program{
    #         Var arr, brr: Array[Int, 3] = Array(1, 2, 3), Array(5, -4, 1);
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(arr),ArrayType(3,IntType),[IntLit(1),IntLit(2),IntLit(3)])),AttributeDecl(Instance,VarDecl(Id(brr),ArrayType(3,IntType),[IntLit(5),UnaryOp(-,IntLit(4)),IntLit(1)]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 408))

    # def test_simple_program_409(self):
    #     """Simple program, with assigned member that are expression"""
    #     input = """
    #     Class Program{
    #         Val a: Int = 4 + 5;
    #         Var $b: Float = a + 2.3;
    #         Val c, d: Int = 0x413EFFAB, 0B0;
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(4),IntLit(5)))),AttributeDecl(Static,VarDecl(Id($b),FloatType,BinaryOp(+,Id(a),FloatLit(2.3)))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,IntLit(1094647723))),AttributeDecl(Instance,ConstDecl(Id(d),IntType,IntLit(0)))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 409))

    # def test_simple_program_410(self):
    #     """Simple program, with an assigned array attribute member that is nested array (mtd_array)"""
    #     input = """
    #     Class Program{
    #         Val arr, $brr: Array[Array[Float, 2], 3] = Array(Array(2.1, -1.3), Array(0.1, 3.1e3), Array(-0.00001, 123.321E-123)), Array(Array(1.2, 0.132), Array(0.9931, 10.1e3), Array(0.00001111, 1111111119.332321e-2));
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(arr),ArrayType(3,ArrayType(2,FloatType)),[[FloatLit(2.1),UnaryOp(-,FloatLit(1.3))],[FloatLit(0.1),FloatLit(3100.0)],[UnaryOp(-,FloatLit(1e-05)),FloatLit(1.23321e-121)]])),AttributeDecl(Static,ConstDecl(Id($brr),ArrayType(3,ArrayType(2,FloatType)),[[FloatLit(1.2),FloatLit(0.132)],[FloatLit(0.9931),FloatLit(10100.0)],[FloatLit(1.111e-05),FloatLit(11111111.19332321)]]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 410))

    # ## Wrong
    # def test_simple_program_411(self):
    #     """Simple program, with an attribute and a method with variable"""
    #     input = """
    #     Class Program {
    #         Val $c: Int = 0x413EFFAB;
    #         main(){
    #             Var f: Int = 0x413EFFAB;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($c),IntType,IntLit(1094647723))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(f),IntType,IntLit(1094647723))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 411))

    # def test_method_412(self):
    #     """Simple program, with a param-passed method with variable"""
    #     input = """
    #     Class Program{
    #         notMain(f: Boolean; arr: Array[Array[Float, 3], 4]){
    #             Val a, b, c: Int = 500, 600, 700;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([ConstDecl(Id(a),IntType,IntLit(500)),ConstDecl(Id(b),IntType,IntLit(600)),ConstDecl(Id(c),IntType,IntLit(700))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 412))

    # def test_simple_program_413(self):
    #     """Simple program, with a param-passed method with variable"""
    #     input = """
    #     Class Program{
    #         notMain(f: Boolean){
    #             Val a, b: Array[Int, 4] = Array(1, 0B101011, 03132, 0x123), Array(-4, 31, 0xEFFE, 5);
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType)],Block([ConstDecl(Id(a),ArrayType(4,IntType),[IntLit(1),IntLit(43),IntLit(1626),IntLit(291)]),ConstDecl(Id(b),ArrayType(4,IntType),[UnaryOp(-,IntLit(4)),IntLit(31),IntLit(61438),IntLit(5)])]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 413))
    
    # def test_simple_program_414(self):
    #     """Simple program, to check output of other than Decimal-base Integer"""
    #     input = """
    #     Class Program{
    #         Val a, b, $c, $d, e, $f: Int = 037415, 1239651, 0x1239EDF, 0xABCDEF01, 0b1000101, 0B110101;
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(16141))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(1239651))),AttributeDecl(Static,ConstDecl(Id($c),IntType,IntLit(19111647))),AttributeDecl(Static,ConstDecl(Id($d),IntType,IntLit(2882400001))),AttributeDecl(Instance,ConstDecl(Id(e),IntType,IntLit(69))),AttributeDecl(Static,ConstDecl(Id($f),IntType,IntLit(53)))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 414))

    # def test_simple_program_415(self):
    #     """Simple program, to check output of other than Decimal-base Integer"""
    #     input = """
    #     Class Program{
    #         main(inp: Int){
    #             Var a: Float;
    #             a = 3.5031041095815;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(inp),IntType)],Block([VarDecl(Id(a),FloatType),AssignStmt(Id(a),FloatLit(3.5031041095815))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 415))

    # def test_simple_program_416(self):
    #     """Simple program, to check assignment statement of array cell"""
    #     input = """
    #     Class Program{
    #         main(){
    #             Var a: Array[Boolean, 4];
    #             a[0] = True;
    #             a[1] = a[0];
    #             a[1 + 1] = False;
    #             a[0xC / 0b100] = True;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(4,BoolType)),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(a),[IntLit(0)])),AssignStmt(ArrayCell(Id(a),[BinaryOp(+,IntLit(1),IntLit(1))]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,IntLit(12),IntLit(4))]),BooleanLit(True))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 416))

    # def test_simple_program_417(self):
    #     """Simple program, to check assignment statement of multidimensional array cell"""
    #     input = """
    #     Class Program{
    #         main(){
    #             Var a: Array[Array[Boolean, 3], 2];
    #             a[0][0] = True;
    #             a[0][1] = False;
    #             a[1][0] = True;
    #             a[1][1] = False;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(2,ArrayType(3,BoolType))),AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(1)]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1)]),BooleanLit(False))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 417))

    # def test_simple_program_418(self):
    #     """Simple program, to check assignment statement of multidimensional array cell"""
    #     input = """
    #     Class Program{
    #         main(){
    #             Var a: Array[Array[Boolean, 2], 2];
    #             a[0][0 * 10000000] = True;
    #             a[0][3 * 2 * 1 / 6] = False;
    #             a[0x270F / 9999][0 * 0B1011110101] = True;
    #             a[9999 / 0x270F][1 * 9 / 9 + 0] = Sys.sampleArray[a[0x1]];
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(2,ArrayType(2,BoolType))),AssignStmt(ArrayCell(Id(a),[IntLit(0),BinaryOp(*,IntLit(0),IntLit(10000000))]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(0),BinaryOp(/,BinaryOp(*,BinaryOp(*,IntLit(3),IntLit(2)),IntLit(1)),IntLit(6))]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,IntLit(9999),IntLit(9999)),BinaryOp(*,IntLit(0),IntLit(757))]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,IntLit(9999),IntLit(9999)),BinaryOp(+,BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(9)),IntLit(9)),IntLit(0))]),ArrayCell(FieldAccess(Id(Sys),Id(sampleArray)),[ArrayCell(Id(a),[IntLit(1)])]))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 418))

    # def test_simple_program_419(self):
    #     """Simple program, with rhs (all_expr) is a mtd_array"""
    #     input = """
    #     Class Program{
    #         Var a: Array[Array[Boolean, 2], 1];
    #         main(){
    #             Var b: Boolean = a[0][2];
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(1,ArrayType(2,BoolType)))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(b),BoolType,ArrayCell(Id(a),[IntLit(0),IntLit(2)]))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 419))

    # def test_simple_program_420(self):
    #     """Simple program, with lhs is a nested array call"""
    #     input = """
    #     Class Program{
    #         Var a: Array[Array[Boolean, 2], 1];
    #         main(){
    #             a[b[1]] = 123;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(1,ArrayType(2,BoolType)))),MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(b),[IntLit(1)])]),IntLit(123))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 420))

    # def test_simple_program_421(self):
    #     """Simple program, with instance field access and call expr"""
    #     input = """
    #     Class Program{
    #         main(){
    #             a = Prog.b(e, f, g);
    #             b = Program.a;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(Prog),Id(b),[Id(e),Id(f),Id(g)])),AssignStmt(Id(b),FieldAccess(Id(Program),Id(a)))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 421))

    # def test_simple_program_422(self):
    #     """Simple program, with static field access and call expr"""
    #     input = """
    #     Class Program{
    #         main(){
    #             a = Prog::$b(e, f, g);
    #             b = Program::$a;
    #             c = Program::$f;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(Prog),Id($b),[Id(e),Id(f),Id(g)])),AssignStmt(Id(b),FieldAccess(Id(Program),Id($a))),AssignStmt(Id(c),FieldAccess(Id(Program),Id($f)))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 422))

    # def test_simple_program_423(self):
    #     """Simple program, spiderman pointing at each other"""
    #     input = """
    #     Class Program{
    #         Val $a: Int = 5;
    #         Constructor(){
    #             Program::$a = 2;
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(5))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Program),Id($a)),IntLit(2))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 423))
    
    # # def test_simple_program_422(self):
    # #     """Simple program, with static field access and call expr"""
    # #     input = """
    # #     Class Program{
    # #         main(){
    # #             a = Prog::$b(e, f, g);
    # #             b = Program::$a;
    # #             c = Self::$f;
    # #         }
    # #     }
    # #     """
    # #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(Prog),Id($b),[Id(e),Id(f),Id(g)])),AssignStmt(Id(b),FieldAccess(Id(Program),Id($a))),AssignStmt(Id(c),FieldAccess(Self(),Id($f)))]))])])"""
    # #     self.assertTrue(TestAST.test(input, expect, 422))

    # # def test_simple_program_423(self):
    # #     """Simple program, spiderman pointing at each other"""
    # #     input = """
    # #     Class Program{
    # #         Val $a: Int = 5;
    # #         Constructor(){
    # #             Program::$a = Self::$a;
    # #         }
    # #     }
    # #     """
    # #     expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(5))),MethodDecl(Id("Constructor"),Instance,[],Block([AssignStmt(FieldAccess(Id(Program),Id($a)),FieldAccess(Self(),Id($a)))]))])])"""
    # #     self.assertTrue(TestAST.test(input, expect, 423))
    
    # def test_short_program_424(self):
    #     """Simple program with partial If statement"""
    #     input = """
    #     Class Program{
    #         main(){
    #             If (a > b){
    #                 a = 2;
    #             }
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 424))

    # def test_short_program_425(self):
    #     """Simple program with partial If - Elseif statement"""
    #     input = """
    #     Class Program{
    #         main(){
    #             If (a > b){
    #                 a = 2;
    #             }
    #             Elseif (a == b){
    #                 a = 1;
    #             }
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))])))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 425))

    # def test_short_program_426(self):
    #     """Simple program with Complete If - Elseif - Else statement"""
    #     input = """
    #     Class Program{
    #         main(){
    #             If (a > b){
    #                 a = 2;
    #             }
    #             Elseif (a == b){
    #                 a = 1;
    #             }
    #             Else{
    #                 a = 0;
    #             }
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))]),Block([AssignStmt(Id(a),IntLit(0))])))]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 426))

    # def test_short_program_427(self):
    #     input = """
    #     Class Program{
    #         main(){
    #             Foreach (a In 1 .. 100000){
    #                 Global::$b = a + 2;
    #             }
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(a),IntLit(1),IntLit(100000),IntLit(1),Block([AssignStmt(FieldAccess(Id(Global),Id($b)),BinaryOp(+,Id(a),IntLit(2)))])])]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 427))

    # def test_short_program_428(self):
    #     """Short program with complete ForEach loop statement"""
    #     input = """
    #     Class Program{
    #         main(){
    #             Foreach (a In 1 .. 100000 By 5){
    #                 Global::$b = a + 2;
    #             }
    #         }
    #     }
    #     """
    #     expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(a),IntLit(1),IntLit(100000),IntLit(5),Block([AssignStmt(FieldAccess(Id(Global),Id($b)),BinaryOp(+,Id(a),IntLit(2)))])])]))])])"""
    #     self.assertTrue(TestAST.test(input, expect, 428))

    # def test_short_program_429(self):
    #     input = """
    #     Class Program : System{
    #         Val a: Int = 1;
    #         fooBar() {
    #             Program::$fooBar();
    #         }
    #         main() {
    #             If (1 >= 2) {
    #                 Out.fooBar(True);
    #             } 
    #             Elseif (a <= 2) {
    #                 Program::$fooBar();
    #             } 
    #             Elseif (a[1][2] <= a[1] * a.a + Some::$a()) {
    #                 Out.println(400);
    #             } 
    #             Else {
    #                 Out.println("What are you looking for?");
    #             }
    #             Return;
    #         }
    #     }"""
    #     expect = "Program([ClassDecl(Id(Program),Id(System),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),MethodDecl(Id(fooBar),Instance,[],Block([Call(Id(Program),Id($fooBar),[])])),MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>=,IntLit(1),IntLit(2)),Block([Call(Id(Out),Id(fooBar),[BooleanLit(True)])]),If(BinaryOp(<=,Id(a),IntLit(2)),Block([Call(Id(Program),Id($fooBar),[])]),If(BinaryOp(<=,ArrayCell(Id(a),[IntLit(1),IntLit(2)]),BinaryOp(+,BinaryOp(*,ArrayCell(Id(a),[IntLit(1)]),FieldAccess(Id(a),Id(a))),CallExpr(Id(Some),Id($a),[]))),Block([Call(Id(Out),Id(println),[IntLit(400)])]),Block([Call(Id(Out),Id(println),[StringLit(What are you looking for?)])])))),Return()]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 429))

    # def test_short_program_430(self):
    #     """Simple program with 2 methods and 1 return on main"""
    #     input = """
    #     Class Program {
    #         Val a: Int = 1;
    #         fooBar(a, b : Int; c : Float) {
    #             Self.fooBar1(True, False, Null);
    #         }
    #         main() {
    #             Self.fooBar(x, y, "ZhongGuo ren");
    #             Return;
    #         }
    #     }"""
    #     expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),MethodDecl(Id(fooBar),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([Call(Self(),Id(fooBar1),[BooleanLit(True),BooleanLit(False),NullLiteral()])])),MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(fooBar),[Id(x),Id(y),StringLit(ZhongGuo ren)]),Return()]))])])"
    #     self.assertTrue(TestAST.test(input, expect, 430))
    
    def test_float_convert_431(self):
        """Simple program to test the conversion of invalid python float literal (.e-3)"""
        input = """
        Class Program {
            main() {
                Out.println(.e-3);
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(println),[FloatLit(0.0)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 431))

    def test_foreach_loop_432(self):
        """Simple program to test missing and complete Foreach loop"""
        input = """
        Class Program {
            Val b: Float = .e-3;
            main() {
                ## Missing incremental value ##
                Foreach(a In 1 .. 0x1234ABCD){
                    b = b + a / 5;
                }
                Foreach(a In -5 .. 0b1101 By 04){
                    b = b - b / (03);
                }
                Return b;
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(b),FloatType,FloatLit(0.0))),MethodDecl(Id(main),Static,[],Block([For(Id(a),IntLit(1),IntLit(305441741),IntLit(1),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),BinaryOp(/,Id(a),IntLit(5))))])]),For(Id(a),UnaryOp(-,IntLit(5)),IntLit(13),IntLit(4),Block([AssignStmt(Id(b),BinaryOp(-,Id(b),BinaryOp(/,Id(b),IntLit(3))))])]),Return(Id(b))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 432))

    def test_none_const_433(self):
        input = """
        Class Program{
            Val $obj: Circle;
            Val obj2: Circle = New Circle(1, 2);
            main(){      
                Val a, b: Int;
                Val d, e: Float;
                Return (obj2.radius * 3.14) + a - b / d * e;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($obj),ClassType(Id(Circle)),None)),AttributeDecl(Instance,ConstDecl(Id(obj2),ClassType(Id(Circle)),NewExpr(Id(Circle),[IntLit(1),IntLit(2)]))),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,None),ConstDecl(Id(b),IntType,None),ConstDecl(Id(d),FloatType,None),ConstDecl(Id(e),FloatType,None),Return(BinaryOp(-,BinaryOp(+,BinaryOp(*,FieldAccess(Id(obj2),Id(radius)),FloatLit(3.14)),Id(a)),BinaryOp(*,BinaryOp(/,Id(b),Id(d)),Id(e))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 433))

    def test_new_expr_434(self):
        """Simple program to test scalar id of Foreach (Scrapped, for assignment 3)"""
        input = """
        Class Program{
            Val $obj: Circle = New Circle();
            Val obj2: Circle = New Circle(obj2);
            main(){      
                Var circle3: Circle = New Circle(1, 2);
                Return (circle3);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($obj),ClassType(Id(Circle)),NewExpr(Id(Circle),[]))),AttributeDecl(Instance,ConstDecl(Id(obj2),ClassType(Id(Circle)),NewExpr(Id(Circle),[Id(obj2)]))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(circle3),ClassType(Id(Circle)),NewExpr(Id(Circle),[IntLit(1),IntLit(2)])),Return(Id(circle3))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 434))

    def test_return_435(self):
        """Simple program to test Return with or without expr"""
        input = """
        Class Program{
            Var $str: String = "From Class Program: ";
            main(){      
                Var circle: Circle = New Circle(math.pi, 4);
                Return circle;
            }
            print(s: String){
                System.out.println(s + " says hello to the world!");
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,VarDecl(Id($str),StringType,StringLit(From Class Program: ))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(circle),ClassType(Id(Circle)),NewExpr(Id(Circle),[FieldAccess(Id(math),Id(pi)),IntLit(4)])),Return(Id(circle))])),MethodDecl(Id(print),Instance,[param(Id(s),StringType)],Block([Call(FieldAccess(Id(System),Id(out)),Id(println),[BinaryOp(+,Id(s),StringLit( says hello to the world!))]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 435))

    def test_constructor_destructor_436(self):
        input = """
        Class Node{
            Var $key: Int;
            Var $value: String;
            Constructor(key: Int; value: String){
                Node::$key = key;
                Node::$value = value;
                Val pair: Pair = New Pair(Node::$key, Node::$value);
                System.print("Object " + System.toString(Self.__str__()) + " has been created !");
                System.print("Pair is: ", pair);
            }
            Destructor(){
                Self.destroy();
                System.print("Object " + System.toString(Self.__str__()) + " has been destroyed !");
            }
            destroy(){
                System.delete(Self);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Node),[AttributeDecl(Static,VarDecl(Id($key),IntType)),AttributeDecl(Static,VarDecl(Id($value),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(key),IntType),param(Id(value),StringType)],Block([AssignStmt(FieldAccess(Id(Node),Id($key)),Id(key)),AssignStmt(FieldAccess(Id(Node),Id($value)),Id(value)),ConstDecl(Id(pair),ClassType(Id(Pair)),NewExpr(Id(Pair),[FieldAccess(Id(Node),Id($key)),FieldAccess(Id(Node),Id($value))])),Call(Id(System),Id(print),[BinaryOp(+,BinaryOp(+,StringLit(Object ),CallExpr(Id(System),Id(toString),[CallExpr(Self(),Id(__str__),[])])),StringLit( has been created !))]),Call(Id(System),Id(print),[StringLit(Pair is: ),Id(pair)])])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Self(),Id(destroy),[]),Call(Id(System),Id(print),[BinaryOp(+,BinaryOp(+,StringLit(Object ),CallExpr(Id(System),Id(toString),[CallExpr(Self(),Id(__str__),[])])),StringLit( has been destroyed !))])])),MethodDecl(Id(destroy),Instance,[],Block([Call(Id(System),Id(delete),[Self()])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 436))

    def test_simple_program_437(self):
        """ Test declared and not-declared variable/attribute """
        input = """
        Class B : C{
            Val a : Int = 100;
            Val $b : Float = 123.303E3;
            Var $_: Boolean;
            Val _: Any = New Any();
            Constructor(){
                a = New C();
                B::$b = New B();
                Return;
            }
        }
        Class Program {
            main() {
                Val a : A = New A();
                a::$b();
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(B),Id(C),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(100))),AttributeDecl(Static,ConstDecl(Id($b),FloatType,FloatLit(123303.0))),AttributeDecl(Static,VarDecl(Id($_),BoolType)),AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(Any)),NewExpr(Id(Any),[]))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(a),NewExpr(Id(C),[])),AssignStmt(FieldAccess(Id(B),Id($b)),NewExpr(Id(B),[])),Return()]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[])),Call(Id(a),Id($b),[]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 437))

    def test_empty_block_stmt_438(self):
        input = """
        Class Program{
            main(){
                {} {} {} {}       
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([]),Block([]),Block([]),Block([])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 438))
    
    def test_block_stmt_439(self):
        input = """
        Class Sys_Clone : System{
            classWorker(){
                {
                    Val a : Int = 100;
                    Var _: Any = New Any();
                } 
                {
                    a = True;
                    b = False;
                    Return;
                } 
                {
                    Foreach (i In 0 .. rows1 By 1) {
                        Foreach (j In 0 .. col2 By (0 + 1) * 2 - 1) {
                            c[i][j]=0;
                            Foreach (k In 0 .. col1 By 1) {
                                c[i][j] = c[i][j] + a[i][k] * b[k][j];
                            }
                            c = a + (b > c) + d;
                            Out.print(c[i][j] +. " ");
                        }
                        Out.println();
                    }
                    Return c;
                }      
            }
        }
        """
        expect = """Program([ClassDecl(Id(Sys_Clone),Id(System),[MethodDecl(Id(classWorker),Instance,[],Block([Block([ConstDecl(Id(a),IntType,IntLit(100)),VarDecl(Id(_),ClassType(Id(Any)),NewExpr(Id(Any),[]))]),Block([AssignStmt(Id(a),BooleanLit(True)),AssignStmt(Id(b),BooleanLit(False)),Return()]),Block([For(Id(i),IntLit(0),Id(rows1),IntLit(1),Block([For(Id(j),IntLit(0),Id(col2),BinaryOp(-,BinaryOp(*,BinaryOp(+,IntLit(0),IntLit(1)),IntLit(2)),IntLit(1)),Block([AssignStmt(ArrayCell(Id(c),[Id(i),Id(j)]),IntLit(0)),For(Id(k),IntLit(0),Id(col1),IntLit(1),Block([AssignStmt(ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(*,ArrayCell(Id(a),[Id(i),Id(k)]),ArrayCell(Id(b),[Id(k),Id(j)]))))])]),AssignStmt(Id(c),BinaryOp(+,BinaryOp(+,Id(a),BinaryOp(>,Id(b),Id(c))),Id(d))),Call(Id(Out),Id(print),[BinaryOp(+.,ArrayCell(Id(c),[Id(i),Id(j)]),StringLit( ))])])]),Call(Id(Out),Id(println),[])])]),Return(Id(c))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 439))

    def test_fake_special_method_440(self):
        input = """
        Class Program{
            main(){    
                Return BCA.doNothing();
            }
            main(fakeParam: NullType){
                ABC.doNothing();
                Return;
            }
            Constructor(){
                System.construct(Self);
            }
            Destructor(){
                System.destroy(Self);
            }
        }
        Class FakeProgram: Program{
            main(){    
                Return BCA.doNothing();
            }
            main(fakeParam: NullType){
                ABC.doNothing();
                Return;
            }
            Constructor(){
                System.construct(Self);
            }
            Destructor(){
                System.destroy(Self);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(CallExpr(Id(BCA),Id(doNothing),[]))])),MethodDecl(Id(main),Instance,[param(Id(fakeParam),ClassType(Id(NullType)))],Block([Call(Id(ABC),Id(doNothing),[]),Return()])),MethodDecl(Id(Constructor),Instance,[],Block([Call(Id(System),Id(construct),[Self()])])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(System),Id(destroy),[Self()])]))]),ClassDecl(Id(FakeProgram),Id(Program),[MethodDecl(Id(main),Instance,[],Block([Return(CallExpr(Id(BCA),Id(doNothing),[]))])),MethodDecl(Id(main),Instance,[param(Id(fakeParam),ClassType(Id(NullType)))],Block([Call(Id(ABC),Id(doNothing),[]),Return()])),MethodDecl(Id(Constructor),Instance,[],Block([Call(Id(System),Id(construct),[Self()])])),MethodDecl(Id(Destructor),Instance,[],Block([Call(Id(System),Id(destroy),[Self()])]))])])""" 
        self.assertTrue(TestAST.test(input, expect, 440))