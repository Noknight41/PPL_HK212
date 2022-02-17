import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
#     def test_bkel_1_301(self):
#         input = """Class main{}"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,301))

#     def test_bkel_2_302(self):
#         input = """
#     Class Rectangle: Shape {
#         getArea() {
#             Return Self.length * Self.width;
#         }
#     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,302))

#     def test_bkel_3_303(self):
#         input = """
#     Class Shape {
#         $getNumOfShape( {
#             Return Self.length * Self.width;
#         }
#     }
#         """
#         expect = "Error on line 3 col 24: {"
#         self.assertTrue(TestParser.test(input, expect,303))

#     def test_304(self):
#         input = """abc = 1;"""
#         expect = "Error on line 1 col 0: abc"
#         self.assertTrue(TestParser.test(input, expect,304))
    
#     # Test with normal class declaration and comment
#     def test_305(self):
#         input = """
#     Class Shape: Rectangle {
#         ##
#         This part should be ignored, just to check, nothing to comment
#         ##
#         $getSomething(yes: Int){
#             Var x : Int = 0;
#             Self.x = 1;
#             Return x;
#         }
#     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect,305))

#     # Test with equal number of variable and value
#     def test_306(self):
#         input = """
#     Class Rectangle: Shape{
#         ##
#         Get area of a Rectangle
#         ##
#         Val length, width, k: Float = 20.3, 10.1, 1.2;
#         getArea(){
#             Val area: Float = length*width*k;
#             Return area;
#         }
#     }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 306))

#     # Test with unequal number of variable and value
#     def test_307(self):
#         input = """
#     Class Rectangle: Shape{
#         ##
#         Get area of a Rectangle
#         ##
#         Val length, width: Float = 20.31, 1.2, 3.E-8;
#         getArea(){
#             Val area: Float = length*width;
#             Return area;
#         }
#     }
#         """
#         expect = "Error on line 6 col 45: ,"
#         self.assertTrue(TestParser.test(input, expect, 307))

#     # Test case with 1 class, comment and array declaration
#     def test_308(self):
#         input = """
#         Class Rectangle: Shape{
#             ## Var somewhat: Int = 2;##
#             Val myArray: Array[Float, 3];
#                 getArray(){
#                     Return myArray;
#             }
#         }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 308))
    
    # Testcase from Justince, original version
    # def test_309(self):
    #     input = """
    #     Class Trt{
    #         Var a: String;
    #         Constructor(x: String){
    #             Self.a = x;
    #         }
    #         Despacito(){
    #             Return Self.a +. "2";
    #         }
    #     }
    #     Class Shape {
    #         Var flag: Trt = Null;
    #         Var x, y : Int;
    #         Constructor(a,b: Int; d: String){
    #             flag = New Trt(d);
    #             Var s: String = flag.Despacito();
    #             Self.x = b;
    #             Self.y = a;
    #             If(d ==. "Hel"){
    #                 Self.x = a;
    #                 Self.y = b;
    #             }
    #         }
    #         Destructor(){
    #             a.print(no);
    #         }
    #     }
    #     Class Program {
    #         ## Muda
    #         Muda ##
    #         Var hello: Array[Int, 5];
    #         Var length, width: Int;
    #         Var flag2: Shape = New Shape(1,2,"Help");
    #         main(){
    #             Self.print(flag2.flag.Despacito());
    #             flag2.flag.a = "s";
    #             a = 1.0;
    #         }
    #     }"""
    #     expect = """successful"""
    #     self.assertTrue(TestParser.test(input, expect,309))

#     # Testcase from Justince, complicated with declaration
#     def test_310(self):
#         input = """
#     Class Trt{
#         Var $a: String;
#         Val $a, b: Int;
#         Var a: Int = 10;
#         Val b, c: Float = 1.5, 3.E8;
#         Var x, y, z: Shape = Null, what, ok;
#         Constructor(x, y: String; z: Int){
#             Var s: Int = 1;
#             Self.a = x;
#         }
#         Despacito(){
#             Var b: String = a.foo().a.foo();
#             Var c: Int = flag.foo;
#             Var d: Float = flag.otherflag.foo();
#             Return Self.a +. "2";
#         }
#     }
#     Class Shape {
#         Var flag: Trt = Null;
#         Var x, y : Int;
#         Constructor(a,b: Int; d: String){
#             flag = New Trt(d);
#             Var s: String = flag.Despacito();
#             Self.x = b;
#             Self.y = a;
#             If(d ==. "Hel"){
#                 Self.x = a;
#                 Self.y = b;
#             }
#         }
#         Destructor(){
#             Self.print("No service");
#         }
#     }
#     Class Program {
#         ## Muda
#         Muda ##
#         Var hello,hello2: Array[Int, 5], Array[Float, 2];
#         Var length, width: Int;
#         Var flag2: Shape = New Shape(1,2,"Help");
#         main(){
#             Self.print(flag2.flag.Despacito());
#             flag2.flag.a = "s";
#             doSomething = m1.a.b().c.d.e.f.g().c[5];
#             a = 1.0;
#         }
#     }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect,310))
#     # Test a program with literal declaration
#     def test_311(self):
#         input = """
#         Class Shape: Rectangle {
#             ##
#             This part should be ignored, just to check, nothing to comment
#             ##
#             $getSomething(yes: Int){
#                 Var x : Float = 12.001;
#                 Var t : Int = 0;
#                 Var varvar: Int = 01_0;
#                 Var y : Float = 0.e1; 
#                 Var z : Float = 1.E23; 
#                 Return x;
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,311))

#     # Test a program with 3 classes and some invocation
#     def test_312(self):
#         input = """
#         Class Shape{
#             Var height, length: Float;
#         }
        
#         Class Rectangle: Shape {
#             $getArea() {
#                 Return Self.height * Self.height;
#             }
#         }
        
#         Class Program {
#             main(){
#                 Out.printInt(Rectangle::$getArea());
#             }
#         }
#         """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input,expect,312))
#     # Test a program with only an unclosed string --> Raise error and print only the string content
#     def test_313(self):
#         input = """ 
#             "Hello
#         """
#         expect = """Hello
# """
#         self.assertTrue(TestParser.test(input,expect,313))
#     def test_314(self):
#         input = """
#     Class StringWorker{
#         getString(someString, anotherString: String){
#             Val someString: String = "hello PPL";
#             Return someString;
#         }
#     }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input,expect,314))

#     # Test from d96 spec pdf
#     def test_315(self):
#         input = """
#         Class Shape {
#             Val $numOfShape: Int = 0;
#             Val immutableAttribute: Int = 0;
#             Var length, width: Int;

#             $getNumOfShape() {
#                 Val temp: Int = 5;
#                 Return $numOfShape;
#             }
#         }

#         Class Rectangle: Shape {
#             getArea() {
#                 Return Self.length * Self.width;
#             }
#         }

#         Class Program {
#             main() {
#                 Out.printInt(Shape::$numOfShape);
#             }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input,expect,315))
    
#     # Test case for Foreach - In loop
#     def test_316(self):
#         input = """
#         Class Program {
#             main() {
#                 Foreach(x In 100 .. 300 By 5){
#                     Out.printInt(x % 10);
#                 }
#                 Foreach(y In 300 .. -0 By -2){
#                     Self::$doNothing = 1;
#                     a::$doNothing();
#                     Foreach(z In -1 .. 50000000){
#                         Out.print("Hello world");
#                     }
#                 }
#             }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input, expect, 316))

#     def test_317(self):
#         input = """
#         Class Program {
#             main() {
#                 Val $invalid_value: Int = 100000000; ## Some error should occur here ##
#                 Return $invalid_value;
#             }
#         }
#         """
#         expect = """Error on line 4 col 20: $invalid_value"""
#         self.assertTrue(TestParser.test(input,expect,317))

#     def test_318(self):
#         input = """
#         Class Program {
#             Var $sus_value: String = "This value is sus!"; ## Susssssss ##
#             main() {
#                 Val valid_value: Int = 100000000;
#                 valid_value.b.c.d() = Program::$a.b.c().d.e.Self.x::$f()::g.h::$i().j + 1;
#                 Return (valid_value - Self::$sus_value + Self.what - Program::$a.b.c(Program::$a.b).d.e.Self.x::$f()::$g.h::$i().j);
#             }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input,expect,318))

#     def test_319(self):
#         input = """
#         Class Program {
#             Var a: Int;
#             main() {
#                 Val valid_value: Float = 0.5;
#                 Self::$a = Program::a::b.c();
#                 Return Program::a.b.c;
#             }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input,expect,319))

#     def test_320(self):
#         input = """"""
#         expect = """Error on line 1 col 0: <EOF>"""
#         self.assertTrue(TestParser.test(input,expect,320))
    
#     # This test-case should return some errors
#     def test_321(self):
#         input = """
#         Class Program {
#             Var a: Array[Array[Int, 5], 5];
#             main() {
#                 Val valid_value: Float = 0.5;
#                 Self::$a = Program::a::b.c();
#                 Return Program::a.b.c;
#             }
#         }
#         """
#         expect = """successful"""
#         self.assertTrue(TestParser.test(input,expect, 321))

#     def test_322(self):
#         input = """
#         Class Rectangle: Shape{
#             Val myArray: Array[Float, 3];
#                 getArray(){
#                     a = a.1;
#                     Return myArray;
#             }
#         }
#             """
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 322))

#     def test_array_323(self):
#         input = """
#         Class Program {
#             main() {
#                 Val a : Array[Array[Int, 10], 0x15];
#                 Return;
#             }
#         }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 323))

#     def test_static_param_324(self):
#         """Static param are not allowed"""
#         input = """
#             Class Program {
#                 main($a : Int) {
#             }
#         }"""
#         expect = "Error on line 3 col 21: $a"
#         self.assertTrue(TestParser.test(input, expect, 324))

#     def test_325(self):
#         """ Test unequal variable and value"""
#         input = """
#         Class Rectangle: Shape{
#             Val length, width: Int = 1, 2;
#             doSomething(){
#                 Val a, b, c: Int = 1; ##Error goes here##
#             }
#         }
#             """
#         expect = "Error on line 5 col 36: ;"
#         self.assertTrue(TestParser.test(input, expect, 325))

    # def test_2(self):
    #     input = """ """
    #     expect = """ """
    #     self.assertTrue(TestParser.test(input,expect,2))

    def test_simple_program(self):
        """Simple program: Class Program {
            main() {}
        } """
        input = """Class Program {
            main() {Return;}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 301))

    def test_more_complex_program(self):
        """More complex program"""
        input = """Class Program {
            main() {
                putStrLn(4);
                putStrLn(5);
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 302))

    def test_wrong_miss_close(self):
        """Miss ) int main( {}"""
        input = """Class Program {
            main( {}
        }"""
        expect = "Error on line 2 col 18: {"
        self.assertTrue(TestParser.test(input, expect, 303))

    def test_if_statement(self):
        """If (a == 3) { putIntLn(4); }"""
        input = """Class Program {
            main() {
                If (a == 3) {
                    putStrLn(4);
                }
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 304))

    def test_nested_if_statement(self):
        """Nested if"""
        input = """Class Program {
            main() {
                If (a == 3) {
                    putIntLn(4);
                    If (b == 4) {
                        putStrLn(4);
                        putStrLn(5);
                    }
                    If ((a == 3) && (b == 4)) {
                        putIntLn(4);
                    }
                    If ((a == 3) || (b == 4)) {
                        putIntLn(5);
                    }
                    If (!(a == 3) && (b != 4)) {
                        putIntLn(4);
                        If ((a > 3) || (b <= 4)) {
                            putIntLn(5);
                        }
                    }
                }
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 305))

    def test_simple_program_1(self):
        """test Class Program {main(){}} Class Rectangle {}"""
        input = """Class Program {main(){Return;}} Class Rectangle {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 306))

    def test_simple_program_2(self):
        """test Class Rectangle {} Class Program{main(){}}"""
        input = """Class Rectangle {} Class Program{main(){Return;}}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 307))

    def test_simple_program_3(self):
        """test Class Rectangle {} Class Program{main(){}} Class SomethingElse {}"""
        input = """Class Rectangle {} Class Program{main(){Return;}} Class SomethingElse {}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 308))

    def test_no_program_class(self):
        """test Class Shape{} Class Circle{}"""
        input = """Class Shape{} Class Circle{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 309))

    def test_simple_program_4(self):
        """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d : Float = 1.0, 2e10;

            main() {
                Out.println(4);
            }
        }"""
        input = """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d : Float = 1.0, 2e10;

            main() {
                Out.println(4);
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 310))

    def test_wrong_attr_declaration_1(self):
        """Class Program {
            Val a : Int, b : String;

            main() {
                Out.println(4);
            }
        }"""
        input = """Class Program {
            Val a : Int, b : String;

            main() {
                Out.println(4);
                Return;
            }
        }"""
        expect = "Error on line 2 col 23: ,"
        self.assertTrue(TestParser.test(input, expect, 311))

    def test_simple_program_5(self):
        """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d : Float = 1.0, 2e10;
            Val a, b : Int;
            Var $a : Float;

            main() {
                Out.println(4);
            }
        }
        """
        input = """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d : Float = 1.0, 2e10;
            Val a, b : Int;
            Var $a : Float;

            main() {
                Out.println(4);
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 312))

        # Weird test?
#     def test_complex_program_1(self):
#         """test complex program 1"""
#         input = """Class TestNameNodeMetrics {
#   Val CONF : Int = New HdfsConfiguration();
#   Var $DFS_REDUNDANCY_INTERVAL : Int = 1;
#   Val $TEST_ROOT_DIR_PATH : String = New Path("/testNameNodeMetrics");
#   Val NN_METRICS : String = "NameNodeActivity";
#   Var BLOCK_SIZE : Float = 1024e10 * 1024.05;

#   ##
#   Number of datanodes in the cluster
#   ##
#   Var $DATANODE_COUNT : Int = EC_POLICY.getNumDataUnits() + EC_POLICY.getNumParityUnits() + 1;

#   Val cluster : Int;
#   Val fs : String;

#    getTestPath(fileName : String) {
#     Return New Path(TEST_ROOT_DIR_PATH, fileName);
#   }

#   setUp(a : Int; b : Float) {
#     cluster.waitActive();
#     a.someFunc();
#     fs.enableErasureCodingPolicy(EC_POLICY.getName());
#     ecDir = a.getTestPath("/ec");
#     fs.setErasureCodingPolicy(ecDir, EC_POLICY.getName());
#   }

#   tearDown() {
#     Val source : Float = DefaultMetricsSystem.instance();
#     If (source != Null) {
#       ##
#       Run only once since the UGI metrics is cleaned up during teardown
#       ##
#       a.assertQuantileGauges("GetGroups1s", rb);
#     }
#     If (hostsFileWriter != Null) {
#         Self.something = 5;
#       hostsFileWriter.cleanup();
#       hostsFileWriter = Null;
#     }
#     If (cluster != Null) {
#       cluster.shutdown();
#       cluster = Null;
#     }

#     Val includeHosts : Array[Int, 100] = New StringBuilder(dnAddresses.length - 1);
#     Foreach (i In 1 .. 100 By 1) {
#         ##
#         Before, we write includeHosts[i] = dnAddresses[(i + 1)];
#         However, the priority is that [] is higher than +, therefore, in order to have +
#         execute first, we must encapsulate into the ()
#         ##
#       includeHosts[i] = dnAddresses[(i + 1)];
#     }
#   }
# }

# Class Program {
#   main() {
#     Out.println("Hello World");
#     Return;
#   }
# }"""
#         expect = "successful"
#         self.assertTrue(TestParser.test(input, expect, 313))

    def test_simple_program_6(self):
        """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d : Float = 1.0, 2e10;
            Val a, b : Int;
            Var $a : Float;

            main() {
                Out.println(4);
            }
        }
        """
        input = """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d : Float = 1.0, 2e10;
            Val a, b : Int;
            Var $a : Float;

            main() {
                Out.println(4);
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 355))

    def test_simple_program_7(self):
        """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d : Float = 1.0, 2e10;
            Val a, b : Int;
            Var $a : Float;

            getArea(w : Int; h : Float; a : String) {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }

            $something(w : Int) {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }

            Something() {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }

            main() {
                Out.println(4);
            }
        }
        """
        input = """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d : Float = 1.0, 2e10;
            Val a, b : Int;
            Var $a : Float;

            getArea(w : Int; h : Float; a : String) {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }

            $something(w : Int) {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }

            Something() {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }

            main() {
                Out.println(4);
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 314))

    def test_simple_program_8(self):
        """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var c, $d : Float = 1.0, 2e10;

            Int Something() {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }

            main() {
                Out.println(4);
            }
        }
        Class Shape {
            Val a, b : Int;
            Var $a : Float;

            Boolean getArea(w : Int; h : Float; a : String) {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }

            String $something(w : Int) {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }
        }
        """
        input = """Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var c, $d : Float = 1.0, 2e10;

            Something() {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }

            main() {
                Out.println(4);
                Return;
            }
        }
        Class Shape {
            Val a, b : Int;
            Var $a : Float;

            getArea(w : Int; h : Float; a : String) {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }

            $something(w : Int) {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var $c, d : Float = 1.0, 2e10;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 315))

    def test_simple_program_9(self):
        """Class Program {
            main() {
            }
        }
        Class Shape {
        }
        Class Rectangle : Shape {
            Val a : Int = 1;
        }
        """
        input = """Class Program {
            main() {
                Return;
            }
        }
        Class Shape {
        }
        Class Rectangle : Shape {
            Val a : Int = 1;
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 316))

    def test_simple_program_10(self):
        """
        Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            Var d: Array[Float, 100];
            Var $c, $d, $e: Array[Boolean, 6];
            main() {
               Out.println(4);
            }
        }
        """
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            Var d: Array[Float, 100];
            Var $c, $d, $e: Array[Boolean, 6];
            main() {
               Out.println(4);
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 317))

    def test_simple_program_11(self):
        """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            Var $a, $b: Array[Array[Int, 10], 0x15];
            main() {
               Out.println(4);
            }
        }
        """
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            Var $a, $b: Array[Array[Int, 10], 0x15];
            main() {
               Out.println(4);
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 318))

    def test_simple_program_12(self):
        """statements inside function, assignments only"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               d = "Something";
               c = 1e15;
               d = 0x1637_ABCB;
               e = True;
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 319))

    def test_simple_program_13(self):
        """statements inside function, assign Array"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            Var c: Array[Int, 10] = Array(1, 2, 3, 4, 5);
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));
               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 320))

    def test_simple_program_14(self):
        """statements inside function, assign identifiers to identifiers"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));
               f = e;
               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 321))

    def test_simple_program_15(self):
        """statements inside function, operator in action"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));

               c = a + b;
               c = a +. b ==. c;
               c = ((a - b) * (c / d)) + (e + f) % 5;
               c = d = e = f;
               c = d = 4;

               d = "Something";
               Return;
            }
        }
        """
        expect = "Error on line 12 col 26: ==."
        self.assertTrue(TestParser.test(input, expect, 322))

    def test_simple_program_16(self):
        """statements inside function"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6)) + Array(1, 2, 3);

               c = a + b;
               c = (a +. b) ==. c;
               d = f.callFunc() - g::$something(a, b);
               e = g::$somethingElse;
               f = g.someValue();

               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 323))

    def test_simple_program_17(self):
        """statements inside function"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));
               f.callFunc();
               callSomething();

               c = a + b;
               c = a +. (b ==. c);
               d = f.callFunc() - g::$something(a, b);
               e = g::$somethingElse;
               f = g.someValue();

               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 324))

    def test_simple_program_18(self):
        """statements inside function"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));
               f.callFunc();
               callSomething();

               c = a + b;
               c = (a +. b) ==. c;
               Val d: Int = f.callFunc() - g::$something(a, b);
               e = g::$somethingElse;
               f = g.someValue();
               Val abc: String = f.something();
               Var c: Float = ((a - b) * (c / d)) + (e + f) % 5;

               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 325))

    def test_simple_program_19(self):
        """statements inside function"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1 + 2, 2 * 5, 3), Array(4, 5, 6));
               f.callFunc();
               callSomething();

               c = a + b;
               c = (a > b) < c;
               Val d: Int = f.callFunc() - g::$something(a, b);
               e = g::$somethingElse;
               f = g.someValue();
               Val abc: String = f.something();
               Var c: Float = ((a - b) * (c / d)) + (e + f) % 5;

               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 326))

    def test_simple_program_20(self):
        """Class Program {
            main() {
            }
        }
        Class Shape {
        }
        Class Rectangle : Shape {
            Int something() {
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
            }
        }
        """
        input = """Class Program {
            main() {
                Return;
            }
        }
        Class Shape {
        }
        Class Rectangle : Shape {
            something() {
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 327))

    def test_simple_program_21(self):
        """testing constructor and destructor"""
        input = """
            Class TestBird {
                Constructor(w: Int; s: Float; a: String; b: Array[Int, 5]; c: Boolean) {
                    Var a : Int = 1;
                    Var $a, $c : Boolean = True, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                    Return;
                }

                Destructor() {
                    Var a : Int = 1;
                    Var $a, $c : Boolean = True, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                }

                Yell(w: Int; h: Float) {
                    Var myBird : Bird = New Bird();

                    myBird.label();
                    myBird.move();
                    myBird.eat();
                }
            }

            Class Program {
                main() {
                    Val myFish : Fish = New Fish();

                    myFish.label();
                    myFish.move();
                    myFish.eat();
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 328))

    def test_simple_program_22(self):
        """test list of expression in params of function calling"""
        input = """
            Class TestBird {
                Constructor(w: Int; s: Float; a: String; b: Array[Int, 5]; c: Boolean) {
                    Var a : Int = 1;
                    Var $a, $c : Boolean = True, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                    Return;
                }

                Destructor() {
                    Var a : Int = 1;
                    Var $a, $c : Boolean = True, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function((a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1)) * f.a - f::$b;
                }

                Yell(w: Int; h: Float) {
                    Var myBird : Bird = New Bird();

                    myBird.label();
                    myBird.move();
                    myBird.eat();
                }
            }

            Class Program {
                main() {
                    Val myFish : Fish = New Fish(1, 2, (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1));

                    myFish.label();
                    myFish.move();
                    myFish.eat();
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 329))

    def test_simple_program_23(self):
        """test Self keyword"""
        input = """
            Class TestBird {
                Constructor(w: Int; s: Float; a: String; b: Array[Int, 5]; c: Boolean) {
                    Var a : Int = 1;
                    Var $a, $c : Boolean = True, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                    Return;
                }

                Destructor() {
                    Var a : Int = 1;
                    Var $a, $c : Boolean = True, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function((a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1)) * f.a - f::$b;
                }

                Yell(w: Int; h: Float) {
                    Self.calling();
                    a = 10;
                }
            }

            Class Program {
                main() {
                    Val myFish : Fish = New Fish(1, 2, (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1));

                    myFish.label();
                    myFish.move();
                    myFish.eat();
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 330))

    def test_simple_program_24(self):
        """testing constructor no params and destructor"""
        input = """
            Class TestBird {
                Constructor() {
                    Var a : Int = 1;
                    Var $a, $c : Boolean = True, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                    Return;
                }

                Destructor() {
                    Var a : Int = 1;
                    Var $a, $c : Boolean = True, False;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                }

                Yell(w: Int; h: Float) {
                    Var myBird : Bird = New Bird();

                    myBird.label();
                    myBird.move();
                    myBird.eat();
                }
            }

            Class Program {
                main() {
                    Val myFish : Fish = New Fish();

                    myFish.label();
                    myFish.move();
                    myFish.eat();
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 331))

    # this one has chaining rule of instance method invocation: a.b().c()
    def test_complex_program_2(self):
        """test complex program 2"""
        input = """Class TestNameNodeMetrics {
  Val CONF : Int = New HdfsConfiguration();
  Var $DFS_REDUNDANCY_INTERVAL : Int = 1;
  Val $TEST_ROOT_DIR_PATH : String = New Path("/testNameNodeMetrics");
  Val NN_METRICS : String = "NameNodeActivity";
  Var BLOCK_SIZE : Float = 1024e10 * 1024.05;

  ##
  Number of datanodes in the cluster
  ##
  Var $DATANODE_COUNT : Int = EC_POLICY.getNumDataUnits() + EC_POLICY.getNumParityUnits() + 1;

  Val cluster : Int;
  Val fs : String;

  getTestPath(fileName : String) {
    Return New Path(TEST_ROOT_DIR_PATH, fileName);
  }

  setUp(a : Int; b : Float) {
    cluster.waitActive();
    someFunc();
    fs.enableErasureCodingPolicy(EC_POLICY.getName());
    ecDir = getTestPath("/ec");
    fs.setErasureCodingPolicy(ecDir, EC_POLICY.getName());
  }

  tearDown() {
    Val source : Float = DefaultMetricsSystem.instance().getSource("UgiMetrics");
    If (source != Null) {
      ##
      Run only once since the UGI metrics is cleaned up during teardown
      ##
      assertQuantileGauges("GetGroups1s", rb);
    }
    If (hostsFileWriter != Null) {
      hostsFileWriter.cleanup();
      hostsFileWriter = Null;
    }
    If (cluster != Null) {
      cluster.shutdown();
      cluster = Null;
    }

    Val includeHosts : Array[Int, 100] = New StringBuilder(dnAddresses.length - 1);
    Foreach (i In 1 .. 100 By 1) {
      includeHosts[i] = dnAddresses[(i + 1)];
    }
  }
}

Class Program {
  main() {
    Out.println("Hello World");
  }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 332))

    def test_simple_program_25(self):
        """testing function with return statement"""
        input = """
            Class Rectangle: Shape {
                getArea() {
                    Return Self.length * Self.width;
                }
            }

            Class Program {
                main() {
                    Val myFish : Fish = New Fish();

                    myFish.label();
                    myFish.move();
                    myFish.eat();
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 333))

    def test_simple_program_26(self):
        """testing function with return statement"""
        input = """
            Class Shape {
                $getNumOfShape( {
                    Return Self.length * Self.width;
                }
            }

            Class Program {
                main() {
                    Val myFish : Fish = New Fish();

                    myFish.label();
                    myFish.move();
                    myFish.eat();
                    Return;
                }
            }
        """
        expect = "Error on line 3 col 32: {"
        self.assertTrue(TestParser.test(input, expect, 334))

    def test_simple_program_27(self):
        """testing function with return statement"""
        input = """
            Class Shape {
                $getNumOfShape() {
                    Return Self.length * Self.width;
                }
            }

            Class Program {
                main() {
                    Val myFish : Fish = New Fish();

                    myFish.label();
                    myFish.move();
                    myFish.eat();
                    {
                        Var r, s: Int;
                        r = 2.0;
                        Var a, b: Array[Int, 5];
                        s = r * r * Self.myPI;
                        a[0] = s;
                    }
                    Return;
                }
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 335))

    def test_simple_program_28(self):
        """test matrix multiplication, multiple dim index access"""
        input = """
Class Program {
   main() {
    Val row1, col1, row2, col2 : Int;
    Val s : Scanner = New Scanner(System.in);
    Out.print("Enter number of rows in first matrix:");
    row1 = s.nextInt();
    Out.print("Enter number of columns in first matrix:");
    col1 = s.nextInt();
    Out.print("Enter number of rows in second matrix:");
    row2 = s.nextInt();
    Out.print("Enter number of columns in second matrix:");
    col2 = s.nextInt();

    If (col1 != row2) {
        Out.println("Matrix multiplication is not possible");
    }
    Else {
        Var a : Array[Array[Int, 100], 100];
        Var b : Array[Array[Int, 100], 100];
        Var c : Array[Array[Int, 100], 100];

        Out.println("Enter values for matrix A : \\n");
        Foreach (i In 0 .. row1 By 1) {
            Foreach (j In 0 .. col1) {
                 a[i][j] = s.nextInt();
            }
        }
        Out.println("Enter values for matrix B : \\n");
        Foreach (i In 0 .. row2 By 1) {
            Foreach (j In 0 .. col2) {
                b[i][j] = s.nextInt();
            }
        }

        Out.println("Matrix multiplication is : \\n");
        Foreach (i In 0 .. rows1 By 1) {
            Foreach (j In 0 .. col2 By (0 + 1) * 2 - 1) {
              c[i][j]=0;
              Foreach (k In 0 .. col1 By 1) {
                c[i][j] = c[i][j] + a[i][k] * b[k][j];
              }
              c = a + b > c + d;
              Out.print(c[i][j] +. " ");
            }
            Out.println();
        }
    }
    Return;
  }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 336))

    def test_simple_program_29(self):
        """constructor must have a return statement"""
        input = """
        Class Map {
            Val key: Array[String, 10];
            Val value: Array[String, 10];
            Constructor(key: Array[String, 10]; value: Array[String, 10]) {
                Self.key = key;
                Self.value = value;
                Return;
            }
            Destructor() {
                Self.clean(Self.key);
                Self.clean(Self.value);
            }
            clean() {
                Out.println("Cleaning");
                Foreach (k In 0 .. Self.key.length() By 1)
                {
                    el = Self.key[k];

                    free(el);
                    Self.key = Null;
                }
                free(key);
                Self.key = Null;
                Foreach (v In 0 .. Self.value.length() By 1)
                {
                    el = Self.value.a[v];

                    free(el);
                    Self.value = Null;
                }
                free(value);
                Self.value = Null;
                Val a : Boolean = True;
                Val b : Int = 1;
                Return (True || False) && (a == b);
            }
        }
        Class Program {
            main() {
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var $x, $y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 337))

    def test_simple_program_30(self):
        """testing matrix multiplication 3"""
        input = """
        Class SomethingNormal {
            aFunc123(str: Array[String, 10]) {
                Val parameters: Map = parseParameters(args);

                Val builder : ChainedOptionsBuilder = New OptionsBuilder()
                .include(BigMatrixMultiplicationBenchmarking.class.getSimpleName())
                .mode(Mode.AverageTime)
                .forks(2)
                .warmupIterations(10)
                .measurementIterations(10)
                .timeUnit(TimeUnit.SECONDS);

                Return New Runner(builder.build()).run();
            }
    homemadeMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Return HomemadeMatrix
          .multiplyMatrices(matrixProvider.getFirstMatrix(), matrixProvider.getSecondMatrix());
    }

    nd4jMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Val firstMatrix : INDArray = Nd4j.create(matrixProvider.getFirstMatrix());
        Val secondMatrix : INDArray = Nd4j.create(matrixProvider.getSecondMatrix());

        Return firstMatrix.mmul(secondMatrix);
    }

    coltMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Val doubleFactory2D : DoubleFactory2D = DoubleFactory2D.dense;

        Val firstMatrix : DoubleMatrix2D= doubleFactory2D.make(matrixProvider.getFirstMatrix());
        Val secondMatrix : DoubleMatrix2D = doubleFactory2D.make(matrixProvider.getSecondMatrix());

        Var algebra : Algebra = New Algebra();
        Return algebra.mult(firstMatrix, secondMatrix);
    }

    ejmlMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Var $firstMatrix : SimpleMatrix = New SimpleMatrix(matrixProvider.getFirstMatrix());
        Var $secondMatrix : SimpleMatrix = New SimpleMatrix(matrixProvider.getSecondMatrix());

        Return firstMatrix.mult(secondMatrix);
    }

    apacheCommonsMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Var firstMatrix : RealMatrix = New Array2DRowRealMatrix(matrixProvider.getFirstMatrix());
        Val secondMatrix : RealMatrix = New Array2DRowRealMatrix(matrixProvider.getSecondMatrix());

        Return firstMatrix.multiply(secondMatrix);
    }

    la4jMatrixMultiplication(matrixProvider : BigMatrixProvider) {
        Val firstMatrix : Matrix = New Basic2DMatrix(matrixProvider.getFirstMatrix());
        Val secondMatrix : Matrix = New Basic2DMatrix(matrixProvider.getSecondMatrix());

        Return firstMatrix.multiply(secondMatrix);
    }
        }
        Class Program {
            main() {
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var $x, $y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Var a : Int = a.b.c.d();
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 338))

    def test_simple_program_31(self):
        """testing simple program"""
        input = """Class Program {
            main() {
                Val b : Int = a[1].func()[0];
                Return;
            }
        }"""
        expect = "Error on line 3 col 34: ."
        self.assertTrue(TestParser.test(input, expect, 339))

    def test_simple_program_32(self):
        """testing simple program"""
        input = """Class Program {
            main() {
                a[1].func();
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 340))

    def test_simple_program_33(self):
        """testing simple program"""
        input = """Class Program {
            main() {
                a[1] = 1;
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 341))

    def test_simple_program_34(self):
        """testing simple program"""
        input = """Class Program {
            main() {
                a.func()[1].foo();
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 342))

    def test_simple_program_35(self):
        """testing simple program"""
        input = """Class Program {
            main() {
                Out.println(a.a[1]);
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 343))

    def test_simple_program_36(self):
        """testing simple program"""
        input = """Class Program {
            main() {
                a[1].func()[0].bar();
                a[1].func();
                a[1] = 1;
                Val b : String = a.func()[1];
                Out.println(a.a[1]);
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 344))

    def test_simple_program_46(self):
        """testing simple program"""
        input = """Class Program {
            main() {
                a[1].func();
                a[1] = 1;
                Out.println(a.a[1]);
                a[1][2].a[1].func()[0].a[1].func();
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 345))

    def test_simple_program_37(self):
        """access static member without assign it -> not a statement, a::$a are just access value"""
        input = """Class Program {
            main() {
                ##a::$a[1].func()[0];##
                a::$a;
                a[1]::$func();
                Return;
            }
        }"""
        expect = "Error on line 4 col 21: ;"
        self.assertTrue(TestParser.test(input, expect, 346))

    def test_simple_program_38(self):
        """statements inside function, operator in action, non associative operator"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));

               c = a + b;
               c = (a +. b) ==. c;
               c = ((a - b) * (c / d)) + (e + f) % 5;
               c = d = e = f;
               c = d = 4;

               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 347))

    def test_simple_program_39(self):
        """statements inside function, operator in action, non associative operator"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));

               c = a + b;
               c = a +. (b ==. c);
               c = ((a - b) * (c / d)) + (e + f) % 5;
               c = d = e = f;
               c = d = 4;

               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 348))

    def test_simple_program_40(self):
        """statements inside function, operator in action, non associative operator and precedence"""
        input = """Class Program {
            Val a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));

               c = a + b;
               c = a +. (b > c ==. a);
               c = ((a - b) * (c / d)) + (e + f) % 5;
               c = d = e = f;
               c = d = 4;

               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 349))

    def test_simple_program_41(self):
        """Idx has lower precendence than member access; therefore, we must put () before execute"""
        input = """Class Program {
            main() {
                Var a : Int = (a::$a[1]).func()[0];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 350))

    def test_simple_program_42(self):
        """Idx has lower precendence than member access; therefore, we must put () before execute"""
        input = """Class Program {
            main() {
                Val a : Int;
                Foreach (i In 1 .. 100 By 1)
                {
                    printf("enter the number:");
                    scanf("%d", a);
                    If ( a == 0 ) {
                        Break;
                    }
                }
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 351))

    def test_simple_program_43(self):
        """Idx has lower precendence than member access; therefore, we must put () before execute"""
        input = """Class Program {
            main() {
                Val a : Int;
                Foreach (i In 1 .. 100 By 1)
                {
                    printf("enter the number:");
                    scanf("%d", a);
                    If ( a == 0 ) {
                        Break;
                    }
                }
                Return 0;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 352))

    def test_simple_program_44(self):
        """Idx has lower precendence than member access; therefore, we must put () before execute"""
        input = """Class Program {
            main() {
                Val a : Int;
                Foreach (i In 1 .. 100 By 1)
                {
                    printf("enter the number:");
                    scanf("%d", &a);
                    If ( a == 0 ) {
                        Break;
                    }
                }
                Return 0;
            }
        }"""
        expect = "&"
        self.assertTrue(TestParser.test(input, expect, 353))

    def test_simple_program_45(self):
        input = """Class Rectangle: Shape {
    getArea() {
        Return Self.length * Self.width;
    }
}
        Class Program {
            main() {
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 354))

    def test_static_access_assign_1(self):
        """access static member without assign it -> not a statement, fix by assign it"""
        input = """Class Program {
            main() {
                Val b : Int = a::$a;
                a::$func();
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 356))

    def test_invalid_statement(self):
        """a statement cannot be a index access"""
        input = """Class Program {
            main() {
                a[1].func()[0];
                a[1].func();
                a[1] = 1;
                Out.println(a.a[1]);
                Return;
            }
        }"""
        expect = "Error on line 3 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 357))

    def test_precedence_of_index_member_1(self):
        """index has lower priority compare to member access -> encapsulate into the ()"""
        input = """Class Program {
            main() {
                Val b : Int = (a[1]).func()[0];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 358))

    def test_no_return_constructor_1(self):
        """constructor that has no return statement"""
        input = """
        Class Map {
            Val key: Array[String, 10];
            Val value: Array[String, 10];
            Constructor(key: Array[String, 10]; value: Array[String, 10]) {
                Self.key = key;
                Self.value = value;
            }
            Destructor() {
                Self.clean(Self.key);
                Self.clean(Self.value);
            }
            clean() {
                Out.println("Cleaning");
                Foreach (k In 0 .. Self.key.length() By 1)
                {
                    el = Self.key[k];

                    free(el);
                    Self.key = Null;
                }
                free(key);
                Self.key = Null;
                Foreach (v In 0 .. Self.value.length() By 1)
                {
                    el = Self.value.a[v];

                    free(el);
                    Self.value = Null;
                }
                free(value);
                Self.value = Null;
                Val a : Boolean = True;
                Val b : Int = 1;
                Return (True || False) && (a == b);
            }
        }
        Class Program {
            main() {
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var $x, $y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 359))

    def test_destructor_with_return_1(self):
        """destructor that has a return statement"""
        input = """
        Class Map {
            Val key: Array[String, 10];
            Val value: Array[String, 10];
            Constructor(key: Array[String, 10]; value: Array[String, 10]) {
                Self.key = key;
                Self.value = value;
                Return;
            }
            Destructor() {
                Self.clean(Self.key);
                Self.clean(Self.value);
                Return;
            }
            clean() {
                Out.println("Cleaning");
                Foreach (k In 0 .. Self.key.length() By 1)
                {
                    el = Self.key[k];

                    free(el);
                    Self.key = Null;
                }
                free(key);
                Self.key = Null;
                Foreach (v In 0 .. Self.value.length() By 1)
                {
                    el = Self.value.a[v];

                    free(el);
                    Self.value = Null;
                }
                free(value);
                Self.value = Null;
                Val a : Boolean = True;
                Val b : Int = 1;
                Return (True || False) && (a == b);
            }
        }
        Class Program {
            main() {
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Var $x, $y : Int = 0, 0;
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 360))

    def test_static_funcall_within_class_1(self):
        """Calling static function call within the class"""
        input = """
        Class Program {
            main() {
                a::$a();
                Return;
            }
            $a() {
                Return $b;
            }
        }
        """
        expect = "Error on line 8 col 23: $b"
        self.assertTrue(TestParser.test(input, expect, 363))

    def test_index_op_1(self):
        """index access as operands"""
        input = """
        Class Program {
            main() {
                a[1][2] = b[1][2][3] - c[1][2][3];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 364))

    def test_elseif_1(self):
        """testing if-elseif-else"""
        input = """
        Class Program {
            Val a: Int = 1;
            fooBar() {
                a.fooBar();
            }
            main() {
                If (1 >= 2) {
                    fooBar();
                } Elseif (a <= 2) {
                    fooBar();
                } Elseif (a[1][2] + b[i][j] <= a[1] * a.a + Some::$a()) {
                    Out.println(4);
                } Else {
                    Out.println("Nothing");
                }
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 365))

    def test_func_params_declare_1(self):
        """testing func params declare"""
        input = """
        Class Program {
            Val a: Int = 1;
            fooBar(a, b : Int; c : Float) {
                fooBar1();
            }
            main() {
                fooBar(a, b, c);
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 366))

    def test_return_sth_constructor_1(self):
        """test return something in constructor"""
        input = """
        Class D {
            Constructor() {
                a = a;
                Return somethingCool;
            }
        }
        Class Program {
            main() {
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 367))

    def test_return_sth_main_1(self):
        """test return something in main"""
        input = """
        Class D {
            Constructor() {
                a = a;
                Return;
            }
        }
        Class Program {
            main() {
                Return 1;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 368))

    def test_return_in_if_1(self):
        """test return something in if statement"""
        input = """
        Class Program {
            main() {
                If (a == 0) {
                    Return 1;
                } Else {
                    Return 0;
                }
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 369))

    def test_return_in_if_2(self):
        """test return something in if statement"""
        input = """
        Class Program {
            main() {
                Foreach (i In 1 .. 10 By 1) {
                    If (a == 0) {
                        Return somthing;
                    }
                }
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 370))

    def test_multi_constructor_1(self):
        """test return something in constructor"""
        input = """
        Class Program {
            Constructor() {
                Return;
            }
            Constructor(some: Some) {
                Return;
            }
            main() {
                Foreach (i In 1 .. 10 By 1) {
                    If (a == 0) {
                        Return somthing;
                    }
                }
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 371))

    def test_multi_destructor_1(self):
        """test return something in destructor"""
        input = """
        Class Program {
            Destructor() {
                Return;
            }
            Destructor() {}
            main() {
                Foreach (i In 1 .. 10 By 1) {
                    If (a == 0) {
                        Return somthing;
                    }
                }
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 372))

    def test_index_static_1(self):
        """static function access for index is illegal"""
        input = """Class Program {
            main() {
                Val b : Int = a::$a;
                a[1]::$func();
                Return;
            }
        }"""
        expect = "Error on line 4 col 20: ::"
        self.assertTrue(TestParser.test(input, expect, 373))

    def test_static_normal_1(self):
        """static and normal test"""
        input = """
        Class C {
            func() {
                Return somethingFun;
            }
        }
        Class B {
            Val a : C;
            Constructor() {
                a = New C();
                Return;
            }
        }
        Class A {
            Val $b : B;
            Constructor() {
                $b = New B();
                Return;
            }
        }
        Class Program {
            main() {
                Val a : A = New A();
                ## a::$b.a.func();##
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 374))

    def test_db_dbcolon_1(self):
        """test a::$b::$c()"""
        input = """
        Class C {
            func() {
                Return somethingFun;
            }
        }
        Class B {
            Val a : C;
            Constructor() {
                a = New C();
                Return;
            }
        }
        Class A {
            Val $b : B;
            Constructor() {
                $b = New B();
                Return;
            }
        }
        Class Program {
            main() {
                Val a : A = New A();
                a::$b::$c();
                Return;
            }
        }"""
        expect = "Error on line 24 col 21: ::"
        self.assertTrue(TestParser.test(input, expect, 375))

    def test_simple_program_reverse_linked_list(self):
        """test some real program"""
        input = """
	Class Node {
		Var data : Int;
		Val next : Node;

		Constructor(d : Int)
		{
			data = d;
			next = Null;
		}

        ## Function to reverse the linked list ##
        reverse(node : Node)
        {
            Var prev : Node = Null;
            Val current : Node = node;
            Val next : Node = Null;
            Foreach (i In 1 .. forever By 1) {
                If (current == Null) {
                    Break;
                } Else {
                    next = current.next;
                    current.next = prev;
                    prev = current;
                    current = next;
                }
            }
            node = prev;
            Return node;
        }

        printList(node : Node)
        {
            Foreach (a In 1 .. infinity By 1) {
                If (node != Null) {
                    System.out.print(node.data +. " ");
                    node = node.next;
                } Else {
                    Break;
                }
            }
        }
    }

    Class Program {
        main()
        {
            Val list : LinkedList = New LinkedList();
            list.head = New Node(85);
            list.head.next = New Node(15);
            list.head.next.next = New Node(4);
            list.head.next.next.next = New Node(20);

            System.out.println("Given Linked list");
            list.printList(head);
            head = list.reverse(head);
            System.out.println("");
            System.out.println("Reversed linked list ");
            list.printList(head);
        }
    }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 362))

    def test_continue_stm_1(self):
        """test continue statement"""
        input = """
        Class Simple {

   main() {
      Val numbers : Array[Int, 5] = Array(10, 20, 30, 40, 50);

      Foreach (i In 0 .. 4 By 1) {
         If ( x == 30 ) {
            Continue;
         }
         System.out.print( x );
         System.out.print("\n");
      }
   }
}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 376))

    def test_more_exp_var_1(self):
        """assign more expression than the var declaration"""
        input = """
        Class Program {
            main() {
                Val a : Int = 1, 2;
                Return;
            }
        }"""
        expect = "Error on line 4 col 31: ,"
        self.assertTrue(TestParser.test(input, expect, 377))

    def test_static_access_1(self):
        """using double colon but access normal attribute"""
        input = """
        Class Program {
            main() {
                a = a::b;
                Return;
            }
        }"""
        expect = "Error on line 4 col 23: b"
        self.assertTrue(TestParser.test(input, expect, 378))

    def test_empty_program_1(self):
        """Totally empty program"""
        input = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 379))

    def test_multi_dim_arr_1(self):
        """Multidimension array"""
        input = """
        Class Program {
            main() {
                Val a : Array[Array[Int, 10], 0x15];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 380))

    def test_static_param_1(self):
        """Static param are not allowed"""
        input = """
        Class Program {
            main($a : Int) {
            }
        }"""
        expect = "Error on line 3 col 17: $a"
        self.assertTrue(TestParser.test(input, expect, 381))

    def test_wrong_static_access(self):
        """Sth::sthElse is wrong"""
        input = """
        Class Program {
            main() {
                Car::$abc = 10;
                a = Sth::sthElse;
            }
        }"""
        expect = "Error on line 5 col 25: sthElse"
        self.assertTrue(TestParser.test(input, expect, 382))

    def test_wrong_static_access_1(self):
        """a::$b::$c"""
        input = """
        Class Program {
            main() {
                Car::$abc = 10;
                a = a::$b::$c;
            }
        }"""
        expect = "Error on line 5 col 25: ::"
        self.assertTrue(TestParser.test(input, expect, 383))

    def test_dot_new_1(self):
        """a.New A()"""
        input = """
        Class Program {
            main() {
                a = a.New A();
            }
        }"""
        expect = "Error on line 4 col 22: New"
        self.assertTrue(TestParser.test(input, expect, 384))
    
    def test_weird_static_access(self):
        input = """
        Class Program {
            main() {
                a = "123"::$getValue();
            }
        }"""
        expect = "Error on line 4 col 25: ::"
        self.assertTrue(TestParser.test(input, expect, 385))

