import unittest
from TestUtils import TestLexer
class LexerSuite(unittest.TestCase):
   def test_101(self):
      test = """ "HelloPatty" 123"""
      exp =  """HelloPatty,123,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,101))
      
   def test_102(self):
      test = """"FirstString
      SecondString" """
      exp = """Unclosed String: FirstString"""
      self.assertTrue(TestLexer.test(test,exp,102))
      
   def test_103(self):
      test = "$getOfShape"
      exp = "$getOfShape,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,103))
      
   def test_104(self):
      test = "$hle_2;$0$___sIF39____42"
      exp = "$hle_2,;,$0,$___sIF39____42,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,104))
      
   def test_105(self):
      test = """ "abc\\h def"  """
      exp = "Illegal Escape In String: abc\h"
      self.assertTrue(TestLexer.test(test,exp,105))
      
   def test_106(self):
      test = "0_120 0x123_12ACD0 0B012 0.10"
      exp = "0,_120,0x12312ACD0,0B0,12,0.10,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,106))
      
   def test_107(self):
      test = "123a123"
      exp = "123,a123,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,107))
      
   def test_108(self): 
      test = """ "\\b\\r\\t" """
      exp = """\\b\\r\\t,<EOF>"""
      self.assertTrue(TestLexer.test(test, exp, 108))
      
   def test_109(self):
      test = "## ew ## 1.234 1. .e3 1.0e-2 10.e-2"
      exp = "1.234,1.,.e3,1.0e-2,10.e-2,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,109))
      
   def test_110(self):
      test = """ .9e-10 """
      exp = """.9e-10,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,110))
      
   def test_111(self):
      test = """ 0x123_AB """
      exp = "0x123AB,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,111))
      
   def test_112(self):
      test = """ "he said: '"abc'"" """
      exp = """he said: '\"abc'\",<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,112))
      
   def test_113(self):
      test = "\\n"
      exp = "Error Token \\"
      self.assertTrue(TestLexer.test(test,exp,113))
      
   def test_114(self):
      test = """ "    _\\v" """
      exp = "Illegal Escape In String:     _\\v"
      self.assertTrue(TestLexer.test(test,exp,114))
      
   def test_115(self):
      test = "\"12345\'\"6 \'\"7891234\""
      exp = "12345\'\"6 \'\"7891234,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,115))
      
   def test_116(self):
      test = """ "This is a string containing tab \\t" """
      exp =  "This is a string containing tab \\t,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,116))
      
   def test_117(self):
      test = "ELSEIFIF-In,If,ElseIf==.Else##new##Return(.,)"
      exp = "ELSEIFIF,-,In,,,If,,,ElseIf,==.,Else,Return,(,.,,,),<EOF>"
      self.assertTrue(TestLexer.test(test,exp, 117))
      
   def test_118(self):
      test = "(1*3)/(8-4*(3+9))"
      exp = "(,1,*,3,),/,(,8,-,4,*,(,3,+,9,),),<EOF>"
      self.assertTrue(TestLexer.test(test,exp,118))
      
   def test_119(self):
      test = "Int Break ForEach 1+2 Destructor"
      exp =  "Int,Break,ForEach,1,+,2,Destructor,<EOF>"
      self.assertTrue(TestLexer.test(test,exp, 119))
      
   def test_120(self):
      test = "\"\""
      exp = ",<EOF>"
      self.assertTrue(TestLexer.test(test,exp,120))
      
   def test_121(self):
      test = """_qZkys3Xbc ##"""
      exp = """_qZkys3Xbc,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,121))
      
   def test_122(self):
      test = """ "The string: """
      exp = "Unclosed String: The string: "
      self.assertTrue(TestLexer.test(test,exp,122))
      
   def test_123(self):
      test = """
      Class StringWorker{
         getString(someString : Float){
            Var someString: String = "hello PPL";
            Return someString;
         }
      }
        """
      exp = """Class,StringWorker,{,getString,(,someString,:,Float,),{,Var,someString,:,String,=,hello PPL,;,Return,someString,;,},},<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,123))
   
   def test_124(self):
      test = """ 
         Class foo {
            Var a : Int = Self.x() + $a.$10 % _12::_abc2 * _84.a12 - 09 + 0xB12_1N;
         }
      """
      exp = "Class,foo,{,Var,a,:,Int,=,Self,.,x,(,),+,$a,.,$10,%,_12,::,_abc2,*,_84,.,a12,-,0,9,+,0xB121,N,;,},<EOF>"
      self.assertTrue(TestLexer.test(test, exp, 124))
      
   def test_125(self):
      test = """ 
           2045o__e*53 0x0x0b9SE++
        """
      exp = "2045,o__e,*,53,0x0,x0b9SE,+,+,<EOF>"
      self.assertTrue(TestLexer.test(test, exp, 125))
      
   def test_126(self):
      test = """
         Foreach(y In 100 .. 300 By 0x5){
            $doNothing();
         } 
      """
      exp = """Foreach,(,y,In,100,..,300,By,0x5,),{,$doNothing,(,),;,},<EOF>"""
      self.assertTrue(TestLexer.test(test, exp, 126))
      
   def test_127(self):
      test = """-0B1001101"""
      exp = """-,0B1001101,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,127))
   
   def test_128(self):
      test = "Array[Int, 0x10_A_B]"
      exp = "Array,[,Int,,,0x10AB,],<EOF>"
      self.assertTrue(TestLexer.test(test,exp,128))
   
   def test_129(self):
      test = "1.E0_2523235"
      exp = "1.E0,_2523235,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,129))
   
   def test_130(self):
      test = """ "ABC: \\" """
      exp = """Illegal Escape In String: ABC: """ + "\\\""
      self.assertTrue(TestLexer.test(test, exp, 130))
      
   def test_131(self):
      test = "\"abc'\""
      exp = "Unclosed String: abc'\""
      self.assertTrue(TestLexer.test(test,exp,131))
      
   def test_132(self):
      test = """<= .== ##== <=<= ::- :::: ==>= Constructor:: ||:: -:: ||## >=== ==& <=== ||. >="""
      exp = """<=,.,==,>=,==,==,Error Token &"""
      self.assertTrue(TestLexer.test(test,exp,132))
      
   def test_133(self):
      test = """dH2-.7E635-537jKo1PYJr8c__G6fje8un_p_f VaVp32q_vcc A0EuLal $0"$H_r59t9JXw"""
      exp = """dH2,-,.7E635,-,537,jKo1PYJr8c__G6fje8un_p_f,VaVp32q_vcc,A0EuLal,$0,Unclosed String: $H_r59t9JXw"""
      self.assertTrue(TestLexer.test(test, exp, 133))
      
   def test_134(self):
      test = """True && False"""
      exp = """True,&&,False,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,134))
      
   def test_135(self):
      test = """ qA_ kMG4__f2I_zy XdPL50B-0B%E +9e-_ """
      exp = """qA_,kMG4__f2I_zy,XdPL50B,-,0,B,%,E,+,9,e,-,_,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,135))
      
   def test_136(self):
      test = """ "He asked me: \'"Where is John? \'"" || <=Self ##RinCPQhvs8 >=/ >=42d7XW6_Ix />= <=! <=|| <=JzELj7JIj3 ||## ||New >=LpOq8468f1 ==In =="""
      exp = """He asked me: \'"Where is John? \'",||,<=,Self,||,New,>=,LpOq8468f1,==,In,==,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,136))
      
   def test_137(self):
      self.assertTrue(TestLexer.test("""<= >=Elseif -|| Program== ::|| 88hk8DMcOyWNb2k_pmzu OML6pQnwSV>= Val:: pa4Xt1sdZM## <=<= ##""","""<=,>=,Elseif,-,||,Program,==,::,||,88,hk8DMcOyWNb2k_pmzu,OML6pQnwSV,>=,Val,::,pa4Xt1sdZM,<EOF>""",137))
   
   def test_138(self):
      test = 'Var urgay: Float = 0 + 0x0 - 0b0 + 00 % 0.0 / 0. + .0 * 0e2 + (.0e3 + 0.e3 - .e3 + e0);'
      exp = 'Var,urgay,:,Float,=,0,+,0x0,-,0b0,+,00,%,0.0,/,0.,+,.,0,*,0e2,+,(,.0e3,+,0.e3,-,.e3,+,e0,),;,<EOF>'
      self.assertTrue(TestLexer.test(test,exp, 138))
      
   def test_139(self):
      test = """ g__2_CF4a O6HSm3GemCZdrxFLt##"dasjklnmkqwiuhu##"S"""
      exp = """g__2_CF4a,O6HSm3GemCZdrxFLt,Unclosed String: S"""
      self.assertTrue(TestLexer.test(test, exp, 139))
      
   def test_140(self):
      test = "Array(1, 2, 3)"
      exp = "Array,(,1,,,2,,,3,),<EOF>"
      self.assertTrue(TestLexer.test(test,exp,140))
   
   def test_141(self):
      test = """ 0x00xA_CD1_200.0000.00E0.0E.0E"""
      exp = """0x0,0xACD1200,.,00,00,.00E0,.,0,E,.,0,E,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,141))
   
   def test_142(self):
      test = "*p = q[12] + -24 * (10.3e5 - 32);"
      exp = "*,p,=,q,[,12,],+,-,24,*,(,10.3e5,-,32,),;,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,142))
   
   def test_143(self):
      test = """< By|| <=>= >=& ==|| .|| Continue! ::|| !## ::% <"""
      exp = """<,By,||,<=,>=,>=,Error Token &"""
      self.assertTrue(TestLexer.test(test,exp,143))
   
   def test_144(self):
      test = "1_2.01e-11"
      exp = "12.01e-11,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,144))
   
   def test_145(self):
      test = """>= ##:: ||== ==== BreakIn ##>= <="""
      exp = """>=,>=,<=,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,145))
   
   def test_146(self):
      test = """##Class >=<= ##<= <=:: >=>= >=:: ==qNFgslkk8T mylOcdmhtx<= Int:: ##<=Program <=## ==>= ::<= <="""
      exp = "<=,<=,::,>=,>=,>=,::,==,qNFgslkk8T,mylOcdmhtx,<=,Int,::,==,>=,::,<=,<=,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,146))
   
   def test_147(self):
      test = """## ##- Main"""
      exp = """-,Main,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,147))
   
   def test_148(self):
      test = """## >=<= |||| -== ==AfDEQB3sPa BreakgiEtT4SPBM ##:: .+ #### !"""
      exp = """::,.,+,!,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,148))
   
   def test_149(self):
      test = 'Var a: String = b +. "Welcome to PPL \'course";'
      expect = 'Var,a,:,String,=,b,+.,Welcome to PPL \'course,;,<EOF>'
      self.assertTrue(TestLexer.test(test, expect, 149))
      
   def test_150(self):
      test = """WfTaMYjbLX ::> ==Constructor ||:: ==<= <- >CQjI3gjBmy ::<= >=|| >=>= Destructor>= ==|| ##|| ||== By## <=## >="""
      exp = """WfTaMYjbLX,::,>,==,Constructor,||,::,==,<=,<,-,>,CQjI3gjBmy,::,<=,>=,||,>=,>=,Destructor,>=,==,||,<=,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,150))
   
   def test_151(self):
      test = """## >=:: >=## <=jCM3xduNCz >=I7JzqkvfqH ||By ##>= ==P53A$GXMqp ##Class Programe6zYdCXHel KtIYkIOxAR>= #### JyAZ9S5lZ2:: ||Continue <="""
      exp = """<=,jCM3xduNCz,>=,I7JzqkvfqH,||,By,Class,Programe6zYdCXHel,KtIYkIOxAR,>=,JyAZ9S5lZ2,::,||,Continue,<=,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,151))
   
   def test_152(self):
      test = """Val a : Int = 1; ## Hello World ## b.call();"""
      exp = "Val,a,:,Int,=,1,;,b,.,call,(,),;,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,152))
   
   def test_153(self):
      test = """Class %Class KSCxqaxYSJInt oj15rQfFpR<= <=>= >=== Self5FGl_coSS "Hello World## " ## $ <=X17d$gapeR& ||< <=:: :::: Var== taaeKWlRA_ ||Float Class== kOHXVHUtTL>= <=:: <=|| >u1TBz40kgr"""
      exp = """Class,%,Class,KSCxqaxYSJInt,oj15rQfFpR,<=,<=,>=,>=,==,Self5FGl_coSS,Hello World## ,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,153))
   
   def test_154(self):
      test = """|| ##:: >=Array gyYssDTo8p<= >=## xvpJd0I94G>= ::Self Self== ==WM43eXT$yH >=- w1Ui8RzOrw>= >=<= ##== ==## llPkAPBVag% ::WPIhgq6hcC *## By## ::GHugnVcqhy Kj$HASlFiL## ||"""
      exp = """||,xvpJd0I94G,>=,::,Self,Self,==,==,WM43eXT,$yH,>=,-,w1Ui8RzOrw,>=,>=,<=,llPkAPBVag,%,::,WPIhgq6hcC,*,::,GHugnVcqhy,Kj,$HASlFiL,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,154))
   
   def test_155(self):
      test = """If ::Destructor 3bYuQSDOkj:: UNGbuy9MeX## ==>= ##<= >=== >|| >=<= <=== .MGuX1pdzHB By"""
      exp = """If,::,Destructor,3,bYuQSDOkj,::,UNGbuy9MeX,<=,>=,==,>,||,>=,<=,<=,==,.,MGuX1pdzHB,By,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,155))
   
   def test_156(self):
      test = """## !Return >== flv3XO9wkp:: ##>= <=|| DzIOef4Puk|| ||+ ##== ==<= =="""
      exp = """>=,<=,||,DzIOef4Puk,||,||,+,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,156))
   
   def test_157(self):
      test = '0xFFFFFFFF + 0b110101111 - 0X1122330F / (0123_321 * 0.0000000004 )+ 3.14E-10'
      exp = '0xFFFFFFFF,+,0b110101111,-,0X1122330F,/,(,0123321,*,0.0000000004,),+,3.14E-10,<EOF>'
      self.assertTrue(TestLexer.test(test,exp, 157))
   
   def test_158(self):
      test = """% ||In >=<= %== <=Int >=>= <=Continue ::>= ##Array >MtMbxOMoc0 >=== &+ <=== ||## RZwTZI$2_dgpPRaKc1c5 |||| <=New ##>= ::<= +"""
      exp = """%,||,In,>=,<=,%,==,<=,Int,>=,>=,<=,Continue,::,>=,RZwTZI,$2_dgpPRaKc1c5,||,||,<=,New,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,158))
   
   def test_159(self):
      test = """:: By|| In& ||CtdDTu42Jd ||BGiendXl65 <=mrRGsc9Ms5 ::== =="""
      exp = """::,By,||,In,Error Token &"""
      self.assertTrue(TestLexer.test(test,exp,159))
   
   def test_160(self):
      test = """<= qObYygmVF1* ||>= ::yCX$Oj8FhQ ==== .== UHhtFUuWoC- ##>= BX67g1erme## BreakForeach >=<= -## ||>= InProgram !MDTDX7JVaF +|| ::## <=== By. ##"""
      exp = """<=,qObYygmVF1,*,||,>=,::,yCX,$Oj8FhQ,==,==,.,==,UHhtFUuWoC,-,BreakForeach,>=,<=,-,<=,==,By,.,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,160))
   
   def test_161(self):
      test = """## ::Continue ##"""
      exp = """<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,161))
   
   def test_162(self):
      test = """|| ##By ==## ::== Continue 123_456_67"""
      exp = """||,::,==,Continue,12345667,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,162))
   
   def test_163(self):
      test = """<= ||= ||"""
      exp = """<=,||,=,||,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,163))
   
   def test_164(self):
      test = """. SelfArray ==:: Float:: <=NNMyzRF4pM ==<= ||## ##== <=o87n_7chHl <=## <=* ||## ==== #### Boolean"""
      exp = """.,SelfArray,==,::,Float,::,<=,NNMyzRF4pM,==,<=,||,==,<=,o87n_7chHl,<=,==,==,Boolean,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,164))
   
   def test_165(self):
      test = """+ >=* ::## ||/ <=>= <=<= *Var <=Foreach />= :::: >=<= ::Else <=## In>= ==:: ValBreak New"""
      exp = """+,>=,*,::,In,>=,==,::,ValBreak,New,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,165))
   
   def test_166(self):
      test = """Destructor "Im talking '"right now'"" ||## ##:: ::Program ||== Var## ##== |||| >=Else >== gR9HeKJXDI"""
      exp = """Destructor,Im talking '"right now'",||,::,::,Program,||,==,Var,==,||,||,>=,Else,>=,=,gR9HeKJXDI,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,166))
   
   def test_167(self):
      test = """== :::: #### >="""
      exp = """==,::,::,>=,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,167))
   
   def test_168(self):
      test = """>= ||+.New|| New|| ||>= >=>= .<= ::>= ||"""
      exp = """>=,||,+.,New,||,New,||,||,>=,>=,>=,.,<=,::,>=,||,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,168))
   
   def test_169(self):
      test = """+ String>= ##::  82fHxTEUHkTR45gM_$OK !:: ++ Array<= >=! -- ==## 12_3 ##== &% ##j5Z$7iodbQ ||"""
      exp = """+,String,>=,123,j5Z,$7iodbQ,||,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,169))
   
   def test_170(self):
      test = """|| ==>= ||>= >=<= ||>= :::: ||== ==## zAR62M6uezmzTqDcWLR2 ##> ##:: ||<= ||== ||<= ::== =="""
      exp = """||,==,>=,||,>=,>=,<=,||,>=,::,::,||,==,==,>,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,170))
   
   def test_171(self):
      test = """ "\\a" """
      exp = "Illegal Escape In String: \\a"
      self.assertTrue(TestLexer.test(test,exp,171))
   
   def test_172(self):
      test = """ \"abc\\\" """
      exp = "Illegal Escape In String: abc\\\""
      self.assertTrue(TestLexer.test(test,exp,172))
   
   def test_173(self):
      test = "0xContinue 0xBreak 0xFalse 0xString Val Var New"
      exp = "0xC,ontinue,0xB,reak,0xF,alse,0,xString,Val,Var,New,<EOF>"
      self.assertTrue(TestLexer.test(test,exp,173))
   
   def test_174(self):
      test = """5KfBQ_b0dL Break>= ::"""
      exp = """5,KfBQ_b0dL,Break,>=,::,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,174))
   
   def test_175(self):
      test = """ 
            Class program {
                Var x : Int = 10;
                get(ac,d,f: Int, b: Float) {
                    Var _12, a : Float = 12, 10.0;
                }
            }
        """
      exp = "Class,program,{,Var,x,:,Int,=,10,;,get,(,ac,,,d,,,f,:,Int,,,b,:,Float,),{,Var,_12,,,a,:,Float,=,12,,,10.0,;,},},<EOF>"
      self.assertTrue(TestLexer.test(test, exp, 175))
      
   def test_176(self):
      test = """:: ==! ||: ==|| ::<= ##"""
      exp = """::,==,!,||,:,==,||,::,<=,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,176))
   
   def test_177(self):
      test = """<= <=|| ::> />= :::: ::## ::_JTBhZNu8j .By =="""
      exp = """<=,<=,||,::,>,/,>=,::,::,::,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,177))
   
   def test_178(self):
      test = """Self <=:: ::<= ==: ==|| ::>= /<= +"""
      exp = """Self,<=,::,::,<=,==,:,==,||,::,>=,/,<=,+,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,178))
   
   def test_179(self):
      test = """## c5jfgIsSyCVal =Array <=<= ||XekO1TkAPm Program== >=% Self>= ||8i6bDK7Qw9 ||: tacx6E0q46>= >=>= ==== Float<= ##== ##|| <== >=|| ||! =="""
      exp = """==,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,179))
   
   def test_180(self):
      test = """oKkdTSbJsJ ||Continue ==8bQgB5yGS9 jMbljcqmBd<= >="""
      exp = """oKkdTSbJsJ,||,Continue,==,8,bQgB5yGS9,jMbljcqmBd,<=,>=,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,180))
   
   def test_181(self):
      test = """4IuQ8NwYHt >=:: ::<= Self>= <=:: !== <=Return >=|| <=|| <=> >=& =="""
      exp = """4,IuQ8NwYHt,>=,::,::,<=,Self,>=,<=,::,!=,=,<=,Return,>=,||,<=,||,<=,>,>=,Error Token &"""
      self.assertTrue(TestLexer.test(test,exp,181))
   
   def test_182(self):
      test = """>= /U01CA5fUXs >=. Program<= New## ||Main <<= iUk3ttV4hx|| ::>= Rl62M4pyNV* ||## <=:: ##Else #### >=<= ==33tthquSNc ||:: Class<= ::"""
      exp = """>=,/,U01CA5fUXs,>=,.,Program,<=,New,<=,::,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,182))
   
   def test_183(self):
      test = """## #### ==## ::0xAE15_617A:: %## .<= |||| |||| New>= SL3hXmdo6f>= Program== ||jOOPlXrRSz 0BDz7MZ2nk:: >=: gfTmtNCi9$jC9ceAsklE <=& ==>= ##Var ReturnElse <=## +"""
      exp = """::,0xAE15617A,::,%,Var,ReturnElse,<=,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,183))
   
   def test_184(self):
      test = """## <=<= VnhFTEyJmw"""
      exp = """Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,184))
   
   def test_185(self):
      test = """Var 0B01010101 ##>= tQ2unL0G1l<= |||| >=<= vMetFwx5$y|| <=>= ==## Elseif|| ==% ||== ##"""
      exp = """Var,0B0,1010101,Elseif,||,==,%,||,==,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,185))
   
   def test_186(self):
      test = """< ||Null ::: >=<= ==== :Return Constructor>= JgZAxbc67V|| :== ==## >=== ##<= .|| ||Var ::"""
      exp = """<,||,Null,::,:,>=,<=,==,==,:,Return,Constructor,>=,JgZAxbc67V,||,:,==,==,<=,.,||,||,Var,::,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,186))
   
   def test_187(self):
      test = """== <=Self ==:: Val>= >=:: >=Self ::== gLvqn$oKVN## =Constructor <a5jG$EfI8V <=|| <=|| <=|| :## <=% ==|| ||>= ka7GI3mslf## >=<= wlMtzqsz4v"""
      exp = """==,<=,Self,==,::,Val,>=,>=,::,>=,Self,::,==,gLvqn,$oKVN,<=,%,==,||,||,>=,ka7GI3mslf,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,187))
   
   def test_188(self):
      test = """== ##iBOeDdHmo9 ||"""
      exp = """==,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,188))
   
   def test_189(self):
      test = '__hp[idxArr[(3+2)*5/-(3*1)] = otherArr[idxArr[-3]]'
      exp = '__hp,[,idxArr,[,(,3,+,2,),*,5,/,-,(,3,*,1,),],=,otherArr,[,idxArr,[,-,3,],],<EOF>'
      self.assertTrue(TestLexer.test(test, exp, 189))
   
   def test_190(self):
      test = """|| 2__345 Ap8dmqNnSelf ElseTYNq1DVD >=:: ||"""
      exp = """||,2,__345,Ap8dmqNnSelf,ElseTYNq1DVD,>=,::,||,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,190))
   
   def test_191(self):
      test = """## ==:: !! ::Constructor <=Self ##== |||| ##Boolean ||>= ##Int ##Main ->= ##Destructor ==Boolean .>= Array== ==QiODSv2ev1 sk52YKSPRj== =="""
      exp = """==,||,||,Int,Destructor,==,Boolean,.,>=,Array,==,==,QiODSv2ev1,sk52YKSPRj,==,==,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,191))
   
   def test_192(self):
      test = """. Continue<= ::"""
      exp = """.,Continue,<=,::,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,192))
   
   def test_193(self):
      test = """8Obf2jW5m1 :By ==>= Foreach<= ##>= !|| $VMO_tpgZI:: ==<= ||## New>= Foreach== =CFKpgeb9Qu #### Array>= X5TEOHM9A9& 3E6FntlGBi% ::## Var>= Boolean:: ||"""
      exp = """8,Obf2jW5m1,:,By,==,>=,Foreach,<=,New,>=,Foreach,==,=,CFKpgeb9Qu,Array,>=,X5TEOHM9A9,Error Token &"""
      self.assertTrue(TestLexer.test(test,exp,193))
   
   def test_194(self):
      test = """i_D4DYiTBJ ##uUqF_rQOOi String:: ==>= ForeachSKum4F3aPV ##<= Foreach## +"""
      exp = """i_D4DYiTBJ,<=,Foreach,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,194))
   
   def test_195(self):
      test = """* ##= ::== ||>= ##|| ::SivGBVBBJ4 ||:: /:: ##== >=Class <=:: <=:: ||## IB3azeKxgC|| ==>= <=## <=:: ::|| Constructor|| ||"""
      exp = """*,||,::,SivGBVBBJ4,||,::,/,::,IB3azeKxgC,||,==,>=,<=,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,195))
   
   def test_196(self):
      test = """:: :::: .zBav5EUduz :::: ::"""
      exp = """::,::,::,.,zBav5EUduz,::,::,::,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,196))
   
   def test_197(self):
      test = """<= ==<= ||If >=## ./ ==qoGQP8ecIF EP3Z7dNg5ovqV9RmKWPJ ::<= String## ::== ==Array >=>= >=|| >=== ==:: ||== ==== ::B6D77KTBLN =="""
      exp = """<=,==,<=,||,If,>=,::,==,==,Array,>=,>=,>=,||,>=,==,==,::,||,==,==,==,::,B6D77KTBLN,==,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,197))
   
   def test_198(self):
      test = """|| ||Class S1$I4$oMR|| >=* ::>= >=== If## ||>= ::== >|| Programh7KeKU2RaU >=<= ##:: -Boolean ClassNew <=>= >=hDn$rE3M4 Val"""
      exp = """||,||,Class,S1,$I4,$oMR,||,>=,*,::,>=,>=,==,If,::,-,Boolean,ClassNew,<=,>=,>=,hDn,$rE3M4,Val,<EOF>"""
      self.assertTrue(TestLexer.test(test,exp,198))
   
   def test_199(self):
      test = """8VX_IX15d1 <=|| <String Float|| adYz1S5KsYNull ||## <=## #### <=|| ::Destructor <=:: ==mOc2RMEEYs :::: Int:: ##"""
      exp = """8,VX_IX15d1,<=,||,<,String,Float,||,adYz1S5KsYNull,||,<=,||,::,Destructor,<=,::,==,mOc2RMEEYs,::,::,Int,::,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,199))
   
   def test_200(self):
      test = """2_333_344 Boolean xVsygC71n5:: ==>= ||Destructor <=Return <## ::! >=Boolean :::: ||== ::<= >=:: #### ::<= ||## ##>= >=>= Break== <=:: Destructor"""
      exp = """2333344,Boolean,xVsygC71n5,::,==,>=,||,Destructor,<=,Return,<,Error Token #"""
      self.assertTrue(TestLexer.test(test,exp,200))

    