import unittest
from TestUtils import TestLexer
class LexerSuite(unittest.TestCase):
   def test_101(self):
      self.assertTrue(TestLexer.test(""" "Hello" 123""","""Hello,123,<EOF>""",101))
   def test_102(self):
      self.assertTrue(TestLexer.test("abc","abc,<EOF>",102))
   def test_103(self):
      self.assertTrue(TestLexer.test("$getNumOfShape","$getNumOfShape,<EOF>",103))
   def test_104(self):
      self.assertTrue(TestLexer.test("aCBbd3","aCBbd3,<EOF>",104))
   def test_105(self):
      self.assertTrue(TestLexer.test("aAsVN3","aAsVN3,<EOF>",105))
   def test_106(self):
      self.assertTrue(TestLexer.test("_jgh","_jgh,<EOF>",106))
   def test_107(self):
      self.assertTrue(TestLexer.test("123a123","123,a123,<EOF>",107))
   def test_108(self):
      self.assertTrue(TestLexer.test("123_123","123123,<EOF>",108))
   def test_109(self):
      self.assertTrue(TestLexer.test("## ew ##","<EOF>",109))
   def test_110(self):
      self.assertTrue(TestLexer.test(""" .9e-10 """,""".9e-10,<EOF>""",110))
   def test_111(self):
      self.assertTrue(TestLexer.test(""" 0x123_AB ""","0x123AB,<EOF>",111))
   def test_112(self):
      self.assertTrue(TestLexer.test("\"New\\y year\"","Illegal Escape In String: New\y",112))
   def test_113(self):
      self.assertTrue(TestLexer.test("\\n","Error Token \\",113))
   def test_114(self):
      self.assertTrue(TestLexer.test("\"\\b\"","Illegal Escape In String: \\b",114))
   def test_115(self):
      self.assertTrue(TestLexer.test("\"12345\'\"67891234\'\"","Unclosed String: 12345\'\"67891234\'\"",115))
   def test_116(self):
      self.assertTrue(TestLexer.test("\"12345\'\"6 \'\"7891234\"","12345\'\"6 \'\"7891234,<EOF>",116))
   def test_117(self):
      self.assertTrue(TestLexer.test("2*3","2,*,3,<EOF>",117))
   def test_118(self):
      self.assertTrue(TestLexer.test("(1*3)/(8-4*(3+9))","(,1,*,3,),/,(,8,-,4,*,(,3,+,9,),),<EOF>",118))
   def test_119(self):
      self.assertTrue(TestLexer.test("\"abc\\h def\"","Illegal Escape In String: abc\h",119))
   def test_120(self):
      self.assertTrue(TestLexer.test("\"\"",",<EOF>",120))
   def test_121(self):
      self.assertTrue(TestLexer.test("""_wZkyH3Xbc ##""","""_wZkyH3Xbc,Error Token #""",121))
   def test_122(self):
      self.assertTrue(TestLexer.test(""">= ##|| ##Val abc, dvc: Int ==""",""">=,Val,abc,,,dvc,:,Int,==,<EOF>""",122))
   def test_123(self):
      self.assertTrue(TestLexer.test("""/ ||:: /Val +Program >=* i2FGA20EnU== ##== By:: ##""","""/,||,::,/,Val,+,Program,>=,*,i2FGA20EnU,==,<EOF>""",123))
   def test_124(self):
      self.assertTrue(TestLexer.test("""|| _abc :::: <=""","""||,_abc,::,::,<=,<EOF>""",124))
   def test_125(self):
      self.assertTrue(TestLexer.test("""Var ##::## Hello ## _abbc ##""","""Var,Hello,<EOF>""",125))
   def test_126(self):
      self.assertTrue(TestLexer.test("""Constructor ||== <=95czeIbILe /|| ##|| ::""","""Constructor,||,==,<=,95,czeIbILe,/,||,Error Token #""",126))
   def test_127(self):
      self.assertTrue(TestLexer.test("""## .>= ==## #### Return## ||## |||| lweNtndVAV== ==String 7kzIG58TDX|| ==""","""Return,||,||,lweNtndVAV,==,==,String,7,kzIG58TDX,||,==,<EOF>""",127))
   def test_128(self):
      self.assertTrue(TestLexer.test("""|| ##""","""||,Error Token #""",128))
   def test_129(self):
      self.assertTrue(TestLexer.test("""## 2rDnLulZwmForeach ==## >=<= &== ==== <=>= ##>= #### |||| 5cSkUAUw$I== :::: >=<= ==* ::= ##If :::: ==<= ==>= +""",""">=,<=,Error Token &""",129))
   def test_130(self):
      self.assertTrue(TestLexer.test("""Main ::Var ||""","""Main,::,Var,||,<EOF>""",130))
   def test_131(self):
      self.assertTrue(TestLexer.test("""= _QQtX5FNVk! Continue|| Continue>= <=>= >=>= Main## <=<= Int|| ##|| ==<= .m0AZf7zrAW :::: ==<= >=+ >=>= Continue## >=""","""=,_QQtX5FNVk,!,Continue,||,Continue,>=,<=,>=,>=,>=,Main,||,==,<=,.,m0AZf7zrAW,::,::,==,<=,>=,+,>=,>=,Continue,Error Token #""",131))
   def test_132(self):
      self.assertTrue(TestLexer.test("""<= .== ##== <=<= ::- :::: ==>= Constructor:: ||:: -:: ||## >=== ==& <=== ||. >=""","""<=,.,==,>=,==,==,Error Token &""",132))
   def test_133(self):
      self.assertTrue(TestLexer.test("""|| >=. New< <=|| .:: ::""","""||,>=,.,New,<,<=,||,.,::,::,<EOF>""",133))
   def test_134(self):
      self.assertTrue(TestLexer.test(""">= ##|| ::""",""">=,Error Token #""",134))
   def test_135(self):
      self.assertTrue(TestLexer.test(""":: Constructor:: KCUsBuCbaw## XQKKv5gY52""","""::,Constructor,::,KCUsBuCbaw,Error Token #""",135))
   def test_136(self):
      self.assertTrue(TestLexer.test(""" "He asked me: \'"Where is John? \'"" || <=Self ##RinCPQhvs8 >=/ >=42d7XW6_Ix />= <=! <=|| <=JzELj7JIj3 ||## ||New >=LpOq8468f1 ==In ==## ::>= ||""","""He asked me: \'"Where is John? \'",||,<=,Self,||,New,>=,LpOq8468f1,==,In,==,Error Token #""",136))
   def test_137(self):
      self.assertTrue(TestLexer.test("""<= >=Elseif -|| Program== ::|| 88hk8DMcOyWNb2k_pmzu OML6pQnwSV>= Val:: pa4Xt1sdZM## <=<= ##""","""<=,>=,Elseif,-,||,Program,==,::,||,88,hk8DMcOyWNb2k_pmzu,OML6pQnwSV,>=,Val,::,pa4Xt1sdZM,<EOF>""",137))
   def test_138(self):
      input = 'Var urgay: Float = 0 + 0x0 - 0b0 + 00 % 0.0 / 0. + .0 * 0e2 + (.0e3 + 0.e3 - .e3 + e0);'
      expect = 'Var,urgay,:,Float,=,0,+,0x0,-,0b0,+,00,%,0.0,/,0.,+,.,0,*,0e2,+,(,.0e3,+,0.e3,-,.e3,+,e0,),;,<EOF>'
      self.assertTrue(TestLexer.test(input, expect, 138))
   def test_139(self):
      self.assertTrue(TestLexer.test("""## VxpT$lLYZn. <=> ::AGz569YYpd ||:: <=> <=<= ||36scLLzWju %|| ::""","""Error Token #""",139))
   def test_140(self):
      self.assertTrue(TestLexer.test("""== 12.000210 ||== =+ Ss0fqa0e1F<= ==<= ||> gGzpBRwbOU""","""==,12.000210,||,==,=,+,Ss0fqa0e1F,<=,==,<=,||,>,gGzpBRwbOU,<EOF>""",140))
   def test_141(self):
      self.assertTrue(TestLexer.test(""">= ||:: >=<= :::: +:: >=== TG8v7gab6R== mQNxG3UcHT% :>= <=:: ==UaKhF60wp1 FPhWQ5AhvB== ||""",""">=,||,::,>=,<=,::,::,+,::,>=,==,TG8v7gab6R,==,mQNxG3UcHT,%,:,>=,<=,::,==,UaKhF60wp1,FPhWQ5AhvB,==,||,<EOF>""",141))
   def test_142(self):
      self.assertTrue(TestLexer.test("""<= >=>= ::! Elseif|| ##Destructor ||>= aUMAuJK0HzwsFZ4mvp_y ==> &## === Boolean>= #### ::>= XlGeVkriWR>= >Self :== ##== MjdYlj89DI== ##|| >=""","""<=,>=,>=,::,!,Elseif,||,==,=,Boolean,>=,::,>=,XlGeVkriWR,>=,>,Self,:,==,||,>=,<EOF>""",142))
   def test_143(self):
      self.assertTrue(TestLexer.test("""< By|| <=>= >=& ==|| .|| Continue! ::|| !## ::% <""","""<,By,||,<=,>=,>=,Error Token &""",143))
   def test_144(self):
      self.assertTrue(TestLexer.test("""== >=## ##:: Constructor|| Self## ||<= ||% ::<= >=Constructor ::== ==Var >=Array ||## Zg1BJM034S## Var:: ##:: ==>= Returnr2Si0OTbmc Foreach>= ::b7SrL6NlWp >=""","""==,>=,::,Constructor,||,Self,Zg1BJM034S,::,==,>=,Returnr2Si0OTbmc,Foreach,>=,::,b7SrL6NlWp,>=,<EOF>""",144))
   def test_145(self):
      self.assertTrue(TestLexer.test(""">= ##:: ||== ==== BreakIn ##>= <=""",""">=,>=,<=,<EOF>""",145))
   def test_146(self):
      self.assertTrue(TestLexer.test("""Class >=<= ##<= <=:: >=>= >=:: ==qNFgslkk8T mylOcdmhtx<= Int:: <=Program <=## ==>= ::<= <=""","""Class,>=,<=,==,>=,::,<=,<=,<EOF>""",146))
   def test_147(self):
      self.assertTrue(TestLexer.test("""## ##- Main""","""-,Main,<EOF>""",147))
   def test_148(self):
      self.assertTrue(TestLexer.test("""## >=<= |||| -== ==AfDEQB3sPa BreakgiEtT4SPBM ##:: .+ #### !""","""::,.,+,!,<EOF>""",148))
   def test_149(self):
      self.assertTrue(TestLexer.test(""">= b2EnNimC_jElseif <=Var ##== :::: .## Array== ||<= Elseif>= >=## Array:: EDKlYrpdze> i9lc2zY0Nt## >=== ||. ##>= .|| ::* <=- <=""",""">=,b2EnNimC_jElseif,<=,Var,Array,==,||,<=,Elseif,>=,>=,>=,==,||,.,Error Token #""",149))
   def test_150(self):
      self.assertTrue(TestLexer.test("""WfTaMYjbLX ::> ==Constructor ||:: ==<= <- >CQjI3gjBmy ::<= >=|| >=>= Destructor>= ==|| ##|| ||== By## <=## >=""","""WfTaMYjbLX,::,>,==,Constructor,||,::,==,<=,<,-,>,CQjI3gjBmy,::,<=,>=,||,>=,>=,Destructor,>=,==,||,<=,Error Token #""",150))
   def test_151(self):
      self.assertTrue(TestLexer.test("""## >=:: >=## <=jCM3xduNCz >=I7JzqkvfqH ||By ##>= ==P53A$GXMqp ##Class Programe6zYdCXHel KtIYkIOxAR>= #### JyAZ9S5lZ2:: ||Continue <=""","""<=,jCM3xduNCz,>=,I7JzqkvfqH,||,By,Class,Programe6zYdCXHel,KtIYkIOxAR,>=,JyAZ9S5lZ2,::,||,Continue,<=,<EOF>""",151))
   def test_152(self):
      self.assertTrue(TestLexer.test("""* ::|| ##|| ||Array BKz_DxzPUz>= ||<= <! ::## Constructor:: ##|| <=## >=/ <=""","""*,::,||,Constructor,::,>=,/,<=,<EOF>""",152))
   def test_153(self):
      self.assertTrue(TestLexer.test("""Class %Class KSCxqaxYSJInt oj15rQfFpR<= <=>= >=== Self5FGl_coSS$ <=## X17d$gapeR& ||< <=:: :::: Var== taaeKWlRA_## ||Float Class== kOHXVHUtTL>= <=:: <=|| >u1TBz40kgr ##""","""Class,%,Class,KSCxqaxYSJInt,oj15rQfFpR,<=,<=,>=,>=,==,Self5FGl_coSS,Error Token $""",153))
   def test_154(self):
      self.assertTrue(TestLexer.test("""|| ##:: >=Array gyYssDTo8p<= >=## xvpJd0I94G>= ::Self Self== ==WM43eXT$yH >=- w1Ui8RzOrw>= >=<= ##== ==## llPkAPBVag% ::WPIhgq6hcC *## By## ::GHugnVcqhy Kj$HASlFiL## ||""","""||,xvpJd0I94G,>=,::,Self,Self,==,==,WM43eXT,$yH,>=,-,w1Ui8RzOrw,>=,>=,<=,llPkAPBVag,%,::,WPIhgq6hcC,*,::,GHugnVcqhy,Kj,$HASlFiL,Error Token #""",154))
   def test_155(self):
      self.assertTrue(TestLexer.test("""If ::Destructor 3bYuQSDOkj:: UNGbuy9MeX## ==>= ##<= >=== >|| >=<= <=== .MGuX1pdzHB By""","""If,::,Destructor,3,bYuQSDOkj,::,UNGbuy9MeX,<=,>=,==,>,||,>=,<=,<=,==,.,MGuX1pdzHB,By,<EOF>""",155))
   def test_156(self):
      self.assertTrue(TestLexer.test("""## !Return >== flv3XO9wkp:: ##>= <=|| DzIOef4Puk|| ||+ ##== ==<= ==""",""">=,<=,||,DzIOef4Puk,||,||,+,Error Token #""",156))
   def test_157(self):
      input = '0xFFFFFFFF + 0b110101111 - 0X1122330F / (0123321 * 0.0000000004 )+ 3.14E-10'
      expect = '0xFFFFFFFF,+,0b110101111,-,0X1122330F,/,(,0123321,*,0.0000000004,),+,3.14E-10,<EOF>'
      self.assertTrue(TestLexer.test(input, expect, 157))
   def test_158(self):
      self.assertTrue(TestLexer.test("""% ||In >=<= %== <=Int >=>= <=Continue ::>= ##Array >MtMbxOMoc0 >=== &+ <=== ||## RZwTZI$2_dgpPRaKc1c5 |||| <=New ##>= ::<= +""","""%,||,In,>=,<=,%,==,<=,Int,>=,>=,<=,Continue,::,>=,RZwTZI,Error Token $""",158))
   def test_159(self):
      self.assertTrue(TestLexer.test(""":: By|| In& ||CtdDTu42Jd ||BGiendXl65 <=mrRGsc9Ms5 ::== ==""","""::,By,||,In,Error Token &""",159))
   def test_160(self):
      self.assertTrue(TestLexer.test("""<= qObYygmVF1* ||>= ::yCX$Oj8FhQ ==== .== UHhtFUuWoC- ##>= BX67g1erme## BreakForeach >=<= -## ||>= InProgram !MDTDX7JVaF +|| ::## <=== By. ##""","""<=,qObYygmVF1,*,||,>=,::,yCX,$Oj8FhQ,==,==,.,==,UHhtFUuWoC,-,BreakForeach,>=,<=,-,<=,==,By,.,Error Token #""",160))
   def test_161(self):
      self.assertTrue(TestLexer.test("""## ::Continue ##""","""<EOF>""",161))
   def test_162(self):
      self.assertTrue(TestLexer.test("""|| ##By ==## ::== Continue""","""||,::,==,Continue,<EOF>""",162))
   def test_163(self):
      self.assertTrue(TestLexer.test("""<= ||= ||""","""<=,||,=,||,<EOF>""",163))
   def test_164(self):
      self.assertTrue(TestLexer.test(""". SelfArray ==:: Float:: <=NNMyzRF4pM ==<= ||## ##== <=o87n_7chHl <=## <=* ||## ==== #### Boolean""",""".,SelfArray,==,::,Float,::,<=,NNMyzRF4pM,==,<=,||,==,<=,o87n_7chHl,<=,==,==,Boolean,<EOF>""",164))
   def test_165(self):
      self.assertTrue(TestLexer.test("""+ >=* ::## ||/ <=>= <=<= *Var <=Foreach />= :::: >=<= ::Else <=## In>= ==:: ValBreak New""","""+,>=,*,::,In,>=,==,::,ValBreak,New,<EOF>""",165))
   def test_166(self):
      self.assertTrue(TestLexer.test("""Destructor ||## ##:: ::Program ||== Var## ##== |||| >=Else >== gR9HeKJXDI""","""Destructor,||,::,::,Program,||,==,Var,==,||,||,>=,Else,>=,=,gR9HeKJXDI,<EOF>""",166))
   def test_167(self):
      self.assertTrue(TestLexer.test("""== :::: #### >=""","""==,::,::,>=,<EOF>""",167))
   def test_168(self):
      self.assertTrue(TestLexer.test(""">= |||| New|| ||>= >=>= .<= ::>= ||""",""">=,||,||,New,||,||,>=,>=,>=,.,<=,::,>=,||,<EOF>""",168))
   def test_169(self):
      self.assertTrue(TestLexer.test("""+ String>= ##:: !:: <=== 82fHxTEUHkTR45gM_$OK Array<= >=! ==## ##== &% ##j5Z$7iodbQ ||""","""+,String,>=,j5Z,Error Token $""",169))
   def test_170(self):
      self.assertTrue(TestLexer.test("""|| ==>= ||>= >=<= ||>= :::: ||== ==## zAR62M6uezmzTqDcWLR2 ##> ##:: ||<= ||== ||<= ::== ==""","""||,==,>=,||,>=,>=,<=,||,>=,::,::,||,==,==,>,Error Token #""",170))
   def test_171(self):
      self.assertTrue(TestLexer.test(""" "\\a" ""","Illegal Escape In String: \\a",171))
   def test_172(self):
      self.assertTrue(TestLexer.test("\"","Unclosed String: ",172))
   def test_173(self):
      self.assertTrue(TestLexer.test("""% ::>= ##<= >=|| 3sxnoN_E6i:: ##Vd4yBroA_e Constructorliey2KIcbq <=<= ||LYipQs437N Else## ::Constructor <=:: Float<= <=""","""%,::,>=,Vd4yBroA_e,Constructorliey2KIcbq,<=,<=,||,LYipQs437N,Else,Error Token #""",173))
   def test_174(self):
      self.assertTrue(TestLexer.test("""5KfBQ_b0dL Break>= ::""","""5,KfBQ_b0dL,Break,>=,::,<EOF>""",174))
   def test_175(self):
      self.assertTrue(TestLexer.test("""== Q0TO7IOEe_== >=## l_cQkPFCmg% ##|| ##String !|| StringNew |||| oXyxipf90H% >=Float ==BXp5sa0Lq3 *== <=<= ||Program =""","""==,Q0TO7IOEe_,==,>=,||,Error Token #""",175))
   def test_176(self):
      self.assertTrue(TestLexer.test(""":: ==! ||: ==|| ::<= ##""","""::,==,!,||,:,==,||,::,<=,Error Token #""",176))
   def test_177(self):
      self.assertTrue(TestLexer.test("""<= <=|| ::> />= :::: ::## ::_JTBhZNu8j .By ==""","""<=,<=,||,::,>,/,>=,::,::,::,Error Token #""",177))
   def test_178(self):
      self.assertTrue(TestLexer.test("""Self <=:: ::<= ==: ==|| ::>= /<= +""","""Self,<=,::,::,<=,==,:,==,||,::,>=,/,<=,+,<EOF>""",178))
   def test_179(self):
      self.assertTrue(TestLexer.test("""## c5jfgIsSyCVal =Array <=<= ||XekO1TkAPm Program== >=% Self>= ||8i6bDK7Qw9 ||: tacx6E0q46>= >=>= ==== Float<= ##== ##|| <== >=|| ||! ==""","""==,Error Token #""",179))
   def test_180(self):
      self.assertTrue(TestLexer.test("""oKkdTSbJsJ ||Continue ==8bQgB5yGS9 jMbljcqmBd<= >=""","""oKkdTSbJsJ,||,Continue,==,8,bQgB5yGS9,jMbljcqmBd,<=,>=,<EOF>""",180))
   def test_181(self):
      self.assertTrue(TestLexer.test("""4IuQ8NwYHt >=:: ::<= Self>= <=:: !== <=Return >=|| <=|| <=> >=& ==""","""4,IuQ8NwYHt,>=,::,::,<=,Self,>=,<=,::,!=,=,<=,Return,>=,||,<=,||,<=,>,>=,Error Token &""",181))
   def test_182(self):
      self.assertTrue(TestLexer.test(""">= /U01CA5fUXs >=. Program<= New## ||Main <<= iUk3ttV4hx|| ::>= Rl62M4pyNV* ||## <=:: ##Else #### >=<= ==33tthquSNc ||:: Class<= ::""",""">=,/,U01CA5fUXs,>=,.,Program,<=,New,<=,::,Error Token #""",182))
   def test_183(self):
      self.assertTrue(TestLexer.test("""## #### ==## :::: %## .<= |||| |||| New>= SL3hXmdo6f>= Program== ||jOOPlXrRSz 0BDz7MZ2nk:: >=: gfTmtNCi9$jC9ceAsklE <=& ==>= ##Var ReturnElse <=## +""","""::,::,%,Var,ReturnElse,<=,Error Token #""",183))
   def test_184(self):
      self.assertTrue(TestLexer.test("""## <=<= VnhFTEyJmw""","""Error Token #""",184))
   def test_185(self):
      self.assertTrue(TestLexer.test("""Var ##>= tQ2unL0G1l<= |||| >=<= vMetFwx5$y|| <=>= ==## Elseif|| ==% ||== ##""","""Var,Elseif,||,==,%,||,==,Error Token #""",185))
   def test_186(self):
      self.assertTrue(TestLexer.test("""< ||Null ::: >=<= ==== :Return Constructor>= JgZAxbc67V|| :== ==## >=== ##<= .|| ||Var ::""","""<,||,Null,::,:,>=,<=,==,==,:,Return,Constructor,>=,JgZAxbc67V,||,:,==,==,<=,.,||,||,Var,::,<EOF>""",186))
   def test_187(self):
      self.assertTrue(TestLexer.test("""== <=Self ==:: Val>= >=:: >=Self ::== gLvqn$oKVN## =Constructor <a5jG$EfI8V <=|| <=|| <=|| :## <=% ==|| ||>= ka7GI3mslf## >=<= wlMtzqsz4v""","""==,<=,Self,==,::,Val,>=,>=,::,>=,Self,::,==,gLvqn,$oKVN,<=,%,==,||,||,>=,ka7GI3mslf,Error Token #""",187))
   def test_188(self):
      self.assertTrue(TestLexer.test("""== ##iBOeDdHmo9 ||""","""==,Error Token #""",188))
   def test_189(self):
      input = '__hp[idxArr[(3+2)*5/-(3*1)] = otherArr[idxArr[-3]]'
      expect = '__hp,[,idxArr,[,(,3,+,2,),*,5,/,-,(,3,*,1,),],=,otherArr,[,idxArr,[,-,3,],],<EOF>'
      self.assertTrue(TestLexer.test(input, expect, 189))
   def test_190(self):
      self.assertTrue(TestLexer.test("""|| 2__345 ApiD8dmqNnSelf ElseTYNq1XFDVD >=:: ||""","""||,2,__345,ApiD8dmqNnSelf,ElseTYNq1XFDVD,>=,::,||,<EOF>""",190))
   def test_191(self):
      self.assertTrue(TestLexer.test("""## ==:: !! ::Constructor <=Self ##== |||| ##Boolean ||>= ##Int ##Main ->= ##Destructor ==Boolean .>= Array== ==QiODSv2ev1 sk52YKSPRj== ==""","""==,||,||,Int,Destructor,==,Boolean,.,>=,Array,==,==,QiODSv2ev1,sk52YKSPRj,==,==,<EOF>""",191))
   def test_192(self):
      self.assertTrue(TestLexer.test(""". Continue<= ::""",""".,Continue,<=,::,<EOF>""",192))
   def test_193(self):
      self.assertTrue(TestLexer.test("""8Obf2jW5m1 :By ==>= Foreach<= ##>= !|| $VMO_tpgZI:: ==<= ||## New>= Foreach== =CFKpgeb9Qu #### Array>= X5TEOHM9A9& 3E6FntlGBi% ::## Var>= Boolean:: ||""","""8,Obf2jW5m1,:,By,==,>=,Foreach,<=,New,>=,Foreach,==,=,CFKpgeb9Qu,Array,>=,X5TEOHM9A9,Error Token &""",193))
   def test_194(self):
      self.assertTrue(TestLexer.test("""i_D4DYiTBJ ##uUqF_rQOOi String:: ==>= ForeachSKum4F3aPV ##<= Foreach## +""","""i_D4DYiTBJ,<=,Foreach,Error Token #""",194))
   def test_195(self):
      self.assertTrue(TestLexer.test("""* ##= ::== ||>= ##|| ::SivGBVBBJ4 ||:: /:: ##== >=Class <=:: <=:: ||## IB3azeKxgC|| ==>= <=## <=:: ::|| Constructor|| ||""","""*,||,::,SivGBVBBJ4,||,::,/,::,IB3azeKxgC,||,==,>=,<=,Error Token #""",195))
   def test_196(self):
      self.assertTrue(TestLexer.test(""":: :::: .zBav5EUduz :::: ::""","""::,::,::,.,zBav5EUduz,::,::,::,<EOF>""",196))
   def test_197(self):
      self.assertTrue(TestLexer.test("""<= ==<= ||If >=## ./ ==qoGQP8ecIF EP3Z7dNg5ovqV9RmKWPJ ::<= String## ::== ==Array >=>= >=|| >=== ==:: ||== ==== ::B6D77KTBLN ==""","""<=,==,<=,||,If,>=,::,==,==,Array,>=,>=,>=,||,>=,==,==,::,||,==,==,==,::,B6D77KTBLN,==,<EOF>""",197))
   def test_198(self):
      self.assertTrue(TestLexer.test("""|| ||Class S1$I4$oMR|| >=* ::>= >=== If## ||>= ::== >|| Programh7KeKU2RaU >=<= ##:: -Boolean ClassNew <=>= >=hDn$rE3M4 Val""","""||,||,Class,S1,$I4,$oMR,||,>=,*,::,>=,>=,==,If,::,-,Boolean,ClassNew,<=,>=,>=,hDn,$rE3M4,Val,<EOF>""",198))
   def test_199(self):
      self.assertTrue(TestLexer.test("""8VX_IX15d1 <=|| <String Float|| adYz1S5KsYNull ||## <=## #### <=|| ::Destructor <=:: ==mOc2RMEEYs :::: Int:: ##""","""8,VX_IX15d1,<=,||,<,String,Float,||,adYz1S5KsYNull,||,<=,||,::,Destructor,<=,::,==,mOc2RMEEYs,::,::,Int,::,Error Token #""",199))
   def test_200(self):
      self.assertTrue(TestLexer.test("""2_333_344 Boolean xVsygC71n5:: ==>= ||Destructor <=Return <## ::! >=Boolean :::: ||== ::<= >=:: #### ::<= ||## ##>= >=>= Break== <=:: Destructor""","""2333344,Boolean,xVsygC71n5,::,==,>=,||,Destructor,<=,Return,<,Error Token #""",200))