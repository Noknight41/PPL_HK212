import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):    
    ### Simple Test
        
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
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(100,StringType))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(c),[]),AssignStmt(Id(d),[StringLit(1),StringLit(2),StringLit(3)])]))])])"""
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
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(100,StringType))),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(d),[StringLit(1),StringLit(2),StringLit(3)]),VarDecl(Id(e),ArrayType(2,ArrayType(2,ArrayType(3,IntType))),[[[IntLit(1),IntLit(3),IntLit(4)],[IntLit(1),IntLit(5),IntLit(6)]],[[IntLit(1),IntLit(7),IntLit(8)],[IntLit(1),IntLit(9),IntLit(10)]]])]))])])"""
        self.assertTrue(TestAST.test(input,expect,306))
    
    ### Var Decl
    def test_307(self):
        input = """
        Class A{
            Var d1, $d2: Int;
            Var d4, d3: Float;
            Var d5, d_6: Boolean;   
            Var d_7, d_8, d_9: String;
            Var array_1, array_2: Array[String, 5];
            Var array_3: Array[Array[Float, 4], 5];
        }
        Class Program {
            main(){
                Var d1, d2: Int;
                Var d4, d3: Float;
                Var d5, d_6: Boolean;   
                Var d_7, d_8, d_9: String;
                Var demo: A = New A();
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(d1),IntType)),AttributeDecl(Static,VarDecl(Id($d2),IntType)),AttributeDecl(Instance,VarDecl(Id(d4),FloatType)),AttributeDecl(Instance,VarDecl(Id(d3),FloatType)),AttributeDecl(Instance,VarDecl(Id(d5),BoolType)),AttributeDecl(Instance,VarDecl(Id(d_6),BoolType)),AttributeDecl(Instance,VarDecl(Id(d_7),StringType)),AttributeDecl(Instance,VarDecl(Id(d_8),StringType)),AttributeDecl(Instance,VarDecl(Id(d_9),StringType)),AttributeDecl(Instance,VarDecl(Id(array_1),ArrayType(5,StringType))),AttributeDecl(Instance,VarDecl(Id(array_2),ArrayType(5,StringType))),AttributeDecl(Instance,VarDecl(Id(array_3),ArrayType(5,ArrayType(4,FloatType))))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(d1),IntType),VarDecl(Id(d2),IntType),VarDecl(Id(d4),FloatType),VarDecl(Id(d3),FloatType),VarDecl(Id(d5),BoolType),VarDecl(Id(d_6),BoolType),VarDecl(Id(d_7),StringType),VarDecl(Id(d_8),StringType),VarDecl(Id(d_9),StringType),VarDecl(Id(demo),ClassType(Id(A)),NewExpr(Id(A),[])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 307))
    
    def test_308(self):
        input = """
        Class A{
            Var a1, $a2: Int = 0x12, 0434;
            Var a4, $a3: Float = 1.23445, 340.041e-4;
            Var a5, $a_6: Boolean = True, False;   
            Var a_7, $a_8, a_9: String = "No", "Seeya", "Gozen";
        }
        Class Program {
            main(){
                Var a1, a2: Int = 0x12, 0434;
                Var a4, a3: Float = 1.23445, 340.041e-4;
                Var a5, a_6: Boolean = True, False;   
                Var a_7, a_8, a_9: String = "No", "Seeya", "Gozen";
                Var demo: A = New A(True);
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a1),IntType,IntLit(18))),AttributeDecl(Static,VarDecl(Id($a2),IntType,IntLit(284))),AttributeDecl(Instance,VarDecl(Id(a4),FloatType,FloatLit(1.23445))),AttributeDecl(Static,VarDecl(Id($a3),FloatType,FloatLit(0.0340041))),AttributeDecl(Instance,VarDecl(Id(a5),BoolType,BooleanLit(True))),AttributeDecl(Static,VarDecl(Id($a_6),BoolType,BooleanLit(False))),AttributeDecl(Instance,VarDecl(Id(a_7),StringType,StringLit(No))),AttributeDecl(Static,VarDecl(Id($a_8),StringType,StringLit(Seeya))),AttributeDecl(Instance,VarDecl(Id(a_9),StringType,StringLit(Gozen)))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a1),IntType,IntLit(18)),VarDecl(Id(a2),IntType,IntLit(284)),VarDecl(Id(a4),FloatType,FloatLit(1.23445)),VarDecl(Id(a3),FloatType,FloatLit(0.0340041)),VarDecl(Id(a5),BoolType,BooleanLit(True)),VarDecl(Id(a_6),BoolType,BooleanLit(False)),VarDecl(Id(a_7),StringType,StringLit(No)),VarDecl(Id(a_8),StringType,StringLit(Seeya)),VarDecl(Id(a_9),StringType,StringLit(Gozen)),VarDecl(Id(demo),ClassType(Id(A)),NewExpr(Id(A),[BooleanLit(True)])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 308))
    
    def test_309(self):
        input = """
        Class A{
            Var array_1, $array_2: Array[Float, 5];
            Var array_3: Array[Int, 5] = Array(1,2,0x4,0b11101,034);
            Var $array_4: Array[Array[String, 2], 2] = Array(
                Array("Person", "Demon"),
                Array("Heaven", "Utopia")
            );
        }
        Class Program {
            main(){
                Var array_1, array_2: Array[Boolean, 5];
                Var array_3: Array[Int, 5] = Array(1,2,0x4,0b11101,034);
                Var array_4: Array[Array[String, 2], 2] = Array(
                    Array("Person", "Demon"),
                    Array("Heaven", "Utopia")
                );
                Var demo: A = New A(False);
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(array_1),ArrayType(5,FloatType))),AttributeDecl(Static,VarDecl(Id($array_2),ArrayType(5,FloatType))),AttributeDecl(Instance,VarDecl(Id(array_3),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(4),IntLit(29),IntLit(28)])),AttributeDecl(Static,VarDecl(Id($array_4),ArrayType(2,ArrayType(2,StringType)),[[StringLit(Person),StringLit(Demon)],[StringLit(Heaven),StringLit(Utopia)]]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(array_1),ArrayType(5,BoolType)),VarDecl(Id(array_2),ArrayType(5,BoolType)),VarDecl(Id(array_3),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(4),IntLit(29),IntLit(28)]),VarDecl(Id(array_4),ArrayType(2,ArrayType(2,StringType)),[[StringLit(Person),StringLit(Demon)],[StringLit(Heaven),StringLit(Utopia)]]),VarDecl(Id(demo),ClassType(Id(A)),NewExpr(Id(A),[BooleanLit(False)])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 309))
    
    ### Const Decl
    def test_310(self):
        input = """
        Class A{
            Val d1, d2: Int;
            Val d4, d3: Float;
            Val d5, d_6: Boolean;   
            Val d_7, d_8, d_9: String;
            Val array_1, array_2: Array[String, 5];
            Val array_3: Array[Array[Float, 4], 5];
        }
        Class Program {
            main(){
                Val d1, d2: Int;
                Val d4, d3: Float;
                Val d5, d_6: Boolean;   
                Val d_7, d_8, d_9: String;
                Var demo: A = New A();
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(d1),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(d2),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(d4),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(d3),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(d5),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(d_6),BoolType,None)),AttributeDecl(Instance,ConstDecl(Id(d_7),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(d_8),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(d_9),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(array_1),ArrayType(5,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(array_2),ArrayType(5,StringType),None)),AttributeDecl(Instance,ConstDecl(Id(array_3),ArrayType(5,ArrayType(4,FloatType)),None))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(d1),IntType,None),ConstDecl(Id(d2),IntType,None),ConstDecl(Id(d4),FloatType,None),ConstDecl(Id(d3),FloatType,None),ConstDecl(Id(d5),BoolType,None),ConstDecl(Id(d_6),BoolType,None),ConstDecl(Id(d_7),StringType,None),ConstDecl(Id(d_8),StringType,None),ConstDecl(Id(d_9),StringType,None),VarDecl(Id(demo),ClassType(Id(A)),NewExpr(Id(A),[])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 310))
    
    def test_311(self):
        input = """
        Class A{
            Val a1, $a2: Int = 0x12, 0434;
            Val a4, $a3: Float = 1.23445, 340.041e-4;
            Val a5, $a_6: Boolean = True, False;   
            Val a_7, $a_8, a_9: String = "No", "Seeya", "Gozen";
        }
        Class Program {
            main(){
                Val a1, a2: Int = 0x12, 0434;
                Val a4, a3: Float = 1.23445, 340.041e-4;
                Val a5, a_6: Boolean = True, False;   
                Val a_7, a_8, a_9: String = "No", "Seeya", "Gozen";
                Var demo: A = New A(True);
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a1),IntType,IntLit(18))),AttributeDecl(Static,ConstDecl(Id($a2),IntType,IntLit(284))),AttributeDecl(Instance,ConstDecl(Id(a4),FloatType,FloatLit(1.23445))),AttributeDecl(Static,ConstDecl(Id($a3),FloatType,FloatLit(0.0340041))),AttributeDecl(Instance,ConstDecl(Id(a5),BoolType,BooleanLit(True))),AttributeDecl(Static,ConstDecl(Id($a_6),BoolType,BooleanLit(False))),AttributeDecl(Instance,ConstDecl(Id(a_7),StringType,StringLit(No))),AttributeDecl(Static,ConstDecl(Id($a_8),StringType,StringLit(Seeya))),AttributeDecl(Instance,ConstDecl(Id(a_9),StringType,StringLit(Gozen)))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a1),IntType,IntLit(18)),ConstDecl(Id(a2),IntType,IntLit(284)),ConstDecl(Id(a4),FloatType,FloatLit(1.23445)),ConstDecl(Id(a3),FloatType,FloatLit(0.0340041)),ConstDecl(Id(a5),BoolType,BooleanLit(True)),ConstDecl(Id(a_6),BoolType,BooleanLit(False)),ConstDecl(Id(a_7),StringType,StringLit(No)),ConstDecl(Id(a_8),StringType,StringLit(Seeya)),ConstDecl(Id(a_9),StringType,StringLit(Gozen)),VarDecl(Id(demo),ClassType(Id(A)),NewExpr(Id(A),[BooleanLit(True)])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 311))
    
    def test_312(self):
        input = """
        Class A{
            Val array_1, $array_2: Array[Float, 5];
            Val array_3: Array[Int, 5] = Array(1,2,0x4,0b11101,034);
            Val $array_4: Array[Array[String, 2], 2] = Array(
                Array("Person", "Demon"),
                Array("Heaven", "Utopia")
            );
        }
        Class Program {
            main(){
                Val array_1, array_2: Array[Boolean, 5];
                Val array_3: Array[Int, 5] = Array(1,2,0x4,0b11101,034);
                Val array_4: Array[Array[String, 2], 2] = Array(
                    Array("Person", "Demon"),
                    Array("Heaven", "Utopia")
                );
                Var demo: A = New A(False);
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(array_1),ArrayType(5,FloatType),None)),AttributeDecl(Static,ConstDecl(Id($array_2),ArrayType(5,FloatType),None)),AttributeDecl(Instance,ConstDecl(Id(array_3),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(4),IntLit(29),IntLit(28)])),AttributeDecl(Static,ConstDecl(Id($array_4),ArrayType(2,ArrayType(2,StringType)),[[StringLit(Person),StringLit(Demon)],[StringLit(Heaven),StringLit(Utopia)]]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(array_1),ArrayType(5,BoolType),None),ConstDecl(Id(array_2),ArrayType(5,BoolType),None),ConstDecl(Id(array_3),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(4),IntLit(29),IntLit(28)]),ConstDecl(Id(array_4),ArrayType(2,ArrayType(2,StringType)),[[StringLit(Person),StringLit(Demon)],[StringLit(Heaven),StringLit(Utopia)]]),VarDecl(Id(demo),ClassType(Id(A)),NewExpr(Id(A),[BooleanLit(False)])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 312))
        
    def test_313(self):
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
            main(){
                
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType)),AttributeDecl(Instance,ConstDecl(Id(c),BoolType,None)),AttributeDecl(Static,ConstDecl(Id($d),BoolType,None)),AttributeDecl(Instance,VarDecl(Id(e),IntType,IntLit(19))),AttributeDecl(Static,VarDecl(Id($f),IntType,IntLit(69))),AttributeDecl(Instance,ConstDecl(Id(w),FloatType,FloatLit(0.01))),AttributeDecl(Static,ConstDecl(Id($x),FloatType,FloatLit(30.0))),MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([VarDecl(Id(a),IntType),ConstDecl(Id(c),BoolType,None),VarDecl(Id(e),IntType,IntLit(19)),VarDecl(Id(f),IntType,IntLit(69)),ConstDecl(Id(w),FloatType,FloatLit(0.01)),ConstDecl(Id(x),FloatType,FloatLit(30.0)),Return(BinaryOp(+,BinaryOp(+,BinaryOp(+,Id(a),Id(c)),Id(e)),Id(w)))])),MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input, expect, 313))
    
    def test_314(self):
        input = """
        Class A{
            Var a1, a2: Int = 1, 4;
            Var a4, a3: Float = 1.2e-3, 0.0001;
            Val a5, a_6: Boolean = True, False;   
            Val a_7, a_8, a_9: String = "No", "Seeya", "Gozen";
        }
        Class Program {
            main(){
                Var b1, b2: Int = 0x231, 034;
                Var b4, b3: Float = 1.2e-3, 0.0001;
                Val b5, b_6: Boolean = True, False;   
                Val b_7, b_8, b_9: String = "No", "Seeya", "Gozen";
                Var demo: A = New A();
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a1),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(a2),IntType,IntLit(4))),AttributeDecl(Instance,VarDecl(Id(a4),FloatType,FloatLit(0.0012))),AttributeDecl(Instance,VarDecl(Id(a3),FloatType,FloatLit(0.0001))),AttributeDecl(Instance,ConstDecl(Id(a5),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(a_6),BoolType,BooleanLit(False))),AttributeDecl(Instance,ConstDecl(Id(a_7),StringType,StringLit(No))),AttributeDecl(Instance,ConstDecl(Id(a_8),StringType,StringLit(Seeya))),AttributeDecl(Instance,ConstDecl(Id(a_9),StringType,StringLit(Gozen)))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(b1),IntType,IntLit(561)),VarDecl(Id(b2),IntType,IntLit(28)),VarDecl(Id(b4),FloatType,FloatLit(0.0012)),VarDecl(Id(b3),FloatType,FloatLit(0.0001)),ConstDecl(Id(b5),BoolType,BooleanLit(True)),ConstDecl(Id(b_6),BoolType,BooleanLit(False)),ConstDecl(Id(b_7),StringType,StringLit(No)),ConstDecl(Id(b_8),StringType,StringLit(Seeya)),ConstDecl(Id(b_9),StringType,StringLit(Gozen)),VarDecl(Id(demo),ClassType(Id(A)),NewExpr(Id(A),[])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 314))
        
    ### Multiple Class
    def test_315(self):
        input = """
        Class A{
            Var $a: Float;
        }
        Class B: A{
            Var $b: Float;
        }
        Class C{
            Var $s: Float;
        }
        Class Application: B{
            Var $f: Float;
        }
        Class Program {
            main(){
                
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($a),FloatType))]),ClassDecl(Id(B),Id(A),[AttributeDecl(Static,VarDecl(Id($b),FloatType))]),ClassDecl(Id(C),[AttributeDecl(Static,VarDecl(Id($s),FloatType))]),ClassDecl(Id(Application),Id(B),[AttributeDecl(Static,VarDecl(Id($f),FloatType))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,315)) 
    
    def test_316(self):
        input = """
        Class AC {
            func() {
                Return somethingFun;
            }
        }
        Class AB {
            Val a : AC;
            Constructor() {
                a = New AC();
                Return;
            }
        }
        Class A {
            Val $b : AB;
            Constructor() {
                A::$b = New AB();
                Return;
            }
        }
        Class Program {
            mainA() {
                Val a : A = New A();
                a::$b.a.func();
                Return;
            }
        }"""
        expect = """Program([ClassDecl(Id(AC),[MethodDecl(Id(func),Instance,[],Block([Return(Id(somethingFun))]))]),ClassDecl(Id(AB),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(AC)),None)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(a),NewExpr(Id(AC),[])),Return()]))]),ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($b),ClassType(Id(AB)),None)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(A),Id($b)),NewExpr(Id(AB),[])),Return()]))]),ClassDecl(Id(Program),[MethodDecl(Id(mainA),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(A)),NewExpr(Id(A),[])),Call(FieldAccess(FieldAccess(Id(a),Id($b)),Id(a)),Id(func),[]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 316))
    
    ### Forloop   
    def test_317(self):
        input = """
        Class C{
            $forfunc(i : Int){
                Foreach(a In 1 .. 0x45){
                    Foreach(b In i - a .. i + 2*a By i){
                        Out::$println(b, a, i);
                    }
                }
            }
        }
        Class Program {
            main(){
                C::$forfunc(1);
            }
        }
        """
        expect = """Program([ClassDecl(Id(C),[MethodDecl(Id($forfunc),Static,[param(Id(i),IntType)],Block([For(Id(a),IntLit(1),IntLit(69),IntLit(1),Block([For(Id(b),BinaryOp(-,Id(i),Id(a)),BinaryOp(+,Id(i),BinaryOp(*,IntLit(2),Id(a))),Id(i),Block([Call(Id(Out),Id($println),[Id(b),Id(a),Id(i)])])])])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(C),Id($forfunc),[IntLit(1)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 317))
    
    def test_318(self):
        input = """
        Class A{
            
        }
        Class B{
            
        }
        Class C{
            Var $a, $b, $c: Int = 034, 045, 067;
            Var str: String = "D";
            $forfunc(i : Int){
                Foreach(a In 1 .. 0x45){
                    If((C::$a > 5) && (C::$b > C::$c)){
                        Foreach(b In i - a .. i + 2*a By i){
                            Out::$println(b, a, i);
                            C::$b = C::$b + b - C::$c;
                        }
                    }
                    C::$a = C::$a + a;
                }
                str = str +. "D";
                Return;
            }
        }
        Class Program {
            main(){
                C::$forfunc(1);
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),[]),ClassDecl(Id(C),[AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(28))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(37))),AttributeDecl(Static,VarDecl(Id($c),IntType,IntLit(55))),AttributeDecl(Instance,VarDecl(Id(str),StringType,StringLit(D))),MethodDecl(Id($forfunc),Static,[param(Id(i),IntType)],Block([For(Id(a),IntLit(1),IntLit(69),IntLit(1),Block([If(BinaryOp(&&,BinaryOp(>,FieldAccess(Id(C),Id($a)),IntLit(5)),BinaryOp(>,FieldAccess(Id(C),Id($b)),FieldAccess(Id(C),Id($c)))),Block([For(Id(b),BinaryOp(-,Id(i),Id(a)),BinaryOp(+,Id(i),BinaryOp(*,IntLit(2),Id(a))),Id(i),Block([Call(Id(Out),Id($println),[Id(b),Id(a),Id(i)]),AssignStmt(FieldAccess(Id(C),Id($b)),BinaryOp(-,BinaryOp(+,FieldAccess(Id(C),Id($b)),Id(b)),FieldAccess(Id(C),Id($c))))])])])),AssignStmt(FieldAccess(Id(C),Id($a)),BinaryOp(+,FieldAccess(Id(C),Id($a)),Id(a)))])]),AssignStmt(Id(str),BinaryOp(+.,Id(str),StringLit(D))),Return()]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(C),Id($forfunc),[IntLit(1)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 318))
    
    def test_319(self):
        input = """
        Class C{
            $forfunc(i : Int){
                Foreach(a In 1 .. 0x45){
                    Foreach(b In i - a .. i + 2*a By i){
                        Out.println(b, a, i);
                    }
                }
            }
        }
        Class Program {
            Val $b5, $b_6: Boolean = True, False;   
            Val b_7, $b_8, $b_9: String = "No I'" Not", "Seeya", "Gozen";
            main(){
                Var demo: C = New C();
                C::$forfunc(1);
            }
        }
        """
        expect = """Program([ClassDecl(Id(C),[MethodDecl(Id($forfunc),Static,[param(Id(i),IntType)],Block([For(Id(a),IntLit(1),IntLit(69),IntLit(1),Block([For(Id(b),BinaryOp(-,Id(i),Id(a)),BinaryOp(+,Id(i),BinaryOp(*,IntLit(2),Id(a))),Id(i),Block([Call(Id(Out),Id(println),[Id(b),Id(a),Id(i)])])])])])]))]),ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($b5),BoolType,BooleanLit(True))),AttributeDecl(Static,ConstDecl(Id($b_6),BoolType,BooleanLit(False))),AttributeDecl(Instance,ConstDecl(Id(b_7),StringType,StringLit(No I'" Not))),AttributeDecl(Static,ConstDecl(Id($b_8),StringType,StringLit(Seeya))),AttributeDecl(Static,ConstDecl(Id($b_9),StringType,StringLit(Gozen))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(demo),ClassType(Id(C)),NewExpr(Id(C),[])),Call(Id(C),Id($forfunc),[IntLit(1)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 319))
    
    ### If stmt
    def test_320(self):
        input = """
        Class Program {
            main(){
                If(x >= 1){
                    Global.doSomthing();
                }
                Elseif(x >= 0.5){
                    
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(>=,Id(x),IntLit(1)),Block([Call(Id(Global),Id(doSomthing),[])]),If(BinaryOp(>=,Id(x),FloatLit(0.5)),Block([])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 320))
    
    def test_321(self):
        input = """
        Class A{
            
        }
        Class D{
            daily(x : A){
                If(x.a > 3){}
                If(x.b >= 3){}
                If(x.a < 3){}
                If(x.a <= a.b().c){}
                If((x.a == x.b) || (x.a != x.b)){}
            }
        }
        Class Program {
            main(){
                D.daily(1);
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[]),ClassDecl(Id(D),[MethodDecl(Id(daily),Instance,[param(Id(x),ClassType(Id(A)))],Block([If(BinaryOp(>,FieldAccess(Id(x),Id(a)),IntLit(3)),Block([])),If(BinaryOp(>=,FieldAccess(Id(x),Id(b)),IntLit(3)),Block([])),If(BinaryOp(<,FieldAccess(Id(x),Id(a)),IntLit(3)),Block([])),If(BinaryOp(<=,FieldAccess(Id(x),Id(a)),FieldAccess(CallExpr(Id(a),Id(b),[]),Id(c))),Block([])),If(BinaryOp(||,BinaryOp(==,FieldAccess(Id(x),Id(a)),FieldAccess(Id(x),Id(b))),BinaryOp(!=,FieldAccess(Id(x),Id(a)),FieldAccess(Id(x),Id(b)))),Block([]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(D),Id(daily),[IntLit(1)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 321))
    
    def test_322(self):
        input = """
        Class A{
            
        }
        Class D{
            daily(x : A){
                If(x.a > 3){}
                Elseif(x.b >= 3){}
                If(x.a < 3){}
                Elseif(x.a <= a.b().c){}
                If((x.a == x.b) || (x.a != x.b)){}
                Else{
                    a = x.a + x.b;
                }
            }
        }
        Class Program {
            main(){
                D.daily(1);
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[]),ClassDecl(Id(D),[MethodDecl(Id(daily),Instance,[param(Id(x),ClassType(Id(A)))],Block([If(BinaryOp(>,FieldAccess(Id(x),Id(a)),IntLit(3)),Block([]),If(BinaryOp(>=,FieldAccess(Id(x),Id(b)),IntLit(3)),Block([]))),If(BinaryOp(<,FieldAccess(Id(x),Id(a)),IntLit(3)),Block([]),If(BinaryOp(<=,FieldAccess(Id(x),Id(a)),FieldAccess(CallExpr(Id(a),Id(b),[]),Id(c))),Block([]))),If(BinaryOp(||,BinaryOp(==,FieldAccess(Id(x),Id(a)),FieldAccess(Id(x),Id(b))),BinaryOp(!=,FieldAccess(Id(x),Id(a)),FieldAccess(Id(x),Id(b)))),Block([]),Block([AssignStmt(Id(a),BinaryOp(+,FieldAccess(Id(x),Id(a)),FieldAccess(Id(x),Id(b))))]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(D),Id(daily),[IntLit(1)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 322))
        
    def test_323(self):
        input = """
        Class D{
            $daily(x : A){
                If(x.a > 3){
                    If(x.b >= 3){}
                    Elseif(x.a < 3){
                        If(x.a <= a.b().c){}
                        Elseif((x.a == x.b) || (x.a != x.b)){}
                    }
                    Else{
                        a = x.a + x.b;
                    }
                }
                Else{
                    a = x.a + x.b;
                }
            }
            $showMaker(y : Array[Int, 5]){
                Global.doSomthing();
            }
        }
        Class Program {
            main(){
                D::$daily(1);
                D::$showMaker(Array(1,2,3,5,6));
            }
        }
        """
        expect = """Program([ClassDecl(Id(D),[MethodDecl(Id($daily),Static,[param(Id(x),ClassType(Id(A)))],Block([If(BinaryOp(>,FieldAccess(Id(x),Id(a)),IntLit(3)),Block([If(BinaryOp(>=,FieldAccess(Id(x),Id(b)),IntLit(3)),Block([]),If(BinaryOp(<,FieldAccess(Id(x),Id(a)),IntLit(3)),Block([If(BinaryOp(<=,FieldAccess(Id(x),Id(a)),FieldAccess(CallExpr(Id(a),Id(b),[]),Id(c))),Block([]),If(BinaryOp(||,BinaryOp(==,FieldAccess(Id(x),Id(a)),FieldAccess(Id(x),Id(b))),BinaryOp(!=,FieldAccess(Id(x),Id(a)),FieldAccess(Id(x),Id(b)))),Block([])))]),Block([AssignStmt(Id(a),BinaryOp(+,FieldAccess(Id(x),Id(a)),FieldAccess(Id(x),Id(b))))])))]),Block([AssignStmt(Id(a),BinaryOp(+,FieldAccess(Id(x),Id(a)),FieldAccess(Id(x),Id(b))))]))])),MethodDecl(Id($showMaker),Static,[param(Id(y),ArrayType(5,IntType))],Block([Call(Id(Global),Id(doSomthing),[])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(D),Id($daily),[IntLit(1)]),Call(Id(D),Id($showMaker),[[IntLit(1),IntLit(2),IntLit(3),IntLit(5),IntLit(6)]])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 323))
    
    ### Constructor / Destructor
    def test_324(self):
        input = """
        Class Pair{
            Var a, b: Int;
            Constructor(x, y: Int){
                Self.a = x;
                Self.b = y;
            }
        }
        Class Program {
            main(){
                Var p: Pair = Null;
                p = New Pair(2,3);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Pair),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(x)),AssignStmt(FieldAccess(Self(),Id(b)),Id(y))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(p),ClassType(Id(Pair)),NullLiteral()),AssignStmt(Id(p),NewExpr(Id(Pair),[IntLit(2),IntLit(3)]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,324))
    
    def test_325(self):
        input = """
        Class Royal{
            Var a, b, c, d, e: Float;
            Constructor(x, y: Float){
                Self.a = x;
                Self.b = y;
                Self.c = x - y;
                Self.d = x * y;
                Self.e = x + y;
            }
            Destructor(){
                Self.a = 0.0;
                Self.b = 0.0;
                Self.c = 0.0;
                Self.d = 0.0;
                Self.e = 0.0;
            }
        }
        Class Program {
            main(){
                Var p: Royal = Null;
                p = New Royal(.23e10, 123e10, 1.23e-10, 2.33e10, .e10);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Royal),[AttributeDecl(Instance,VarDecl(Id(a),FloatType)),AttributeDecl(Instance,VarDecl(Id(b),FloatType)),AttributeDecl(Instance,VarDecl(Id(c),FloatType)),AttributeDecl(Instance,VarDecl(Id(d),FloatType)),AttributeDecl(Instance,VarDecl(Id(e),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(x),FloatType),param(Id(y),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(x)),AssignStmt(FieldAccess(Self(),Id(b)),Id(y)),AssignStmt(FieldAccess(Self(),Id(c)),BinaryOp(-,Id(x),Id(y))),AssignStmt(FieldAccess(Self(),Id(d)),BinaryOp(*,Id(x),Id(y))),AssignStmt(FieldAccess(Self(),Id(e)),BinaryOp(+,Id(x),Id(y)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),FloatLit(0.0)),AssignStmt(FieldAccess(Self(),Id(b)),FloatLit(0.0)),AssignStmt(FieldAccess(Self(),Id(c)),FloatLit(0.0)),AssignStmt(FieldAccess(Self(),Id(d)),FloatLit(0.0)),AssignStmt(FieldAccess(Self(),Id(e)),FloatLit(0.0))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(p),ClassType(Id(Royal)),NullLiteral()),AssignStmt(Id(p),NewExpr(Id(Royal),[FloatLit(2300000000.0),FloatLit(1230000000000.0),FloatLit(1.23e-10),FloatLit(23300000000.0),FloatLit(0.0)]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,325))
    
    def test_326(self):
        input = """
        Class Pair{
            Var a, b: Int;
            Constructor(x, y: Int){
                Self.a = x;
                Self.b = y;
            }
            Constructor(x: Int){
                Self.a = x;
                Self.b = x;
            }
        }
        Class Program {
            main(){
                Var p, s: Pair = Null, New Pair(5);
                p = New Pair(2,3);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Pair),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(x)),AssignStmt(FieldAccess(Self(),Id(b)),Id(y))])),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(x)),AssignStmt(FieldAccess(Self(),Id(b)),Id(x))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(p),ClassType(Id(Pair)),NullLiteral()),VarDecl(Id(s),ClassType(Id(Pair)),NewExpr(Id(Pair),[IntLit(5)])),AssignStmt(Id(p),NewExpr(Id(Pair),[IntLit(2),IntLit(3)]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,326))
    
    def test_327(self):
        input = """
        Class Pair{
            Var a, b: Int;
            Constructor(x, y: Int){
                Self.a = x;
                Self.b = y;
            }
            Constructor(x: Int){
                Self.a = x;
                Self.b = x;
            }
            Destructor(){
                Self.a = 1;
                Self.b = 2;
            }
        }
        Class Program {
            main(){
                Var p, s: Pair = Null, New Pair(5);
                p = New Pair(2,3);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Pair),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType),param(Id(y),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(x)),AssignStmt(FieldAccess(Self(),Id(b)),Id(y))])),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(a)),Id(x)),AssignStmt(FieldAccess(Self(),Id(b)),Id(x))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(a)),IntLit(1)),AssignStmt(FieldAccess(Self(),Id(b)),IntLit(2))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(p),ClassType(Id(Pair)),NullLiteral()),VarDecl(Id(s),ClassType(Id(Pair)),NewExpr(Id(Pair),[IntLit(5)])),AssignStmt(Id(p),NewExpr(Id(Pair),[IntLit(2),IntLit(3)]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,327))
    
    ### Array
    def test_328(self):
        input = """Class A{
            Val a, b : Array[Int, 3] = Array(1, 100, 11),  Array(0x12, 0100, 0b11);
            Var c, d, e : Array[String, 4];
        }
        Class Program{
            main(){}
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(3,IntType),[IntLit(1),IntLit(100),IntLit(11)])),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(3,IntType),[IntLit(18),IntLit(64),IntLit(3)])),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(4,StringType))),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(4,StringType))),AttributeDecl(Instance,VarDecl(Id(e),ArrayType(4,StringType)))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input, expect, 328))
    
    def test_329(self):
        input = """
        Class A{
        
        }
        Class Program{
            main(){
                Val a, b : Array[Int, 3] = Array(1, 100, 11),  Array(0x12, 0100, 0b11);
                Var c, d, e : Array[String, 4];
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),ArrayType(3,IntType),[IntLit(1),IntLit(100),IntLit(11)]),ConstDecl(Id(b),ArrayType(3,IntType),[IntLit(18),IntLit(64),IntLit(3)]),VarDecl(Id(c),ArrayType(4,StringType)),VarDecl(Id(d),ArrayType(4,StringType)),VarDecl(Id(e),ArrayType(4,StringType))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 329))
    
    def test_330(self):
        input = """
        Class A{
            Var a : Array[Int, 5] = Array(1 * 2 / 3, 3 + 3 / 3, 10 - -9, 100 * 3, 100 % 10);
            Val b : Array[Array[Float, 5], 5];
            Val includeHosts : Array[Int, 100] = A::$x;
        }
        Class Program{
            main(){
                Val a1, b2 : Array[Int, 3] = Array(1, 100, 11),  Array(0x12, 0100, 0b11);
                Var c5, d4, e3 : Array[String, 4];
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(+,IntLit(3),BinaryOp(/,IntLit(3),IntLit(3))),BinaryOp(-,IntLit(10),UnaryOp(-,IntLit(9))),BinaryOp(*,IntLit(100),IntLit(3)),BinaryOp(%,IntLit(100),IntLit(10))])),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(5,ArrayType(5,FloatType)),None)),AttributeDecl(Instance,ConstDecl(Id(includeHosts),ArrayType(100,IntType),FieldAccess(Id(A),Id($x))))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a1),ArrayType(3,IntType),[IntLit(1),IntLit(100),IntLit(11)]),ConstDecl(Id(b2),ArrayType(3,IntType),[IntLit(18),IntLit(64),IntLit(3)]),VarDecl(Id(c5),ArrayType(4,StringType)),VarDecl(Id(d4),ArrayType(4,StringType)),VarDecl(Id(e3),ArrayType(4,StringType))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 330))
    
    ### Array Cell
    def test_331(self):
        input = """
        Class Program{
            main(){
                Var a: Array[Boolean, 4];
                a[1] = True;
                a[2] = a[1];
                a[1 + 2] = False;
                a[0xC / 0b100] = True;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(4,BoolType)),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(2)]),ArrayCell(Id(a),[IntLit(1)])),AssignStmt(ArrayCell(Id(a),[BinaryOp(+,IntLit(1),IntLit(2))]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[BinaryOp(/,IntLit(12),IntLit(4))]),BooleanLit(True))]))])])"""       
        self.assertTrue(TestAST.test(input, expect, 331))
    
    def test_332(self):
        input = """
        Class Program{
            main(){
                Var arr: Array[Array[Boolean, 3], 2];
                arr[0][0] = True;
                arr[0][1] = False;
                arr[1][0] = True;
                arr[1][1] = False;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(arr),ArrayType(2,ArrayType(3,BoolType))),AssignStmt(ArrayCell(Id(arr),[IntLit(0),IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(arr),[IntLit(0),IntLit(1)]),BooleanLit(False)),AssignStmt(ArrayCell(Id(arr),[IntLit(1),IntLit(0)]),BooleanLit(True)),AssignStmt(ArrayCell(Id(arr),[IntLit(1),IntLit(1)]),BooleanLit(False))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 332))
    
    def test_333(self):
        input = """
        Class Program{
            Val $arr, $brr: Array[Array[Float, 2], 3] = Array(Array(2.1, -1.3), Array(0.1, 3.1e3), Array(-0.00001, 123.321E-123)), Array(Array(1.2, 0.132), Array(0.9931, 10.1e3), Array(0.00001111, 1111111119.332321e-2));
            main(){
                Val a : Array[Array[String, 2], 2];
                a = Array(Array("Yo", "Hello"), Array("Nice", "To"));
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($arr),ArrayType(3,ArrayType(2,FloatType)),[[FloatLit(2.1),UnaryOp(-,FloatLit(1.3))],[FloatLit(0.1),FloatLit(3100.0)],[UnaryOp(-,FloatLit(1e-05)),FloatLit(1.23321e-121)]])),AttributeDecl(Static,ConstDecl(Id($brr),ArrayType(3,ArrayType(2,FloatType)),[[FloatLit(1.2),FloatLit(0.132)],[FloatLit(0.9931),FloatLit(10100.0)],[FloatLit(1.111e-05),FloatLit(11111111.19332321)]])),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),ArrayType(2,ArrayType(2,StringType)),None),AssignStmt(Id(a),[[StringLit(Yo),StringLit(Hello)],[StringLit(Nice),StringLit(To)]])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 333))
    
    def test_334(self):
        input = """
        Class Program{
            Val $arr, $brr: Array[Array[Float, 2], 3] = Array(Array(2.1, -1.3), Array(0.1, 3.1e3), Array(-0.00001, 123.321E-123)), Array(Array(1.2, 0.132), Array(0.9931, 10.1e3), Array(0.00001111, 1111111119.332321e-2));
            nest(x : Array[Array[Float, 2], 3]){
                Return x[0];
            }
            main(){
                Out.print(Self.nest(Program::$arr)[1]);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($arr),ArrayType(3,ArrayType(2,FloatType)),[[FloatLit(2.1),UnaryOp(-,FloatLit(1.3))],[FloatLit(0.1),FloatLit(3100.0)],[UnaryOp(-,FloatLit(1e-05)),FloatLit(1.23321e-121)]])),AttributeDecl(Static,ConstDecl(Id($brr),ArrayType(3,ArrayType(2,FloatType)),[[FloatLit(1.2),FloatLit(0.132)],[FloatLit(0.9931),FloatLit(10100.0)],[FloatLit(1.111e-05),FloatLit(11111111.19332321)]])),MethodDecl(Id(nest),Instance,[param(Id(x),ArrayType(3,ArrayType(2,FloatType)))],Block([Return(ArrayCell(Id(x),[IntLit(0)]))])),MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(print),[ArrayCell(CallExpr(Self(),Id(nest),[FieldAccess(Id(Program),Id($arr))]),[IntLit(1)])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 334))
    
    ### Multiple method
    def test_335(self):
        input = """
        Class Work{
            
        }
        Class Util: Work{
            func1(){}
            func2(a, b: Int){}
            func3(c, d: Float; e: String){}
            func4(a, c, d: Array[String, 3]; f: Boolean){}
            Constructor(a: Array[Array[String, 3], 2]){}
            Destructor(){}
        }
        Class Program{
            main(){
                Var w : Work;
                w = New Util(Array(Array("Yo", "Hello", "Sup"), Array("Nice", "To", "Meet")));
            }
        }
        """
        expect = """Program([ClassDecl(Id(Work),[]),ClassDecl(Id(Util),Id(Work),[MethodDecl(Id(func1),Instance,[],Block([])),MethodDecl(Id(func2),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([])),MethodDecl(Id(func3),Instance,[param(Id(c),FloatType),param(Id(d),FloatType),param(Id(e),StringType)],Block([])),MethodDecl(Id(func4),Instance,[param(Id(a),ArrayType(3,StringType)),param(Id(c),ArrayType(3,StringType)),param(Id(d),ArrayType(3,StringType)),param(Id(f),BoolType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ArrayType(2,ArrayType(3,StringType)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(w),ClassType(Id(Work)),NullLiteral()),AssignStmt(Id(w),NewExpr(Id(Util),[[[StringLit(Yo),StringLit(Hello),StringLit(Sup)],[StringLit(Nice),StringLit(To),StringLit(Meet)]]]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 335))
    
    def test_336(self):
        input = """
        Class AB{}
        Class Work{
            func(a: Int; b: Float; c: Boolean; d: String; e: AB; f: Array[Float, 3]){}
        }
        Class Util: Work{
            func1(){}
            func2(a, b: Int){}
            $func3(c, d: Float; e: String){}
            $func4(a, c, d: Array[String, 3]; f: Boolean){}
            Constructor(a: Array[Array[String, 3], 2]){}
            Destructor(){}
        }
        Class Program{
            main(){
                Var w : Work;
                w = New Util(Array(Array("Yo", "Hello", "Sup"), Array("Nice", "To", "Meet")));
                w.func();
                w.func1();
                w.func2(1, 0x4);
                Util::$func3(1.0, 0.2e3, "Nope");
                Util::$func4(Array("Yo", "Hello", "Sup"), True);
            }
        }
        """
        expect = """Program([ClassDecl(Id(AB),[]),ClassDecl(Id(Work),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),BoolType),param(Id(d),StringType),param(Id(e),ClassType(Id(AB))),param(Id(f),ArrayType(3,FloatType))],Block([]))]),ClassDecl(Id(Util),Id(Work),[MethodDecl(Id(func1),Instance,[],Block([])),MethodDecl(Id(func2),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([])),MethodDecl(Id($func3),Static,[param(Id(c),FloatType),param(Id(d),FloatType),param(Id(e),StringType)],Block([])),MethodDecl(Id($func4),Static,[param(Id(a),ArrayType(3,StringType)),param(Id(c),ArrayType(3,StringType)),param(Id(d),ArrayType(3,StringType)),param(Id(f),BoolType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ArrayType(2,ArrayType(3,StringType)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(w),ClassType(Id(Work)),NullLiteral()),AssignStmt(Id(w),NewExpr(Id(Util),[[[StringLit(Yo),StringLit(Hello),StringLit(Sup)],[StringLit(Nice),StringLit(To),StringLit(Meet)]]])),Call(Id(w),Id(func),[]),Call(Id(w),Id(func1),[]),Call(Id(w),Id(func2),[IntLit(1),IntLit(4)]),Call(Id(Util),Id($func3),[FloatLit(1.0),FloatLit(200.0),StringLit(Nope)]),Call(Id(Util),Id($func4),[[StringLit(Yo),StringLit(Hello),StringLit(Sup)],BooleanLit(True)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 336))
    
    def test_337(self):
        input = """
        Class AB{
            func1(){}
        }
        Class Work{
            func(a: Int; b: Float; c: Boolean; d: String; e: AB; f: Array[Float, 3]){
                Val a: AB = New AB();
                a.func1();
            }
            func2(a, b: Int){
                Self.func(a + b, 1.2, False, "Nope", New AB(), Array(1.2, 3.234, 1.2e3));
            }
        }
        Class Util: Work{
            $func3(c, d: Float; e: String){}
            $func4(a, c, d: Array[String, 3]; f: Boolean){}
            Constructor(a: Array[Array[String, 3], 2]){}
            Destructor(){}
        }
        Class Program{
            main(){
                Var w : Work;
                w = New Util(Array(Array("Yo", "Hello", "Sup"), Array("Nice", "To", "Meet")));
                w.func();
                w.func1();
                w.func2(1, 0x4);
                Util::$func3(1.0, 0.2e3, "Nope");
                Util::$func4(Array("Yo", "Hello", "Sup"), True);
            }
        }
        """
        expect = """Program([ClassDecl(Id(AB),[MethodDecl(Id(func1),Instance,[],Block([]))]),ClassDecl(Id(Work),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),BoolType),param(Id(d),StringType),param(Id(e),ClassType(Id(AB))),param(Id(f),ArrayType(3,FloatType))],Block([ConstDecl(Id(a),ClassType(Id(AB)),NewExpr(Id(AB),[])),Call(Id(a),Id(func1),[])])),MethodDecl(Id(func2),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Call(Self(),Id(func),[BinaryOp(+,Id(a),Id(b)),FloatLit(1.2),BooleanLit(False),StringLit(Nope),NewExpr(Id(AB),[]),[FloatLit(1.2),FloatLit(3.234),FloatLit(1200.0)]])]))]),ClassDecl(Id(Util),Id(Work),[MethodDecl(Id($func3),Static,[param(Id(c),FloatType),param(Id(d),FloatType),param(Id(e),StringType)],Block([])),MethodDecl(Id($func4),Static,[param(Id(a),ArrayType(3,StringType)),param(Id(c),ArrayType(3,StringType)),param(Id(d),ArrayType(3,StringType)),param(Id(f),BoolType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ArrayType(2,ArrayType(3,StringType)))],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(w),ClassType(Id(Work)),NullLiteral()),AssignStmt(Id(w),NewExpr(Id(Util),[[[StringLit(Yo),StringLit(Hello),StringLit(Sup)],[StringLit(Nice),StringLit(To),StringLit(Meet)]]])),Call(Id(w),Id(func),[]),Call(Id(w),Id(func1),[]),Call(Id(w),Id(func2),[IntLit(1),IntLit(4)]),Call(Id(Util),Id($func3),[FloatLit(1.0),FloatLit(200.0),StringLit(Nope)]),Call(Id(Util),Id($func4),[[StringLit(Yo),StringLit(Hello),StringLit(Sup)],BooleanLit(True)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 337))
    
    ### Expr
    def test_338(self):
        input = """
        Class Shape {
            Val My1stCons, My2ndCons: Int = 1 + 5/2, 2;
            Var $x, $y : Int = 0 + - 2 * 4 % 3, 0 -- 1;
        }
        Class Program {
            ## Muda
            Muda ##
            main(){
                a = 1.0;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),BinaryOp(/,IntLit(5),IntLit(2))))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($x),IntType,BinaryOp(+,IntLit(0),BinaryOp(%,BinaryOp(*,UnaryOp(-,IntLit(2)),IntLit(4)),IntLit(3))))),AttributeDecl(Static,VarDecl(Id($y),IntType,BinaryOp(-,IntLit(0),UnaryOp(-,IntLit(1)))))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),FloatLit(1.0))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 338))
        
    def test_339(self):
        input = """
        Class Shape {
            Val S1stCons, S2ndCons: Int = 1 * -5/2, -2 + 3 - Self.length("Sup" +. "Daily");
            Var $x, $y : Int = 0 + - 2 * 4 % 3, 0 -- 1;
            Var $array: Array[Int, 5] = Array(1,2,3,4,5);
        }
        Class Program {
            ## Muda
            Muda ##
            main(){
                Var d: Shape = New Shape();
                If (!(Shape::$x > Shape::$y + d.S1stCons)){
                    
                }
                Elseif((Shape::$x > Shape::$y + d.array[1]) && c > 2){
                    
                }
                Else{
                    a = 1.0;
                }
                
            }
        }
        """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(S1stCons),IntType,BinaryOp(/,BinaryOp(*,IntLit(1),UnaryOp(-,IntLit(5))),IntLit(2)))),AttributeDecl(Instance,ConstDecl(Id(S2ndCons),IntType,BinaryOp(-,BinaryOp(+,UnaryOp(-,IntLit(2)),IntLit(3)),CallExpr(Self(),Id(length),[BinaryOp(+.,StringLit(Sup),StringLit(Daily))])))),AttributeDecl(Static,VarDecl(Id($x),IntType,BinaryOp(+,IntLit(0),BinaryOp(%,BinaryOp(*,UnaryOp(-,IntLit(2)),IntLit(4)),IntLit(3))))),AttributeDecl(Static,VarDecl(Id($y),IntType,BinaryOp(-,IntLit(0),UnaryOp(-,IntLit(1))))),AttributeDecl(Static,VarDecl(Id($array),ArrayType(5,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(d),ClassType(Id(Shape)),NewExpr(Id(Shape),[])),If(UnaryOp(!,BinaryOp(>,FieldAccess(Id(Shape),Id($x)),BinaryOp(+,FieldAccess(Id(Shape),Id($y)),FieldAccess(Id(d),Id(S1stCons))))),Block([]),If(BinaryOp(>,BinaryOp(&&,BinaryOp(>,FieldAccess(Id(Shape),Id($x)),BinaryOp(+,FieldAccess(Id(Shape),Id($y)),ArrayCell(FieldAccess(Id(d),Id(array)),[IntLit(1)]))),Id(c)),IntLit(2)),Block([]),Block([AssignStmt(Id(a),FloatLit(1.0))])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 339))
    
    ### Heap
    def test_340(self):
        input = """
        Class A{
            Val $a, $b: Int;
            Val $d, $e: Float;
        }
        Class Program {
            main(){
                Var d : Int = A::$a + A::$b;
                Var e: Float = A::$d + A::$e; 
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Static,ConstDecl(Id($b),IntType,None)),AttributeDecl(Static,ConstDecl(Id($d),FloatType,None)),AttributeDecl(Static,ConstDecl(Id($e),FloatType,None))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(d),IntType,BinaryOp(+,FieldAccess(Id(A),Id($a)),FieldAccess(Id(A),Id($b)))),VarDecl(Id(e),FloatType,BinaryOp(+,FieldAccess(Id(A),Id($d)),FieldAccess(Id(A),Id($e))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,340))
    
    def test_341(self):
        input = """
        Class A{
            Val $a, $b: Int;
            Val $d, $e: Float;
            Var $s: Int = 1;
            main(){
                If(d * 5 + 1 == 0){
                    Return 2;
                }
                Elseif(A::$a > 4){
                    Foreach(ad In -1 .. A::$b By 2){
                        A::$s = A::$s + ad;
                    }
                    Return A::$s;
                }
            }
            gg(a: Array[Int, 5]){
                A::$s = A::$s + a[1];
            }
        }
        Class Program {
            main(){
                Var d : Int = A::$a + A::$b;
                Var e: Float = A::$d + A::$e; 
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Static,ConstDecl(Id($b),IntType,None)),AttributeDecl(Static,ConstDecl(Id($d),FloatType,None)),AttributeDecl(Static,ConstDecl(Id($e),FloatType,None)),AttributeDecl(Static,VarDecl(Id($s),IntType,IntLit(1))),MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(==,BinaryOp(+,BinaryOp(*,Id(d),IntLit(5)),IntLit(1)),IntLit(0)),Block([Return(IntLit(2))]),If(BinaryOp(>,FieldAccess(Id(A),Id($a)),IntLit(4)),Block([For(Id(ad),UnaryOp(-,IntLit(1)),FieldAccess(Id(A),Id($b)),IntLit(2),Block([AssignStmt(FieldAccess(Id(A),Id($s)),BinaryOp(+,FieldAccess(Id(A),Id($s)),Id(ad)))])]),Return(FieldAccess(Id(A),Id($s)))])))])),MethodDecl(Id(gg),Instance,[param(Id(a),ArrayType(5,IntType))],Block([AssignStmt(FieldAccess(Id(A),Id($s)),BinaryOp(+,FieldAccess(Id(A),Id($s)),ArrayCell(Id(a),[IntLit(1)])))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(d),IntType,BinaryOp(+,FieldAccess(Id(A),Id($a)),FieldAccess(Id(A),Id($b)))),VarDecl(Id(e),FloatType,BinaryOp(+,FieldAccess(Id(A),Id($d)),FieldAccess(Id(A),Id($e))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,341))
    
    def test_342(self):
        input = """
        Class A{
            Val $a, $b: Int;
            Val $d, $e: Float;
            Var $s: Int = 1;
            main(){
                If(d * 5 + 1 == 0){
                    Return 2;
                }
                Elseif(A::$a > 4){
                    Foreach(ad In -1 .. A::$b By 2){
                        A::$s = A::$s + ad;
                    }
                    Return A::$s;
                }
            }
            gg(a: Array[Int, 2]){
                A::$s = A::$s + a[1];
            }
            Constructor(a: Array[Int, 2]; b: Array[Float, 2]){
                A::$a = a[1];
                A::$b = a[2];
                A::$c = b[1];
                A::$d = b[2];
            }
        }
        Class Program {
            main(){
                Var d : Int = A::$a + A::$b;
                Var e: Float = A::$d + A::$e; 
                Var c, f: A;
                c = New A(Array(d, d + 1), Array(e, -e));
                c.gg(Array(d, d + 1));
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($a),IntType,None)),AttributeDecl(Static,ConstDecl(Id($b),IntType,None)),AttributeDecl(Static,ConstDecl(Id($d),FloatType,None)),AttributeDecl(Static,ConstDecl(Id($e),FloatType,None)),AttributeDecl(Static,VarDecl(Id($s),IntType,IntLit(1))),MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(==,BinaryOp(+,BinaryOp(*,Id(d),IntLit(5)),IntLit(1)),IntLit(0)),Block([Return(IntLit(2))]),If(BinaryOp(>,FieldAccess(Id(A),Id($a)),IntLit(4)),Block([For(Id(ad),UnaryOp(-,IntLit(1)),FieldAccess(Id(A),Id($b)),IntLit(2),Block([AssignStmt(FieldAccess(Id(A),Id($s)),BinaryOp(+,FieldAccess(Id(A),Id($s)),Id(ad)))])]),Return(FieldAccess(Id(A),Id($s)))])))])),MethodDecl(Id(gg),Instance,[param(Id(a),ArrayType(2,IntType))],Block([AssignStmt(FieldAccess(Id(A),Id($s)),BinaryOp(+,FieldAccess(Id(A),Id($s)),ArrayCell(Id(a),[IntLit(1)])))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ArrayType(2,IntType)),param(Id(b),ArrayType(2,FloatType))],Block([AssignStmt(FieldAccess(Id(A),Id($a)),ArrayCell(Id(a),[IntLit(1)])),AssignStmt(FieldAccess(Id(A),Id($b)),ArrayCell(Id(a),[IntLit(2)])),AssignStmt(FieldAccess(Id(A),Id($c)),ArrayCell(Id(b),[IntLit(1)])),AssignStmt(FieldAccess(Id(A),Id($d)),ArrayCell(Id(b),[IntLit(2)]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(d),IntType,BinaryOp(+,FieldAccess(Id(A),Id($a)),FieldAccess(Id(A),Id($b)))),VarDecl(Id(e),FloatType,BinaryOp(+,FieldAccess(Id(A),Id($d)),FieldAccess(Id(A),Id($e)))),VarDecl(Id(c),ClassType(Id(A)),NullLiteral()),VarDecl(Id(f),ClassType(Id(A)),NullLiteral()),AssignStmt(Id(c),NewExpr(Id(A),[[Id(d),BinaryOp(+,Id(d),IntLit(1))],[Id(e),UnaryOp(-,Id(e))]])),Call(Id(c),Id(gg),[[Id(d),BinaryOp(+,Id(d),IntLit(1))]])]))])])"""
        self.assertTrue(TestAST.test(input,expect,342))
    
    def test_343(self):
        input = """
        Class Program{
            main(){
                Var str: String = "Ta jia hao! Wo shi zhenguoyue.";
                If (str < "a"){
                    If (str.len > 10){
                        If (str.contains("jia")){
                            Return "jia";
                        }
                        Else{
                            Return str.strip("!");
                        }
                    }
                    Elseif(str.len == 10){
                        If (str.contains("jia")){
                            Return str +. "Lai zi Yuenan, xin nian kuai le!";
                        }
                    }
                    ## str.len < 10##
                    Else{
                        If(str.len < 3){
                            Foreach (i In 1 .. 100){
                                A::$DoNothing();
                            }
                        }
                        Elseif(str.len != 5){
                            If(str.len % 3 == 0){
                                System.print(a || b);
                            }
                        }
                    }
                }
            }
            Constructor(a, b: Boolean){
                If (!a){
                    Return a && b;
                }
                Else{
                    Return a || b;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(str),StringType,StringLit(Ta jia hao! Wo shi zhenguoyue.)),If(BinaryOp(<,Id(str),StringLit(a)),Block([If(BinaryOp(>,FieldAccess(Id(str),Id(len)),IntLit(10)),Block([If(CallExpr(Id(str),Id(contains),[StringLit(jia)]),Block([Return(StringLit(jia))]),Block([Return(CallExpr(Id(str),Id(strip),[StringLit(!)]))]))]),If(BinaryOp(==,FieldAccess(Id(str),Id(len)),IntLit(10)),Block([If(CallExpr(Id(str),Id(contains),[StringLit(jia)]),Block([Return(BinaryOp(+.,Id(str),StringLit(Lai zi Yuenan, xin nian kuai le!)))]))]),Block([If(BinaryOp(<,FieldAccess(Id(str),Id(len)),IntLit(3)),Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(A),Id($DoNothing),[])])])]),If(BinaryOp(!=,FieldAccess(Id(str),Id(len)),IntLit(5)),Block([If(BinaryOp(==,BinaryOp(%,FieldAccess(Id(str),Id(len)),IntLit(3)),IntLit(0)),Block([Call(Id(System),Id(print),[BinaryOp(||,Id(a),Id(b))])]))])))])))]))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),BoolType),param(Id(b),BoolType)],Block([If(UnaryOp(!,Id(a)),Block([Return(BinaryOp(&&,Id(a),Id(b)))]),Block([Return(BinaryOp(||,Id(a),Id(b)))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 343))
    
    def test_344(self):
        input = """
        Class str{
            Var d: String;
            Constructor(a, b: Boolean){
                If (!a){
                    Return a && b;
                }
                Else{
                    Return a || b;
                }
            }
            Constructor(v: String){
                Self.d = v;
            }
            contains(v: String){
                Return v ==. sv;
            }
        }
        Class Program{
            main(){
                Var str: String = "Ta jia hao! Wo shi zhenguoyue.";
                If (str ==. "a"){
                    If (str.len > 10){
                        If (str.contains("jia")){
                            Return "jia";
                        }
                        Else{
                            Return str.strip("!");
                        }
                    }
                    Elseif(str.len == 10){
                        If (str.contains("jia")){
                            Return str +. "Lai zi Yuenan, xin nian kuai le!";
                        }
                    }
                    ## str.len < 10##
                    Else{
                        If(str.len < 3){
                            Foreach (i In 1 .. 100){
                                A::$DoNothing();
                            }
                        }
                        Elseif(str.len != 5){
                            If(str.len % 3 == 0){
                                System.print(a || b);
                            }
                        }
                    }
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(str),[AttributeDecl(Instance,VarDecl(Id(d),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(a),BoolType),param(Id(b),BoolType)],Block([If(UnaryOp(!,Id(a)),Block([Return(BinaryOp(&&,Id(a),Id(b)))]),Block([Return(BinaryOp(||,Id(a),Id(b)))]))])),MethodDecl(Id(Constructor),Instance,[param(Id(v),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(d)),Id(v))])),MethodDecl(Id(contains),Instance,[param(Id(v),StringType)],Block([Return(BinaryOp(==.,Id(v),Id(sv)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(str),StringType,StringLit(Ta jia hao! Wo shi zhenguoyue.)),If(BinaryOp(==.,Id(str),StringLit(a)),Block([If(BinaryOp(>,FieldAccess(Id(str),Id(len)),IntLit(10)),Block([If(CallExpr(Id(str),Id(contains),[StringLit(jia)]),Block([Return(StringLit(jia))]),Block([Return(CallExpr(Id(str),Id(strip),[StringLit(!)]))]))]),If(BinaryOp(==,FieldAccess(Id(str),Id(len)),IntLit(10)),Block([If(CallExpr(Id(str),Id(contains),[StringLit(jia)]),Block([Return(BinaryOp(+.,Id(str),StringLit(Lai zi Yuenan, xin nian kuai le!)))]))]),Block([If(BinaryOp(<,FieldAccess(Id(str),Id(len)),IntLit(3)),Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(A),Id($DoNothing),[])])])]),If(BinaryOp(!=,FieldAccess(Id(str),Id(len)),IntLit(5)),Block([If(BinaryOp(==,BinaryOp(%,FieldAccess(Id(str),Id(len)),IntLit(3)),IntLit(0)),Block([Call(Id(System),Id(print),[BinaryOp(||,Id(a),Id(b))])]))])))])))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 344))
    
    def test_345(self):
        input="""
        Class Program{
            main(){
                If(a==b){}
                If(b<c){}Else{}
                If(a==b){}Elseif(b<c){}
                If(a==b){}Elseif(b<c){}Else{}
            }
        }
        """
        expect="Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([])),If(BinaryOp(<,Id(b),Id(c)),Block([]),Block([])),If(BinaryOp(==,Id(a),Id(b)),Block([]),If(BinaryOp(<,Id(b),Id(c)),Block([]))),If(BinaryOp(==,Id(a),Id(b)),Block([]),If(BinaryOp(<,Id(b),Id(c)),Block([]),Block([])))]))])])"
        self.assertTrue(TestAST.test(input,expect,345))
     
    def test_346(self):
        input = """Class PrimeNumber {
            isPrimeNumber(n: Int) {
                Foreach(i In 2 .. n/2) {
                    If (n % i == 0) {
                        Return false;
                    }
                }
                Return true;
            }
        }
        Class Fibonacci {
            isFibonacci(n: Int) {
                Var a, b, Sum: Int = 0, 1, 0;
                Foreach(Sum In 0 .. n) {
                    Sum = a + b;
                    a = b;
                    b = Sum;
                    If (n == Sum) {
                        Return true;
                    }
                    Return false;
                }
            }
        }
        Class TriangleNumber{
            isTriangleNumber(n: Int) {
                Return (n * (n + 1)) / 2;
            }
        }
        Class Display {
            display(pR: Float) {
                If (pR < 0) {
                    pR = 0;
                }
                If (pR > 1) {
                    pR = 1;
                }
                pR = System.round(pR * 1000) / 1000;
                Out.print(pR);
            }
        }
        Class Program {
            main() {
                Var hp, d, s: Int = 0, 0, 0;
                Var P1, P2, f, pR: Float = 0, 0, 0, -1;
                If (System.readFile(hp, d, s)) {
                    If (PrimeNumber.isPrimeNumber(hp)) {
                        P1 = 1000;
                        P2 = (hp + s) % 1000;
                    }
                    Else {
                        P1 = hp;
                        P2 = (hp + d) % 100;
                    }
                }
                Var g: Float;
                If (d < 200 && !Fibonacci.isFibonacci(d + s)) {
                    f = 0;
                }
                Elseif (((d >= 200) && (d <= 800)) || (d < 200 && Fibonacci.isFibonacci(d + s))) {
                    If (s % 6 == 0) {
                        g = s/2;
                    }
                    Elseif (s % 6 == 1) {
                        g = 2 * s;
                    }
                    Elseif (s % 6 == 2) {
                        g = -Math.pow(s % 9, 3) / 5;
                    }
                    Elseif (s % 6 == 3) {
                        g = -Math.pow(s % 30, 2) + 3 * s;
                    }
                    Elseif (s % 6 == 4) {
                        g = -s;
                    }
                    Elseif (s % 6 == 5) {
                        g = -TriangleNumber.isTriangleNumber((s % 5) + 5);
                    }
                    f = 40 - Math.abs(d - 500) / 20 + g;
                }
                Elseif (d > 800) {
                    f = (-d * s) / 1000;
                }
                Var Bitten: Float;
                If ((d >= 200) && (d <= 300)) {
                    Bitten = (d + P1 + P2) / 1000;
                    If (Bitten > 0.8) {
                        pR = 0;
                    }
                }
                Else {
                    pR = (P1 + P2 * f) / (1000 + Math.abs(P2 * f));
                }
                Display.display(pR);
            }
        }
        """
        expect = "Program([ClassDecl(Id(PrimeNumber),[MethodDecl(Id(isPrimeNumber),Instance,[param(Id(n),IntType)],Block([For(Id(i),IntLit(2),BinaryOp(/,Id(n),IntLit(2)),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,Id(n),Id(i)),IntLit(0)),Block([Return(Id(false))]))])]),Return(Id(true))]))]),ClassDecl(Id(Fibonacci),[MethodDecl(Id(isFibonacci),Instance,[param(Id(n),IntType)],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(1)),VarDecl(Id(Sum),IntType,IntLit(0)),For(Id(Sum),IntLit(0),Id(n),IntLit(1),Block([AssignStmt(Id(Sum),BinaryOp(+,Id(a),Id(b))),AssignStmt(Id(a),Id(b)),AssignStmt(Id(b),Id(Sum)),If(BinaryOp(==,Id(n),Id(Sum)),Block([Return(Id(true))])),Return(Id(false))])])]))]),ClassDecl(Id(TriangleNumber),[MethodDecl(Id(isTriangleNumber),Instance,[param(Id(n),IntType)],Block([Return(BinaryOp(/,BinaryOp(*,Id(n),BinaryOp(+,Id(n),IntLit(1))),IntLit(2)))]))]),ClassDecl(Id(Display),[MethodDecl(Id(display),Instance,[param(Id(pR),FloatType)],Block([If(BinaryOp(<,Id(pR),IntLit(0)),Block([AssignStmt(Id(pR),IntLit(0))])),If(BinaryOp(>,Id(pR),IntLit(1)),Block([AssignStmt(Id(pR),IntLit(1))])),AssignStmt(Id(pR),BinaryOp(/,CallExpr(Id(System),Id(round),[BinaryOp(*,Id(pR),IntLit(1000))]),IntLit(1000))),Call(Id(Out),Id(print),[Id(pR)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(hp),IntType,IntLit(0)),VarDecl(Id(d),IntType,IntLit(0)),VarDecl(Id(s),IntType,IntLit(0)),VarDecl(Id(P1),FloatType,IntLit(0)),VarDecl(Id(P2),FloatType,IntLit(0)),VarDecl(Id(f),FloatType,IntLit(0)),VarDecl(Id(pR),FloatType,UnaryOp(-,IntLit(1))),If(CallExpr(Id(System),Id(readFile),[Id(hp),Id(d),Id(s)]),Block([If(CallExpr(Id(PrimeNumber),Id(isPrimeNumber),[Id(hp)]),Block([AssignStmt(Id(P1),IntLit(1000)),AssignStmt(Id(P2),BinaryOp(%,BinaryOp(+,Id(hp),Id(s)),IntLit(1000)))]),Block([AssignStmt(Id(P1),Id(hp)),AssignStmt(Id(P2),BinaryOp(%,BinaryOp(+,Id(hp),Id(d)),IntLit(100)))]))])),VarDecl(Id(g),FloatType),If(BinaryOp(<,Id(d),BinaryOp(&&,IntLit(200),UnaryOp(!,CallExpr(Id(Fibonacci),Id(isFibonacci),[BinaryOp(+,Id(d),Id(s))])))),Block([AssignStmt(Id(f),IntLit(0))]),If(BinaryOp(||,BinaryOp(&&,BinaryOp(>=,Id(d),IntLit(200)),BinaryOp(<=,Id(d),IntLit(800))),BinaryOp(<,Id(d),BinaryOp(&&,IntLit(200),CallExpr(Id(Fibonacci),Id(isFibonacci),[BinaryOp(+,Id(d),Id(s))])))),Block([If(BinaryOp(==,BinaryOp(%,Id(s),IntLit(6)),IntLit(0)),Block([AssignStmt(Id(g),BinaryOp(/,Id(s),IntLit(2)))]),If(BinaryOp(==,BinaryOp(%,Id(s),IntLit(6)),IntLit(1)),Block([AssignStmt(Id(g),BinaryOp(*,IntLit(2),Id(s)))]),If(BinaryOp(==,BinaryOp(%,Id(s),IntLit(6)),IntLit(2)),Block([AssignStmt(Id(g),BinaryOp(/,UnaryOp(-,CallExpr(Id(Math),Id(pow),[BinaryOp(%,Id(s),IntLit(9)),IntLit(3)])),IntLit(5)))]),If(BinaryOp(==,BinaryOp(%,Id(s),IntLit(6)),IntLit(3)),Block([AssignStmt(Id(g),BinaryOp(+,UnaryOp(-,CallExpr(Id(Math),Id(pow),[BinaryOp(%,Id(s),IntLit(30)),IntLit(2)])),BinaryOp(*,IntLit(3),Id(s))))]),If(BinaryOp(==,BinaryOp(%,Id(s),IntLit(6)),IntLit(4)),Block([AssignStmt(Id(g),UnaryOp(-,Id(s)))]),If(BinaryOp(==,BinaryOp(%,Id(s),IntLit(6)),IntLit(5)),Block([AssignStmt(Id(g),UnaryOp(-,CallExpr(Id(TriangleNumber),Id(isTriangleNumber),[BinaryOp(+,BinaryOp(%,Id(s),IntLit(5)),IntLit(5))])))]))))))),AssignStmt(Id(f),BinaryOp(+,BinaryOp(-,IntLit(40),BinaryOp(/,CallExpr(Id(Math),Id(abs),[BinaryOp(-,Id(d),IntLit(500))]),IntLit(20))),Id(g)))]),If(BinaryOp(>,Id(d),IntLit(800)),Block([AssignStmt(Id(f),BinaryOp(/,BinaryOp(*,UnaryOp(-,Id(d)),Id(s)),IntLit(1000)))])))),VarDecl(Id(Bitten),FloatType),If(BinaryOp(&&,BinaryOp(>=,Id(d),IntLit(200)),BinaryOp(<=,Id(d),IntLit(300))),Block([AssignStmt(Id(Bitten),BinaryOp(/,BinaryOp(+,BinaryOp(+,Id(d),Id(P1)),Id(P2)),IntLit(1000))),If(BinaryOp(>,Id(Bitten),FloatLit(0.8)),Block([AssignStmt(Id(pR),IntLit(0))]))]),Block([AssignStmt(Id(pR),BinaryOp(/,BinaryOp(+,Id(P1),BinaryOp(*,Id(P2),Id(f))),BinaryOp(+,IntLit(1000),CallExpr(Id(Math),Id(abs),[BinaryOp(*,Id(P2),Id(f))]))))])),Call(Id(Display),Id(display),[Id(pR)])]))])])"
        self.assertTrue(TestAST.test(input, expect, 346))
    
    def test_347(self):
        input = """
        Class Solution {
            threeSum(nums: Array[Int, 10]) {
                Math.sort(nums.begin(), nums.end());
                Var ans: Array[Int, 10];
                Foreach(i In 0 .. nums.size()) {
                    If ((i != 0) && (nums[i] == nums[(i-1)])) {
                        Continue;
                    }
                    Var sum, start, end: Int = (-1) * nums[i], i + 1, nums.size() - 1;
                    Foreach(j In start .. end) {
                        If (nums[start] + nums[end] == sum) {
                            Var vec: Array[Int, 10];
                            vec.push_back(nums[i]);
                            vec.push_back(nums[start]);
                            vec.push_back(nums[end]);
                            ans.push_back(vec);
                            If (nums[start] == nums[end]) {
                                Break;
                            }
                        }
                        Elseif (nums[start] + nums[end] < sum) {
                            start = start + 1;
                        }
                        Else {
                            end = end - 1;
                        }
                    }
                }
                Return ans;
            }
        }"""
        expect = "Program([ClassDecl(Id(Solution),[MethodDecl(Id(threeSum),Instance,[param(Id(nums),ArrayType(10,IntType))],Block([Call(Id(Math),Id(sort),[CallExpr(Id(nums),Id(begin),[]),CallExpr(Id(nums),Id(end),[])]),VarDecl(Id(ans),ArrayType(10,IntType)),For(Id(i),IntLit(0),CallExpr(Id(nums),Id(size),[]),IntLit(1),Block([If(BinaryOp(&&,BinaryOp(!=,Id(i),IntLit(0)),BinaryOp(==,ArrayCell(Id(nums),[Id(i)]),ArrayCell(Id(nums),[BinaryOp(-,Id(i),IntLit(1))]))),Block([Continue])),VarDecl(Id(sum),IntType,BinaryOp(*,UnaryOp(-,IntLit(1)),ArrayCell(Id(nums),[Id(i)]))),VarDecl(Id(start),IntType,BinaryOp(+,Id(i),IntLit(1))),VarDecl(Id(end),IntType,BinaryOp(-,CallExpr(Id(nums),Id(size),[]),IntLit(1))),For(Id(j),Id(start),Id(end),IntLit(1),Block([If(BinaryOp(==,BinaryOp(+,ArrayCell(Id(nums),[Id(start)]),ArrayCell(Id(nums),[Id(end)])),Id(sum)),Block([VarDecl(Id(vec),ArrayType(10,IntType)),Call(Id(vec),Id(push_back),[ArrayCell(Id(nums),[Id(i)])]),Call(Id(vec),Id(push_back),[ArrayCell(Id(nums),[Id(start)])]),Call(Id(vec),Id(push_back),[ArrayCell(Id(nums),[Id(end)])]),Call(Id(ans),Id(push_back),[Id(vec)]),If(BinaryOp(==,ArrayCell(Id(nums),[Id(start)]),ArrayCell(Id(nums),[Id(end)])),Block([Break]))]),If(BinaryOp(<,BinaryOp(+,ArrayCell(Id(nums),[Id(start)]),ArrayCell(Id(nums),[Id(end)])),Id(sum)),Block([AssignStmt(Id(start),BinaryOp(+,Id(start),IntLit(1)))]),Block([AssignStmt(Id(end),BinaryOp(-,Id(end),IntLit(1)))])))])])])]),Return(Id(ans))]))])])"
        self.assertTrue(TestAST.test(input, expect, 347))
        
    def test_348(self):
        input="""
        Class Function{
            func(a, b: Int){
                Return a + list[b];
            }
            $Sum(list: Array[Int, 5]){
                Var s: Int = 0;
                Foreach(i In 1 .. 5){
                    s = s + Self.func(list[i]);
                }
            }
        }
        Class Program{
            main(){
            }
        }
        """
        expect="""Program([ClassDecl(Id(Function),[MethodDecl(Id(func),Instance,[param(Id(a),IntType),param(Id(b),IntType)],Block([Return(BinaryOp(+,Id(a),ArrayCell(Id(list),[Id(b)])))])),MethodDecl(Id($Sum),Static,[param(Id(list),ArrayType(5,IntType))],Block([VarDecl(Id(s),IntType,IntLit(0)),For(Id(i),IntLit(1),IntLit(5),IntLit(1),Block([AssignStmt(Id(s),BinaryOp(+,Id(s),CallExpr(Self(),Id(func),[ArrayCell(Id(list),[Id(i)])])))])])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,348))
    
    def test_349(self):
        input = """
        Class Program{
            main(){
                _.getVar = 100_000_000_000;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(_),Id(getVar)),IntLit(100000000000))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 349))
    
    def test_350(self):
        input = """
        Class Program{
            main(){
                _.getVar = 100_000_000_000;
                Shape::$new = Array(1.0, 3.4, 1.2);
                Shape::$newArray[1] = "Hello";
                Shape::$noOne.array[2] = .12e10;
                _1_.dh[1] = True;
                Self.we.one = False;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Id(_),Id(getVar)),IntLit(100000000000)),AssignStmt(FieldAccess(Id(Shape),Id($new)),[FloatLit(1.0),FloatLit(3.4),FloatLit(1.2)]),AssignStmt(ArrayCell(FieldAccess(Id(Shape),Id($newArray)),[IntLit(1)]),StringLit(Hello)),AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(Shape),Id($noOne)),Id(array)),[IntLit(2)]),FloatLit(1200000000.0)),AssignStmt(ArrayCell(FieldAccess(Id(_1_),Id(dh)),[IntLit(1)]),BooleanLit(True)),AssignStmt(FieldAccess(FieldAccess(Self(),Id(we)),Id(one)),BooleanLit(False))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_351(self):
        input="""
        Class Program{
            main(){
                If(a < c) {} Else {}
                If(a == b) {} Elseif (b <= c) {a = "HERE!";} Else {}
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(<,Id(a),Id(c)),Block([]),Block([])),If(BinaryOp(==,Id(a),Id(b)),Block([]),If(BinaryOp(<=,Id(b),Id(c)),Block([AssignStmt(Id(a),StringLit(HERE!))]),Block([])))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 351))
    
    def test_352(self):
        input = """
        Class Program{
            Val e: Float = 1.02;
            doo(){
                Shape::$new = Array(1.0, 3.4, 1.2);
                Shape::$newArray[1] = "Hello";
                Shape::$noOne.array[2] = .12e10;
                Self.we.one = False;
                Return 1;
            }
            main(){
                Foreach(lit In d .. e By 2){
                    Foreach(it In 1 .. lit){
                        If(e >= lit){
                            e = e - lit;
                        }
                        Elseif((e < lit) && (e >= i)){
                            e = e + lit - i;
                            Continue;
                        }
                        Elseif(e < i){
                            e = lit * i;
                        }
                        e = e * 1.02;
                        If(e >= 1.e2){
                            Break;
                        }
                    }
                }
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(e),FloatType,FloatLit(1.02))),MethodDecl(Id(doo),Instance,[],Block([AssignStmt(FieldAccess(Id(Shape),Id($new)),[FloatLit(1.0),FloatLit(3.4),FloatLit(1.2)]),AssignStmt(ArrayCell(FieldAccess(Id(Shape),Id($newArray)),[IntLit(1)]),StringLit(Hello)),AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(Shape),Id($noOne)),Id(array)),[IntLit(2)]),FloatLit(1200000000.0)),AssignStmt(FieldAccess(FieldAccess(Self(),Id(we)),Id(one)),BooleanLit(False)),Return(IntLit(1))])),MethodDecl(Id(main),Static,[],Block([For(Id(lit),Id(d),Id(e),IntLit(2),Block([For(Id(it),IntLit(1),Id(lit),IntLit(1),Block([If(BinaryOp(>=,Id(e),Id(lit)),Block([AssignStmt(Id(e),BinaryOp(-,Id(e),Id(lit)))]),If(BinaryOp(&&,BinaryOp(<,Id(e),Id(lit)),BinaryOp(>=,Id(e),Id(i))),Block([AssignStmt(Id(e),BinaryOp(-,BinaryOp(+,Id(e),Id(lit)),Id(i))),Continue]),If(BinaryOp(<,Id(e),Id(i)),Block([AssignStmt(Id(e),BinaryOp(*,Id(lit),Id(i)))])))),AssignStmt(Id(e),BinaryOp(*,Id(e),FloatLit(1.02))),If(BinaryOp(>=,Id(e),FloatLit(100.0)),Block([Break]))])])])]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 352))
    
    def test_353(self):
        input = """
        Class Program{
            main(){
                Var str: String = "Ta jia hao! Wo shi zhenguoyue.";
                If (str < "a"){
                    If (str.len > 10){
                        If (str.contains("jia")){
                            Return "jia";
                        }
                        Else{
                            Return str.strip("!");
                        }
                    }
                    Elseif(str.len == 10){
                        If (str.contains("jia")){
                            Return str +. "Lai zi Yuenan, xin nian kuai le!";
                        }
                    }
                    ## str.len < 10##
                    Else{
                        If(str.len < 3){
                            Foreach (i In 1 .. 100){
                                A::$DoNothing();
                            }
                        }
                        Elseif(str.len != 5){
                            If(str.len % 3 == 0){
                                System.print(a || b);
                            }
                        }
                    }
                }
            }
            Constructor(a, b: Boolean){
                If (!a){
                    Return a && b;
                }
                Else{
                    Return a || b;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(str),StringType,StringLit(Ta jia hao! Wo shi zhenguoyue.)),If(BinaryOp(<,Id(str),StringLit(a)),Block([If(BinaryOp(>,FieldAccess(Id(str),Id(len)),IntLit(10)),Block([If(CallExpr(Id(str),Id(contains),[StringLit(jia)]),Block([Return(StringLit(jia))]),Block([Return(CallExpr(Id(str),Id(strip),[StringLit(!)]))]))]),If(BinaryOp(==,FieldAccess(Id(str),Id(len)),IntLit(10)),Block([If(CallExpr(Id(str),Id(contains),[StringLit(jia)]),Block([Return(BinaryOp(+.,Id(str),StringLit(Lai zi Yuenan, xin nian kuai le!)))]))]),Block([If(BinaryOp(<,FieldAccess(Id(str),Id(len)),IntLit(3)),Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(A),Id($DoNothing),[])])])]),If(BinaryOp(!=,FieldAccess(Id(str),Id(len)),IntLit(5)),Block([If(BinaryOp(==,BinaryOp(%,FieldAccess(Id(str),Id(len)),IntLit(3)),IntLit(0)),Block([Call(Id(System),Id(print),[BinaryOp(||,Id(a),Id(b))])]))])))])))]))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),BoolType),param(Id(b),BoolType)],Block([If(UnaryOp(!,Id(a)),Block([Return(BinaryOp(&&,Id(a),Id(b)))]),Block([Return(BinaryOp(||,Id(a),Id(b)))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 353))
    
    def test_354(self):
        input = """
        Class Util{
            length(s: String){
                Return 9;
            }
            $pb(s: String){
                If(Self.length(s) == 10) {Return "2410183712";}
                Elseif(Self.length(s) > 7){
                    Return Util::$ad(s +. "2");
                }
                Else{
                    Return s +. s;
                }
            }
            $ad(s : String){
                If(Self.length(s) >= 10) {
                    Return Util::$pb(s +. "aas");
                }
                Else{
                    Return s;
                }
            }
        }
        Class Program{
            Var s: String;
            $main(){
                s = "Hello Ther";
                Return Util::$ad(s);
            }
            main(){
                Val f: String = Program::$main();
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Util),[MethodDecl(Id(length),Instance,[param(Id(s),StringType)],Block([Return(IntLit(9))])),MethodDecl(Id($pb),Static,[param(Id(s),StringType)],Block([If(BinaryOp(==,CallExpr(Self(),Id(length),[Id(s)]),IntLit(10)),Block([Return(StringLit(2410183712))]),If(BinaryOp(>,CallExpr(Self(),Id(length),[Id(s)]),IntLit(7)),Block([Return(CallExpr(Id(Util),Id($ad),[BinaryOp(+.,Id(s),StringLit(2))]))]),Block([Return(BinaryOp(+.,Id(s),Id(s)))])))])),MethodDecl(Id($ad),Static,[param(Id(s),StringType)],Block([If(BinaryOp(>=,CallExpr(Self(),Id(length),[Id(s)]),IntLit(10)),Block([Return(CallExpr(Id(Util),Id($pb),[BinaryOp(+.,Id(s),StringLit(aas))]))]),Block([Return(Id(s))]))]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(s),StringType)),MethodDecl(Id($main),Static,[],Block([AssignStmt(Id(s),StringLit(Hello Ther)),Return(CallExpr(Id(Util),Id($ad),[Id(s)]))])),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(f),StringType,CallExpr(Id(Program),Id($main),[])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 354))
    
    def test_355(self):
        input = """
        Class Solution {
            $fib(n: Int) {
                Var d: Array[Int, 100];
                If (n == 0) {
                    Return 0;
                }
                If (n == 1) {
                    Return 1;
                }
                d[n] = Self.fib(n-1) + Self.fib(n-2);
                Return d[n];
            }
        }
        Class Program{
            main(){
                Var input1, input2: Int = It.read(), It.read();
                Output.print(Solution::$fib(input1 * input2));
            }
        }
        """
        expect = """Program([ClassDecl(Id(Solution),[MethodDecl(Id($fib),Static,[param(Id(n),IntType)],Block([VarDecl(Id(d),ArrayType(100,IntType)),If(BinaryOp(==,Id(n),IntLit(0)),Block([Return(IntLit(0))])),If(BinaryOp(==,Id(n),IntLit(1)),Block([Return(IntLit(1))])),AssignStmt(ArrayCell(Id(d),[Id(n)]),BinaryOp(+,CallExpr(Self(),Id(fib),[BinaryOp(-,Id(n),IntLit(1))]),CallExpr(Self(),Id(fib),[BinaryOp(-,Id(n),IntLit(2))]))),Return(ArrayCell(Id(d),[Id(n)]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(input1),IntType,CallExpr(Id(It),Id(read),[])),VarDecl(Id(input2),IntType,CallExpr(Id(It),Id(read),[])),Call(Id(Output),Id(print),[CallExpr(Id(Solution),Id($fib),[BinaryOp(*,Id(input1),Id(input2))])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 355))
    
    def test_356(self):
        input = """
        Class Solution {
            fib(n: Int) {
                If (n == 0) {
                    Return 0;
                }
                If (n == 1) {
                    Return 1;
                }
                Return Self.fib(n-1) + Self.fib(n-2);
            }
        }
        """
        expect = "Program([ClassDecl(Id(Solution),[MethodDecl(Id(fib),Instance,[param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(0)),Block([Return(IntLit(0))])),If(BinaryOp(==,Id(n),IntLit(1)),Block([Return(IntLit(1))])),Return(BinaryOp(+,CallExpr(Self(),Id(fib),[BinaryOp(-,Id(n),IntLit(1))]),CallExpr(Self(),Id(fib),[BinaryOp(-,Id(n),IntLit(2))])))]))])])"
        self.assertTrue(TestAST.test(input, expect, 356))
    
    def test_357(self):
        input = """
        Class Program{
            Var a, b: String = "abc" +. "xyz", "abc" ==. "xyz";
            Var a, b, c, d, e, f: Boolean = 1 == 1, 1 != 1, a > b, a >= b, a < 1, a <= 1;
            Var a, b: Boolean = a && True, b || False;
            main(){
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),StringType,BinaryOp(+.,StringLit(abc),StringLit(xyz)))),AttributeDecl(Instance,VarDecl(Id(b),StringType,BinaryOp(==.,StringLit(abc),StringLit(xyz)))),AttributeDecl(Instance,VarDecl(Id(a),BoolType,BinaryOp(==,IntLit(1),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(b),BoolType,BinaryOp(!=,IntLit(1),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(c),BoolType,BinaryOp(>,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(d),BoolType,BinaryOp(>=,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(e),BoolType,BinaryOp(<,Id(a),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(f),BoolType,BinaryOp(<=,Id(a),IntLit(1)))),AttributeDecl(Instance,VarDecl(Id(a),BoolType,BinaryOp(&&,Id(a),BooleanLit(True)))),AttributeDecl(Instance,VarDecl(Id(b),BoolType,BinaryOp(||,Id(b),BooleanLit(False)))),MethodDecl(Id(main),Static,[],Block([Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 357))
    
    def test_358(self):
        input = """
        Class Program{
            Val a, b, c: Int = a * 1, b / 1, c % 1;
            Val a1, b2: Boolean = !True, !a1;
            Var $a, $b: Int = -1, -a;
            main(){
                Var s: Int = d[1][2][3][4][a][1+2];
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(*,Id(a),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(/,Id(b),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(%,Id(c),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(a1),BoolType,UnaryOp(!,BooleanLit(True)))),AttributeDecl(Instance,ConstDecl(Id(b2),BoolType,UnaryOp(!,Id(a1)))),AttributeDecl(Static,VarDecl(Id($a),IntType,UnaryOp(-,IntLit(1)))),AttributeDecl(Static,VarDecl(Id($b),IntType,UnaryOp(-,Id(a)))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(s),IntType,ArrayCell(Id(d),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),Id(a),BinaryOp(+,IntLit(1),IntLit(2))])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 358))
    
    def test_359(self):
        input = """
        Class Program{
            Var a_1, a_2, a_3, a_4, a_5, a_6: Int = 0, 00, 0x0, 0X0, 0b0, 0B0;
            Var b_1, b_2, b_3: Int = 123456, 1_2_3_4_5_6, 123_456;
            main(){
                Var a: Int;
                a = class_var.attr.attr.attribute;
                a = class_var.attr.attr.method(a,b,c);
                a = class_name::$od(abc).method(a,b,c);
                a = New X(a).a();
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a_1),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a_2),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a_3),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a_4),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a_5),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(a_6),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b_1),IntType,IntLit(123456))),AttributeDecl(Instance,VarDecl(Id(b_2),IntType,IntLit(123456))),AttributeDecl(Instance,VarDecl(Id(b_3),IntType,IntLit(123456))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType),AssignStmt(Id(a),FieldAccess(FieldAccess(FieldAccess(Id(class_var),Id(attr)),Id(attr)),Id(attribute))),AssignStmt(Id(a),CallExpr(FieldAccess(FieldAccess(Id(class_var),Id(attr)),Id(attr)),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(CallExpr(Id(class_name),Id($od),[Id(abc)]),Id(method),[Id(a),Id(b),Id(c)])),AssignStmt(Id(a),CallExpr(NewExpr(Id(X),[Id(a)]),Id(a),[]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 359))
    
    def test_360(self):
        input = """
        Class Program{
            main(){
                Var var: Int;
                var = a * b + c || d / e % f + - d;
                var = a || b || c && d && e;  
                var = !!!a;
                var = ---a;
                var = array[1][2][3][4];
                var = a.a.a.a.a;
                var = a.a().a.a().a();
                var = New Isl(New Parm(New ssi (1)));
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var),IntType),AssignStmt(Id(var),BinaryOp(||,BinaryOp(+,BinaryOp(*,Id(a),Id(b)),Id(c)),BinaryOp(+,BinaryOp(%,BinaryOp(/,Id(d),Id(e)),Id(f)),UnaryOp(-,Id(d))))),AssignStmt(Id(var),BinaryOp(&&,BinaryOp(&&,BinaryOp(||,BinaryOp(||,Id(a),Id(b)),Id(c)),Id(d)),Id(e))),AssignStmt(Id(var),UnaryOp(!,UnaryOp(!,UnaryOp(!,Id(a))))),AssignStmt(Id(var),UnaryOp(-,UnaryOp(-,UnaryOp(-,Id(a))))),AssignStmt(Id(var),ArrayCell(Id(array),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),AssignStmt(Id(var),FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(a)),Id(a)),Id(a)),Id(a))),AssignStmt(Id(var),CallExpr(CallExpr(FieldAccess(CallExpr(Id(a),Id(a),[]),Id(a)),Id(a),[]),Id(a),[])),AssignStmt(Id(var),NewExpr(Id(Isl),[NewExpr(Id(Parm),[NewExpr(Id(ssi),[IntLit(1)])])]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 360))
    
    def test_361(self):
        input = """
        Class Object{
            Var key: Int;
            Constructor(key: Int){
                Self.key = key;
            }
        }
        Class Program {
            Var a: Object = New Object();
            Var b: Object = New Object(New Object(1,2,3));
            main() {
                If (a.key == b.key) {
                    Self.print("Hurray");
                } Elseif (a.key > b.key) {
                    Self.print("Greater");
                } Elseif (a.key < b.key) {
                    Self.print("Less");
                } Else {
                    Self.print("Oh no");
                }
            }    
        }
        """
        expect = """Program([ClassDecl(Id(Object),[AttributeDecl(Instance,VarDecl(Id(key),IntType)),MethodDecl(Id(Constructor),Instance,[param(Id(key),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(key)),Id(key))]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Object)),NewExpr(Id(Object),[]))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(Object)),NewExpr(Id(Object),[NewExpr(Id(Object),[IntLit(1),IntLit(2),IntLit(3)])]))),MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,FieldAccess(Id(a),Id(key)),FieldAccess(Id(b),Id(key))),Block([Call(Self(),Id(print),[StringLit(Hurray)])]),If(BinaryOp(>,FieldAccess(Id(a),Id(key)),FieldAccess(Id(b),Id(key))),Block([Call(Self(),Id(print),[StringLit(Greater)])]),If(BinaryOp(<,FieldAccess(Id(a),Id(key)),FieldAccess(Id(b),Id(key))),Block([Call(Self(),Id(print),[StringLit(Less)])]),Block([Call(Self(),Id(print),[StringLit(Oh no)])]))))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 361))
    
    def test_362(self):
        input = """
        Class Program {
            main(a: Int) {
                If (a >= 0) {
                    If (b == 1) {}
                    Elseif ((b <= 10) && (b >= 0)) {}
                    Else {}
                }
                Elseif (a >= 10) {
                    If (b == 11) {}
                    Elseif ((b <= 100) && (b >= 10)) {}
                    Else {}
                }
                Elseif (a >= 100) {
                    If (b == 111) {}
                    Elseif ((b <= 1000) && (b >= 100)) {}
                    Else {}
                }
                Else {
                    If (b == 100) {}
                    Elseif (b == 102) {}
                    Elseif (b == 3) {}
                    Else {}
                }
            }
            main(){
                Var a: Int = Self.main(1);
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(>=,Id(a),IntLit(0)),Block([If(BinaryOp(==,Id(b),IntLit(1)),Block([]),If(BinaryOp(&&,BinaryOp(<=,Id(b),IntLit(10)),BinaryOp(>=,Id(b),IntLit(0))),Block([]),Block([])))]),If(BinaryOp(>=,Id(a),IntLit(10)),Block([If(BinaryOp(==,Id(b),IntLit(11)),Block([]),If(BinaryOp(&&,BinaryOp(<=,Id(b),IntLit(100)),BinaryOp(>=,Id(b),IntLit(10))),Block([]),Block([])))]),If(BinaryOp(>=,Id(a),IntLit(100)),Block([If(BinaryOp(==,Id(b),IntLit(111)),Block([]),If(BinaryOp(&&,BinaryOp(<=,Id(b),IntLit(1000)),BinaryOp(>=,Id(b),IntLit(100))),Block([]),Block([])))]),Block([If(BinaryOp(==,Id(b),IntLit(100)),Block([]),If(BinaryOp(==,Id(b),IntLit(102)),Block([]),If(BinaryOp(==,Id(b),IntLit(3)),Block([]),Block([]))))]))))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,CallExpr(Self(),Id(main),[IntLit(1)])),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 362))
    
    def test_363(self):
        input = """
        Class Program{
            Var a: Array[Int, 5];
            Var a: Array[Int, 0xFFFF];
            Var a: Array[Int, 0XFFFF];
            Var a: Array[Int, 0b1111];
            Var a: Array[Int, 0B1111];
            Var a: Array[Int, 01234];
            main(){
                Var a: Float = 9999999999999999123999.999999999999;
                Var a: Float = 1.1111111111111111;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(65535,IntType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(65535,IntType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(15,IntType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(15,IntType))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(668,IntType))),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),FloatType,FloatLit(1e+22)),VarDecl(Id(a),FloatType,FloatLit(1.1111111111111112))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 363))
    
    def test_364(self):
        input = """
        Class X{
            Var a: AB = New AB();
            $b(){}
            a(){}
        }
        Class Program{
            Var var: Int;
            main(){
                New X().a();
                New X().a.b();
                X::$b();
                X::$b.c();
                X::$b.c.d();
                var = Self.a.a.a[1];
                var = a.b(1,2,3)[1][2][3];
            }
        }
        """
        expect = """Program([ClassDecl(Id(X),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(AB)),NewExpr(Id(AB),[]))),MethodDecl(Id($b),Static,[],Block([])),MethodDecl(Id(a),Instance,[],Block([]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(var),IntType)),MethodDecl(Id(main),Static,[],Block([Call(NewExpr(Id(X),[]),Id(a),[]),Call(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b),[]),Call(Id(X),Id($b),[]),Call(FieldAccess(Id(X),Id($b)),Id(c),[]),Call(FieldAccess(FieldAccess(Id(X),Id($b)),Id(c)),Id(d),[]),AssignStmt(Id(var),ArrayCell(FieldAccess(FieldAccess(FieldAccess(Self(),Id(a)),Id(a)),Id(a)),[IntLit(1)])),AssignStmt(Id(var),ArrayCell(CallExpr(Id(a),Id(b),[IntLit(1),IntLit(2),IntLit(3)]),[IntLit(1),IntLit(2),IntLit(3)]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 364))
    
    def test_365(self):
        input = """
        Class Other_class {    
            Var $a, $b: Int = 1, 2;
            $Method(n: Int) {
                If (n == 1) {
                    Return True;
                }
                Else {
                    Return False;
                }
            }    
            Constructor(int: Int; string: String) {
                Some_class::$Method(1,2,3);
                Self.Method(1,2,3);
                a = Some_class::$Method(1,2,3);
                a = Self.Method(1,2,3);
            }
            Destructor() {}
        }
        Class Program{
            main(){
                a = Array(
                    Array(1,2,3),
                    Array(0x11,0x22),
                    Array(Array(1,2,3), Array(1,2,3,4), Array(1,2,3,4,5)),
                    Array(a[1], New X(), New X()[1], a==b, "String" ==. "String"),
                    Array(a[1],a[2],a[3],a[4]),
                    Array(New X().x, New X().y)
                );
            }
        }
        """
        expect = """Program([ClassDecl(Id(Other_class),[AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(1))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(2))),MethodDecl(Id($Method),Static,[param(Id(n),IntType)],Block([If(BinaryOp(==,Id(n),IntLit(1)),Block([Return(BooleanLit(True))]),Block([Return(BooleanLit(False))]))])),MethodDecl(Id(Constructor),Instance,[param(Id(int),IntType),param(Id(string),StringType)],Block([Call(Id(Some_class),Id($Method),[IntLit(1),IntLit(2),IntLit(3)]),Call(Self(),Id(Method),[IntLit(1),IntLit(2),IntLit(3)]),AssignStmt(Id(a),CallExpr(Id(Some_class),Id($Method),[IntLit(1),IntLit(2),IntLit(3)])),AssignStmt(Id(a),CallExpr(Self(),Id(Method),[IntLit(1),IntLit(2),IntLit(3)]))])),MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(17),IntLit(34)],[[IntLit(1),IntLit(2),IntLit(3)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)]],[ArrayCell(Id(a),[IntLit(1)]),NewExpr(Id(X),[]),ArrayCell(NewExpr(Id(X),[]),[IntLit(1)]),BinaryOp(==,Id(a),Id(b)),BinaryOp(==.,StringLit(String),StringLit(String))],[ArrayCell(Id(a),[IntLit(1)]),ArrayCell(Id(a),[IntLit(2)]),ArrayCell(Id(a),[IntLit(3)]),ArrayCell(Id(a),[IntLit(4)])],[FieldAccess(NewExpr(Id(X),[]),Id(x)),FieldAccess(NewExpr(Id(X),[]),Id(y))]])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 365))
    
    def test_366(self):
        input = """
        Class Object {
            Var x: Int = Self.a();
            main() {
                x = Self.a();
                x = a.a();
                Self.a();
                a.a();
            }
        }
        Class Program{
            main() {
                Var x: Int = Object::$main();
                Var x: Int = Object.main();
                Object::$main();
                object.main();
                object.main(object.main());
            }
        }
        """
        expect = """Program([ClassDecl(Id(Object),[AttributeDecl(Instance,VarDecl(Id(x),IntType,CallExpr(Self(),Id(a),[]))),MethodDecl(Id(main),Instance,[],Block([AssignStmt(Id(x),CallExpr(Self(),Id(a),[])),AssignStmt(Id(x),CallExpr(Id(a),Id(a),[])),Call(Self(),Id(a),[]),Call(Id(a),Id(a),[])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType,CallExpr(Id(Object),Id($main),[])),VarDecl(Id(x),IntType,CallExpr(Id(Object),Id(main),[])),Call(Id(Object),Id($main),[]),Call(Id(object),Id(main),[]),Call(Id(object),Id(main),[CallExpr(Id(object),Id(main),[])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 366))
    
    def test_367(self):
        input = """
        Class So : A {
            Var a : Array[Array[Int, 5], 5];
            main(i, j, k : Int) {
                Return a[i][j] * a[j][k] + a[i][k] * a[k][j];
            }
            b(w, h : Int; b, c : Float) {
                Self.gg();
                Continue;
                Self.callFunc(1, a, b, a != b);
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(So),Id(A),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,ArrayType(5,IntType)))),MethodDecl(Id(main),Instance,[param(Id(i),IntType),param(Id(j),IntType),param(Id(k),IntType)],Block([Return(BinaryOp(+,BinaryOp(*,ArrayCell(Id(a),[Id(i),Id(j)]),ArrayCell(Id(a),[Id(j),Id(k)])),BinaryOp(*,ArrayCell(Id(a),[Id(i),Id(k)]),ArrayCell(Id(a),[Id(k),Id(j)]))))])),MethodDecl(Id(b),Instance,[param(Id(w),IntType),param(Id(h),IntType),param(Id(b),FloatType),param(Id(c),FloatType)],Block([Call(Self(),Id(gg),[]),Continue,Call(Self(),Id(callFunc),[IntLit(1),Id(a),Id(b),BinaryOp(!=,Id(a),Id(b))])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 367))
    
    def test_368(self):
        input = """
        Class Util{
            Val a : ClassAC = Null;
            a() {
                Obj.doMany();
                Return a[1][2][3];
            }
            aaa() {
                Self.print(a);
                Foreach(i In 1 .. 100 By 7){
                    Self.doSth();
                    Continue;
                }
                Return Self.Something();
            }
            $a() {
                ClassABC::$foo = 123;
                ClassABC::$eng[1][2] = 1841 + 138;
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Util),[AttributeDecl(Instance,ConstDecl(Id(a),ClassType(Id(ClassAC)),NullLiteral())),MethodDecl(Id(a),Instance,[],Block([Call(Id(Obj),Id(doMany),[]),Return(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]))])),MethodDecl(Id(aaa),Instance,[],Block([Call(Self(),Id(print),[Id(a)]),For(Id(i),IntLit(1),IntLit(100),IntLit(7),Block([Call(Self(),Id(doSth),[]),Continue])]),Return(CallExpr(Self(),Id(Something),[]))])),MethodDecl(Id($a),Static,[],Block([AssignStmt(FieldAccess(Id(ClassABC),Id($foo)),IntLit(123)),AssignStmt(ArrayCell(FieldAccess(Id(ClassABC),Id($eng)),[IntLit(1),IntLit(2)]),BinaryOp(+,IntLit(1841),IntLit(138)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 368))
    
    def test_369(self):
        input = """
        Class Program {
            Var array_1, array_2, array_3: Array[Array[Int,6], 6] = Array(
                Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x))
            ),
            Array(
                Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x))
            ),
            Array(
                Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x)),
                Array(1+2+3, 4*5*6, 100/2/10, 100 % 2, !-100, Self.f(x))
            );  
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(array_1),ArrayType(6,ArrayType(6,IntType)),[[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])]])),AttributeDecl(Instance,VarDecl(Id(array_2),ArrayType(6,ArrayType(6,IntType)),[[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])]])),AttributeDecl(Instance,VarDecl(Id(array_3),ArrayType(6,ArrayType(6,IntType)),[[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])],[BinaryOp(+,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(*,BinaryOp(*,IntLit(4),IntLit(5)),IntLit(6)),BinaryOp(/,BinaryOp(/,IntLit(100),IntLit(2)),IntLit(10)),BinaryOp(%,IntLit(100),IntLit(2)),UnaryOp(!,UnaryOp(-,IntLit(100))),CallExpr(Self(),Id(f),[Id(x)])]]))])])"""
        self.assertTrue(TestAST.test(input, expect, 369))
    
    def test_370(self):
        input = """
        Class Program {
            hello(){
                Foreach (i In 1 .. 100 By -1) {}
                Foreach (i In 100 .. 1) {}
                Foreach (i In 100 .. 1 By 1) {}
                Return 1;
            }
            main() {
                Val a : Int;
                Foreach (i In 1 .. 100 By 1)
                {
                    Object.printf("enter the number:");
                    Object.scanf("%d", a);
                    If ( a == 0 ) {
                        Self.hello();
                        Break;
                    }
                }
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(hello),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),UnaryOp(-,IntLit(1)),Block([])]),For(Id(i),IntLit(100),IntLit(1),IntLit(1),Block([])]),For(Id(i),IntLit(100),IntLit(1),IntLit(1),Block([])]),Return(IntLit(1))])),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),IntType,None),For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Call(Id(Object),Id(printf),[StringLit(enter the number:)]),Call(Id(Object),Id(scanf),[StringLit(%d),Id(a)]),If(BinaryOp(==,Id(a),IntLit(0)),Block([Call(Self(),Id(hello),[]),Break]))])]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 370))
    
    def test_371(self):
        input = """
        Class Program{
            main(){
                Foreach (i In 1 .. 100) {
                    Foreach (j In 1 .. i By i * i) {
                        Foreach (i In 1 .. 100) {
                            Return i * i + a.b;
                        }
                    }
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([For(Id(j),IntLit(1),Id(i),BinaryOp(*,Id(i),Id(i)),Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([Return(BinaryOp(+,BinaryOp(*,Id(i),Id(i)),FieldAccess(Id(a),Id(b))))])])])])])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 371))
    
    def test_372(self):
        input = """
        Class Program{
            $a() {
                ClassABC::$foo = 123;
                ClassABC::$eng[1][2] = 1841 + 138;
            }
            b() {
                Self.a.b = 10;
                Program::$gn = 210490;
                a[1][(i - j)][3] = c[i][k] + b[1][j+1][k - 2][3];
                Return 105189;
            }
            main(){
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id($a),Static,[],Block([AssignStmt(FieldAccess(Id(ClassABC),Id($foo)),IntLit(123)),AssignStmt(ArrayCell(FieldAccess(Id(ClassABC),Id($eng)),[IntLit(1),IntLit(2)]),BinaryOp(+,IntLit(1841),IntLit(138)))])),MethodDecl(Id(b),Instance,[],Block([AssignStmt(FieldAccess(FieldAccess(Self(),Id(a)),Id(b)),IntLit(10)),AssignStmt(FieldAccess(Id(Program),Id($gn)),IntLit(210490)),AssignStmt(ArrayCell(Id(a),[IntLit(1),BinaryOp(-,Id(i),Id(j)),IntLit(3)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(k)]),ArrayCell(Id(b),[IntLit(1),BinaryOp(+,Id(j),IntLit(1)),BinaryOp(-,Id(k),IntLit(2)),IntLit(3)]))),Return(IntLit(105189))])),MethodDecl(Id(main),Static,[],Block([Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 372))
    
    def test_373(self):
        input = """
         Class Ofc {
            Constructor() {}
            Constructor(x: Int) {}
            method(a,b,c: Int; x,y,z: String) {}
            Destructor() {}
            main(x: Int) {}
            main(a,b,c: Int; x,y,z: String) {}
        }
        Class Program{
            main(){
                Var a: Array[Array[Array[Int, 1], 1], 1];
                a[1] = Array(Array(1));
                a[1][1] = Array(2);
                a[1][1][1] = 3;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Ofc),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType)],Block([])),MethodDecl(Id(method),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(x),StringType),param(Id(y),StringType),param(Id(z),StringType)],Block([])),MethodDecl(Id(Destructor),Instance,[],Block([])),MethodDecl(Id(main),Instance,[param(Id(x),IntType)],Block([])),MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(x),StringType),param(Id(y),StringType),param(Id(z),StringType)],Block([]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(1,ArrayType(1,ArrayType(1,IntType)))),AssignStmt(ArrayCell(Id(a),[IntLit(1)]),[[IntLit(1)]]),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1)]),[IntLit(2)]),AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(1),IntLit(1)]),IntLit(3))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 373))
    
    def test_374(self):
        input = """
        Class Number {
            Var data: String = "1234"; 
        }
        Class Integ : Number{
            Var data: Number;
            Constructor(x: Int) {
                Self.data = x;
            }
        }
        Class Program {
            Var x: Integ = New Integ(1);
            main() {
                Self.x = 1;
                Self.x();
                Self.x(1,2,3);
                Self.x = Null;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Number),[AttributeDecl(Instance,VarDecl(Id(data),StringType,StringLit(1234)))]),ClassDecl(Id(Integ),Id(Number),[AttributeDecl(Instance,VarDecl(Id(data),ClassType(Id(Number)),NullLiteral())),MethodDecl(Id(Constructor),Instance,[param(Id(x),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(data)),Id(x))]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(x),ClassType(Id(Integ)),NewExpr(Id(Integ),[IntLit(1)]))),MethodDecl(Id(main),Static,[],Block([AssignStmt(FieldAccess(Self(),Id(x)),IntLit(1)),Call(Self(),Id(x),[]),Call(Self(),Id(x),[IntLit(1),IntLit(2),IntLit(3)]),AssignStmt(FieldAccess(Self(),Id(x)),NullLiteral())]))])])"""
        self.assertTrue(TestAST.test(input, expect, 374))
    
    def test_375(self):
        input = """
        Class Program{
            method() {
                Foreach (i In 1 .. 100) {}
                Foreach (i In 2 * a + b .. a + b * c / d By Self.a) {
                    If(i > 2){
                        Break;
                    }
                }
                Foreach (i In Self.a .. Self.b() By a::$b) {}
            }
            main(){
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(method),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(1),Block([])]),For(Id(i),BinaryOp(+,BinaryOp(*,IntLit(2),Id(a)),Id(b)),BinaryOp(+,Id(a),BinaryOp(/,BinaryOp(*,Id(b),Id(c)),Id(d))),FieldAccess(Self(),Id(a)),Block([If(BinaryOp(>,Id(i),IntLit(2)),Block([Break]))])]),For(Id(i),FieldAccess(Self(),Id(a)),CallExpr(Self(),Id(b),[]),FieldAccess(Id(a),Id($b)),Block([])])])),MethodDecl(Id(main),Static,[],Block([Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 375))
    
    def test_376(self):
        input = """
        Class Program{
            Var a, b: Array[Int, 100] = Array(), Array(1,2,3,4);
            Var c: Array[String, 100] = Array("mr", "mr", "bean");
            Var array_1: Array[Array[Array[Array[Int,1],1],1],1];
            Var array_2: Array[Array[Array[Int, 5], 1], 1] = Array (
                Array (Array (1, 2, 3, 4, 5), Array (0x11, 0x21, 0x31, 0x41, 0x51)),
                Array (Array (1, 2, 3, 4, 5), Array (0x11, 0x21, 0x31, 0x41, 0x51))
            );
            main(){
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(100,IntType),[])),AttributeDecl(Instance,VarDecl(Id(b),ArrayType(100,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(100,StringType),[StringLit(mr),StringLit(mr),StringLit(bean)])),AttributeDecl(Instance,VarDecl(Id(array_1),ArrayType(1,ArrayType(1,ArrayType(1,ArrayType(1,IntType)))))),AttributeDecl(Instance,VarDecl(Id(array_2),ArrayType(1,ArrayType(1,ArrayType(5,IntType))),[[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)],[IntLit(17),IntLit(33),IntLit(49),IntLit(65),IntLit(81)]],[[IntLit(1),IntLit(2),IntLit(3),IntLit(4),IntLit(5)],[IntLit(17),IntLit(33),IntLit(49),IntLit(65),IntLit(81)]]])),MethodDecl(Id(main),Static,[],Block([Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 376))
    
    def test_377(self):
        input = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;

            $getNumOfShape() {
                Return Shape::$numOfShape;
            }
        }
        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }
        Class Program {
            main() {
                Out.printInt(Shape::$numOfShape);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(FieldAccess(Id(Shape),Id($numOfShape)))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = """
        Class Program{
            Var a: Obj;
            Var $a: Obj;
            Val b: Obj;
            Val $b: Obj;
            Var a1: Obj = New Obj();
            Var $a1: Obj = New Obj();
            Var b1: Obj = New Obj();
            Var $b1: Obj = New Obj();
            Constructor(){
                Var c: Obj;
                Val d: Obj;
                Var e: Obj = New Obj();
                Val f: Obj = New Obj();
                Return f.cloneObject(c);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),ClassType(Id(Obj)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($a),ClassType(Id(Obj)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(b),ClassType(Id(Obj)),None)),AttributeDecl(Static,ConstDecl(Id($b),ClassType(Id(Obj)),None)),AttributeDecl(Instance,VarDecl(Id(a1),ClassType(Id(Obj)),NewExpr(Id(Obj),[]))),AttributeDecl(Static,VarDecl(Id($a1),ClassType(Id(Obj)),NewExpr(Id(Obj),[]))),AttributeDecl(Instance,VarDecl(Id(b1),ClassType(Id(Obj)),NewExpr(Id(Obj),[]))),AttributeDecl(Static,VarDecl(Id($b1),ClassType(Id(Obj)),NewExpr(Id(Obj),[]))),MethodDecl(Id(Constructor),Instance,[],Block([VarDecl(Id(c),ClassType(Id(Obj)),NullLiteral()),ConstDecl(Id(d),ClassType(Id(Obj)),None),VarDecl(Id(e),ClassType(Id(Obj)),NewExpr(Id(Obj),[])),ConstDecl(Id(f),ClassType(Id(Obj)),NewExpr(Id(Obj),[])),Return(CallExpr(Id(f),Id(cloneObject),[Id(c)]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 378))
    
    def test_379(self):
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
        self.assertTrue(TestAST.test(input, expect, 379))
    
    def test_380(self):
        input = """
        Class Program{
            Var $a: IntObj;
            main(){
                Var b: IntObj = New IntObj();
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Static,VarDecl(Id($a),ClassType(Id(IntObj)),NullLiteral())),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(b),ClassType(Id(IntObj)),NewExpr(Id(IntObj),[]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 380))
    
    def test_381(self):
        input = """
        Class NFT {
            Var fyou: String = "If you dumb enough to buy this";
            Var utrash : String = "You dumb enough to survive on sunlight";
            Constructor(){
                fyou = Self.fyou;
                utrash = Self.utrash;
            }
        }
        Class Program {
            main() {
                Val b : Int = a::$a;
                a::$func();
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(NFT),[AttributeDecl(Instance,VarDecl(Id(fyou),StringType,StringLit(If you dumb enough to buy this))),AttributeDecl(Instance,VarDecl(Id(utrash),StringType,StringLit(You dumb enough to survive on sunlight))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(fyou),FieldAccess(Self(),Id(fyou))),AssignStmt(Id(utrash),FieldAccess(Self(),Id(utrash)))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(b),IntType,FieldAccess(Id(a),Id($a))),Call(Id(a),Id($func),[]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 381))
    
    def test_382(self):
        input = """
        Class Program {
            Val b: Float = .e-3;
            main() {
                Foreach(a In 1 .. 0x1234ABCD){
                    If ((3*i + 5)%4 == 2){
                        b = b + a / 5;
                        Continue;
                    }
                    Else{
                        b = a + 2;
                        Break;
                    }
                }
                Foreach(a In -5 .. 0b1101 By 04){
                    If ((2*i + 5)%3 >= 2){
                        b = b + 5;
                        Continue;
                    }
                    Else{
                        b = a + 2;
                        Break;
                    }
                }
                Return b;
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(b),FloatType,FloatLit(0.0))),MethodDecl(Id(main),Static,[],Block([For(Id(a),IntLit(1),IntLit(305441741),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,BinaryOp(+,BinaryOp(*,IntLit(3),Id(i)),IntLit(5)),IntLit(4)),IntLit(2)),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),BinaryOp(/,Id(a),IntLit(5)))),Continue]),Block([AssignStmt(Id(b),BinaryOp(+,Id(a),IntLit(2))),Break]))])]),For(Id(a),UnaryOp(-,IntLit(5)),IntLit(13),IntLit(4),Block([If(BinaryOp(>=,BinaryOp(%,BinaryOp(+,BinaryOp(*,IntLit(2),Id(i)),IntLit(5)),IntLit(3)),IntLit(2)),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(5))),Continue]),Block([AssignStmt(Id(b),BinaryOp(+,Id(a),IntLit(2))),Break]))])]),Return(Id(b))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 382))
    
    def test_383(self):
        input = """
        Class Program{
            Val a, b, $c, $d, e, $f: Int = 037415, 2345651, 0x329EDF, 0xABCDEF01, 0b101111100101, 0B1101101010111101;
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(16141))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(2345651))),AttributeDecl(Static,ConstDecl(Id($c),IntType,IntLit(3317471))),AttributeDecl(Static,ConstDecl(Id($d),IntType,IntLit(2882400001))),AttributeDecl(Instance,ConstDecl(Id(e),IntType,IntLit(3045))),AttributeDecl(Static,ConstDecl(Id($f),IntType,IntLit(55997)))])])"""
        self.assertTrue(TestAST.test(input, expect, 383))    
    
    def test_384(self):
        input = """
        Class Program{
            notMain(f: Boolean){
                Val a, b: Array[Int, 4] = Array(1, 0B101011, 03132, 0x123), Array(-4, 31, 0xEFFE, 5);
                If(!f){
                    Return a[0] + a[b[1]] + b[a[1]];
                }
                Else{
                    Return a[0] + b[a[1]];
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType)],Block([ConstDecl(Id(a),ArrayType(4,IntType),[IntLit(1),IntLit(43),IntLit(1626),IntLit(291)]),ConstDecl(Id(b),ArrayType(4,IntType),[UnaryOp(-,IntLit(4)),IntLit(31),IntLit(61438),IntLit(5)]),If(UnaryOp(!,Id(f)),Block([Return(BinaryOp(+,BinaryOp(+,ArrayCell(Id(a),[IntLit(0)]),ArrayCell(Id(a),[ArrayCell(Id(b),[IntLit(1)])])),ArrayCell(Id(b),[ArrayCell(Id(a),[IntLit(1)])])))]),Block([Return(BinaryOp(+,ArrayCell(Id(a),[IntLit(0)]),ArrayCell(Id(b),[ArrayCell(Id(a),[IntLit(1)])])))]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 384))
    
    def test_385(self):
        input = """
        Class Program{
            main(inp: Int){
                Var a: Float;
                a = 3.5031041095815;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(inp),IntType)],Block([VarDecl(Id(a),FloatType),AssignStmt(Id(a),FloatLit(3.5031041095815))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 385))
    
    def test_386(self):
        input = """
        Class Program{
            main(){
                {} {} {} {}       
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Block([]),Block([]),Block([]),Block([])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 386))
    
    def test_387(self):
        input = """
        Class Program{
            main(){
                Var a: Array[Array[Boolean, 2], 2];
                a[1][0b10 * 0x123 % 2] = True;
                a[1][3 * 2 * 1 / 6] = False;
                a[0x270F / 9999 + 1][0 * 0B1011110101] = True;
                a[9999 / 0x270F * 2][1 * 9 / 9] = Sys.sampleArray(a[0x1]);
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(2,ArrayType(2,BoolType))),AssignStmt(ArrayCell(Id(a),[IntLit(1),BinaryOp(%,BinaryOp(*,IntLit(2),IntLit(291)),IntLit(2))]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[IntLit(1),BinaryOp(/,BinaryOp(*,BinaryOp(*,IntLit(3),IntLit(2)),IntLit(1)),IntLit(6))]),BooleanLit(False)),AssignStmt(ArrayCell(Id(a),[BinaryOp(+,BinaryOp(/,IntLit(9999),IntLit(9999)),IntLit(1)),BinaryOp(*,IntLit(0),IntLit(757))]),BooleanLit(True)),AssignStmt(ArrayCell(Id(a),[BinaryOp(*,BinaryOp(/,IntLit(9999),IntLit(9999)),IntLit(2)),BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(9)),IntLit(9))]),CallExpr(Id(Sys),Id(sampleArray),[ArrayCell(Id(a),[IntLit(1)])]))]))])])"""
        self.assertTrue(TestAST.test(input, expect, 387))
    
    def test_388(self):
        input = """
        Class AC{
            A(){
                Return 1 + 2 % 3 - 4 * 5 - a[7];
            }
        }
        Class Program {
            Var var_1, var_2 : AC;
            main(){
                Var var_3, var_4 : AC;
                var_3.A();
            }
        }
        """
        expect = """Program([ClassDecl(Id(AC),[MethodDecl(Id(A),Instance,[],Block([Return(BinaryOp(-,BinaryOp(-,BinaryOp(+,IntLit(1),BinaryOp(%,IntLit(2),IntLit(3))),BinaryOp(*,IntLit(4),IntLit(5))),ArrayCell(Id(a),[IntLit(7)])))]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(var_1),ClassType(Id(AC)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(var_2),ClassType(Id(AC)),NullLiteral())),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var_3),ClassType(Id(AC)),NullLiteral()),VarDecl(Id(var_4),ClassType(Id(AC)),NullLiteral()),Call(Id(var_3),Id(A),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,388))
    
    def test_389(self):
        input = """
        Class Program {
            Var var_1, var_2 : AC;
            Val val_1, val_2 : ABC;
            main(){
                Var var_3, var_4 : AC;
                Val val_3, val_4 : ABC;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(var_1),ClassType(Id(AC)),NullLiteral())),AttributeDecl(Instance,VarDecl(Id(var_2),ClassType(Id(AC)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(val_1),ClassType(Id(ABC)),None)),AttributeDecl(Instance,ConstDecl(Id(val_2),ClassType(Id(ABC)),None)),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(var_3),ClassType(Id(AC)),NullLiteral()),VarDecl(Id(var_4),ClassType(Id(AC)),NullLiteral()),ConstDecl(Id(val_3),ClassType(Id(ABC)),None),ConstDecl(Id(val_4),ClassType(Id(ABC)),None)]))])])"""
        self.assertTrue(TestAST.test(input,expect,389))
    
    def test_390(self):
        input = r"""
            Class Program {
                Var a_1: String = "abcdef";
                Var a_2: String = "abc\n\t\b\f\r'""; 
            }
        """
        expect = r"""Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a_1),StringType,StringLit(abcdef))),AttributeDecl(Instance,VarDecl(Id(a_2),StringType,StringLit(abc\n\t\b\f\r'")))])])"""
        self.assertTrue(TestAST.test(input, expect, 390))
    
    def test_391(self):
        input = """Class A {
            Val a : Array[Int, 3] = Array(1, 100, 11);
            Val b : Array[String, 4] = Array("This is a string", "Another string", "A", "B\\n");
            Var c : Array[Boolean, 3] = Array(True, False, True);
            Var d : Array[Float, 5] = Array(.e5, 1123E123, .5e5, 0.2, 50.1123E-5);
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(3,IntType),[IntLit(1),IntLit(100),IntLit(11)])),AttributeDecl(Instance,ConstDecl(Id(b),ArrayType(4,StringType),[StringLit(This is a string),StringLit(Another string),StringLit(A),StringLit(B\\n)])),AttributeDecl(Instance,VarDecl(Id(c),ArrayType(3,BoolType),[BooleanLit(True),BooleanLit(False),BooleanLit(True)])),AttributeDecl(Instance,VarDecl(Id(d),ArrayType(5,FloatType),[FloatLit(0.0),FloatLit(1.123e+126),FloatLit(50000.0),FloatLit(0.2),FloatLit(0.000501123)]))])])"""
        self.assertTrue(TestAST.test(input, expect, 391))
    
    def test_392(self):
        input = """
        Class A : B {
            Val a, b : Boolean = True, False;
        }"""
        expect = "Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(b),BoolType,BooleanLit(False)))])])"
        self.assertTrue(TestAST.test(input, expect, 392))
    
    def test_393(self):
        input = """
        Class Something : Object {
            Var $a, b, c : Float = 10.0, 11., 1e15;
            Val a, c, d : Float = .e5, 0.000, 0.2;
            Var c, d, e : Float = 1e-12, 1E+4, 11.1123e10;
            Val $a, $y, $x : Float = 50.1123E-5, .5e5, .4e+5;
            Var x, y : Float = .1123e-10, 1123E123;
        }
        """
        expect = "Program([ClassDecl(Id(Something),Id(Object),[AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(10.0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(11.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(1000000000000000.0))),AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,FloatLit(0.0))),AttributeDecl(Instance,ConstDecl(Id(d),FloatType,FloatLit(0.2))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(1e-12))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(10000.0))),AttributeDecl(Instance,VarDecl(Id(e),FloatType,FloatLit(111123000000.0))),AttributeDecl(Static,ConstDecl(Id($a),FloatType,FloatLit(0.000501123))),AttributeDecl(Static,ConstDecl(Id($y),FloatType,FloatLit(50000.0))),AttributeDecl(Static,ConstDecl(Id($x),FloatType,FloatLit(40000.0))),AttributeDecl(Instance,VarDecl(Id(x),FloatType,FloatLit(1.123e-11))),AttributeDecl(Instance,VarDecl(Id(y),FloatType,FloatLit(1.123e+126)))])])"
        self.assertTrue(TestAST.test(input, expect, 393))
    
    def test_394(self):
        input = """
        Class Rectangle {
            Var b, c, $d, $e, _f: Float = 10, -20.1, 30.2, 40.3, 50.4 - 1;
        }"""
        expect = "Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(b),FloatType,IntLit(10))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,UnaryOp(-,FloatLit(20.1)))),AttributeDecl(Static,VarDecl(Id($d),FloatType,FloatLit(30.2))),AttributeDecl(Static,VarDecl(Id($e),FloatType,FloatLit(40.3))),AttributeDecl(Instance,VarDecl(Id(_f),FloatType,BinaryOp(-,FloatLit(50.4),IntLit(1))))])])"
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = """
        Class B{
            main(){
                Var x, y, z, t: Array[Int, 5];
            }
        }
        Class Program {
            Var d: B = New B();
            main(t: Array[Int, 5]){
                Return t[0];
            }
            main(){
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(B),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(x),ArrayType(5,IntType)),VarDecl(Id(y),ArrayType(5,IntType)),VarDecl(Id(z),ArrayType(5,IntType)),VarDecl(Id(t),ArrayType(5,IntType))]))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(d),ClassType(Id(B)),NewExpr(Id(B),[]))),MethodDecl(Id(main),Instance,[param(Id(t),ArrayType(5,IntType))],Block([Return(ArrayCell(Id(t),[IntLit(0)]))])),MethodDecl(Id(main),Static,[],Block([Return()]))])])"""
        self.assertTrue(TestAST.test(input,expect,395))

    def test_396(self):
        input = """
        Class A{
            Var a: Boolean = (a && b) || (300 > 35 % 4 + 3);
        }
        Class Program{
            main(){
                Out.print("Help me", "Please");
            }
        }
        """
        expect = """Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),BoolType,BinaryOp(||,BinaryOp(&&,Id(a),Id(b)),BinaryOp(>,IntLit(300),BinaryOp(+,BinaryOp(%,IntLit(35),IntLit(4)),IntLit(3))))))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(print),[StringLit(Help me),StringLit(Please)])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
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
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
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
                Var sdf : Array[Array[Float, 3], 4];
                Self.notMain(True, sdf);
                Return;
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(52))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(5))),MethodDecl(Id(notMain),Instance,[param(Id(f),BoolType),param(Id(arr),ArrayType(4,ArrayType(3,FloatType)))],Block([VarDecl(Id(s),IntType,IntLit(3)),For(Id(i),IntLit(1),IntLit(2),IntLit(1),Block([AssignStmt(Id(s),BinaryOp(+,Id(s),Id(i))),Call(Id(Out),Id(print),[StringLit(2346),Id(i)]),Continue,Break])]),Call(Self(),Id(notMain),[]),Return(Id(s))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(sdf),ArrayType(4,ArrayType(3,FloatType))),Call(Self(),Id(notMain),[BooleanLit(True),Id(sdf)]),Return()]))])])"""
        self.assertTrue(TestAST.test(input, expect, 398))
    
    def test_399(self):
        input = """
        Class Program {
            Var var_1: Int;
            m0(){
                var_1 = New X(New D()).a().a().a().a().a();
            }
            m1(){
                var_1 = class_name::$attr;
            }
            m2(){
                var_1 = var.just(1,b,c).go(a,2,c).pls(a,b,3);
            }
            m3(){
                var_1 = var.attr.justgo(a,b,c);
            }
            m4(){
                var_1 = var.attr.just(a,b,c).go(a,b,c);
            }
            m5(){
                var_1 = var.justgo(a,b,c).attr;
            }
            m6(){
                var_1 = var.attr.attr.just(New X(1).x).go();
            }
            m7(){
                var_1 = var.just(a,b,c).go(a,b,New D(a, b)).attr;
            }
            m8(){
                var_1 = class_name::$just(abc).go(a,b,1.2).pls(a,b,c);
            }
            m9(){
                var_1 = class_name::$just(abc).go(a,b,1.2).pls(a,b,c).attr.attr;
            }
            main() {
                Self.m0();
                Self.m1();
                Self.m2();
                Self.m3();
                Self.m4();
                Self.m5();
                Self.m6();
                Self.m7();
                Self.m8();
                Self.m9();
            }
        }
        """
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(var_1),IntType)),MethodDecl(Id(m0),Instance,[],Block([AssignStmt(Id(var_1),CallExpr(CallExpr(CallExpr(CallExpr(CallExpr(NewExpr(Id(X),[NewExpr(Id(D),[])]),Id(a),[]),Id(a),[]),Id(a),[]),Id(a),[]),Id(a),[]))])),MethodDecl(Id(m1),Instance,[],Block([AssignStmt(Id(var_1),FieldAccess(Id(class_name),Id($attr)))])),MethodDecl(Id(m2),Instance,[],Block([AssignStmt(Id(var_1),CallExpr(CallExpr(CallExpr(Id(var),Id(just),[IntLit(1),Id(b),Id(c)]),Id(go),[Id(a),IntLit(2),Id(c)]),Id(pls),[Id(a),Id(b),IntLit(3)]))])),MethodDecl(Id(m3),Instance,[],Block([AssignStmt(Id(var_1),CallExpr(FieldAccess(Id(var),Id(attr)),Id(justgo),[Id(a),Id(b),Id(c)]))])),MethodDecl(Id(m4),Instance,[],Block([AssignStmt(Id(var_1),CallExpr(CallExpr(FieldAccess(Id(var),Id(attr)),Id(just),[Id(a),Id(b),Id(c)]),Id(go),[Id(a),Id(b),Id(c)]))])),MethodDecl(Id(m5),Instance,[],Block([AssignStmt(Id(var_1),FieldAccess(CallExpr(Id(var),Id(justgo),[Id(a),Id(b),Id(c)]),Id(attr)))])),MethodDecl(Id(m6),Instance,[],Block([AssignStmt(Id(var_1),CallExpr(CallExpr(FieldAccess(FieldAccess(Id(var),Id(attr)),Id(attr)),Id(just),[FieldAccess(NewExpr(Id(X),[IntLit(1)]),Id(x))]),Id(go),[]))])),MethodDecl(Id(m7),Instance,[],Block([AssignStmt(Id(var_1),FieldAccess(CallExpr(CallExpr(Id(var),Id(just),[Id(a),Id(b),Id(c)]),Id(go),[Id(a),Id(b),NewExpr(Id(D),[Id(a),Id(b)])]),Id(attr)))])),MethodDecl(Id(m8),Instance,[],Block([AssignStmt(Id(var_1),CallExpr(CallExpr(CallExpr(Id(class_name),Id($just),[Id(abc)]),Id(go),[Id(a),Id(b),FloatLit(1.2)]),Id(pls),[Id(a),Id(b),Id(c)]))])),MethodDecl(Id(m9),Instance,[],Block([AssignStmt(Id(var_1),FieldAccess(FieldAccess(CallExpr(CallExpr(CallExpr(Id(class_name),Id($just),[Id(abc)]),Id(go),[Id(a),Id(b),FloatLit(1.2)]),Id(pls),[Id(a),Id(b),Id(c)]),Id(attr)),Id(attr)))])),MethodDecl(Id(main),Static,[],Block([Call(Self(),Id(m0),[]),Call(Self(),Id(m1),[]),Call(Self(),Id(m2),[]),Call(Self(),Id(m3),[]),Call(Self(),Id(m4),[]),Call(Self(),Id(m5),[]),Call(Self(),Id(m6),[]),Call(Self(),Id(m7),[]),Call(Self(),Id(m8),[]),Call(Self(),Id(m9),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect, 399))

    def test_400(self):
        input =  """
        Class myClass : parentClass {
            Var a, b, c: Boolean;
            Var a, $e : String = "Hello", "Hola";
            Var w, $q : Array[String, 3] = Array (1, 5, 7), Array (1, 5, "s");
            Val f, G : Float;
            Val $h, _Jk : Int = a.b(), a[1][2] + a::$ac;
            Val o: Object = New Object();
            Val x : Name;
            Var y : Something;
            Var $a : Array[Array[Array[Int,2],3],4] = 1;
            method1(){
                ## Vardecls ##
                Var a, b, c: Boolean;
                Var a, e : String = "Hello", "Hola";
                Var w, q : Array[String, 3] = Array (1, 5, 7), Array (1, 5, "s");
                ## ConstDecls ##
                Val f, G : Float;
                Val h, _Jk : Int = a.b(), a[1][2] + a::$ac;
                Val o: Object = New Object();
                Val x : Name;
                Var y : Something;
                ## Assignments ##

            }
            
            statement(a, b, c: Boolean; j: Classtype){
                thisIs_anId = Array (1, 5, 7) + 1.2 * 0x12AB / (- 01100) +. Null;
                Somevar = b.X()[2][True];
                staticId::$a.Id = !(a <= b) % 2 + a.b(); 
                donD_j.func().Id = !True + (False - 2 % 8) + b.asb(!True + (False - 2 % 8), 1).a;
                Self.a.h = Id::$a.B(Array (1, 5, 7) + 1.2, !(a <= b) % 2 + a.b());
                (A[1][2])[True] = New x() + 2 * New Y();
                (a[1][True]["Hola"])[2][1+2]["Hey"]["What"] = Array (Array (1, 5, 7), Array (1, 5, 7), Array (1, 5, 7));
                Return;
                Return !True + (False - 2 % 8) + b.asb(!True + (False - 2 % 8), 1).a;
                New X().a.b();
                b.asb(!True + (False - 2 % 8));
                asa::$jas();
            }
            
            $if_statement(){
                If (True && False) {New X().a.b();}
                If (Self.a[1][2]) { ## Do something ## } Else {
                    Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                    }
                    If (123 >= 45) {asa::$jas();} Elseif (45 == 455) {
                        Val x : Name;
                        Var y : Something;
                    }
                }
                If (123 >= 45) {asa::$jas();} Elseif (45 == 455) {}
                If ("hi" >= 45) {asa::$jas();} Elseif (False) {} Else {Break;}
            }
            main(){
                Foreach (i In 1 .. 100 By 2) {
                    Out.printInt(i);
                }
                Foreach (i In 1 .. 100 By !True + (False - 2 % 8)) {
                    If (123 >= 45) {asa::$jas();} Elseif (45 == 455) {}
                    If ("hi" >= 45) {asa::$jas();} Elseif (False) {} Else {}
                    Foreach (x In 5 .. 2) { Break; }
                    Continue;
                }
            }
            Constructor(){
                Var a, e : String = "Hello", "Hola";
                Var w, q : Array[String, 3] = Array (1, 5, 7), Array (1, 5, "s");
                If (123 >= 45) {asa::$jas();} Elseif (45 == 455) {} Elseif (45 == 455) {} Elseif (45 == 455) {} Elseif (45 == 455) {} Else {}
            }
            Constructor(f, G : Float; a, b, c: Boolean){
                Return;
            }
            Destructor(){
                If (123 >= 45) { Return; }
            }
        }
        
        Class otherClass {
            Val $h, _Jk : Int = a.b(), a[1][2] + a::$ac;
            Val o: Object = New Object();
            main(){
                If ("ah") {
                    Foreach (i In 1 .. 100 By 2) {
                        Var r, s: Int;
                        r = 2.0;
                        Var a, b: Array[Int, 5];
                        s = r * r * Self;
                        a[0] = s;
                        a = "## adfa ##";
                    }
                }
                Var Student : Student = New Student();
            }
        }
        
        Class Program {
            main(){
                If ("ah") {
                    Var r, s: Int;
                    r = 2.0;
                    Var a, b: Array[Int, 5];
                    s = r * r * Self;
                    a[0] = s;
                    a = "## adfa ##";
                }
                Var Student : Student = New Student();
            }
            
            main(a, b, c: Boolean; e: Int){
                Var Student : Student = New Student();
                Foreach (i In 1 .. 100 By 2) {
                    Continue;
                }
            }
        }
        """
        expect = """Program([ClassDecl(Id(myClass),Id(parentClass),[AttributeDecl(Instance,VarDecl(Id(a),BoolType)),AttributeDecl(Instance,VarDecl(Id(b),BoolType)),AttributeDecl(Instance,VarDecl(Id(c),BoolType)),AttributeDecl(Instance,VarDecl(Id(a),StringType,StringLit(Hello))),AttributeDecl(Static,VarDecl(Id($e),StringType,StringLit(Hola))),AttributeDecl(Instance,VarDecl(Id(w),ArrayType(3,StringType),[IntLit(1),IntLit(5),IntLit(7)])),AttributeDecl(Static,VarDecl(Id($q),ArrayType(3,StringType),[IntLit(1),IntLit(5),StringLit(s)])),AttributeDecl(Instance,ConstDecl(Id(f),FloatType,None)),AttributeDecl(Instance,ConstDecl(Id(G),FloatType,None)),AttributeDecl(Static,ConstDecl(Id($h),IntType,CallExpr(Id(a),Id(b),[]))),AttributeDecl(Instance,ConstDecl(Id(_Jk),IntType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2)]),FieldAccess(Id(a),Id($ac))))),AttributeDecl(Instance,ConstDecl(Id(o),ClassType(Id(Object)),NewExpr(Id(Object),[]))),AttributeDecl(Instance,ConstDecl(Id(x),ClassType(Id(Name)),None)),AttributeDecl(Instance,VarDecl(Id(y),ClassType(Id(Something)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($a),ArrayType(4,ArrayType(3,ArrayType(2,IntType))),IntLit(1))),MethodDecl(Id(method1),Instance,[],Block([VarDecl(Id(a),BoolType),VarDecl(Id(b),BoolType),VarDecl(Id(c),BoolType),VarDecl(Id(a),StringType,StringLit(Hello)),VarDecl(Id(e),StringType,StringLit(Hola)),VarDecl(Id(w),ArrayType(3,StringType),[IntLit(1),IntLit(5),IntLit(7)]),VarDecl(Id(q),ArrayType(3,StringType),[IntLit(1),IntLit(5),StringLit(s)]),ConstDecl(Id(f),FloatType,None),ConstDecl(Id(G),FloatType,None),ConstDecl(Id(h),IntType,CallExpr(Id(a),Id(b),[])),ConstDecl(Id(_Jk),IntType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2)]),FieldAccess(Id(a),Id($ac)))),ConstDecl(Id(o),ClassType(Id(Object)),NewExpr(Id(Object),[])),ConstDecl(Id(x),ClassType(Id(Name)),None),VarDecl(Id(y),ClassType(Id(Something)),NullLiteral())])),MethodDecl(Id(statement),Instance,[param(Id(a),BoolType),param(Id(b),BoolType),param(Id(c),BoolType),param(Id(j),ClassType(Id(Classtype)))],Block([AssignStmt(Id(thisIs_anId),BinaryOp(+.,BinaryOp(+,[IntLit(1),IntLit(5),IntLit(7)],BinaryOp(/,BinaryOp(*,FloatLit(1.2),IntLit(4779)),UnaryOp(-,IntLit(576)))),NullLiteral())),AssignStmt(Id(Somevar),ArrayCell(CallExpr(Id(b),Id(X),[]),[IntLit(2),BooleanLit(True)])),AssignStmt(FieldAccess(FieldAccess(Id(staticId),Id($a)),Id(Id)),BinaryOp(+,BinaryOp(%,UnaryOp(!,BinaryOp(<=,Id(a),Id(b))),IntLit(2)),CallExpr(Id(a),Id(b),[]))),AssignStmt(FieldAccess(CallExpr(Id(donD_j),Id(func),[]),Id(Id)),BinaryOp(+,BinaryOp(+,UnaryOp(!,BooleanLit(True)),BinaryOp(-,BooleanLit(False),BinaryOp(%,IntLit(2),IntLit(8)))),FieldAccess(CallExpr(Id(b),Id(asb),[BinaryOp(+,UnaryOp(!,BooleanLit(True)),BinaryOp(-,BooleanLit(False),BinaryOp(%,IntLit(2),IntLit(8)))),IntLit(1)]),Id(a)))),AssignStmt(FieldAccess(FieldAccess(Self(),Id(a)),Id(h)),CallExpr(FieldAccess(Id(Id),Id($a)),Id(B),[BinaryOp(+,[IntLit(1),IntLit(5),IntLit(7)],FloatLit(1.2)),BinaryOp(+,BinaryOp(%,UnaryOp(!,BinaryOp(<=,Id(a),Id(b))),IntLit(2)),CallExpr(Id(a),Id(b),[]))])),AssignStmt(ArrayCell(ArrayCell(Id(A),[IntLit(1),IntLit(2)]),[BooleanLit(True)]),BinaryOp(+,NewExpr(Id(x),[]),BinaryOp(*,IntLit(2),NewExpr(Id(Y),[])))),AssignStmt(ArrayCell(ArrayCell(Id(a),[IntLit(1),BooleanLit(True),StringLit(Hola)]),[IntLit(2),BinaryOp(+,IntLit(1),IntLit(2)),StringLit(Hey),StringLit(What)]),[[IntLit(1),IntLit(5),IntLit(7)],[IntLit(1),IntLit(5),IntLit(7)],[IntLit(1),IntLit(5),IntLit(7)]]),Return(),Return(BinaryOp(+,BinaryOp(+,UnaryOp(!,BooleanLit(True)),BinaryOp(-,BooleanLit(False),BinaryOp(%,IntLit(2),IntLit(8)))),FieldAccess(CallExpr(Id(b),Id(asb),[BinaryOp(+,UnaryOp(!,BooleanLit(True)),BinaryOp(-,BooleanLit(False),BinaryOp(%,IntLit(2),IntLit(8)))),IntLit(1)]),Id(a)))),Call(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b),[]),Call(Id(b),Id(asb),[BinaryOp(+,UnaryOp(!,BooleanLit(True)),BinaryOp(-,BooleanLit(False),BinaryOp(%,IntLit(2),IntLit(8))))]),Call(Id(asa),Id($jas),[])])),MethodDecl(Id($if_statement),Static,[],Block([If(BinaryOp(&&,BooleanLit(True),BooleanLit(False)),Block([Call(FieldAccess(NewExpr(Id(X),[]),Id(a)),Id(b),[])])),If(ArrayCell(FieldAccess(Self(),Id(a)),[IntLit(1),IntLit(2)]),Block([]),Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])]),If(BinaryOp(>=,IntLit(123),IntLit(45)),Block([Call(Id(asa),Id($jas),[])]),If(BinaryOp(==,IntLit(45),IntLit(455)),Block([ConstDecl(Id(x),ClassType(Id(Name)),None),VarDecl(Id(y),ClassType(Id(Something)),NullLiteral())])))])),If(BinaryOp(>=,IntLit(123),IntLit(45)),Block([Call(Id(asa),Id($jas),[])]),If(BinaryOp(==,IntLit(45),IntLit(455)),Block([]))),If(BinaryOp(>=,StringLit(hi),IntLit(45)),Block([Call(Id(asa),Id($jas),[])]),If(BooleanLit(False),Block([]),Block([Break])))])),MethodDecl(Id(main),Instance,[],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])]),For(Id(i),IntLit(1),IntLit(100),BinaryOp(+,UnaryOp(!,BooleanLit(True)),BinaryOp(-,BooleanLit(False),BinaryOp(%,IntLit(2),IntLit(8)))),Block([If(BinaryOp(>=,IntLit(123),IntLit(45)),Block([Call(Id(asa),Id($jas),[])]),If(BinaryOp(==,IntLit(45),IntLit(455)),Block([]))),If(BinaryOp(>=,StringLit(hi),IntLit(45)),Block([Call(Id(asa),Id($jas),[])]),If(BooleanLit(False),Block([]),Block([]))),For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Break])]),Continue])])])),MethodDecl(Id(Constructor),Instance,[],Block([VarDecl(Id(a),StringType,StringLit(Hello)),VarDecl(Id(e),StringType,StringLit(Hola)),VarDecl(Id(w),ArrayType(3,StringType),[IntLit(1),IntLit(5),IntLit(7)]),VarDecl(Id(q),ArrayType(3,StringType),[IntLit(1),IntLit(5),StringLit(s)]),If(BinaryOp(>=,IntLit(123),IntLit(45)),Block([Call(Id(asa),Id($jas),[])]),If(BinaryOp(==,IntLit(45),IntLit(455)),Block([]),If(BinaryOp(==,IntLit(45),IntLit(455)),Block([]),If(BinaryOp(==,IntLit(45),IntLit(455)),Block([]),If(BinaryOp(==,IntLit(45),IntLit(455)),Block([]),Block([]))))))])),MethodDecl(Id(Constructor),Instance,[param(Id(f),FloatType),param(Id(G),FloatType),param(Id(a),BoolType),param(Id(b),BoolType),param(Id(c),BoolType)],Block([Return()])),MethodDecl(Id(Destructor),Instance,[],Block([If(BinaryOp(>=,IntLit(123),IntLit(45)),Block([Return()]))]))]),ClassDecl(Id(otherClass),[AttributeDecl(Static,ConstDecl(Id($h),IntType,CallExpr(Id(a),Id(b),[]))),AttributeDecl(Instance,ConstDecl(Id(_Jk),IntType,BinaryOp(+,ArrayCell(Id(a),[IntLit(1),IntLit(2)]),FieldAccess(Id(a),Id($ac))))),AttributeDecl(Instance,ConstDecl(Id(o),ClassType(Id(Object)),NewExpr(Id(Object),[]))),MethodDecl(Id(main),Instance,[],Block([If(StringLit(ah),Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),Self())),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s)),AssignStmt(Id(a),StringLit(## adfa ##))])])])),VarDecl(Id(Student),ClassType(Id(Student)),NewExpr(Id(Student),[]))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(StringLit(ah),Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),Self())),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s)),AssignStmt(Id(a),StringLit(## adfa ##))])),VarDecl(Id(Student),ClassType(Id(Student)),NewExpr(Id(Student),[]))])),MethodDecl(Id(main),Instance,[param(Id(a),BoolType),param(Id(b),BoolType),param(Id(c),BoolType),param(Id(e),IntType)],Block([VarDecl(Id(Student),ClassType(Id(Student)),NewExpr(Id(Student),[])),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Continue])])]))])])"""
        self.assertTrue(TestAST.test(input, expect, 400))

    
