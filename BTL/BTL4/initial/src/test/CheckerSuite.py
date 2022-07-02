import unittest
from TestUtils import TestChecker
from AST import *
from main.d96.checker.StaticError import *

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
                Return 1;
            }
        }
            """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
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
                Return 2;
            }
        }
            """
        expect = "Type Mismatch In Statement: Return(IntLit(2))"
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
                Return 2;
            }
        }
            """
        expect = "Type Mismatch In Statement: Return(IntLit(2))"
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
                Return;
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
                Return 2;
            }
        }
            """
        expect = "Type Mismatch In Statement: Return(IntLit(2))"
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
                Var i: Int;
                Foreach(i In 1 .. 10 By 2){
                   Break; 
                }
                Return;
                Return 1;
            }
        }
        Class Program{
            main(){
                
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
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
            Var test: A = New A();
            main(){
                Return 2;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(2))"
        self.assertTrue(TestChecker.test(input,expect,409))
    
    def test_410(self):
        input = """
        Class A{
            Var a, d: Int;
            sickle(s: String; e: Int){
                Var i : Int;
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
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
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
            yo(a: String){
                Return a;
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
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
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
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
                Var scalar: Int;
                Foreach(scalar In 1 .. 5 By 1){
                   Var d: Int = scalar;
                   a = a + d + A::$d[scalar];
                }
                Return a;   
            }
        }
        Class Program{
            main(){
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
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
            do(){
                Return "s";
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
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
            do(){
                Return "s";
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
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
                Return 2;
            }
            
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(2))"
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
    
    def test_429(self):
        input = """
            Class A{
                a(){
                    Var a: Int;
                    Val b: Int = Null.a;
                }
            }
            Class Program{
                main(){
                    
                }
            }
        """
        expect = "Type Mismatch In Expression: FieldAccess(NullLiteral(),Id(a))"
        self.assertTrue(TestChecker.test(input,expect,429))
    
    def test_430(self):
        input = """
            Class A{
                a(){
                    Var a: Int;
                    Val b: Int = a;
                }
            }
            Class Program{
                main(){
                    
                }
            }
        """
        expect = "Illegal Constant Expression: Id(a)"
        self.assertTrue(TestChecker.test(input,expect,430))
        
    def test_431(self):
        input = """
            Class Program{
                main(a: Int){
                    
                }
            }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,431))
        
    def test_432(self):
        input = """
            Class Program{
                main(){
                    Return 1;
                }
            }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,432))
    
    def test_433(self):
        input = """
        Class A{
            Var a, d: Int;
            sickle(s: String; e: Int){
                Var i : String;
                Foreach(i In 1 .. 10 By 2){
                   Break; 
                   Continue;
                }
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),IntLit(10),IntLit(2),Block([Break,Continue])])"
        self.assertTrue(TestChecker.test(input,expect,433))
    
    def test_434(self):
        input = """
            Class Program{
                main(){
                    
                }
                Var myVar: String = "Hello World";
                Var myVar: Int;
            }
        """
        expect = "Redeclared Attribute: myVar"
        self.assertTrue(TestChecker.test(input,expect,434))
    
    def test_435(self):
        input = """
        Class A{
            Var a, d: Int;
            sickle(s: String; e: Int){
                Foreach(i In Self.a .. 10 By Self.d){
                   Break; 
                   Continue;
                }
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,435))
    
    def test_436(self):
        input = Program([
            ClassDecl(
                        Id('Shape'),
                        [
                            AttributeDecl(Instance(), VarDecl(
                                Id('x'), FloatType(), FloatLiteral(0.001))),
                            AttributeDecl(Static(), VarDecl(
                                Id('$y'), StringType(), StringLiteral('PPL')))
                        ],
                        ),
            ClassDecl(
                Id('Program'),
                [
                    AttributeDecl(Instance(), VarDecl(Id('x'), IntType())),
                    AttributeDecl(Instance(), VarDecl(
                        Id('y'), StringType(), FieldAccess(Id('x'), Id('$x')))),
                    MethodDecl(Static(), Id('main'), [], Block([]))
                ],
            )
        ])
        expect = 'Undeclared Class: x'
        self.assertTrue(TestChecker.test(input, expect, 436))
        
    def test_437(self):
        input = """
        Class A {
            Var a: Array[Int, 1] = Array(1, 2, 3, 4);
            Var b: Array[Int, 1] = Array(True);

            Var d,e: Int;
            Val f: Array[Array[Int,1], 2] = Array( Array(d), Array(e) );
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(a),ArrayType(1,IntType),[IntLit(1),IntLit(2),IntLit(3),IntLit(4)])"
        self.assertTrue(TestChecker.test(input,expect,437))
    
    def test_438(self):
        input = """
        Class A {
            Var b: Array[Int, 1] = Array(True);

            Var d,e: Int;
            Val f: Array[Array[Int,1], 2] = Array( Array(d), Array(e));
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),ArrayType(1,IntType),[BooleanLit(True)])"
        self.assertTrue(TestChecker.test(input,expect,438))
    
    def test_439(self):
        input = """
        Class A {
            Var A: Int;
            Sicle(){
                Return 1;
            }
            Destroy(){
                Var x: Int = 1;
                Return x;
            }
            
            Constructor(){
                Self.A = Self.Sicle();
                Self.A = Self.Destroy();
            }
        }
        Class Program{
            main(){
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,439))
    
    def test_440(self):
        input = """
        Class A {
            Var a: Int = 10;
            foo() { 
                Val a : Array[Int, 3] = Array(Self.a, 1, 2);
                Val b : Int = a[0];
            }
        }
        Class Program{
            main(){
                Return "String";
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(StringLit(String))"
        self.assertTrue(TestChecker.test(input,expect,440))
    
    def test_441(self):
        input = """
        Class A {
            Val a: Array[Int, 4] = Array(1,2,3,4);
            foo() { 
                Val a : Array[Int, 3] = Array(Self.a, 1, 2);
                Val b : Int = a[0];
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Illegal Array Literal: [FieldAccess(Self(),Id(a)),IntLit(1),IntLit(2)]"
        self.assertTrue(TestChecker.test(input,expect,441))
    
    def test_442(self):
        input = """
        Class Program{
            Val $someStatic : Int = 10;
            main() {
                Var Program : Float = 1.0;
                Var x : Int = Program::$someStatic;
                Var d: Int = 1 && 3.0;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(&&,IntLit(1),FloatLit(3.0))"
        self.assertTrue(TestChecker.test(input,expect,442))
        
    def test_443(self):
        input = """
        Class A{
            Val $a: Int = 2;
            Val a: Int = 3;
        }
        Class B : A {
            Sicla(){
                Var s: Int = Self.a;
                Return 1;
            }
        }
        Class Program{
            main() {
                
            }
        }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,443))
    
    def test_444(self):
        input = """
        Class Program {
            main() {
                a = b;
            }
        }
        """
        expect = "Undeclared Identifier: b"
        self.assertTrue(TestChecker.test(input,expect,444))
    
    def test_445(self):
        input = """
        Class A{
            Val $a: Int = 2;
            Val a: Int = 3;
        }
        Class B : A {
            Sicla(){
                Var s: Int = Self.a;
                Return 1;
            }
        }
        Class Program{
            main() {
                
            }
        }
        """
        expect = "Undeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,445))
    
    def test_446(self):
        input = """
        Class A {
            $foo(){
                Val a: Int = 1;
                Foreach(a In 1 .. a){
                    Break;
                }
                Return;
            }
        }
        Class Program {
            main(){
                Var y : A = New A();
                Var z : Int = 10;
                y::$foo();
                z::$foo();
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(a),IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,446))
    
    def test_447(self):
        input = """
        Class A {
            $foo(){
                
            }
        }
        Class Program {
            main(){
                Var y : A = New A();
                Var z : Int = 10;
                y::$foo();
                z::$foo();
            }
        }
        """
        expect = "Illegal Member Access: Call(Id(y),Id($foo),[])"
        self.assertTrue(TestChecker.test(input,expect,447))
    
    def test_448(self):
        input = """
        Class A {
            $foo(){
                
            }
        }
        Class Program {
            main(){
                Var y : A = New A();
                Var z : Int = 10;
                z::$foo();
            }
        }
        """
        expect = "Type Mismatch In Statement: Call(Id(z),Id($foo),[])"
        self.assertTrue(TestChecker.test(input,expect,448))
    
    def test_449(self):
        input = """
        Class A {
            $foo(){
                
            }
        }
        Class Program {
            main(){
                z::$foo();
            }
        }
        """
        expect = "Undeclared Class: z"
        self.assertTrue(TestChecker.test(input,expect,449))
    
    def test_450(self):
        input = """
        Class A{
            Var B: Int = 10;
        }
        Class Program {
            Var C: A = New A();
            main(){
                Val b: Int = Self.C.B;
            }
        }
        """
        expect = 'Illegal Constant Expression: FieldAccess(FieldAccess(Self(),Id(C)),Id(B))'
        self.assertTrue(TestChecker.test(input, expect, 450))
    
    def test_451(self):
        input = '''
        Class A{
            Constructor(){
                
            }
            Constructor(){
                
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        '''
        expect = "Redeclared Method: Constructor"
        self.assertTrue(TestChecker.test(input, expect, 451))
    
    def test_452(self):
        input = '''
        Class A:A{
            a(){
                
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        '''
        expect = "Undeclared Class: A"
        self.assertTrue(TestChecker.test(input, expect, 452))
    
    def test_453(self):
        input = """
        Class A{
            Var $B: Int = 10;
        }
        Class B{
            Val C: Int = A::$B;
        }
        Class C{
            Var B: String = New A();
        }
        Class Program {
            Var C: C = New C();
            main(){
                Val b: Int = Self.C.B;
            }
        }
        """
        expect = 'Illegal Constant Expression: FieldAccess(Id(A),Id($B))'
        self.assertTrue(TestChecker.test(input, expect, 453))
    
    def test_454(self):
        input = '''
        Class A{
            Val $B: Int = 10;
        }
        Class B{
            Val C: Int = A::$B;
        }
        Class C{
            Var B: String = New A();
        }
        Class Program {
            Var C: C = New C();
            main(){
                Val b: Int = Self.C.B;
            }
        }
        '''
        expect = "Type Mismatch In Statement: VarDecl(Id(B),StringType,NewExpr(Id(A),[]))"
        self.assertTrue(TestChecker.test(input, expect, 454))
    
    def test_455(self):
        input = '''
        Class A{
            Val $B: Int = 10;
        }
        Class B{
            Val C: Int = A::$B;
            cast(a: Int){
                Return "Stuff";
            }
            i2s(a: Int){
                If(a == 1){
                    Return "One";
                }
                Elseif(a == 0){
                    Return "Zero";
                }
                Elseif(a == 0x2){
                    Return "Two";
                }
                Elseif(a == (0x4 - 0b1)){
                    Return "Three";
                }
                Else{
                    Return Self.cast(a - 1);
                } 
                Return "2";
            }
        }
        Class C{
            Var B: String = "String";
            Val C: Array[Int, 2] = Array(1, 2, A::$B);
        }
        Class Program {
            Var C: C = New C();
            main(){
                Return;
            }
        }
        '''
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(C),ArrayType(2,IntType),[IntLit(1),IntLit(2),FieldAccess(Id(A),Id($B))])"
        self.assertTrue(TestChecker.test(input, expect, 455))
    
    def test_456(self):
        input = """
        Class A{
            Val $B: Int = 10;
        }
        
        Class B{
            Val C: Int = A::$B;
            a(a : Int){
                Return "a";
            }
            cast(a : Int){
                If(a == 0){
                    Return "Zero";
                }
                Elseif(a == 1){
                    Return "One";
                }
                Elseif(a == 0x2){
                    Return "Two";
                }
                Elseif(a == (0x4 - 0b1)){
                    Return "Three";
                }
                Else{
                    Return Self.a(a - 1) +. "Three";
                } 
                Return "Other";
            }
            fibonacci(a : Int){
                Var s: Int;
                Var arr: Array[Int, 1000];
                arr[0] = 0;
                arr[1] = 1;
                If(s == 0){
                    Return 0;
                }
                Elseif(s == 1){
                    Return 1;
                }
                Foreach(s In 2 .. a){
                    arr[s] = arr[s - 1] + arr[s - 2];
                }
                Return arr[a];
            }
        }
        Class Program {
            Var C: A = New A();
            main(){
                Val b: Int = Self.C.B;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(FieldAccess(Self(),Id(C)),Id(B))"
        self.assertTrue(TestChecker.test(input, expect, 456))
        
    def test_457(self):
        input = '''
        Class A{
            Val $B: Int = 10;
        }
        
        Class B{
            Val C: Int = A::$B;
            a(a : Int){
                If (a % 2 == 0){
                    Return Array("a");
                }
                Else{
                    Return Array("b");    
                }
            }
            func1(){
                Var s, ss: Int;
                Var result : String = "I";
                Foreach(s In 1 .. 100){
                    Foreach(ss In 1 .. 100){
                        result = result +. (Self.a(ss))[0];
                        Break;
                    }
                }
                Return result;
                Break;
            }
        }
        Class Program {
            Var C: A = New A();
            main(){
                Val b: Int = Self.C.B;
            }
        }
        '''
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 457)) 
    
    def test_458(self):
        input = '''
        Class A{
            Var a1, a2, a3: String;
            Var $s: Int = 0; 
            Constructor(a, b, c : String){
                A::$s = A::$s + 1;
                Self.a1 = a;
                Self.a2 = b;
                Self.a3 = c;
            }
        }
        Class Program{
            Var x : A = Null;
            main(){
                Return 1;
            }
        }
        '''
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 458))
    
    def test_459(self):
        input = '''
        Class A{
            Var arr1: Array[Array[String, 2], 2] = Array(Array("Kangzi", "Ploew"), Array("Quanzan", "Fuming"));
            Var arr2: Array[String, 4] = Array(Self.arr1[0][0], Self.arr1[1][0], Self.arr1[0][1], Self.arr1[1][1]);
            Var d: Boolean = ! True;
            Constructor(){
                Return 1;
            }
            Destructor(){
                Return;
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        '''
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 459))
    
    def test_461(self):
        input = """
        Class Program{
            main(s: String){
                Return 1;
            }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input,expect,461))
        
    def test_462(self):
        input = """
        Class A{
            Var a, d: Int;
            Constructor(){
                Return;
            }
        }
        Class Program{
            main(){
                Return 1;
            }
        }
            """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,462))
    
    def test_463(self):
        input = """
        Class A{
            Var a, d: Int; 
            sickle(s: String){
                Return 1;
            }  
        }
        Class Program{
            main(){
                Return 1;
            }
        }
            """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,463))
        
    def test_464(self):
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
                Return 1;
            }
        }
            """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,464))
    
    def test_465(self):
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
        self.assertTrue(TestChecker.test(input,expect,465))
    
    def test_466(self):
        input = """
        Class A{
            Val a, d: Int = 1, 2;
        }
        Class Si{
            Val $d: Int = 1;
            Constructor(){
                Return;
            }
        }
        Class Program{
            Var s: Si = Null;
            main(){
                Return;
            }
            $so(){
                Return 1.2;
                Return 1;
            }
        }
            """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,466))
    
    def test_467(self):
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
        self.assertTrue(TestChecker.test(input,expect,467))
    
    def test_468(self):
        input = """
        Class A{
            Var a, d: Int;
            sickle(s: String; e: Int){
                Var i: Int;
                Foreach(i In 1 .. 10 By 2){
                   Break; 
                }
                Return;
            }
        }
        Class Program{
            Var test: Int = (New A()).a;
            main(){
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,468))
    
    def test_469(self):
        input = """
        Class A{
            Var a, d: Int;
            Var test_array: Array[Float, 3] = Array(1, 2, 3);
        }
        Class B : A {
            Var b: Int;
        }
        Class Program{
            Var test: A = New A();
            main(){
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,469))
    
    def test_470(self):
        input = """
        Class A{
            Var a, d: Int;
            sickle(s: String; e: Int){
                Var i : Int;
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
        self.assertTrue(TestChecker.test(input,expect,470))
    
    def test_471(self):
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
        self.assertTrue(TestChecker.test(input,expect,471))
    
    def test_472(self):
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
        self.assertTrue(TestChecker.test(input,expect,472))
    
    def test_473(self):
        input = """
        Class A: L{
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
        expect = "Undeclared Class: L"
        self.assertTrue(TestChecker.test(input,expect,473))
    
    def test_474(self):
        input = """
        Class A{
            Var a: Int;
            Constructor(start: Int){
                Var d: String;
                {
                    d = "2";
                    Var d: Int = 2;
                    Self.a = d;
                }
                Return;
            }
            Val b: Int = 1;
        }
        Class Program{
            main(){
                Return 2.0;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(FloatLit(2.0))"
        self.assertTrue(TestChecker.test(input,expect,474))
    
    def test_475(self):
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
                    Var a : Int;
                    {
                        Val a: String = "2";
                    }
                    Return 1;
                }
                Return s;
            }
        }
        Class Program{
            main(){
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,475))
        
    def test_476(self):
        input = """
        Class A {
            Constructor() {}
        }
        Class B {
            Constructor() {}
        }
        Class Program {
            print(a: Float) {}
            main() {
                Val a: A = New B();
                Self.print(a.getInt());
            }
        }
        """
        expect = str(TypeMismatchInConstant(
            ConstDecl(
                Id('a'),
                ClassType(Id('A')),
                NewExpr(Id('B'), [])
            )
        ))
        
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        input = """
        Class A {
            Constructor() {}
        }
        Class B {
            Constructor() {}
        }
        Class Program {
            print(a: Float) {}
            main() {
                Var a: A = New B();
                Self.print(a.getInt());
            }
        }
        """
        expect = str(TypeMismatchInStatement(
            VarDecl(
                Id('a'),
                ClassType(Id('A')),
                NewExpr(Id('B'), [])
            )
        ))
        
        self.assertTrue(TestChecker.test(input, expect, 477))
        
    def test_478(self):
        input = """
        Class Program {
            print(a: Int) {}
            main() {
                Continue;
            }
        }
        """
        expect = str(MustInLoop(Continue()))
        
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        input = """
        Class A {
            Val a: Int = 10;
        }
        Class Program {
            print(a: Int) {}
            main() {
                Self.print(A.a);
            }
        }
        """
        expect = str(IllegalMemberAccess(FieldAccess(Id('A'), Id('a'))))
        
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
        input = """
        Class A {
            Val a: Int = 10;
        }
        Class Program {
            print(a: Int) {}
            main() {
                Var i: Int;
                Foreach (i In 0 .. 10) {}
                Return "main";
            }
        }
        """
        expect = str(TypeMismatchInStatement(Return(StringLiteral("main"))))
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        input = """
        Class A {
            Val a: Int = 10;
        }
        Class Program {
            print(a: Int) {}
            method() {}
        }
        """
        expect = str(NoEntryPoint())
        
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
        input = """
        Class A {
            Val a: Int = -10;
        }
        Class Program {
            print(a: Int) {}
            method() {}
        }
        """
        expect = str(NoEntryPoint())
        
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        input = """
        Class Program {
            Var a: Int = 10;
            $print(a: Int) {
                Self.a = 20;
            }
            main() {
            }
        }
        """
        expect = str(IllegalMemberAccess(
            FieldAccess(SelfLiteral(), Id('a'))
        ))
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        input = """
        Class Program {
            Var a: A;
            main() {
            }
        }
        """
        expect = str(Undeclared(Class(), 'A'))
        
        self.assertTrue(TestChecker.test(input, expect, 484))
    
    def test_485(self):
        input = """
        Class Car {}
        Class Program {
            main(){
                Val car: Car = New Car();
                Var x : Int = 1 + Car;
            }
        }
        """
        expect = str(Undeclared(Identifier(), 'Car'))
        
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = """
        Class Program {
            main(){
                Var b: Boolean = True == 2;  
            }
        }
        """
        expect = str(TypeMismatchInExpression(
            BinaryOp(
                '==',
                BooleanLiteral(True),
                IntLiteral(2) 
            )
        ))
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        input = """
        Class Program {
            main(){
                Var a: Int;
                Val b: Int = a + 10;
            }
        }
        """
        expect = str(IllegalConstantExpression(
            BinaryOp(
                '+',
                Id('a'),
                IntLiteral(10)
            )
        ))
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_488(self):
        input = """
        Class Program {
            Var $a: Int;
            main(){
                Var a: Int = Program::$a + 1;
                Val b: Int = a + 10;
            }
        }
        """
        expect = str(IllegalConstantExpression(
            BinaryOp(
                '+',
                Id('a'),
                IntLiteral(10)
            )
        ))
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = """
        Class A {
            Var $a: Int;
        }
        Class Program {
            main() {
                Var a: A = New A();
                Val b: Int = a::$a + 10;
            }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Id(a),Id($a))"
        self.assertTrue(TestChecker.test(input, expect, 489))
    
    
    def test_490(self):
        input = """
        Class Program {
            Var a: Int;
            a() {
                Return 1;
            }
            main() {
                Val b: Int = Self.a * Self.a();
            }
        }
        """
        expect = str(
            IllegalConstantExpression(
                BinaryOp(
                    '*',
                    FieldAccess(SelfLiteral(), Id('a')),
                    CallExpr(SelfLiteral(), Id('a'), [])
                )
            )
        )
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """
        Class Program {
            print(a: Float) {}
            print2(a, b: Int) {}
            main() {
                Self.print(10);
                Self.print2(20);
            }
        }
        """
        expect = str(TypeMismatchInStatement(
            CallStmt(
                SelfLiteral(),
                Id('print2'),
                [IntLiteral(20)]
            )
        ))
        self.assertTrue(TestChecker.test(input, expect, 491))
    
    def test_492(self):
        input = """
            Class Program{
                dutch(){
                    Var a: Int = 0;
                    If(a == 0){
                        Var a: Int = 1;
                        Return a;
                    }
                    Else{
                        Return a + 1;
                    }
                }
                main(){
                    Return 1;
                }
            }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input,expect,492))
    
    def test_493(self):
        input = """
        Class A{
            Var a, d: Int;
            sickle(s: String; e: Int){
                Var i : String;
                Foreach(i In 1 .. 10 By 2){
                   Break; 
                   Continue;
                }
            }
        }
        Class Program{
            main(){
                Return;
            }
        }
        """
        expect = "Type Mismatch In Statement: For(Id(i),IntLit(1),IntLit(10),IntLit(2),Block([Break,Continue])])"
        self.assertTrue(TestChecker.test(input,expect,493))
    
    def test_494(self):
        input = """
        Class Program {
            main() {
                Var a: Int = 10;
                {
                    Var a: Int = 10;
                    Var arr: Array[Int, 3] = Array(1, 2, 3);
                    a = a + arr[1.0];
                }
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(arr),[FloatLit(1.0)])"
        self.assertTrue(TestChecker.test(input,expect,494))
    
    def test_495(self):
        input = """
        Class Program {
            main() {
                Val a: Int = 10;
                Val a: Int = 20;
            }
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """
        Class Program {
            main() {
                Var a: Int = 10;
                Var a: Int = 20;
            }
        }
        """
        expect = "Redeclared Variable: a"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
        input = """
        Class Program {
            main() {
                Var a: Int = 10;
                Val a: Int = 20;
            }
        }
        """
        expect = "Redeclared Constant: a"
        self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """
        Class Program {
            main() {}
        }
        Class Program {
            main() {
                Var a: Int = 10;
            }
        }
        """
        expect = "Redeclared Class: Program"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """
        Class Program {
            main() {
                {
                    Var a: Int = 10;
                    {
                        Var a: Int = 10;
                    }
                }
                Var a: Int = 10;
            }
            main() {}
        }
        """
        expect = "Redeclared Method: main"
        self.assertTrue(TestChecker.test(input, expect, 499))

    def test_500(self):
        input = """
        Class Program {
            Val $a: Int = 10;
            Var $a: Float = 20.2;
            main() {}
        }
        """
        expect = "Redeclared Attribute: $a"
        self.assertTrue(TestChecker.test(input, expect, 500))
    
    def test_501(self):
        input = """Class io {
            $getInt() { Return 1; }
            $putIntLn(a: Int) {}
            $putFloatLn(a: Float) {}
        }
        Class Program {
            main() {
                io::$putIntLn();
            }
        }"""
        expect = "Type Mismatch In Statement: Call(Id(io),Id($putIntLn),[])"
        self.assertTrue(TestChecker.test(input,expect,501))
        
    
    