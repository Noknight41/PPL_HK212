import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_401(self):
        input = """
        Class Program{
            main(s: String){
                Return 1;
            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,401))
        
    def test_402(self):
        input = """
        Class A{
            Var a, d: Int;
            Constructor(){
                Return;
            }
        }
        Class Program{
            main(){
                
            }
        }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,402))
    
    def test_403(self):
        input = """
        Class A{
            Var a, d: Int; 
            sickle(s: String){
                Return 1;
            }  
        }
        Class Program{
            main(){
                
            }
        }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,403))
        
    def test_404(self):
        input = """
        Class A{
            Var a, d: Int;
            sickle(s: String){
                Return 1;
            }
        }
        Class B : A{
            Var a: Float;
        }
        Class Program{
            main(){
                
            }
        }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test_405(self):
        input = """
        Class A{
            Var a, d: Int;
            sickle(s: String){
                Break;
                Return 1;
            }
        }
        Class Program{
            main(){
                
            }
        }
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,405))
    
    def test_406(self):
        input = """
        Class A{
            Val a, d: Int = 1, 2;
        }
        Class Program{
            main(){
                
            }
        }
            """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,406))
    
    def test_407(self):
        input = """
        Class A{
            Val a, d: Int = 1, 7.5;
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(d),IntType,FloatLit(7.5))"
        self.assertTrue(TestChecker.test(input,expect,407))
    
    def test_408(self):
        input = """
        Class A{
            Var a, d: Int;
            sickle(s: String; e: Int){
                Foreach(i In 1 .. 10 By 2){
                   Break; 
                }
                Return;
            }
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,408))
    
    def test_409(self):
        input = """
        Class A{
            Var a, d: Int;
            Var test_array: Array[Float, 3] = Array(1, 2, 3);
        }
        Class B : A {
            Var b: Int;
        }
        Class Program{
            Var test: A = New B();
            main(){
                
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_410(self):
        input = """
        Class A{
            Var a, d: Int;
            sickle(s: String; e: Int){
                Foreach(i In 1 .. 10 By 2){
                   Break; 
                }
                Continue;
                Return;
            }
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input,expect,410))
    
    def test_411(self):
        input = """
        Class A{
            Var a: Array[Int, 2] = Array(1, 2, 3);
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),ArrayType(2,IntType),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input,expect,411))
    
    def test_412(self):
        input = """
        Class A{
            Var a: Array[Int, 2] = Array(1, 2.0);
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "Illegal Array Literal: [IntLit(1),FloatLit(2.0)]"
        self.assertTrue(TestChecker.test(input,expect,412))
    
    def test_413(self):
        input = """
        Class A{
            sicle(){
                Return;
            }
            s(a: String){
                Return;
            }
            d(sa: Int; swq: Float){
                Return;
            }
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,413))
    
    def test_414(self):
        input = """
        Class A{
            Var a: Int;
            Constructor(start: Int){
                Return;
            }
            Val b: Int = 1;
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,414))
    
    def test_415(self):
        input = """
        Class A{
            Var a: Int = 1 + 2;
            Constructor(start: Int){
                Return;
            }
            s(a: String){
                Var s: Int = 1 * 2;
                Var e: Float = s / 2.0;
                If((True == True) || (True != False)){
                    Return 1;
                }
                Return s;
            }
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,415))
    
    def test_416(self):
        input = """
        Class A{
            Val $a: Int = 1 + 2;
            Constructor(start: Int){
                Return;
            }
            s(a: String){
                Val as: Array[Float, 3] = Array(1, 2, 3);
                as[2] = 1;
                Return;
            }
        }
        Class B{
            
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(as),[IntLit(2)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,416))
    
    def test_417(self):
        input = """
        Class Starter{
            Constructor(){
                Return;
            }
        }
        Class A{
            Val $d: Array[Int, 5] = Array(1 + 2, 3, 0x23, 56, 0b111);
            Cosntructor(a: Int; b: Float; s: Array[Int, 3]){
                Return;
            }
            sicle(){
                Var a: Int = A::$d[1] + A::$d[2];
                Foreach(scalar In 1 .. 5 By 1){
                   Var d: Int = scalar;
                   a = a + d + A::$d[scalar];
                }
                Return a;   
            }
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,417))
    
    def test_418(self):
        input = """
        Class A{
            Var a: Int = 1;
            Var $a: String = "12";
            a(a: Int){
                Return;
            }
            a(){
                Return 1;
            }
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "Redeclared Method: a"
        self.assertTrue(TestChecker.test(input,expect,418))
    
    def test_419(self):
        input = """
        Class A{
            Var a: Int = 1;
            Var a: String = "12";
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,419))
    
    def test_420(self):
        input = """
        Class A{
            Var d: String = "Hello Im Sting";
        }
        Class A{
            Var a: Int = 1;
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "Redeclared Class: A"
        self.assertTrue(TestChecker.test(input,expect,420))
    
    def test_421(self):
        input = """
        Class A{
            Var a: Int = 1;
            Var d: Int = Self.s;
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "Undeclared Attribute: s"
        self.assertTrue(TestChecker.test(input,expect,421))
    
    def test_422(self):
        input = """
        Class E {
            Var d : Int;
        }
        
        Class Program{
            main() {
                Var E: E = New E();
                Var b : Int = E.a;
            }
        }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,422))
    
    def test_423(self):
        input = """
        Class E {
            Var a : Int;
        }
        
        Class Program{
            main() {
                Var b : Int = E.a;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(E),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,423))
    
    def test_424(self):
        input = """
        Class A{
            Var a: Int = 1;
        }
        Class E : A {
            Var a : Int;
            ##Var a : String;##
        }
        Class Program{
            main() {
                Return;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,424))
    
    def test_425(self):
        input = """
        Class Starter{
            Var s, a: Float = 1.0, 0x3;
            Constructor(Nigel: Int){
                Self.a = Nigel + 1.0;
                Self.s = Nigel;
                Return;
            }
        }
        Class A{
            Var a: Int = 1;
            Var test: Starter = New Starter(2);
        }
        Class Program{
            main() {
                Return;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_426(self):
        input = """
        Class Starter{
            Var s, a: Float = 1.0, 0x3;
            Constructor(Nigel: Int){
                Self.a = Nigel + 1.0;
                Self.s = Nigel;
                Return;
            }
            Ss(a1: Int){
                Return;
            }
        }
        Class A{
            Var a: Int = 1;
            Var test: Starter = New Starter(2);
            sum(){
                Self.test.Ss(1);
                Return;
            }
        }
        Class Program{
            main() {
                Return;
            }
        }
        """
        expect = "[]"
        self.assertTrue(TestChecker.test(input,expect,426))
    
    def test_427(self):
        input = """
        Class Program{
            main() {
                
            }
            Var myVar: String = "Hello World";
            Var myVar: Int;
        }
        """
        expect = "Redeclared Attribute: myVar"
        self.assertTrue(TestChecker.test(input,expect,427))
    
    def test_428(self):
        input = """
        Class A{
            Var myVar: String = "Hello World";
            dummy(a: Int){
                Return a + 4;
            }
            dummy2(){
                Return;
            }
            d(a: Int){
                Self.dummy2();
                Var s: Int = Self.dummy(2 + 2);
                Var d: Int = Self.dummy(s);
            }
            s(){
                Self.d(2);
            }
        }
        Class Program{
            main() {
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,428))
    
    def test_498(self):
        """Simple program: int main() {} """
        input = """
            Class Program{
                main(){
                    
                }
                Var myVar: String = "Hello World";
                Var myVar: Int;
            }
        """
        expect = "Redeclared Attribute: myVar"
        self.assertTrue(TestChecker.test(input,expect,498))