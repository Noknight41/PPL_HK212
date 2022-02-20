import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
###
    def test_201(self):
        test = """
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
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,201))
    
    def test_202(self):
        test = """
        Class Entity {
            Var UUID: String;
            Var $numOfEntities: Int = 0;
            Constructor() {
                Entity::$numOfEntities = Entity::$numOfEntities + 1;
            }
            Destructor() {
                Entity::$numOfEntities = Entity::$numOfEntities - 1;
            }
        }
        """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(test,expect,202))
        
    def test_203(self):
        test = """
        Class Program {
            Var _Fool: Float = 1.2e3;
            main(){
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,203))
        
    def test_204(self):
        test = """
        Class Program {
            Var _Fool, _Magician: String = "Hello World", "I am '"Mr.Coren'"";
            main(){
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,204))
        
    def test_205(self):
        test = """
        Class Program {
            Var _Fool, _Magician: Array[Int, 5];
            main(){
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,205))
        
    def test_206(self):
        test = """
        Class Program {
            ## Hello Everybody ##
            Var _Fool, _Magician: Int = 1,2;
            main(){
                
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,206))
        
    def test_207(self):
        test = """
        Class Program {
            ## Hello Everybody ##
            Var _Fool, _Magician: Boolean = True, False;
            main(){
                Return self._Fool;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,207))
        
    def test_208(self):
        test = """
        Class Program {
            ## Hello Everybody ##
            Var _Fool, _Magician: Array[Int, 4] = Array(1,2,3,4), Array(5,56,7,8);
            main(){
                Return self._Fool;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,208))
        
    def test_209(self):
        test = """
        Class Program {
            ## Hello Everybody ##
            Val $Emperor, Empress: Int = 1_465_3, 0223_334_545;
            Var $Fool, $Magician: Int = 0b11, 0x1A6_7;
            main(){
                Return self._Fool;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,209))
    
    def test_210(self):
        test = """
        Class Hello{
            Var _Fool, _Magician : String;
            Constructor(x, y: String){
                _Fool = x;
                _Magician = y;
                Self.print("Constructor is good");
            }
        }
        
        Class Program {
            ## Hello Everybody ##
            main(){
                Var x: Hello = New Hello();
                Return x._Fool;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,210))
        
    def test_211(self):
        test = """
        ##jlkjlk##
        Class Program {
            main() { 
                ##kl;k##
                x = "##2+"; 
            }
        }
        """ 
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,211))
    
    def test_212(self):
        test = """
        Class Program{
            main () {
                Self.putIntLn(4_5, 4.3e10);
                x = "f";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,212))
        
    def test_213(self):
        test = """
        Class Program{
            main( {}
        }
        """
        expect = "Error on line 3 col 18: {"
        self.assertTrue(TestParser.test(test,expect,213))
    
    def test_214(self):
        test = """
        Class Program{
            main() {
                a = New OPER();
                Var a_c: Array[Int, 4]= Array(1,3, 1e-10);
                Val b: Int = a::$xan;
            }
        }
        Class OPER {
            getXan(){   
                Return xan;
            }
            Constructor(){
                xan = 5+-3-5*4/2*New OPPER(6,5).a;
                xan=-a;
            }
            Destructor(){
                xan=0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,214))
        
    def test_215(self):
        test = """
        Class Person
        {
            Var name: String;
            Var height: Float;
            Var salary: Float;
            Var $maxHeight: Float = -INT_MAX;
            Person(_salary, _height : Float; _name: String)
            {
                Self.name = _name;
                Self.height = _height;
                Self.salary = _salary;
                If (_height > Person::$maxHeight)
                {
                    Person::$maxHeight = _height;
                }
                Else
                {
                    System.Out.printLn("Sorry you must be higher \\j");
                }
            }
        }
        Class OSR {
            getXan(x, a: Int; y,b : Float){
                Foreach(i In 2+5 .. 45 By (b+x)){
                    If (a + b) {
                        x = y+x+a ;   
                    }
                    Elseif (a+b>c){
                        x = 5 - x;
                        y = -5;
                    }
                    Else {
                        y = New OPER().xan;
                    }
                }        
                Return xan;
            }
            Constructor(){
                xan = 5;
            }
            Destructor(){
                xan=0;
            }
        }
        Class Program{
            main() {
                a = New OSR();
                Var a_c: Array[Int, 4]= Array(1,3);
                Val b:Int = a :: $xan;
            }
        }
        
        """
        expect = """Sorry you must be higher \\j"""
        self.assertTrue(TestParser.test(test,expect,215))
    
    def test_216(self):
        test = """
        Class HelloWorld {
            Val World: Boolean = ((0.0 + 2) > 5) || False && ("22" ==. "55");
            Hello(a: Int){
                Return World;
            }
        }
        
        Class Program {
            main(){
                Out.printInt(New HelloWorld().Hello());
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,216))
        
    def test_217(self):
        test = """
        Class HelloWorld {
            Val Sinc: Float = 0;
            Hello(){
                If(((0.0 + 2) > 5) || False && ("22" ==. "55")){
                    Return 1 + 2.0 -- 2;
                }
                Else{
                    Return 1.0 * 1.3 - 2.4e-12;
                }
            }
        }
        
        Class Program {
            main(){
                Out.printInt(New HelloWorld().Hello());
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,217))
    
    def test_218(self):
        test = """
        Class Shape{
            Var height, length: Float;
        }
        
        Class Rectangle: Shape {
            $getArea() {
                Return Self.height * Self.height;
            }
        }
        
        Class Program {
            main(){
                Out.printInt(Rectangle::$getArea());
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,218))
        
    def test_219(self):
        test = """
        Class Program {
            ## Hello Everybody ##
            Var _Fool, _Magician: Array[, 4];
            main(){
                Return self._Fool;
            }
        }
        """
        expect = "Error on line 4 col 40: ,"
        self.assertTrue(TestParser.test(test,expect,219))
        
    def test_220(self):
        test = """
        Class main {
            
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,220))
        
    def test_221(self):
        test = """
        Class Shape{
            Var height, length: Float;
        }
        
        Class Rectangle: Shape {
            $getArea() {
                Return Self.height * Self.height;
            }
        }
        
        Class Program {
            Var x, y: Float;
            main(){
                x = (Rectangle::$height[1])* 23 + .9e-45 - 23/21 - y[2][3] ; 
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,221))
        
    def test_222(self):
        test = """
        Class HelloWorld {
            Val World: Array[Int, 1] = Array();
            Hello(a: Int){
                Return World;
            }
        }
        
        Class Program {
            Var c : Hello = New HelloWorld();
            main(){
                Out.printInt(New HelloWorld().Hello());
            }
        }
        ##jlkj##
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,222))
    
    def test_223(self):
        test=""" 
            Class Test{ 
               Var ins: Int; 
               Var $static: Int; 
                
                Test(){ 
                  Var a: Int= Self::ins; 
                  Var b: Int= Self::$static(); 
                } 
            }""" 
        expect = "Error on line 7 col 34: ::"  
        self.assertTrue(TestParser.test(test,expect,223))

    def test_224(self):
        test1 = """
        Class Shape {
            Val My1stCons, My2ndCons: Int = 1 + 5/2, 2;
            Var $x, $y : Int = 0, 0;
        }
        Class Program {
            ## Muda
            Muda ##
            Var hello: Array[Int, 5];
            Var length, width: Int;
            main(){
                a = 1.0;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test1,expect,224))

    def test_225(self):
        test = """
        Class Program {
            Var a : Int 1    
        }
        ## Hello ##
        """
        expect = "Error on line 3 col 24: 1"
        self.assertTrue(TestParser.test(test,expect,225))
    
    def test_226(self):
        test = """Class Program {
            Var length, width: Int    
        }
        ## Hello ##
        """
        expect = "Error on line 3 col 8: }"
        self.assertTrue(TestParser.test(test,expect,226))
        
    def test_227(self):
        test = """
        Class Program {
            main(){
                ## Muda ##
                Foreach (x In 1 .. 25 By x + 1) {
                    Out.printInt(arr[x]);
                }
            }
            ## Muda
            Muda ##
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,227))
    
    def test_228(self):
        test = """
        Class Shape{
            Val $n: Int = 1;
            ## Var s: Int = 2 ##
            Var s: Int = 2;
        }
        Class Program {
            Var $numOfShape: Int;
            Var immutableAttribute: Int;
            Var a_c: Array[Int, 4] = Array(1, 3, 5, 8);
            
            $getNumOfShape(){
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
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,228))
        
    def test_229(self):
        test = """
        Class Program {
            main(){
                Foreach (x In 1 .. 25 By x + 1) {
                    If(("22" +. "22") ==. "2222"){
                        Break;
                    }
                    Continue;
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,229))
    
    def test_230(self):
        test = """
        Class Program {
            Var $numOfShape: Int;
            Var immutableAttribute: Int;
            Var a_c: Array[Array[String, 0], 3] = Array ( Array("Volvo", "22", "18"), Array("Saab", "5", "2"), Array("Land Rover", "17", "15"));
            main(){
                ## Muda ##
                Out.printInt(Shape::$numOfShape[1]);
            }
            ## Muda
            Muda ##
        }"""
        expect = "Error on line 5 col 41: 0"
        self.assertTrue(TestParser.test(test,expect,230))
        
    def test_231(self):
        test = """
        Class Diagram{
            getArea(){
                Return a;
            }
        }
        Class Program {
            Var $numOfShape: Int;
            Var immutableAttribute: Int;
            Var a_c: Array[Array[String, 3], 3] = Array ( Array("Volvo", "22", "18"), Array("Saab", "5", "2"), Array("Land Rover", "17", "15"));
            main(){
                ## Muda ## ## Muda ##
                Out.printInt(Shape::$numOfShape[1]);
            }
            ## Muda
            Muda ##
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,231))
    
    def test_232(self):
        test = """
        Class Program {
            Var $numOfShape: Int;
            Var immutableAttribute: Int;
            Var a_c: Array[Array[String, 3], 3] = Array ( Array("Volvo", "22", "18"), Array("Saab", "5", "2"), Array("Land Rover", "17", "15"));
            main(){
                ## Muda ## ## Muda ##
                a 1.2e2;
                Out.printInt(Shape::$numOfShape[1]);
            }
            ## Muda
            Muda ##
        }"""
        expect = "Error on line 8 col 18: 1.2e2"
        self.assertTrue(TestParser.test(test,expect,232))
        
    def test_233(self):
        test = """
        Class Trt{
            Var a, b : String;
            Constructor(x: String){
                Self.a = "No";
                Self.b = x;
            }
            Despacito(){
                Return Self.a + Self.b;
            }
        }
        Class Shape {
            Var flag: Trt = Null;
            Var x, y : Int;
            Constructor(a,b: Int; d: String){
                Trt = New Trt(d);
                Var s: String = Self.Trt.b;
                If(d ==. "Hel"){
                    Self.x = a;
                    Self.y = b;
                }
                Elseif(d ==. "Heav"){
                    Self.x = b;
                    Self.y = a;
                }
                Else{
                    Self.x = Self.num(1,2);
                    Self.y = a*b;
                }
            }
            Destructor(){
                a.print("No service");
            }
        }
        Class Program {
            ## Muda
            Muda ##
            Var hello: Array[Int, 5];
            Var length, width: Int;
            main(){
                a = 1.0;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,233))
    
    def test_234(self):
        test = """
        Class Trt{
            Var a, b : String;
            Constructor(x: String){
                Self.a = "No";
                Self.b = x;
            }
            Despacito(){
                Return Self.a + Self.b;
            }
        }
        Class Shape {
            Var flag: Trt = Null;
            Var x, y : Int;
            Constructor(a,b: Int; d: String){
                flag = New Trt(d);
                Var s: String = flag.Despacito();
                Self.x = b;
                Self.y = a;
                If(d ==. "Hel"){
                    Self.x = a;
                    Self.y = b;
                }
            }
            Destructor(){
                Self.print("No service");
            }
        }
        Class Program {
            ## Muda
            Muda ##
            Var hello: Array[Int, 5];
            Var length, width: Int;
            main(){
                a = 1.0;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,234))
    
    def test_235(self):
        test = """
        Class Program
        {
            binarySearch(myArray: Array[Int, 1000]; low, high, target : Int)
            {
                If(high < low)
                {
                    Return "Sorry We cannot found it";
                }
                Var middle: Int = (high + low)/2;
                If(myArray[middle] > target)
                {
                    Return Self.binarySearch(myArray, middle + 1, high);
                }
                Elseif(myArray[middle] < target)
                {
                    Return binarySearch(myArray, low, middle - 1);
                }
                Else
                {
                    Return middle;
                }
            }
            main()
            {
                Val myArray: Array[Int, 10] = 
                Array(1,2,3,4,5,6,7,8,9,10);
                Var pos: Int = Self.binarySearch(myArray, 1 , 10 , 9);
            }
        }""" 
        expect = """Error on line 17 col 39: ("""
        self.assertTrue(TestParser.test(test,expect,235))
    
    def test_236(self):
        test = """
        Class Trt{
            Var a: String;
            Constructor(x: String){
                Self.a = x;
            }
            Despacito(){
                Return Self.a +. "2";
            }
        }
        Class Shape {
            Var flag: Trt = Null;
            Var x, y : Int;
            Constructor(a,b: Int; d: String){
                flag = New Trt(d);
                Var s: String = flag.Despacito();
                Self.x = b;
                Self.y = a;
                If(d ==. "Hel"){
                    Self.x = a;
                    Self.y = b;
                }
            }
            Destructor(){
                a.print("No service");
            }
        }
        Class Program {
            ## Muda
            Muda ##
            Var hello: Array[Int, 5];
            Var length, width: Int;
            Var flag2: Shape = New Shape(1,2,"Help");
            main(){
                a.print(flag2.flag.Despacito());
                flag2.flag. = "s";
                a = 1.0;
            }
        }"""
        expect = "Error on line 36 col 28: ="
        self.assertTrue(TestParser.test(test,expect,236))
        
    def test_237(self):
        test = """
        Class Rectangle : Shape{
            $getSomething(yes: Int){
                Var x : Int = 0;
                Return x;
                Foreach(x In 1 .. 100){
                    bf.doSomething("2","2");
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,237))
    
    def test_238(self):
        test = """
        Class Entity {
            Var $numOfEntities: Int = 0;
            Var UID: String;
            Constructor() {
                Entity::$numOfEntities = Entity::$numOfEntities + 1;
            }
            Destructor() {
                Entity::$numOfEntities = Entity::$numOfEntities - 1;
            }
        }
        Class Pig:Entity{
            Var height: Float = 0.75;
            Var width: Float = 0.8;
        }
        Class Creeper:Entity{
            Var height: Float = 1.75;
            Var width: Float = 0.8;
            Var $explosion: Float = 56.7;
        }
        """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(test,expect,238))
    
    def test_239(self):
        test = """
        Class Shape: Rectangle {
            ##
            This part should be ignored, just to check, nothing to comment
            ##
            $getSomething(yes: Int){
                Var x : Float = 12_0.001;
                Var t : Int = 01_0;
                Var y : Float = 0.; 
                a = - desp;
                a = - a.foo().foo();
                Return x;
            }
            Sup(){
                Shape::$getSomething(7);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,239))
        
    def test_240(self):
        test = """
        Class Shape: Rectangle {
            ##
            This part should be ignored, just to check, nothing to comment
            ##
            $getSomething(yes: Int){
                Var x : Float = 12_0.001;
                Var t : Int = 01_0;
                Var y : Float = 0.; 
                a[2][3] = - desp;
                Return x;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,240))
        
    def test_241(self):
        test = """
        Class Shape: Rectangle {
            ##
            This part should be ignored, just to check, nothing to comment
            ##
            $getSomething(yes: Int){
                Var x : Float = 12_0.0_01;
                Var t : Int = 01_0;
                Var y : Float = 0.; 
                a[2][3] = - desp;
                a = - a.foo().foo();
                b = ab::$cd.a().b() + 23;
                A::$foo().foo();
                a.a().foo.foo();
                Return x;
            }
        }
        """
        expect = "Error on line 7 col 38: _01"
        self.assertTrue(TestParser.test(test,expect,241))
    
    def test_242(self):
        test = """
        Class Shape: Rectangle {
            ##
            This part should be ignored, just to check, nothing to comment
            ##
            $getSomething(yes: Int){
                Var x : Float = 12_0.01;
                Var t : Int = 01_0;
                Var y : Float = 0.; 
                t.d.s = 1;
            }
        }
        Class Program {
            ## Muda
            Muda ##
            Var hello: Array[Int, 5];
            Var length, width: Int;
            Var flag2: Shape = New Shape(1,2,"Help");
            main(){
                Out.print(flag2.flag.Despacito());
                flag2.flag = "s";
                a = 1.0;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,242))
    
    def test_243(self):
        test = """
        Class Toy{
            Var height, length: Array[Float,2];
            Constructor(h, l: Float; a: Array[Float,2]){
                Self.height[1] = h + a[1];
                Self.height[2] = h + a[2];
                b.a[1] = 1;
            }
            $gg(a: Float){
                a.f();
            }
        }
        
        Class Box{
            $getArea() {
                Return Self.height * Self.height;
                Toy::$gg();
            }
        }
        
        Class Program {
            main(){
                Out.printInt(Rectangle::$getArea());
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,243))
    
    def test_244(self):
        test = """
        "Hello"""
        expect = "Hello"
        self.assertTrue(TestParser.test(test,expect,244))
    
    def test_245(self):
        test = """
        Class Shape{
            Val $n: Int = 1;
            ## Var s: Int = 2 ##
            Var s: Int = 2;
        }
        Class Program {
            Val immutableAttribute: Int = 1;
            Var a_c: Array[Int, 4] = Array(1, 3, 5, 8);
            Var $a,$b,$c,$d : String = "2","4","23","57";
            
            $getNumOfShape(){
                {
                    Val fShap: String = "243 '" Hello '"";
                }
                ## Var s: Int = 2 ##
                Var y: Shape = New Shape();
                x = y.s + y::n;
                Return Hape::$numOfShape + Self::$a + Self::$b + Self::$c + Self::$d;
            }
            ## Muda
            Muda ##
        }"""
        expect = "Error on line 18 col 29: n"
        self.assertTrue(TestParser.test(test,expect,245))
    
    def test_246(self):
        test = """
        Class Program{
            Var $a: Array[Int, 3] = Array(0, 3, 1);
            main () {
                A::$a = Array(0, 3, 5);
                a.putIntLn(4_5, 4.3e10);
                x = "f";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,246))
    
    def test_247(self):
        test = """
        Class Toy{
            Var height, length: Array[Float,2];
            Constructor(h, l: Float; a: Array[Float,2]){
                Self.height[1] = h + a[1];
                Self.height[2] = h + a[2];
                b.a[1] = 1;
            }
            $gg(a: Float){
                a.f();
            }
        }
        Class Box{
            Var $a: Array[Int, 3] = Array(0, 3, 5);
            $getArea() {
                Return Self.height * Self.height + Toy::$gg();
            }
        }
        Class Program{
            
            main () {
                Box::$a = Array(0, 3, 1);
                a.putIntLn(4_5, .5e5);
                x = "f";
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,247))
        
    def test_248(self):
        test = """
            Class TestBird {
                Constructor(w: Int; s: Float; a: String; b: Array[Int, 5]; c: Boolean) {
                    Var a : Int = 1;
                    c = (a + b) * (c + d) - (a - b) / (5 % 2) == (1 + 1);
                    d = g.function() * f.a - f::$b;
                    Return;
                }

                Destructor() {
                    Var a : Int = 1;
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
        self.assertTrue(TestParser.test(test, expect, 248))
    
    def test_249(self):
        test = """
        Class Program{
            main(){
                ## Comment something here ##
                Var a : Int;
                a = 5;
                ## Comment something here ##
                Var b : String; 
                Val c, d, acc: String = "Here is another string","asd","Another string";
                Foreach(a In 12_3.0 .. 13 By 2+1){
                    Self.callMe(asdhfjk);
                }
                Foreach(a In 1 .. 2){
                    Var a: Int;
                    If(a ==1){
                        a = 2 * Self.call(aladin);
                        Break;
                        Invocation::$id();
                    }
                }
                Return;
            }
        }
        """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(test,expect,249))
    
    def test_250(self):
        test = """
        Class Main{
                Var v : Boolean;
                setIsValue(isSaved:Boolean){
                    v = isSaved;
                }
            }
            Class Program{
                main(){
                    Var x : Main = New Main();
                    x.setIsValue(True);
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,250))
        
    def test_251(self):
        test = """
        Class Program {
            Val a, b: Array[Int, 5] = Array(), Array();
            Var c: Array[String, 10_0];
            main() {
               sd = 1;
               DF = 2;
               sad = Array();
               sa = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));
               f.callFunc();
               d.callSomething();

               nkjk = g::$sthElse;
               Val d: Int = f.callFunc() - g::$something(a, b);
               
               f = g.someValue();
               Val abc: String = f.something();
               Var c: Float = ((a - b) * (c / d)) + (e + f) % 5;

               d = "Something";
               Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 251))
    
    def test_252(self):
        test = """Class Program{ main(){
            Var a, b : Array[String,-4];
            }
            }"""
        expect = "Error on line 2 col 36: -"
        self.assertTrue(TestParser.test(test,expect,252))
    
    def test_253(self):
        test="""
            Class Account {
                Var userName, password : String;
                Var pin : Int;
                Var date: String;
                    
                Constructor(name:String; pw:String; pin:Float){
                    user = name;
                    password = pw;
                    Self.pin = pin;
                }
                    
                getInfo(){
                    date = "13";
                    Out.printString(username,password,pin);
                }
                    
            }
            
            Class Program {
                main(){
                    Val myuserAccount : Account = New Account("novice.nguyenHCMUT", "NK1707", 1612);
                    myuserAccount.getInfo();
                }
            }
            
            """
        expect="successful"
        self.assertTrue(TestParser.test(test,expect,253))
    
    def test_254(self):
        test = """
        Class Person {
            Var name : String;
            Var age : Int;
            
            Constructor(){
                name = "default name";
                age = 1;
            }
        }
            
        Class Program{ 
            main(){
                ##khoi tao object##
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,254))
        
    def test_255(self):
        test = """Class Student{
            Var name : String;
            Var id: Int;
            Var email: String;
            
                Destructor(){
                    Out.printString("Destroying obj done!");
                }
                
                Constructor(name,email:String;id:Int){
                    Self.name = name;
                    Self.id = id;
                    Self.email = email;
                }
                
                getName(){
                    Return name;
                }
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,255)) 
    
    def test_256(self):
        test = """
        Class Student{
            Var $id : Int;
            Destructor(cmnd,sdt,ten){
                Out.print("Destroying obj done!")
            }
        }
            """
        expect = "Error on line 4 col 23: cmnd"
        self.assertTrue(TestParser.test(test,expect,256)) 
        
    def test_257(self):
        test = """
        Class Program{ 
            main(){
                Var a, b : Int = 012, 321, 0xAB;
            }
        }
        """
        expect = "Error on line 4 col 41: ,"
        self.assertTrue(TestParser.test(test,expect,257))
    
    def test_258(self):
        test = """
        Class Program{ 
            main(){
                Var a, b : Int = 1;
            }
        }
        """
        expect = "Error on line 4 col 34: ;"
        self.assertTrue(TestParser.test(test,expect,258))
    
    def test_259(self):
        test = """
        Class Program {
            main() {
                Foreach(x In 100 .. 300 By 5){
                    Out.printInt(x % 10);
                }
                Foreach(y In 300 .. -0 By -2){
                    B::$doNothing = 1;
                    a::$doNothing();
                    Foreach(z In -1 .. 50000000){
                        Out.print("Hello world");
                    }
                }
            }
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(test, expect, 259))
    
    def test_260(self):
        test = """
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;

            $getNumOfShape() {
                Val temp: Int = 5;
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
        expect = """successful"""
        self.assertTrue(TestParser.test(test,expect,260))
        
    def test_261(self):
        test = """
        Class Program {
            main() {
                Val $invalid_value: Int = 100000000; ## Some error should occur here ##
                Return $invalid_value;
            }
        }
        """
        expect = """Error on line 4 col 20: $invalid_value"""
        self.assertTrue(TestParser.test(test,expect,261))
    
    def test_262(self):
        test = """
        Class Program {
            Var $sus_value: String = "This value is sus!"; ## Susssssss ##
            main() {
                Val valid_value: Int = 100000000;
                Var s: SH = Null;
            }
        }
        """
        expect = """successful"""
        self.assertTrue(TestParser.test(test,expect,262))
        
    def test_263(self):
        test = """
        Class Program {
            main() {
                a = "123"::$getValue();
            }
        }"""
        expect = "Error on line 4 col 25: ::"
        self.assertTrue(TestParser.test(test, expect, 263))
    
    def test_264(self):
        test = """
        Class Program {
            main() {
                a = a.New A();
            }
        }"""
        expect = "Error on line 4 col 22: New"
        self.assertTrue(TestParser.test(test, expect, 264))
    
    def test_265(self):
        test = """
        Class Program {
            main() {
                Car::$abc = 10;
                a = a::$b::$c;
            }
        }"""
        expect = "Error on line 5 col 25: ::"
        self.assertTrue(TestParser.test(test, expect, 265))
    
    def test_266(self):
        """Sth::sthElse is wrong"""
        test = """
        Class Program {
            main() {
                Car::$abc = 10;
                a = Sth::sthElse;
            }
        }"""
        expect = "Error on line 5 col 25: sthElse"
        self.assertTrue(TestParser.test(test, expect, 266))
        
    def test_267(self):
        test = """
        Class Program {
            main($a : Int) {
            }
        }"""
        expect = "Error on line 3 col 17: $a"
        self.assertTrue(TestParser.test(test, expect, 267))
        
    def test_268(self):
        test = """
        Class Program {
            main() {
                Var a : Array[Array[Int, 012], 0x15];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 268))
    
    def test_269(self):
        """Totally empty program"""
        test = """"""
        expect = "Error on line 1 col 0: <EOF>"
        self.assertTrue(TestParser.test(test, expect, 269))
    
    def test_270(self):
        test = """
        Class Program {
            main() {
                a = a::b;
                Return;
            }
        }"""
        expect = "Error on line 4 col 23: b"
        self.assertTrue(TestParser.test(test, expect, 270))
    
    def test_271(self):
        test = """
        Class Program {
            main() {
                Var a : Float;
                Val d : Int = 1, 2;
                Return;
            }
        }"""
        expect = "Error on line 5 col 31: ,"
        self.assertTrue(TestParser.test(test, expect, 271))
        
    def test_272(self):
        test = """
        Class Simple {
            main() {
                Val numbers : Array[Int, 5] = Array(100, 720, 310, 440, 20);
                Foreach (i In 0 .. 4 By 1) {
                    If ( x == 30 ) {
                        Continue;
                    }
                    System.out.print( x );
                }
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 272))
        
    def test_273(self):
        test = """
	    Class Node {
		    Var data : Int;
		    Var next : Node;

		    Constructor(d : Int){
			    data = d;
			    next = Null;
		    }

            ## Function to reverse the linked list ##
            reverse(node : Node){
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

            printList(node : Node){
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
                list.printList(head);
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 273))
        
    def test_274(self):
        test = """
        Class Cdf {
            func() {
                Return somethingFun;
            }
        }
        Class Bdf {
            Var a : Cdf;
            Constructor() {
                a = New Cdf();
                Return;
            }
        }
        Class Afd {
            Var $b : Bdf;
            Constructor() {
                A::$b = New Bdf();
                Return;
            }
        }
        Class Program {
            main() {
                Val a : Afd = New Afd();
                a::$b::$c();
                Return;
            }
        }"""
        expect = "Error on line 24 col 21: ::"
        self.assertTrue(TestParser.test(test, expect, 274))
    
    def test_275(self):
        test = """
        Class Shape {
            GetFunc(a,b : Int ; c : Float) {
                Val num1: Array [Int, 5] = Array();
                Val num1, num2: Int = 1,2;
            }
        }
        Class Program{
            main(){
                something = (True == (!False));
            }
        }
        """ 
        expect = """successful"""
        self.assertTrue(TestParser.test(test, expect, 275))
        
    def test_276(self):
        test = """Class Program {
            main() {
                Val b : Int = a::$a;
                a[1]::$func();
                Return;
            }
        }"""
        expect = "Error on line 4 col 20: ::"
        self.assertTrue(TestParser.test(test, expect, 276))
    
    def test_277(self):
        test = """
        Class Program {
            Destructor() {
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
        self.assertTrue(TestParser.test(test, expect, 277))
    
    def test_278(self):
        test = """
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
        self.assertTrue(TestParser.test(test, expect, 278))
    
    def test_279(self):
        test = """
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
        self.assertTrue(TestParser.test(test, expect, 279))
    
    def test_280(self):
        test = """
        Class Diagram{
            getArea(){
                Return a[4];
            }
        }
        Class Program{
            main(){
                ## Comment something here ##
                Var a : Int;
                a = foo().foo();
                Var b : String;
            }
        }
        """ 
        expect = """Error on line 11 col 23: ("""
        self.assertTrue(TestParser.test(test, expect, 280))
    
    def test_281(self):
        test = """
        Class Program {
            main() {
                a[1][2] = b[1][2][3] - c[1][2][3];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 281))

    def test_282(self):
        test = """
        Class Program {
            Val a: Int = 1;
            fooBar() {
                a.fooBar();
            }
            main() {
                If (1 >= 2) {
                    a.fooBar();
                } Elseif (a <= 2) {
                    b.fooBar();
                } Elseif (a[1][2] + b[i][j] <= a[1] * a.a + Some::$a()) {
                    Out.println(4);
                } Else {
                    Out.println("Nothing");
                }
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 282))

    def test_283(self):
        test = """
        Class Program {
            Val a: Int = 1;
            fooBar(a, b : Int; c : Float) {
                Self.fooBar1();
            }
            main() {
                Self.fooBar(a, b, c);
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 283))
        
    def test_284(self):
        test = """
        Class HelloWorld {
            Val World: Boolean = ((0.0 + 2) > 5) || False && ("22" ==. "55");
            Hello(a: Int){
                Return World;
            }
        }
        
        Class Program {
            main(){
                Out.printInt(New HelloWorld().Hello());
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test,expect,284))

    def test_285(self):
        test = """
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
        self.assertTrue(TestParser.test(test, expect, 285))
    
    def test_286(self):
        test = """
        Class Program {
            main() {
                (b[1]).func()[0];
                (a[1]).func();
                a[1] = 1;
                Out.println(a.a[1]);
                Return;
            }
        }
        """
        expect = "Error on line 4 col 32: ;"
        self.assertTrue(TestParser.test(test, expect, 286))

    def test_287(self):
        test = """Class Program {
            main() {
                Val b : Int = (a[1]).func()[0];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 287))

    def test_288(self):
        test = """
        Class Map {
            Var key: Array[String, 10];
            Var value: Array[String, 10];
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
                    a.free(el);
                    Self.key = Null;
                }
                a.free(key);
                Self.key = Null;
                Foreach (v In 0 .. Self.value.length() By 1)
                {
                    el = Self.value.a[v];

                    a.free(el);
                    Self.value = Null;
                }
                a.free(value);
                Self.value = Null;
                Val a : Boolean = True;
                Val b : Int = Self.a[5];
                Return (True || False) && (a == b);
            }
        }
        Class Program {
            main() {
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 288))

    def test_289(self):
        test = """
        Class Map {
            Var key: Array[String, 10];
            Var value: Array[String, 10];
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
                    a.free(el);
                    Self.key = Null;
                }
                a.free(key);
                Self.key = Null;
                Foreach (v In 0 .. Self.value.length() By 1)
                {
                    el = Self.value.a[v];
                    a.free(el);
                    Self.value = Null;
                }
                a.free(value);
                Self.value = Null;
                Val a : Boolean = True;
                Val b : Int = 1;
                Return (True || False) && (a == b);
            }
        }
        Class Program {
            main() {
                Val My1stCons, My2ndCons: Int = 1 + 5, 2;
                Val sth : Sth = New Sth();
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 289))

    def test_290(self):
        test = """
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
        self.assertTrue(TestParser.test(test, expect, 290))
    
    def test_291(self):
        test = """
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
                Var a : Int;
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
        self.assertTrue(TestParser.test(test, expect, 291))

    def test_292(self):
        test = """
        Class Program {
            Constructor() {
                Return;
            }
            Constructor(x: Int; y: String; a: Array[Array[Int,1],1]) {
                Return a + x + y;
            }
            Destructor() {
                Console.log("End");
            }
            Destructor(x: Int) {
                Return x;
            }
        }
        """
        expect = """Error on line 12 col 23: x"""
        self.assertTrue(TestParser.test(test, expect, 292))

    def test_293(self):
        test = """
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
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 293))
    
    def test_294(self):
        test = """
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
                Var N : NFT = New NFT();
                Var a : Int = (a::$a[1]).func()[0];
                Return;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 294))

    def test_295(self):
        test = """
        Class Program {
            Var a : Int = 4;
            Val b : String = "Hello World";
            Var $c, d : Float = 1.0, 2e10;
            Var a, b : Int;
            Var $a : Float;

            getArea(w : Int; h : Float; a : String) {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var c, d : Float = 1.0, 2e10;
            }

            $something(w : Int) {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var c, d : Float = 1.0, 2e10;
            }

            Something() {
                Out.println(4);
                Out.something(5);
                Var a : Int = 4;
                Val b : String = "Hello World";
                Var c, d : Float = 1.0, 2e10;
            }

            main() {
                Out.println(4);
                Foreach (i In 1 .. 100 By 1)
                {
                    Out.printf("enter the number:");
                    G.scanf("%d", a);
                    If ( a == 0 ) {
                        Break;
                    }
                }
                Return;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 295))

    def test_296(self):
        test = """
        Class Program {
            main() {
                Var a : Int;
                Foreach (i In 1+2 .. 100 By 1)
                {
                    a.printf("enter the number:");
                    b.scanf("%d", a);
                    Continue;
                    If ( a == 0 ) {
                        Break;
                    }
                }
                Return 0;
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(test, expect, 296))
    
    def test_297(self):
        test = """
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
        self.assertTrue(TestParser.test(test, expect, 297))

    def test_298(self):
        test = """
        Class Test{
            Var $staticVar: Int;
            Test(){
                Val helpMe : String = "I found the light";
                Var b: Int= Test::$staticVar;
            }
        }
        Class Program {
            main() {
                ##a::$a[1].func()[0];##
                Var a: Array[Array[Array[Int,3],2],2] = Array(
                    Array(Array(1,3,4), Array(1,5,6)),
                    Array(Array(1,7,8), Array(1,9,10))
                );
                a::$a;
                a[1]::$func();
                Return;
            }
        }"""
        expect = "Error on line 16 col 21: ;"
        self.assertTrue(TestParser.test(test, expect, 298))

    def test_299(self):
        test = """
        Class Program {
            Var a, b: Array[Int, 5];
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
        expect = "Error on line 13 col 26: ==."
        self.assertTrue(TestParser.test(test, expect, 299))

    def test_300(self):
        test = """
        Class Program {
            Var a, b: Array[Int, 5];
            Var c: Array[String, 10_0];
            main() {
               a = 1;
               b = 2;
               c = Array();
               d = Array("1", "2", "3");
               e = Array(Array(1, 2, 3), Array(4, 5, 6));
            {
               c = a + b;
               c = a +. b ==. c;
               c = ((a - b) * (c / d)) + (e + f) % 5;
               c = d = e = f;
               c = d = 4;
            }
              
               d = "Something";
               Return;
            }
        }
        """
        expect = "Error on line 13 col 26: ==."
        self.assertTrue(TestParser.test(test, expect, 300))

    



          
        
        
    
    
        
    
        
    
    
    