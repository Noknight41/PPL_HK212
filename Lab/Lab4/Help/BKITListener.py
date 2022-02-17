# Generated from BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete listener for a parse tree produced by BKITParser.
class BKITListener(ParseTreeListener):

    # Enter a parse tree produced by BKITParser#program.
    def enterProgram(self, ctx:BKITParser.ProgramContext):
        pass

    # Exit a parse tree produced by BKITParser#program.
    def exitProgram(self, ctx:BKITParser.ProgramContext):
        pass


    # Enter a parse tree produced by BKITParser#bclasses.
    def enterBclasses(self, ctx:BKITParser.BclassesContext):
        pass

    # Exit a parse tree produced by BKITParser#bclasses.
    def exitBclasses(self, ctx:BKITParser.BclassesContext):
        pass


    # Enter a parse tree produced by BKITParser#bclass.
    def enterBclass(self, ctx:BKITParser.BclassContext):
        pass

    # Exit a parse tree produced by BKITParser#bclass.
    def exitBclass(self, ctx:BKITParser.BclassContext):
        pass


    # Enter a parse tree produced by BKITParser#class_body.
    def enterClass_body(self, ctx:BKITParser.Class_bodyContext):
        pass

    # Exit a parse tree produced by BKITParser#class_body.
    def exitClass_body(self, ctx:BKITParser.Class_bodyContext):
        pass


    # Enter a parse tree produced by BKITParser#class_stmt_list.
    def enterClass_stmt_list(self, ctx:BKITParser.Class_stmt_listContext):
        pass

    # Exit a parse tree produced by BKITParser#class_stmt_list.
    def exitClass_stmt_list(self, ctx:BKITParser.Class_stmt_listContext):
        pass


    # Enter a parse tree produced by BKITParser#class_stmt.
    def enterClass_stmt(self, ctx:BKITParser.Class_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#class_stmt.
    def exitClass_stmt(self, ctx:BKITParser.Class_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#funcdecl.
    def enterFuncdecl(self, ctx:BKITParser.FuncdeclContext):
        pass

    # Exit a parse tree produced by BKITParser#funcdecl.
    def exitFuncdecl(self, ctx:BKITParser.FuncdeclContext):
        pass


    # Enter a parse tree produced by BKITParser#id_vas.
    def enterId_vas(self, ctx:BKITParser.Id_vasContext):
        pass

    # Exit a parse tree produced by BKITParser#id_vas.
    def exitId_vas(self, ctx:BKITParser.Id_vasContext):
        pass


    # Enter a parse tree produced by BKITParser#id_va.
    def enterId_va(self, ctx:BKITParser.Id_vaContext):
        pass

    # Exit a parse tree produced by BKITParser#id_va.
    def exitId_va(self, ctx:BKITParser.Id_vaContext):
        pass


    # Enter a parse tree produced by BKITParser#valdecl.
    def enterValdecl(self, ctx:BKITParser.ValdeclContext):
        pass

    # Exit a parse tree produced by BKITParser#valdecl.
    def exitValdecl(self, ctx:BKITParser.ValdeclContext):
        pass


    # Enter a parse tree produced by BKITParser#vardecl.
    def enterVardecl(self, ctx:BKITParser.VardeclContext):
        pass

    # Exit a parse tree produced by BKITParser#vardecl.
    def exitVardecl(self, ctx:BKITParser.VardeclContext):
        pass


    # Enter a parse tree produced by BKITParser#constructor.
    def enterConstructor(self, ctx:BKITParser.ConstructorContext):
        pass

    # Exit a parse tree produced by BKITParser#constructor.
    def exitConstructor(self, ctx:BKITParser.ConstructorContext):
        pass


    # Enter a parse tree produced by BKITParser#destructor.
    def enterDestructor(self, ctx:BKITParser.DestructorContext):
        pass

    # Exit a parse tree produced by BKITParser#destructor.
    def exitDestructor(self, ctx:BKITParser.DestructorContext):
        pass


    # Enter a parse tree produced by BKITParser#datatype.
    def enterDatatype(self, ctx:BKITParser.DatatypeContext):
        pass

    # Exit a parse tree produced by BKITParser#datatype.
    def exitDatatype(self, ctx:BKITParser.DatatypeContext):
        pass


    # Enter a parse tree produced by BKITParser#dttype.
    def enterDttype(self, ctx:BKITParser.DttypeContext):
        pass

    # Exit a parse tree produced by BKITParser#dttype.
    def exitDttype(self, ctx:BKITParser.DttypeContext):
        pass


    # Enter a parse tree produced by BKITParser#param.
    def enterParam(self, ctx:BKITParser.ParamContext):
        pass

    # Exit a parse tree produced by BKITParser#param.
    def exitParam(self, ctx:BKITParser.ParamContext):
        pass


    # Enter a parse tree produced by BKITParser#paramlist.
    def enterParamlist(self, ctx:BKITParser.ParamlistContext):
        pass

    # Exit a parse tree produced by BKITParser#paramlist.
    def exitParamlist(self, ctx:BKITParser.ParamlistContext):
        pass


    # Enter a parse tree produced by BKITParser#bidlist.
    def enterBidlist(self, ctx:BKITParser.BidlistContext):
        pass

    # Exit a parse tree produced by BKITParser#bidlist.
    def exitBidlist(self, ctx:BKITParser.BidlistContext):
        pass


    # Enter a parse tree produced by BKITParser#idlist.
    def enterIdlist(self, ctx:BKITParser.IdlistContext):
        pass

    # Exit a parse tree produced by BKITParser#idlist.
    def exitIdlist(self, ctx:BKITParser.IdlistContext):
        pass


    # Enter a parse tree produced by BKITParser#valuelist.
    def enterValuelist(self, ctx:BKITParser.ValuelistContext):
        pass

    # Exit a parse tree produced by BKITParser#valuelist.
    def exitValuelist(self, ctx:BKITParser.ValuelistContext):
        pass


    # Enter a parse tree produced by BKITParser#arraylist.
    def enterArraylist(self, ctx:BKITParser.ArraylistContext):
        pass

    # Exit a parse tree produced by BKITParser#arraylist.
    def exitArraylist(self, ctx:BKITParser.ArraylistContext):
        pass


    # Enter a parse tree produced by BKITParser#blockstmt.
    def enterBlockstmt(self, ctx:BKITParser.BlockstmtContext):
        pass

    # Exit a parse tree produced by BKITParser#blockstmt.
    def exitBlockstmt(self, ctx:BKITParser.BlockstmtContext):
        pass


    # Enter a parse tree produced by BKITParser#stmtlist.
    def enterStmtlist(self, ctx:BKITParser.StmtlistContext):
        pass

    # Exit a parse tree produced by BKITParser#stmtlist.
    def exitStmtlist(self, ctx:BKITParser.StmtlistContext):
        pass


    # Enter a parse tree produced by BKITParser#stmt.
    def enterStmt(self, ctx:BKITParser.StmtContext):
        pass

    # Exit a parse tree produced by BKITParser#stmt.
    def exitStmt(self, ctx:BKITParser.StmtContext):
        pass


    # Enter a parse tree produced by BKITParser#semi_stmt.
    def enterSemi_stmt(self, ctx:BKITParser.Semi_stmtContext):
        pass

    # Exit a parse tree produced by BKITParser#semi_stmt.
    def exitSemi_stmt(self, ctx:BKITParser.Semi_stmtContext):
        pass


    # Enter a parse tree produced by BKITParser#bid_vas.
    def enterBid_vas(self, ctx:BKITParser.Bid_vasContext):
        pass

    # Exit a parse tree produced by BKITParser#bid_vas.
    def exitBid_vas(self, ctx:BKITParser.Bid_vasContext):
        pass


    # Enter a parse tree produced by BKITParser#bid_va.
    def enterBid_va(self, ctx:BKITParser.Bid_vaContext):
        pass

    # Exit a parse tree produced by BKITParser#bid_va.
    def exitBid_va(self, ctx:BKITParser.Bid_vaContext):
        pass


    # Enter a parse tree produced by BKITParser#bvardecl.
    def enterBvardecl(self, ctx:BKITParser.BvardeclContext):
        pass

    # Exit a parse tree produced by BKITParser#bvardecl.
    def exitBvardecl(self, ctx:BKITParser.BvardeclContext):
        pass


    # Enter a parse tree produced by BKITParser#bvaldecl.
    def enterBvaldecl(self, ctx:BKITParser.BvaldeclContext):
        pass

    # Exit a parse tree produced by BKITParser#bvaldecl.
    def exitBvaldecl(self, ctx:BKITParser.BvaldeclContext):
        pass


    # Enter a parse tree produced by BKITParser#scalar.
    def enterScalar(self, ctx:BKITParser.ScalarContext):
        pass

    # Exit a parse tree produced by BKITParser#scalar.
    def exitScalar(self, ctx:BKITParser.ScalarContext):
        pass


    # Enter a parse tree produced by BKITParser#index_scalar.
    def enterIndex_scalar(self, ctx:BKITParser.Index_scalarContext):
        pass

    # Exit a parse tree produced by BKITParser#index_scalar.
    def exitIndex_scalar(self, ctx:BKITParser.Index_scalarContext):
        pass


    # Enter a parse tree produced by BKITParser#varass.
    def enterVarass(self, ctx:BKITParser.VarassContext):
        pass

    # Exit a parse tree produced by BKITParser#varass.
    def exitVarass(self, ctx:BKITParser.VarassContext):
        pass


    # Enter a parse tree produced by BKITParser#func.
    def enterFunc(self, ctx:BKITParser.FuncContext):
        pass

    # Exit a parse tree produced by BKITParser#func.
    def exitFunc(self, ctx:BKITParser.FuncContext):
        pass


    # Enter a parse tree produced by BKITParser#dollarfunc.
    def enterDollarfunc(self, ctx:BKITParser.DollarfuncContext):
        pass

    # Exit a parse tree produced by BKITParser#dollarfunc.
    def exitDollarfunc(self, ctx:BKITParser.DollarfuncContext):
        pass


    # Enter a parse tree produced by BKITParser#funccall.
    def enterFunccall(self, ctx:BKITParser.FunccallContext):
        pass

    # Exit a parse tree produced by BKITParser#funccall.
    def exitFunccall(self, ctx:BKITParser.FunccallContext):
        pass


    # Enter a parse tree produced by BKITParser#returnal.
    def enterReturnal(self, ctx:BKITParser.ReturnalContext):
        pass

    # Exit a parse tree produced by BKITParser#returnal.
    def exitReturnal(self, ctx:BKITParser.ReturnalContext):
        pass


    # Enter a parse tree produced by BKITParser#cont.
    def enterCont(self, ctx:BKITParser.ContContext):
        pass

    # Exit a parse tree produced by BKITParser#cont.
    def exitCont(self, ctx:BKITParser.ContContext):
        pass


    # Enter a parse tree produced by BKITParser#brk.
    def enterBrk(self, ctx:BKITParser.BrkContext):
        pass

    # Exit a parse tree produced by BKITParser#brk.
    def exitBrk(self, ctx:BKITParser.BrkContext):
        pass


    # Enter a parse tree produced by BKITParser#forstmt.
    def enterForstmt(self, ctx:BKITParser.ForstmtContext):
        pass

    # Exit a parse tree produced by BKITParser#forstmt.
    def exitForstmt(self, ctx:BKITParser.ForstmtContext):
        pass


    # Enter a parse tree produced by BKITParser#ifstmt.
    def enterIfstmt(self, ctx:BKITParser.IfstmtContext):
        pass

    # Exit a parse tree produced by BKITParser#ifstmt.
    def exitIfstmt(self, ctx:BKITParser.IfstmtContext):
        pass


    # Enter a parse tree produced by BKITParser#ifpart.
    def enterIfpart(self, ctx:BKITParser.IfpartContext):
        pass

    # Exit a parse tree produced by BKITParser#ifpart.
    def exitIfpart(self, ctx:BKITParser.IfpartContext):
        pass


    # Enter a parse tree produced by BKITParser#else_part.
    def enterElse_part(self, ctx:BKITParser.Else_partContext):
        pass

    # Exit a parse tree produced by BKITParser#else_part.
    def exitElse_part(self, ctx:BKITParser.Else_partContext):
        pass


    # Enter a parse tree produced by BKITParser#expr.
    def enterExpr(self, ctx:BKITParser.ExprContext):
        pass

    # Exit a parse tree produced by BKITParser#expr.
    def exitExpr(self, ctx:BKITParser.ExprContext):
        pass


    # Enter a parse tree produced by BKITParser#term1.
    def enterTerm1(self, ctx:BKITParser.Term1Context):
        pass

    # Exit a parse tree produced by BKITParser#term1.
    def exitTerm1(self, ctx:BKITParser.Term1Context):
        pass


    # Enter a parse tree produced by BKITParser#term2.
    def enterTerm2(self, ctx:BKITParser.Term2Context):
        pass

    # Exit a parse tree produced by BKITParser#term2.
    def exitTerm2(self, ctx:BKITParser.Term2Context):
        pass


    # Enter a parse tree produced by BKITParser#term3.
    def enterTerm3(self, ctx:BKITParser.Term3Context):
        pass

    # Exit a parse tree produced by BKITParser#term3.
    def exitTerm3(self, ctx:BKITParser.Term3Context):
        pass


    # Enter a parse tree produced by BKITParser#term4.
    def enterTerm4(self, ctx:BKITParser.Term4Context):
        pass

    # Exit a parse tree produced by BKITParser#term4.
    def exitTerm4(self, ctx:BKITParser.Term4Context):
        pass


    # Enter a parse tree produced by BKITParser#term5.
    def enterTerm5(self, ctx:BKITParser.Term5Context):
        pass

    # Exit a parse tree produced by BKITParser#term5.
    def exitTerm5(self, ctx:BKITParser.Term5Context):
        pass


    # Enter a parse tree produced by BKITParser#term6.
    def enterTerm6(self, ctx:BKITParser.Term6Context):
        pass

    # Exit a parse tree produced by BKITParser#term6.
    def exitTerm6(self, ctx:BKITParser.Term6Context):
        pass


    # Enter a parse tree produced by BKITParser#term7.
    def enterTerm7(self, ctx:BKITParser.Term7Context):
        pass

    # Exit a parse tree produced by BKITParser#term7.
    def exitTerm7(self, ctx:BKITParser.Term7Context):
        pass


    # Enter a parse tree produced by BKITParser#term8.
    def enterTerm8(self, ctx:BKITParser.Term8Context):
        pass

    # Exit a parse tree produced by BKITParser#term8.
    def exitTerm8(self, ctx:BKITParser.Term8Context):
        pass


    # Enter a parse tree produced by BKITParser#term9.
    def enterTerm9(self, ctx:BKITParser.Term9Context):
        pass

    # Exit a parse tree produced by BKITParser#term9.
    def exitTerm9(self, ctx:BKITParser.Term9Context):
        pass


    # Enter a parse tree produced by BKITParser#term10.
    def enterTerm10(self, ctx:BKITParser.Term10Context):
        pass

    # Exit a parse tree produced by BKITParser#term10.
    def exitTerm10(self, ctx:BKITParser.Term10Context):
        pass


    # Enter a parse tree produced by BKITParser#sd.
    def enterSd(self, ctx:BKITParser.SdContext):
        pass

    # Exit a parse tree produced by BKITParser#sd.
    def exitSd(self, ctx:BKITParser.SdContext):
        pass


    # Enter a parse tree produced by BKITParser#sdc.
    def enterSdc(self, ctx:BKITParser.SdcContext):
        pass

    # Exit a parse tree produced by BKITParser#sdc.
    def exitSdc(self, ctx:BKITParser.SdcContext):
        pass


    # Enter a parse tree produced by BKITParser#intlit.
    def enterIntlit(self, ctx:BKITParser.IntlitContext):
        pass

    # Exit a parse tree produced by BKITParser#intlit.
    def exitIntlit(self, ctx:BKITParser.IntlitContext):
        pass


    # Enter a parse tree produced by BKITParser#array.
    def enterArray(self, ctx:BKITParser.ArrayContext):
        pass

    # Exit a parse tree produced by BKITParser#array.
    def exitArray(self, ctx:BKITParser.ArrayContext):
        pass



del BKITParser