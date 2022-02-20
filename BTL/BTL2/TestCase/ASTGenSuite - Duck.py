import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
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

    def test_simple_program_414(self):
        """Simple program, to check output of other than Decimal-base Integer"""
        input = """
        Class Program{
            Val a, b, $c, $d, e, $f: Int = 037415, 1239651, 0x1239EDF, 0xABCDEF01, 0b1000101, 0B110101;
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(16141))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(1239651))),AttributeDecl(Static,ConstDecl(Id($c),IntType,IntLit(19111647))),AttributeDecl(Static,ConstDecl(Id($d),IntType,IntLit(2882400001))),AttributeDecl(Instance,ConstDecl(Id(e),IntType,IntLit(69))),AttributeDecl(Static,ConstDecl(Id($f),IntType,IntLit(53)))])])"""
        self.assertTrue(TestAST.test(input, expect, 414))

    def test_simple_program_415(self):
        """Simple program, to check output of other than Decimal-base Integer"""
        input = """
        Class Program{
            main(inp: Int){
                Var a: Float;
                a = 3.5031041095815;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(inp),IntType)],Block([VarDecl(Id(a),FloatType),AssignStmt(Id(a),FloatLit(3.5031041095815))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 415))

    def test_simple_program_416(self):
        """Simple program, to check assignment statement of array cell"""
        input = """
        Class Program{
            main(){
                Var a: Array[Boolean, 4];
                a[0] = True;
                a[1] = a[0];
                a[1 + 1] = False;
                a[0xC / 0b100] = True;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(4,BoolType)),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(a),[IntLit(0)])),AssignStmt(ArrayCell(Id(a),[BinaryOp(+,IntLit(1),IntLit(1))]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,IntLit(12),IntLit(4))]),BooleanLit(True))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 416))

    def test_simple_program_417(self):
        """Simple program, to check assignment statement of multidimensional array cell"""
        input = """
        Class Program{
            main(){
                Var a: Array[Array[Boolean, 3], 2];
                a[0][0] = True;
                a[0][1] = False;
                a[1][0] = True;
                a[1][1] = False;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(2,ArrayType(3,BoolType))),AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(0),IntLit(1)]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1)]),BooleanLit(False))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 417))

    def test_simple_program_418(self):
        """Simple program, to check assignment statement of multidimensional array cell"""
        input = """
        Class Program{
            main(){
                Var a: Array[Array[Boolean, 2], 2];
                a[0][0 * 10000000] = True;
                a[0][3 * 2 * 1 / 6] = False;
                a[0x270F / 9999][0 * 0B1011110101] = True;
                a[9999 / 0x270F][1 * 9 / 9 + 0] = Sys.sampleArray[a[0x1]];
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(2,ArrayType(2,BoolType))),AssignStmt(ArrayCell(Id(a),[IntLit(0),BinaryOp(*,IntLit(0),IntLit(10000000))]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(0),BinaryOp(/,BinaryOp(*,BinaryOp(*,IntLit(3),IntLit(2)),IntLit(1)),IntLit(6))]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,IntLit(9999),IntLit(9999)),BinaryOp(*,IntLit(0),IntLit(757))]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,IntLit(9999),IntLit(9999)),BinaryOp(+,BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(9)),IntLit(9)),IntLit(0))]),ArrayCell(FieldAccess(Id(Sys),Id(sampleArray)),[ArrayCell(Id(a),[IntLit(1)])]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 418))

    def test_simple_program_419(self):
        """Simple program, with rhs (all_expr) is a mtd_array"""
        input = """
        Class Program{
            Var a: Array[Array[Boolean, 2], 1];
            main(){
                Var b: Boolean = a[0][2];
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(1,ArrayType(2,BoolType)))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(b),BoolType,ArrayCell(Id(a),[IntLit(0),IntLit(2)]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 419))

    def test_simple_program_420(self):
        """Simple program, with lhs is a nested array call"""
        input = """
        Class Program{
            Var a: Array[Array[Boolean, 2], 1];
            main(){
                a[b[1]] = 123;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(1,ArrayType(2,BoolType)))),MethodDecl(Id(main),Static,[],Block([AssignStmt(ArrayCell(Id(a),[ArrayCell(Id(b),[IntLit(1)])]),IntLit(123))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 420))

    def test_simple_program_421(self):
        """Simple program, with instance field access and call expr"""
        input = """
        Class Program{
            main(){
                a = Prog.b(e, f, g);
                b = Program.a;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(Prog),Id(b),[Id(e),Id(f),Id(g)])),AssignStmt(Id(b),FieldAccess(Id(Program),Id(a)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 421))

    def test_simple_program_422(self):
        """Simple program, with static field access and call expr"""
        input = """
        Class Program{
            main(){
                a = Prog::$b(e, f, g);
                b = Program::$a;
                c = Self::$f;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),CallExpr(Id(Prog),Id($b),[Id(e),Id(f),Id(g)])),AssignStmt(Id(b),FieldAccess(Id(Program),Id($a))),AssignStmt(Id(c),FieldAccess(Self(),Id($f)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 422))

    def test_simple_program_423(self):
        """Simple program, spiderman pointing at each other"""
        input = """
        Class Program{
            Val $a: Int = 5;
            Constructor(){
                Program::$a = Self::$a;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($a),IntType,IntLit(5))),MethodDecl(Id("Constructor"),Instance,[],Block([AssignStmt(FieldAccess(Id(Program),Id($a)),FieldAccess(Self(),Id($a)))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 423))

    def test_short_program_424(self):
        """Simple program with partial If statement"""
        input = """
        Class Program{
            main(){
                If (a > b){
                    a = 2;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 424))

    def test_short_program_425(self):
        """Simple program with partial If - Elseif statement"""
        input = """
        Class Program{
            main(){
                If (a > b){
                    a = 2;
                }
                Elseif (a == b){
                    a = 1;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 425))

    def test_short_program_426(self):
        """Simple program with Complete If - Elseif - Else statement"""
        input = """
        Class Program{
            main(){
                If (a > b){
                    a = 2;
                }
                Elseif (a == b){
                    a = 1;
                }
                Else{
                    a = 0;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(2))]),If(BinaryOp(==,Id(a),Id(b)),Block([AssignStmt(Id(a),IntLit(1))]),Block([AssignStmt(Id(a),IntLit(0))])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 426))

    def test_short_program_427(self):
        """Simple program with partial ForEach loop statement"""
        input = """
        Class Program{
            main(){
                Foreach (a In 1 .. 100000){
                    Global::$b = a + 2;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(a),IntLit(1),IntLit(100000),IntLit(1),Block([AssignStmt(FieldAccess(Id(Global),Id($b)),BinaryOp(+,Id(a),IntLit(2)))])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 427))

    def test_short_program_428(self):
        """Short program with complete ForEach loop statement"""
        input = """
        Class Program{
            main(){
                Foreach (a In 1 .. 100000 By 5){
                    Global::$b = a + 2;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(a),IntLit(1),IntLit(100000),IntLit(5),Block([AssignStmt(FieldAccess(Id(Global),Id($b)),BinaryOp(+,Id(a),IntLit(2)))])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 428))

    def test_short_program_429(self):
        """Simple program with Complete If - Elseif - Else statement (2 Elseif)"""
        input = """
        Class Program : System{
            Val a: Int = 1;
            fooBar() {
                Self::$fooBar();
            }
            main() {
                If (1 >= 2) {
                    Out.fooBar(True);
                } 
                Elseif (a <= 2) {
                    Self::$fooBar();
                } 
                Elseif (a[1][2] <= a[1] * a.a + Some::$a()) {
                    Out.println(400);
                } 
                Else {
                    Out.println("What are you looking for?");
                }
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(System),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),MethodDecl(Id(fooBar),Instance,[],Block([Call(Self(),Id($fooBar),[])])),MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>=,IntLit(1),IntLit(2)),Block([Call(Id(Out),Id(fooBar),[BooleanLit(True)])]),If(BinaryOp(<=,Id(a),IntLit(2)),Block([Call(Self(),Id($fooBar),[])]),If(BinaryOp(<=,ArrayCell(Id(a),[IntLit(1),IntLit(2)]),BinaryOp(+,BinaryOp(*,ArrayCell(Id(a),[IntLit(1)]),FieldAccess(Id(a),Id(a))),CallExpr(Id(Some),Id($a),[]))),Block([Call(Id(Out),Id(println),[IntLit(400)])]),Block([Call(Id(Out),Id(println),[StringLit(What are you looking for?)])])))),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 429))

    def test_short_program_430(self):
        """Simple program with 2 methods and 1 return on main"""
        input = """
        Class Program {
            Val a: Int = 1;
            fooBar(a, b : Int; c : Float) {
                Self.fooBar1(True, False, Null);
            }
            main() {
                Self.fooBar(x, y, "ZhongGuo ren");
                Return;
            }
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),MethodDecl(Id(fooBar),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([Call(Self(),Id(fooBar1),[BooleanLit(True),BooleanLit(False),NullLiteral()])])),MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(fooBar),[Id(x),Id(y),StringLit(ZhongGuo ren)]),Return()]))])])"
        self.assertTrue(TestAST.test(input, expect, 430))

    def test_float_convert_431(self):
        """Simple program to test the conversion of invalid python float literal (.e-3)"""
        input = """
        Class Program {
            main() {
                Out.println(.e-3);
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(println),[FloatLit(0.0)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 432))

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
        """Simple program to test None in ConstDecl"""
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
        """Simple program to test Constructor and Destructor"""
        input = """
        Class Node{
            Var $key: Int;
            Var $value: String;
            Constructor(key: Int; value: String){
                Self::$key = key;
                Self::$value = value;
                Val pair: Pair = New Pair(Self::$key, Self::$value);
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
        expect = """Program([ClassDecl(Id(Node),[AttributeDecl(Static,VarDecl(Id($key),IntType)),AttributeDecl(Static,VarDecl(Id($value),StringType)),MethodDecl(Id("Constructor"),Instance,[param(Id(key),IntType),param(Id(value),StringType)],Block([AssignStmt(FieldAccess(Self(),Id($key)),Id(key)),AssignStmt(FieldAccess(Self(),Id($value)),Id(value)),ConstDecl(Id(pair),ClassType(Id(Pair)),NewExpr(Id(Pair),[FieldAccess(Self(),Id($key)),FieldAccess(Self(),Id($value))])),Call(Id(System),Id(print),[BinaryOp(+,BinaryOp(+,StringLit(Object ),CallExpr(Id(System),Id(toString),[CallExpr(Self(),Id(__str__),[])])),StringLit( has been created !))]),Call(Id(System),Id(print),[StringLit(Pair is: ),Id(pair)])])),MethodDecl(Id("Destructor"),Instance,[],Block([Call(Self(),Id(destroy),[]),Call(Id(System),Id(print),[BinaryOp(+,BinaryOp(+,StringLit(Object ),CallExpr(Id(System),Id(toString),[CallExpr(Self(),Id(__str__),[])])),StringLit( has been destroyed !))])])),MethodDecl(Id(destroy),Instance,[],Block([Call(Id(System),Id(delete),[Self()])]))])])"""
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
                Self::$b = New B();
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
        expect = """Program([ClassDecl(Id(B),Id(C),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(100))),AttributeDecl(Static,ConstDecl(Id($b),FloatType,FloatLit(123303.0))),AttributeDecl(Static,VarDecl(Id($_),BoolType)),AttributeDecl(Instance,ConstDecl(Id(_),ClassType(Id(Any)),NewExpr(Id(Any),[]))),MethodDecl(Id("Constructor"),Instance,[],Block([AssignStmt(Id(a),NewExpr(Id(C),[])),AssignStmt(FieldAccess(Self(),Id($b)),NewExpr(Id(B),[])),Return()]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[])),Call(Id(a),Id($b),[]),Return()]))])])"""
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
                    _.getVar() = 100_000_000_000;
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
        expect = """Program([ClassDecl(Id(Sys_Clone),Id(System),[MethodDecl(Id(classWorker),Instance,[],Block([Block([ConstDecl(Id(a),IntType,IntLit(100)),VarDecl(Id(_),ClassType(Id(Any)),NewExpr(Id(Any),[])),AssignStmt(CallExpr(Id(_),Id(getVar),[]),IntLit(100000000000))]),Block([AssignStmt(Id(a),BooleanLit(True)),AssignStmt(Id(b),BooleanLit(False)),Return()]),Block([For(Id(i),IntLit(0),Id(rows1),IntLit(1),Block([For(Id(j),IntLit(0),Id(col2),BinaryOp(-,BinaryOp(*,BinaryOp(+,IntLit(0),IntLit(1)),IntLit(2)),IntLit(1)),Block([AssignStmt(ArrayCell(Id(c),[Id(i),Id(j)]),IntLit(0)),For(Id(k),IntLit(0),Id(col1),IntLit(1),Block([AssignStmt(ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(j)]),BinaryOp(*,ArrayCell(Id(a),[Id(i),Id(k)]),ArrayCell(Id(b),[Id(k),Id(j)]))))])]),AssignStmt(Id(c),BinaryOp(+,BinaryOp(+,Id(a),BinaryOp(>,Id(b),Id(c))),Id(d))),Call(Id(Out),Id(print),[BinaryOp(+.,ArrayCell(Id(c),[Id(i),Id(j)]),StringLit( ))])])]),Call(Id(Out),Id(println),[])])]),Return(Id(c))])]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(CallExpr(Id(BCA),Id(doNothing),[]))])),MethodDecl(Id(main),Instance,[param(Id(fakeParam),ClassType(Id(NullType)))],Block([Call(Id(ABC),Id(doNothing),[]),Return()])),MethodDecl(Id("Constructor"),Instance,[],Block([Call(Id(System),Id(construct),[Self()])])),MethodDecl(Id("Destructor"),Instance,[],Block([Call(Id(System),Id(destroy),[Self()])]))]),ClassDecl(Id(FakeProgram),Id(Program),[MethodDecl(Id(main),Instance,[],Block([Return(CallExpr(Id(BCA),Id(doNothing),[]))])),MethodDecl(Id(main),Instance,[param(Id(fakeParam),ClassType(Id(NullType)))],Block([Call(Id(ABC),Id(doNothing),[]),Return()])),MethodDecl(Id("Constructor"),Instance,[],Block([Call(Id(System),Id(construct),[Self()])])),MethodDecl(Id("Destructor"),Instance,[],Block([Call(Id(System),Id(destroy),[Self()])]))])])""" 
        self.assertTrue(TestAST.test(input, expect, 440))

    # def test_simple_program_(self):
    #     input = """
    #     Class Program{
    #         main(){       
    #         }
    #     }
    #     """
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input, expect, ))
