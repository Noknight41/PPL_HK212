import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_1(self):
        """Simple program: int main() {} """
        input = """
        Class Duong
        {
        }
        """
        expect = """Program([ClassDecl(Id(Duong),[])])"""
        self.assertTrue(TestAST.test(input,expect,300))
    def test_2 (self):
        input = """
        Class Program
        {
            main()
            {
                
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,301))
        

    def test_3 (self):
        input = """
        Class A {
            foo(a,b:Int;c:Float){}
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([]))])])'
        self.assertTrue(TestAST.test(input,expect,302))
        

    def test_4 (self):
        input = """
        Class A {
            NoParameters(){}
        }
        """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(NoParameters),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input,expect,303))
        

    def test_5 (self):
        input = """
        Class Student
        {
            Var $maxHeight: Float = 0;
        }""" 
        expect = """Program([ClassDecl(Id(Student),[AttributeDecl(Static,VarDecl(Id($maxHeight),FloatType,IntLit(0)))])])"""
        self.assertTrue(TestAST.test(input,expect,304))
        

    def test_6 (self):
        input = """
        Class Student
        {
            Var $maxHeight: Float = 0;
            Var name, class: String;
        }""" 
        expect = """Program([ClassDecl(Id(Student),[AttributeDecl(Static,VarDecl(Id($maxHeight),FloatType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(class),StringType))])])"""
        self.assertTrue(TestAST.test(input,expect,305))
        

    def test_7 (self):
        input = """
        Class Student
        {
            Var $maxHeight: Float = 0;
            Var name, class: String;
            Val $max, $min: Int = 100, 10;
        }""" 
        expect = """Program([ClassDecl(Id(Student),[AttributeDecl(Static,VarDecl(Id($maxHeight),FloatType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(name),StringType)),AttributeDecl(Instance,VarDecl(Id(class),StringType)),AttributeDecl(Static,ConstDecl(Id($max),IntType,IntLit(100))),AttributeDecl(Static,ConstDecl(Id($min),IntType,IntLit(10)))])])"""
        self.assertTrue(TestAST.test(input,expect,306))
        

    def test_8 (self):
        input = """
        Class Student
        {
            Var $maxHeight: Float = 0;
            $getMaxHeight()
            {
                Return Student::$maxHeight;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Student),[AttributeDecl(Static,VarDecl(Id($maxHeight),FloatType,IntLit(0))),MethodDecl(Id($getMaxHeight),Static,[],Block([Return(FieldAccess(Id(Student),Id($maxHeight)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,307))
        

    def test_9 (self):
        input = """
        Class Circle
        {
            Val radius: Float;
        }
        Class Program
        {
            main()
            {

            }
        }""" 
        expect = """Program([ClassDecl(Id(Circle),[AttributeDecl(Instance,ConstDecl(Id(radius),FloatType,None))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,308))
        

    def test_10 (self):
        input = """
        Class A {
            Var a:Int;
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])'
        self.assertTrue(TestAST.test(input,expect,309))
        

    def test_11 (self):
        input = """
        Class Program
        {
            main ()
            {
            Var Num: Int = 1 + 3;
            System.out.printLn(Num);
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(Num),IntType,BinaryOp(+,IntLit(1),IntLit(3))),Call(FieldAccess(Id(System),Id(out)),Id(printLn),[Id(Num)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,310))
        

    def test_12 (self):
        input = """
        Class Shape
        {
            Val radius: Float;
            getArea()
            {
                Val pi: Float = 3.14;
                Return Self.radius * Self.radius * pi;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(radius),FloatType,None)),MethodDecl(Id(getArea),Instance,[],Block([ConstDecl(Id(pi),FloatType,FloatLit(3.14)),Return(BinaryOp(*,BinaryOp(*,FieldAccess(Self(),Id(radius)),FieldAccess(Self(),Id(radius))),Id(pi)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,311))
        

    def test_13 (self):
        input = """
        Class A 
        {
            Val a:String=b[1][1];
        }
        """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,ArrayCell(Id(b),[IntLit(1),IntLit(1)])))])])'
        self.assertTrue(TestAST.test(input,expect,312))
        

    def test_14 (self):
        input = """
        Class Program
        {
            main()
            {
                Var a,b : Int = 123_56, 5689_89;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(12356)),VarDecl(Id(b),IntType,IntLit(568989))]))])])"""
        self.assertTrue(TestAST.test(input,expect,313))
        

    def test_15 (self):
        input = """
        Class Program
        {
            main()
            {
                Val a: Float = 4.5e-45;
                Var b: Int = 13533_13;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(a),FloatType,FloatLit(4.5e-45)),VarDecl(Id(b),IntType,IntLit(1353313))]))])])"""
        self.assertTrue(TestAST.test(input,expect,314))
        

    def test_16 (self):
        input = """
        Class Shape2 
        {
            $getNumOfShape() 
            {
                If (a == (1+1) ){
                    Var b,c:Boolean = True, False;
                }
                Foreach (i In 1 .. 100 By 2) 
                {
                    Var a:Boolean = True;
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(Shape2),[MethodDecl(Id($getNumOfShape),Static,[],Block([If(BinaryOp(==,Id(a),BinaryOp(+,IntLit(1),IntLit(1))),Block([VarDecl(Id(b),BoolType,BooleanLit(True)),VarDecl(Id(c),BoolType,BooleanLit(False))])),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([VarDecl(Id(a),BoolType,BooleanLit(True))])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,315))
        

    def test_17 (self):
        input = """
        Class Program
        {
            main()
            {
                Var a: Int = 5;
                If(a == 5)
                {
                    System.print(a);
                }
                Else
                {
                    System.print(a);
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(5)),If(BinaryOp(==,Id(a),IntLit(5)),Block([Call(Id(System),Id(print),[Id(a)])]),Block([Call(Id(System),Id(print),[Id(a)])]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,316))
        

    def test_18 (self):
        input = """
        Class Program
        {
            main()
            {
                Var a: Int = 5;
                If(a == 5)
                {
                    System.print(a);
                }
                Elseif(a == 6)
                {
                    System.print(a);
                }
                Elseif(a == 7)
                {
                    System.print(a);
                }
                Else
                {
                    System.print(a);
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(5)),If(BinaryOp(==,Id(a),IntLit(5)),Block([Call(Id(System),Id(print),[Id(a)])]),If(BinaryOp(==,Id(a),IntLit(6)),Block([Call(Id(System),Id(print),[Id(a)])]),If(BinaryOp(==,Id(a),IntLit(7)),Block([Call(Id(System),Id(print),[Id(a)])]),Block([Call(Id(System),Id(print),[Id(a)])]))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,317))
        

    def test_19 (self):
        input = """
        Class A: B
        {
            Foo()
            {
                If(3)
                    {Val a: Int = 4660;}
                Elseif(4)
                    {{}}
                Elseif(5)
                    {Return Self;}
                Else
                    {a = 1;}
            }
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([If(IntLit(3),Block([ConstDecl(Id(a),IntType,IntLit(4660))]),If(IntLit(4),Block([Block([])]),If(IntLit(5),Block([Return(Self())]),Block([AssignStmt(Id(a),IntLit(1))]))))]))])])'
        self.assertTrue(TestAST.test(input,expect,318))
        

    def test_20 (self):
        input = """
        Class Shape2 
        {
            $getNumOfShape() 
            {
                If (a == (1+1) )
                {
                    Var b,c:Boolean = True, False;
                }
                Foreach (i In 1 .. 100 By 2) 
                {
                     Var a:Boolean = True;
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(Shape2),[MethodDecl(Id($getNumOfShape),Static,[],Block([If(BinaryOp(==,Id(a),BinaryOp(+,IntLit(1),IntLit(1))),Block([VarDecl(Id(b),BoolType,BooleanLit(True)),VarDecl(Id(c),BoolType,BooleanLit(False))])),For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([VarDecl(Id(a),BoolType,BooleanLit(True))])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,319))
        

    def test_21 (self):
        input = """
        Class Program {
            Var a : Float;
            Var $b : Array[String, 10];
            mainA () {
                Self.getIntLn();
            }
        }
        """
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(a),FloatType)),AttributeDecl(Static,VarDecl(Id($b),ArrayType(10,StringType))),MethodDecl(Id(mainA),Instance,[],Block([Call(Self(),Id(getIntLn),[])]))])])"
        self.assertTrue(TestAST.test(input,expect,320))
        

    def test_22 (self):
        input = """
        Class Program
        {
            main()
            {
                Var a: Array[Array[Array[Int,4],2],2] = Array(
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    ),
                    Array(
                        Array(1,2,3,4),
                        Array(1,2,3,4)
                    )
                );
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(2,ArrayType(2,ArrayType(4,IntType))),[[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]],[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(1),IntLit(2),IntLit(3),IntLit(4)]]])]))])])"""
        self.assertTrue(TestAST.test(input,expect,321))
        

    def test_23 (self):
        input = """
        Class Program
        {
            main()
            {
                Val  myArray: Array[Int, 4] = Array(5, 6, 7, 8);
                Foreach (i In 1 .. 4 By 1) 
                {
                    System.print(myArray[i]);
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(myArray),ArrayType(4,IntType),[IntLit(5),IntLit(6),IntLit(7),IntLit(8)]),For(Id(i),IntLit(1),IntLit(4),IntLit(1),Block([Call(Id(System),Id(print),[ArrayCell(Id(myArray),[Id(i)])])])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,322))
        

    def test_24 (self):
        input = """Class Program { notmain(a,b:Int; c:String) {Val a,b:Int = 2,3;}notmain2(a:Int) {Val a:Int = 2;}}"""
        expect = str(Program([ClassDecl(Id("Program"),[MethodDecl(Instance(),Id("notmain"),[VarDecl(Id("a"),IntType()),VarDecl(Id("b"),IntType()),VarDecl(Id("c"),StringType())],Block([ConstDecl(Id('a'), IntType(), IntLiteral(2)),ConstDecl(Id('b'), IntType(), IntLiteral(3))])), MethodDecl(Instance(),Id("notmain2"),[VarDecl(Id("a"),IntType())],Block([ConstDecl(Id('a'), IntType(), IntLiteral(2))]))])]))
        self.assertTrue(TestAST.test(input,expect,323))
        

    def test_25 (self):
        input = """
        Class Rectangle
        {
            Var height: Float;
            Var width: Float;
            Constructor(height, width: Float)
            {
                Self.height = height;
                Self.width = width;
            }
        }
        """ 
        expect = """Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(height),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(height),FloatType),param(Id(width),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(height)),Id(height)),AssignStmt(FieldAccess(Self(),Id(width)),Id(width))]))])])"""
        self.assertTrue(TestAST.test(input,expect,324))
        
    def test_26 (self):
        input = """
        Class Rectangle
        {
            Var height: Float;
            Var width: Float;
            Constructor(height, width: Float)
            {
                Self.height = height;
                Self.width = width;
            }
            getArea()
            {
                Return Self.height * Self.width;
            }
        }
        """ 
        expect = """Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(height),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(height),FloatType),param(Id(width),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(height)),Id(height)),AssignStmt(FieldAccess(Self(),Id(width)),Id(width))])),MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(height)),FieldAccess(Self(),Id(width))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,325))
        

    def test_27 (self):
        input = """
        Class Rectangle
        {
            Var height: Float;
            Var width: Float;
            Constructor(height, width: Float)
            {
                Self.height = height;
                Self.width = width;
            }
            getArea()
            {
                Return Self.height * Self.width;
            }
        }
        Class Program
        {
            main()
            {
                Var myShape: Rectangle = New Rectangle(5,6);
                System.print(myShape.getArea());
            }
        }
        """ 
        expect = """Program([ClassDecl(Id(Rectangle),[AttributeDecl(Instance,VarDecl(Id(height),FloatType)),AttributeDecl(Instance,VarDecl(Id(width),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(height),FloatType),param(Id(width),FloatType)],Block([AssignStmt(FieldAccess(Self(),Id(height)),Id(height)),AssignStmt(FieldAccess(Self(),Id(width)),Id(width))])),MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(height)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(myShape),ClassType(Id(Rectangle)),NewExpr(Id(Rectangle),[IntLit(5),IntLit(6)])),Call(Id(System),Id(print),[CallExpr(Id(myShape),Id(getArea),[])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,326))
        

    def test_28 (self):
        input = """
        Class Program : ABC 
        {
            Val a : Float = 0.0;
            Var b : SomeMeta = Null;
            Val c : Delta = Self;
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(ABC),[AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(SomeMeta)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(c),ClassType(Id(Delta)),Self()))])])"
        self.assertTrue(TestAST.test(input,expect,327))
        

    def test_29 (self):
        input = """
        Class Program 
        {
            Val a, b, c : Int = 1 + 1, 2 * 2, 3 / 3;
            Var a : Array[Int, 5] = Array(1 * 2 / 3, 3 + 3 / 3, 10 - -9, 100 * 3, 100 % 10);
        }"""
        expect = "Program([ClassDecl(Id(Program),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(1)))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,BinaryOp(*,IntLit(2),IntLit(2)))),AttributeDecl(Instance,ConstDecl(Id(c),IntType,BinaryOp(/,IntLit(3),IntLit(3)))),AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType),[BinaryOp(/,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),BinaryOp(+,IntLit(3),BinaryOp(/,IntLit(3),IntLit(3))),BinaryOp(-,IntLit(10),UnaryOp(-,IntLit(9))),BinaryOp(*,IntLit(100),IntLit(3)),BinaryOp(%,IntLit(100),IntLit(10))]))])])"
        self.assertTrue(TestAST.test(input,expect,328))
        

    def test_30 (self):
        input = """
        Class Program {
            a() 
            {
                If (a == b) 
                {
                    Self.print("Hurray");
                } 
                Elseif (a > b) 
                {
                    Self.print("Greater");
                } 
                Elseif (a < b) 
                {
                    Self.print("Less");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Hurray)])]),If(BinaryOp(>,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Greater)])]),If(BinaryOp(<,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Less)])]))))]))])])"
        self.assertTrue(TestAST.test(input,expect,329))
        

    def test_31 (self):
        """String operator"""
        input = """
        Class Program : Facebook 
        {
            Val a, b : String = "Hello", "World";
            Var c : String = a +. b;
            Var d : String = ("Hello" +. " ") +. "World";
            Var e : Boolean = c ==. d;
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(Facebook),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,StringLit(Hello))),AttributeDecl(Instance,ConstDecl(Id(b),StringType,StringLit(World))),AttributeDecl(Instance,VarDecl(Id(c),StringType,BinaryOp(+.,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(d),StringType,BinaryOp(+.,BinaryOp(+.,StringLit(Hello),StringLit( )),StringLit(World)))),AttributeDecl(Instance,VarDecl(Id(e),BoolType,BinaryOp(==.,Id(c),Id(d))))])])"
        self.assertTrue(TestAST.test(input,expect,330))
        

    def test_32 (self):
        input = """
        Class Program : ABCMeta 
        {
            Val a, b : Int = 1, 1;
            Var c : Boolean = a > b;
            Var d : Boolean = a < b;
            Var e, f, g, h : Boolean = a == b, a != b, a >= b, a <= b;
            Var i, j, k, l : Boolean = 1 <= 2, 2 != 3, 3.0 == 4.0, 4.5 > 4.0;
        }"""
        expect = "Program([ClassDecl(Id(Program),Id(ABCMeta),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(c),BoolType,BinaryOp(>,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(d),BoolType,BinaryOp(<,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(e),BoolType,BinaryOp(==,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(f),BoolType,BinaryOp(!=,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(g),BoolType,BinaryOp(>=,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(h),BoolType,BinaryOp(<=,Id(a),Id(b)))),AttributeDecl(Instance,VarDecl(Id(i),BoolType,BinaryOp(<=,IntLit(1),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(j),BoolType,BinaryOp(!=,IntLit(2),IntLit(3)))),AttributeDecl(Instance,VarDecl(Id(k),BoolType,BinaryOp(==,FloatLit(3.0),FloatLit(4.0)))),AttributeDecl(Instance,VarDecl(Id(l),BoolType,BinaryOp(>,FloatLit(4.5),FloatLit(4.0))))])])"
        self.assertTrue(TestAST.test(input,expect,331))
        

    def test_33 (self):
        input = """
        Class Program
        {
            recursion(a:Int)
            {
                If((a == 0) || (a== 1))
                    {
                        Return 1;
                    }
                Else
                    {
                        Return Self.recursion(a - 1);
                    }
            }
            main()
            {
                Var a: Int = Self.recursion(6);
                System.out.printLn(a);
            }
        }
        """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(recursion),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(||,BinaryOp(==,Id(a),IntLit(0)),BinaryOp(==,Id(a),IntLit(1))),Block([Return(IntLit(1))]),Block([Return(CallExpr(Self(),Id(recursion),[BinaryOp(-,Id(a),IntLit(1))]))]))])),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,CallExpr(Self(),Id(recursion),[IntLit(6)])),Call(FieldAccess(Id(System),Id(out)),Id(printLn),[Id(a)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,332))
        
    def test_34 (self):
        input = """
        Class Program
        {
            main()
            {
                ##Val my_array: Array[Int, 6] = Array(2,3,1,4,5,6,7,8);
                Var my_sum : Int = 0;##
                Foreach (my_index In 1 .. 8)
                    {
                        my_sum = my_sum + my_array[my_index];
                    }
                    Return my_sum;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(my_index),IntLit(1),IntLit(8),IntLit(1),Block([AssignStmt(Id(my_sum),BinaryOp(+,Id(my_sum),ArrayCell(Id(my_array),[Id(my_index)])))])]),Return(Id(my_sum))]))])])"""
        self.assertTrue(TestAST.test(input,expect,333))
        

    def test_35 (self):
        input = """
        Class Program
        {
            main()
            {
                Val my_array: Array[Int, 6] = Array(2,3,1,4,5,6,7,8);
                Var my_sum_odd : Int = 0;
                Var my_sum_even: Int = 0;
                Foreach (my_index In 1 .. 8)
                {
                    If(my_array[my_index] % 2 == 0)
                    {
                        my_sum_even  = my_sum_even + my_array[my_index];
                    }
                    Else
                    {
                        my_sum_odd  = my_sum_odd + my_array[my_index];
                    }
                }
                If (my_sum_even > my_sum_odd)
                {
                    Return True;
                }
                Else
                {
                    Return False;
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(my_array),ArrayType(6,IntType),[IntLit(2),IntLit(3),IntLit(1),IntLit(4),IntLit(5),IntLit(6),IntLit(7),IntLit(8)]),VarDecl(Id(my_sum_odd),IntType,IntLit(0)),VarDecl(Id(my_sum_even),IntType,IntLit(0)),For(Id(my_index),IntLit(1),IntLit(8),IntLit(1),Block([If(BinaryOp(==,BinaryOp(%,ArrayCell(Id(my_array),[Id(my_index)]),IntLit(2)),IntLit(0)),Block([AssignStmt(Id(my_sum_even),BinaryOp(+,Id(my_sum_even),ArrayCell(Id(my_array),[Id(my_index)])))]),Block([AssignStmt(Id(my_sum_odd),BinaryOp(+,Id(my_sum_odd),ArrayCell(Id(my_array),[Id(my_index)])))]))])]),If(BinaryOp(>,Id(my_sum_even),Id(my_sum_odd)),Block([Return(BooleanLit(True))]),Block([Return(BooleanLit(False))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,334))
        

    def test_36 (self):
        input = """
        Class Program
        {
            fibonacci(myNum:Int)
            {
                If((myNum == 0) || (myNum == 1))
                    {
                        Return 1;
                    }
                Else
                {
                    Return Self.fibonacci(myNum - 1) + Self.fibonacci(myNum - 1);
                }
            }
            main ()
            {
                Val my_num : Int = Self.fibonacci(10);
                System.Out.printLn(my_num);
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(fibonacci),Instance,[param(Id(myNum),IntType)],Block([If(BinaryOp(||,BinaryOp(==,Id(myNum),IntLit(0)),BinaryOp(==,Id(myNum),IntLit(1))),Block([Return(IntLit(1))]),Block([Return(BinaryOp(+,CallExpr(Self(),Id(fibonacci),[BinaryOp(-,Id(myNum),IntLit(1))]),CallExpr(Self(),Id(fibonacci),[BinaryOp(-,Id(myNum),IntLit(1))])))]))])),MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(my_num),IntType,CallExpr(Self(),Id(fibonacci),[IntLit(10)])),Call(FieldAccess(Id(System),Id(Out)),Id(printLn),[Id(my_num)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,335))
        

    def test_37 (self):
        # This testcase is error-prone your result may be different due to priority of * operator anf % operator
        input = """
        Class BaseClass 
        {
            Var $numOfObjs: Int = 0;
            Constructor() 
            {
                BaseClass::$numOfObjs = BaseClass::$numOfObjs + 1;
            }
            Destructor() 
            {
                BaseClass::$numOfObjs = BaseClass::$numOfObjs - 1;
                Out.printLn("Can\'t even be free for a day huh");
            }
            $staticMethod() {
                Out.printLn(Program.gcd(123_456,46*75%3));
            }
        }
        Class DerivedClass : BaseClass 
        {
            Var UUID: Int;
        }"""
        expect = """Program([ClassDecl(Id(BaseClass),[AttributeDecl(Static,VarDecl(Id($numOfObjs),IntType,IntLit(0))),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(BaseClass),Id($numOfObjs)),BinaryOp(+,FieldAccess(Id(BaseClass),Id($numOfObjs)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Id(BaseClass),Id($numOfObjs)),BinaryOp(-,FieldAccess(Id(BaseClass),Id($numOfObjs)),IntLit(1))),Call(Id(Out),Id(printLn),[StringLit(Can't even be free for a day huh)])])),MethodDecl(Id($staticMethod),Static,[],Block([Call(Id(Out),Id(printLn),[CallExpr(Id(Program),Id(gcd),[IntLit(123456),BinaryOp(%,BinaryOp(*,IntLit(46),IntLit(75)),IntLit(3))])])]))]),ClassDecl(Id(DerivedClass),Id(BaseClass),[AttributeDecl(Instance,VarDecl(Id(UUID),IntType))])])"""
        self.assertTrue(TestAST.test(input,expect,336))
        

    def test_38 (self):
        input = """
        Class Hello
        {
            Var _Fool, _Magician : String;
            Constructor(x, y: String){
                _Fool = x;
                _Magician = y;
                Self.print("Constructor is good");
            }
        }
        
        Class Program 
        {
            ## Hello Everybody ##
            main()
            {
                Var x: Hello = New Hello();
                Return x._Fool;
            }
        }"""
        expect = """Program([ClassDecl(Id(Hello),[AttributeDecl(Instance,VarDecl(Id(_Fool),StringType)),AttributeDecl(Instance,VarDecl(Id(_Magician),StringType)),MethodDecl(Id(Constructor),Instance,[param(Id(x),StringType),param(Id(y),StringType)],Block([AssignStmt(Id(_Fool),Id(x)),AssignStmt(Id(_Magician),Id(y)),Call(Self(),Id(print),[StringLit(Constructor is good)])]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),ClassType(Id(Hello)),NewExpr(Id(Hello),[])),Return(FieldAccess(Id(x),Id(_Fool)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,337))
        

    def test_39 (self):
        input = """
        Class Program
        {
            main()
            {
                Var mytemp: ABC;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(mytemp),ClassType(Id(ABC)),NullLiteral())]))])])"""
        self.assertTrue(TestAST.test(input,expect,338))
        

    def test_40 (self):
        input = """
        Class Program
        {
            Var myshape, $myroad: ABC;
            main()
            {
                Var a,b,d : Shape;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(myshape),ClassType(Id(ABC)),NullLiteral())),AttributeDecl(Static,VarDecl(Id($myroad),ClassType(Id(ABC)),NullLiteral())),MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ClassType(Id(Shape)),NullLiteral()),VarDecl(Id(b),ClassType(Id(Shape)),NullLiteral()),VarDecl(Id(d),ClassType(Id(Shape)),NullLiteral())]))])])"""
        self.assertTrue(TestAST.test(input,expect,339))
        

    def test_41 (self):
        input = """
        Class Shape 
        {
            Val My1stCons, My2ndCons: Int = 1 + 5/2, 2;
            Var $x, $y : Int = 0, 0;
        }
        Class Program 
        {
            ## Muda
            Muda ##
            Var hello: Array[Int, 5];
            Var length, width: Int;
            main(){
                a = 1.0;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(My1stCons),IntType,BinaryOp(+,IntLit(1),BinaryOp(/,IntLit(5),IntLit(2))))),AttributeDecl(Instance,ConstDecl(Id(My2ndCons),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0)))]),ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(hello),ArrayType(5,IntType))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id(main),Static,[],Block([AssignStmt(Id(a),FloatLit(1.0))]))])])"""
        self.assertTrue(TestAST.test(input,expect,340))
        

    def test_42 (self):
        input = """
        Class Shape
        {
            Val $n: Int = 1;
            ## Var s: Int = 2 ##
            Var s: Int = 2;
        }
        Class Program 
        {
            Val $numOfShape: Int;
            Val immutableAttribute: Int;
            Var a_c: Array[Int, 4] = Array(1, 3, 5, 8);
            
            $getNumOfShape()
            {
                {
                    Val fShap: String = "243 '" Hello '"";
                }
                ## Var s: Int = 2 ##
                Var y: Shape = New Shape();
                x = y.s + y::$n;
                Return Shape::$numOfShape;
            }
            ## Muda
            Muda ##
        }""" 
        expect = """Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($n),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(s),IntType,IntLit(2)))]),ClassDecl(Id(Program),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,None)),AttributeDecl(Instance,VarDecl(Id(a_c),ArrayType(4,IntType),[IntLit(1),IntLit(3),IntLit(5),IntLit(8)])),MethodDecl(Id($getNumOfShape),Static,[],Block([Block([ConstDecl(Id(fShap),StringType,StringLit(243 '" Hello '"))]),VarDecl(Id(y),ClassType(Id(Shape)),NewExpr(Id(Shape),[])),AssignStmt(Id(x),BinaryOp(+,FieldAccess(Id(y),Id(s)),FieldAccess(Id(y),Id($n)))),Return(FieldAccess(Id(Shape),Id($numOfShape)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,341))
        

    def test_43 (self):
        input = """Class Something : Object {
            Var $a, b, c : Float = 10.0, 11., 1e15;
            Val a, c, d : Float = .e5, 0.000, 0.2;
            Var c, d, e : Float = 1e-12, 1E+4, 11.1123e10;
            Val $a, $y, $x : Float = 50.1123E-5, .5e5, .4e+5;
            Var x, y : Float = .1123e-10, 1123E123;
        }"""
        expect = "Program([ClassDecl(Id(Something),Id(Object),[AttributeDecl(Static,VarDecl(Id($a),FloatType,FloatLit(10.0))),AttributeDecl(Instance,VarDecl(Id(b),FloatType,FloatLit(11.0))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(1000000000000000.0))),AttributeDecl(Instance,ConstDecl(Id(a),FloatType,FloatLit(0.0))),AttributeDecl(Instance,ConstDecl(Id(c),FloatType,FloatLit(0.0))),AttributeDecl(Instance,ConstDecl(Id(d),FloatType,FloatLit(0.2))),AttributeDecl(Instance,VarDecl(Id(c),FloatType,FloatLit(1e-12))),AttributeDecl(Instance,VarDecl(Id(d),FloatType,FloatLit(10000.0))),AttributeDecl(Instance,VarDecl(Id(e),FloatType,FloatLit(111123000000.0))),AttributeDecl(Static,ConstDecl(Id($a),FloatType,FloatLit(0.000501123))),AttributeDecl(Static,ConstDecl(Id($y),FloatType,FloatLit(50000.0))),AttributeDecl(Static,ConstDecl(Id($x),FloatType,FloatLit(40000.0))),AttributeDecl(Instance,VarDecl(Id(x),FloatType,FloatLit(1.123e-11))),AttributeDecl(Instance,VarDecl(Id(y),FloatType,FloatLit(1.123e+126)))])])"
        self.assertTrue(TestAST.test(input,expect,342))
        

    def test_44 (self):
        input = """
        Class Program
        {
            main() 
            {
                Val b : String;
                a = New OPER();
                Var a_c: Array[Float, 4]= Array(1e5,3.0, 1e-10);
                Val b: Int = a::$xan;
            }
        }
        Class OPER 
        {
            Val xan: Int;
            getXan()
            {   
                Return xan;
            }
            Constructor()
            {
                xan = 5+-3-5*4/2*New OPPER(6,5).a;
                xan=-a;
            }
            Destructor()
            {
                xan=0;
            }
        }
""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(b),StringType,None),AssignStmt(Id(a),NewExpr(Id(OPER),[])),VarDecl(Id(a_c),ArrayType(4,FloatType),[FloatLit(100000.0),FloatLit(3.0),FloatLit(1e-10)]),ConstDecl(Id(b),IntType,FieldAccess(Id(a),Id($xan)))]))]),ClassDecl(Id(OPER),[AttributeDecl(Instance,ConstDecl(Id(xan),IntType,None)),MethodDecl(Id(getXan),Instance,[],Block([Return(Id(xan))])),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(Id(xan),BinaryOp(-,BinaryOp(+,IntLit(5),UnaryOp(-,IntLit(3))),BinaryOp(*,BinaryOp(/,BinaryOp(*,IntLit(5),IntLit(4)),IntLit(2)),FieldAccess(NewExpr(Id(OPPER),[IntLit(6),IntLit(5)]),Id(a))))),AssignStmt(Id(xan),UnaryOp(-,Id(a)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(xan),IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input,expect,343))
        

    def test_45 (self):
        input = """
        Class Program 
        {
            main()
            {
                Foreach (x In 1 .. 25 By x + 1) 
                {
                    If(("22" +. "22") ==. "2222")
                    {
                        Break;
                    }
                    Continue;
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(x),IntLit(1),IntLit(25),BinaryOp(+,Id(x),IntLit(1)),Block([If(BinaryOp(==.,BinaryOp(+.,StringLit(22),StringLit(22)),StringLit(2222)),Block([Break])),Continue])])]))])])"""
        self.assertTrue(TestAST.test(input,expect,344))
        

    def test_46 (self):
        input = """
        Class Image{
                Var width, height: Int;
                Var matrix: Array[Array[Array[Int, 3], 256], 256];
                hstack(img: Image){
                    Var concatMatrix: Array[Array[Array[Int, 3], 512], 512];
                    Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.concatMatrix[row][col][channel] = Self.matrix[row][col][channel];
                                Self.concatMatrix[row][col+256][channel] = Self.matrix[row][col][channel];
                            } 
                        }
                    }
                }
            }
        """
        expect = "Program([ClassDecl(Id(Image),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(matrix),ArrayType(256,ArrayType(256,ArrayType(3,IntType))))),MethodDecl(Id(hstack),Instance,[param(Id(img),ClassType(Id(Image)))],Block([VarDecl(Id(concatMatrix),ArrayType(512,ArrayType(512,ArrayType(3,IntType)))),For(Id(row),IntLit(1),IntLit(256),IntLit(1),Block([For(Id(col),IntLit(256),IntLit(1),UnaryOp(-,IntLit(1)),Block([For(Id(channel),IntLit(1),IntLit(3),IntLit(1),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(concatMatrix)),[Id(row),Id(col),Id(channel)]),ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)])),AssignStmt(ArrayCell(FieldAccess(Self(),Id(concatMatrix)),[Id(row),BinaryOp(+,Id(col),IntLit(256)),Id(channel)]),ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)]))])])])])])])]))])])"
        self.assertTrue(TestAST.test(input,expect,345))
        

    def test_47 (self):
        input = """
        Class ElectricalDevice
        {
                Var weight: Float;
                Var useBattery: Boolean;
                Constructor()
                {}
                Constructor(weight: Float; useBat:Boolean)
                {
                    Self.weight = weight/100;
                    Self.useBattery = useBat;
                }
            }
            Class Laptop:Electrical
            {
                start()
                {
                    Laptop::$nothing();
                    Return useBattery;
                }
            }
        """
        expect = "Program([ClassDecl(Id(ElectricalDevice),[AttributeDecl(Instance,VarDecl(Id(weight),FloatType)),AttributeDecl(Instance,VarDecl(Id(useBattery),BoolType)),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(weight),FloatType),param(Id(useBat),BoolType)],Block([AssignStmt(FieldAccess(Self(),Id(weight)),BinaryOp(/,Id(weight),IntLit(100))),AssignStmt(FieldAccess(Self(),Id(useBattery)),Id(useBat))]))]),ClassDecl(Id(Laptop),Id(Electrical),[MethodDecl(Id(start),Instance,[],Block([Call(Id(Laptop),Id($nothing),[]),Return(Id(useBattery))]))])])"
        self.assertTrue(TestAST.test(input,expect,346))
        

    def test_48 (self):
        input = """
            Class Laptop:Electrical
            {
                start()
                {
                    Laptop::$nothing();
                    Return useBattery;
                }
            }""" 
        expect = """Program([ClassDecl(Id(Laptop),Id(Electrical),[MethodDecl(Id(start),Instance,[],Block([Call(Id(Laptop),Id($nothing),[]),Return(Id(useBattery))]))])])"""
        self.assertTrue(TestAST.test(input,expect,347))
        

    def test_49 (self):
        input = """
        Class Program 
        {
            Var _Fool: Float = 1.2e3;
            main()
            {
                
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(_Fool),FloatType,FloatLit(1200.0))),MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,348))
        

    def test_50 (self):
        input = """
        Class Program 
        {
            Var _Fool, _Magician: String = "Hello World", "I am '"Mr.Coren'"";
            main()
            {
                
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[AttributeDecl(Instance,VarDecl(Id(_Fool),StringType,StringLit(Hello World))),AttributeDecl(Instance,VarDecl(Id(_Magician),StringType,StringLit(I am '"Mr.Coren'"))),MethodDecl(Id(main),Static,[],Block([]))])])"""
        self.assertTrue(TestAST.test(input,expect,349))
        

    def test_51 (self):
        input = """
        Class Program
        {
            main()
            {
                Var a,b: Int = 0b11, 0B1001;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(3)),VarDecl(Id(b),IntType,IntLit(9))]))])])"""
        self.assertTrue(TestAST.test(input,expect,350))
        

    def test_52 (self):
        input = """
        Class TestHex
        {
            main()
            {
                Var a,b,c,d : Int = 00, 0, 0b0, 0x0;
            }
        }""" 
        expect = """Program([ClassDecl(Id(TestHex),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),VarDecl(Id(d),IntType,IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input,expect,351))
        

    def test_53 (self):
        input = """
        Class Program
        {
            main()
            {
                Var a,b,c,d : Int = 00, 0, 0b0, 0x0;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(0)),VarDecl(Id(b),IntType,IntLit(0)),VarDecl(Id(c),IntType,IntLit(0)),VarDecl(Id(d),IntType,IntLit(0))]))])])"""
        self.assertTrue(TestAST.test(input,expect,352))
        

    def test_54 (self):
        input = """
        Class Program
        {
            main()
            {
                Var a: Int = 0x234_F;
                Self.helloworld();
            }
            helloworld()
            {
                System.print("Hello world");
            }
        }
        """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType,IntLit(9039)),Call(Self(),Id(helloworld),[])])),MethodDecl(Id(helloworld),Instance,[],Block([Call(Id(System),Id(print),[StringLit(Hello world)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,353))
        

    def test_55 (self):
        input = """
        Class Test
        {
            main()
            {
                Var a: Int = 0x234_F;
                Self.helloworld();
            }
            helloworld()
            {
                System.print("Hello world");
            }
        }
        """ 
        expect = """Program([ClassDecl(Id(Test),[MethodDecl(Id(main),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(9039)),Call(Self(),Id(helloworld),[])])),MethodDecl(Id(helloworld),Instance,[],Block([Call(Id(System),Id(print),[StringLit(Hello world)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,354))
        

    def test_56 (self):
        input = """
        Class Program
        {
            main(a:Int; b:Float; c: String; e,f: Boolean)
            {
                Var a: Int = 0x234_F;
                Self.helloworld();
            }
            helloworld()
            {
                System.print("Hello world");
            }
        }
        """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType),param(Id(b),FloatType),param(Id(c),StringType),param(Id(e),BoolType),param(Id(f),BoolType)],Block([VarDecl(Id(a),IntType,IntLit(9039)),Call(Self(),Id(helloworld),[])])),MethodDecl(Id(helloworld),Instance,[],Block([Call(Id(System),Id(print),[StringLit(Hello world)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,355))
        

    def test_57 (self):
        input = """
        Class Program 
        {
            a() 
            {
                If (a == b) 
                {
                    Foreach (i In j .. b By a/2) 
                    {
                        b = b + 1;
                        c = b * a;
                        d = c / 2;
                        Self.print(d.foo().a.bar());
                    }
                } Elseif ((a < b) || (b < d) && (i == (j + 1))) 
                {
                    If (a == b) 
                    {
                        Self.print("Index out of bound");
                    } Else 
                    {
                        a[1][2][(b+1)] = c[(b+2)][(b*2)];
                    }
                } Else 
                {
                    Out.println("An error has occured");
                }
            }    
        }"""
        expect = "Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([If(BinaryOp(==,Id(a),Id(b)),Block([For(Id(i),Id(j),Id(b),BinaryOp(/,Id(a),IntLit(2)),Block([AssignStmt(Id(b),BinaryOp(+,Id(b),IntLit(1))),AssignStmt(Id(c),BinaryOp(*,Id(b),Id(a))),AssignStmt(Id(d),BinaryOp(/,Id(c),IntLit(2))),Call(Self(),Id(print),[CallExpr(FieldAccess(CallExpr(Id(d),Id(foo),[]),Id(a)),Id(bar),[])])])])]),If(BinaryOp(&&,BinaryOp(||,BinaryOp(<,Id(a),Id(b)),BinaryOp(<,Id(b),Id(d))),BinaryOp(==,Id(i),BinaryOp(+,Id(j),IntLit(1)))),Block([If(BinaryOp(==,Id(a),Id(b)),Block([Call(Self(),Id(print),[StringLit(Index out of bound)])]),Block([AssignStmt(ArrayCell(Id(a),[IntLit(1),IntLit(2),BinaryOp(+,Id(b),IntLit(1))]),ArrayCell(Id(c),[BinaryOp(+,Id(b),IntLit(2)),BinaryOp(*,Id(b),IntLit(2))]))]))]),Block([Call(Id(Out),Id(println),[StringLit(An error has occured)])])))]))])])"
        self.assertTrue(TestAST.test(input,expect,356))
        

    def test_58 (self):
        input = """
        Class Program
        {
            main ()
            {
                Var a: Array[Array[Array[Int,1],2],2] = Array(
                    Array(Array(1), Array(1)),
                    Array(Array(1), Array(1))
                );
            }
        }
        """ 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ArrayType(2,ArrayType(2,ArrayType(1,IntType))),[[[IntLit(1)],[IntLit(1)]],[[IntLit(1)],[IntLit(1)]]])]))])])"""
        self.assertTrue(TestAST.test(input,expect,357))
        

    def test_59 (self):
        input = """        
        Class Program 
        {
            main() 
            {
            Var a, b, c: Int;
            Val d, e, f: Float = 2.2, 3e3, 4.4e4;
            Var arr: Array[Int, 7];
                Return;
            }
        }"""
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType),ConstDecl(Id(d),FloatType,FloatLit(2.2)),ConstDecl(Id(e),FloatType,FloatLit(3000.0)),ConstDecl(Id(f),FloatType,FloatLit(44000.0)),VarDecl(Id(arr),ArrayType(7,IntType)),Return()]))])])"""
        self.assertTrue(TestAST.test(input,expect,358))
        

    def test_60 (self):
        input = """
        Class Program
        {
            addNewNode(newNode,head: Int)
            {
                newNode.next_node = head;
                head = new_node;
            }
            deleteNode(position,head: Int)
            {
                If(head == 0)
                {
                    head = head.next_node;
                }
                Else
                {
                    Var curr: Int = head.next.next;
                    Var prev: Int = curr;
                    Foreach(i In 2 .. position)
                    {
                        prev = curr;
                        curr = curr.next_node;
                    }
                    prev.next = curr;
                    head = prev;
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(addNewNode),Instance,[param(Id(newNode),IntType),param(Id(head),IntType)],Block([AssignStmt(FieldAccess(Id(newNode),Id(next_node)),Id(head)),AssignStmt(Id(head),Id(new_node))])),MethodDecl(Id(deleteNode),Instance,[param(Id(position),IntType),param(Id(head),IntType)],Block([If(BinaryOp(==,Id(head),IntLit(0)),Block([AssignStmt(Id(head),FieldAccess(Id(head),Id(next_node)))]),Block([VarDecl(Id(curr),IntType,FieldAccess(FieldAccess(Id(head),Id(next)),Id(next))),VarDecl(Id(prev),IntType,Id(curr)),For(Id(i),IntLit(2),Id(position),IntLit(1),Block([AssignStmt(Id(prev),Id(curr)),AssignStmt(Id(curr),FieldAccess(Id(curr),Id(next_node)))])]),AssignStmt(FieldAccess(Id(prev),Id(next)),Id(curr)),AssignStmt(Id(head),Id(prev))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,359))
        

    def test_61 (self):
        input = """
        Class LinkedList
        {
            LinkedList()
            {
                Self.value = 0;
                Self.next_node = Null;
            }
            LinkedList(new_value: Int; nextNode: Int)
            {
                Self.value = new_value;
                Self.next_node = nextNode;
            }
            Val value:Int;
            Val next_node: Boolean;
        }""" 
        expect = """Program([ClassDecl(Id(LinkedList),[MethodDecl(Id(LinkedList),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(value)),IntLit(0)),AssignStmt(FieldAccess(Self(),Id(next_node)),NullLiteral())])),MethodDecl(Id(LinkedList),Instance,[param(Id(new_value),IntType),param(Id(nextNode),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(value)),Id(new_value)),AssignStmt(FieldAccess(Self(),Id(next_node)),Id(nextNode))])),AttributeDecl(Instance,ConstDecl(Id(value),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(next_node),BoolType,None))])])"""
        self.assertTrue(TestAST.test(input,expect,360))
        

    def test_62 (self):
        input = """
        Class Program
        {
            main()
            {
                Var a,b: Shape;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(a),ClassType(Id(Shape)),NullLiteral()),VarDecl(Id(b),ClassType(Id(Shape)),NullLiteral())]))])])"""
        self.assertTrue(TestAST.test(input,expect,361))
        

    def test_63 (self):
        input = """
        Class Family
        {
            Val name, office: String;
            Val Age: Int;
            Val Income: Float;
            goOut()
            {
                System.print("Lets go out together");
                ## Family hang out ##
            }
        }""" 
        expect = """Program([ClassDecl(Id(Family),[AttributeDecl(Instance,ConstDecl(Id(name),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(office),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(Age),IntType,None)),AttributeDecl(Instance,ConstDecl(Id(Income),FloatType,None)),MethodDecl(Id(goOut),Instance,[],Block([Call(Id(System),Id(print),[StringLit(Lets go out together)])]))])])"""
        self.assertTrue(TestAST.test(input,expect,362))
        

    def test_64 (self):
        input = """
        Class Animal
        {
            Var isFeed: Boolean;
            Var weight, height: Float;
            Val Name: String;
            feeding()
            {
                Self.isFeed = True;
            }
            getPrice()
            {
                Return 100_56_16 * Self.weight * Self.height;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Animal),[AttributeDecl(Instance,VarDecl(Id(isFeed),BoolType)),AttributeDecl(Instance,VarDecl(Id(weight),FloatType)),AttributeDecl(Instance,VarDecl(Id(height),FloatType)),AttributeDecl(Instance,ConstDecl(Id(Name),StringType,None)),MethodDecl(Id(feeding),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(isFeed)),BooleanLit(True))])),MethodDecl(Id(getPrice),Instance,[],Block([Return(BinaryOp(*,BinaryOp(*,IntLit(1005616),FieldAccess(Self(),Id(weight))),FieldAccess(Self(),Id(height))))]))])])"""
        self.assertTrue(TestAST.test(input,expect,363))
        

    def test_65 (self):
        input = """
        Class Zoo
        {
            Var $listAnimal : Array[Animal, 0b111111011];
            Var $maxSize : Int;
            Constructor()
            {
                Self::$maxSize = 1;
            }
            addAnimal(newAnimal: Animal)
            {
                Self.listAnimal[Self::$maxSize] = newAnimal;
                Self::$maxSize = Self::$maxSize + 1;
            }
        }""" 
        expect = """Program([ClassDecl(Id(Zoo),[AttributeDecl(Static,VarDecl(Id($listAnimal),ArrayType(507,ClassType(Id(Animal))))),AttributeDecl(Static,VarDecl(Id($maxSize),IntType)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id($maxSize)),IntLit(1))])),MethodDecl(Id(addAnimal),Instance,[param(Id(newAnimal),ClassType(Id(Animal)))],Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(listAnimal)),[FieldAccess(Self(),Id($maxSize))]),Id(newAnimal)),AssignStmt(FieldAccess(Self(),Id($maxSize)),BinaryOp(+,FieldAccess(Self(),Id($maxSize)),IntLit(1)))]))])])"""
        self.assertTrue(TestAST.test(input,expect,364))
        

    def test_66 (self):
        input = """
        Class Bird: Animal
        {
            Var WingsLength : Float;
            Val Color: String;
            demonstrate()
            {
                Val myString: String = "This is: ";
                Val printedSentence : String = myString +. Self.name;
                System.print();
            }
        }""" 
        expect = """Program([ClassDecl(Id(Bird),Id(Animal),[AttributeDecl(Instance,VarDecl(Id(WingsLength),FloatType)),AttributeDecl(Instance,ConstDecl(Id(Color),StringType,None)),MethodDecl(Id(demonstrate),Instance,[],Block([ConstDecl(Id(myString),StringType,StringLit(This is: )),ConstDecl(Id(printedSentence),StringType,BinaryOp(+.,Id(myString),FieldAccess(Self(),Id(name)))),Call(Id(System),Id(print),[])]))])])"""
        self.assertTrue(TestAST.test(input,expect,365))
        

    def test_67 (self):
        input = """
        Class Program
        {
            main()
            {
                Val s1: String = "Hello \\n";
                Var s2: String = "World \\n";
                If(s1 ==. s2)
                {
                    System.print("You are right");
                }
                Else
                {
                    System.print("Noooo");
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(s1),StringType,StringLit(Hello \\n)),VarDecl(Id(s2),StringType,StringLit(World \\n)),If(BinaryOp(==.,Id(s1),Id(s2)),Block([Call(Id(System),Id(print),[StringLit(You are right)])]),Block([Call(Id(System),Id(print),[StringLit(Noooo)])]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,366))
        

    def test_68 (self):
        input = """
        Class Student
        {
            ## This a a comment here##
            Val name, major: String;
            Var grade : Float;
            classifyStudent()
            {
                If (Self.grade <= 5.e0)
                {
                    Return "So so";
                }
                Elseif ((Self.grade > 5) && (Self.grade <= 8))
                {
                    Return "Good";
                }
                Else
                {
                    Return "Excellent";
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(Student),[AttributeDecl(Instance,ConstDecl(Id(name),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(major),StringType,None)),AttributeDecl(Instance,VarDecl(Id(grade),FloatType)),MethodDecl(Id(classifyStudent),Instance,[],Block([If(BinaryOp(<=,FieldAccess(Self(),Id(grade)),FloatLit(5.0)),Block([Return(StringLit(So so))]),If(BinaryOp(&&,BinaryOp(>,FieldAccess(Self(),Id(grade)),IntLit(5)),BinaryOp(<=,FieldAccess(Self(),Id(grade)),IntLit(8))),Block([Return(StringLit(Good))]),Block([Return(StringLit(Excellent))])))]))])])"""
        self.assertTrue(TestAST.test(input,expect,367))
        

    def test_69 (self):
        input = """
        Class University
        {
            Val name: String;
            Var $highestScore : Float = 0;
            Var Score: Float;
            Constructor(newName : String; newScore: String)
            {
                Self.name = newName;
                Self.score = newScore;
                If(University::$highestScore < newScore)
                {
                    Unisersity::$highestScore = newScore;
                }
            }
        }""" 
        expect = """Program([ClassDecl(Id(University),[AttributeDecl(Instance,ConstDecl(Id(name),StringType,None)),AttributeDecl(Static,VarDecl(Id($highestScore),FloatType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(Score),FloatType)),MethodDecl(Id(Constructor),Instance,[param(Id(newName),StringType),param(Id(newScore),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(name)),Id(newName)),AssignStmt(FieldAccess(Self(),Id(score)),Id(newScore)),If(BinaryOp(<,FieldAccess(Id(University),Id($highestScore)),Id(newScore)),Block([AssignStmt(FieldAccess(Id(Unisersity),Id($highestScore)),Id(newScore))]))]))])])"""
        self.assertTrue(TestAST.test(input,expect,368))
        

    def test_70 (self):
        input = """
        Class Image
        {
            Var width, height: Int;
            Var matrix: Array[Array[Array[Int, 3], 256], 256];
            Constructor()
            {
            }
            foo()
            {
                x = a + b
            }
        }
        """
        expect = "Program([ClassDecl(Id(Image),[AttributeDecl(Instance,VarDecl(Id(width),IntType)),AttributeDecl(Instance,VarDecl(Id(height),IntType)),AttributeDecl(Instance,VarDecl(Id(matrix),ArrayType(256,ArrayType(256,ArrayType(3,IntType))))),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(x),BinaryOp(+,Id(a),Id(b)))]))])])"
        self.assertTrue(TestAST.test(input,expect,369))
        

    # def test_71 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,370))
        

    # def test_72 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,371))
        

    # def test_73 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,372))
        

    # def test_74 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,373))
        

    # def test_75 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,374))
        

    # def test_76 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,375))
        

    # def test_77 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,376))
        

    # def test_78 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,377))
        

    # def test_79 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,378))
        

    # def test_80 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,379))
        

    # def test_81 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,380))
        

    # def test_82 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,381))
        

    # def test_83 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,382))
        

    # def test_84 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,383))
        

    # def test_85 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,384))
        

    # def test_86 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,385))
        

    # def test_87 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,386))
        

    # def test_88 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,387))
        

    # def test_89 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,388))
        

    # def test_90 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,389))
        

    # def test_91 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,390))
        

    # def test_92 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,391))
        

    # def test_93 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,392))
        

    # def test_94 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,393))
        

    # def test_95 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,394))
        

    # def test_96 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,395))
        

    # def test_97 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,396))
        

    # def test_98 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,397))
        

    # def test_99 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,398))
   
    # def test_100 (self):
    #     input = """""" 
    #     expect = """"""
    #     self.assertTrue(TestAST.test(input,expect,399))