# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bclass.
    def visitBclass(self, ctx:D96Parser.BclassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_stmt.
    def visitClass_stmt(self, ctx:D96Parser.Class_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_vas.
    def visitId_vas(self, ctx:D96Parser.Id_vasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#id_va.
    def visitId_va(self, ctx:D96Parser.Id_vaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#valdecl.
    def visitValdecl(self, ctx:D96Parser.ValdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#vardecl.
    def visitVardecl(self, ctx:D96Parser.VardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funcdecl.
    def visitFuncdecl(self, ctx:D96Parser.FuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#paramlist.
    def visitParamlist(self, ctx:D96Parser.ParamlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bidlist.
    def visitBidlist(self, ctx:D96Parser.BidlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#valuelist.
    def visitValuelist(self, ctx:D96Parser.ValuelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#blockstmt.
    def visitBlockstmt(self, ctx:D96Parser.BlockstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmtlist.
    def visitStmtlist(self, ctx:D96Parser.StmtlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#semi_stmt.
    def visitSemi_stmt(self, ctx:D96Parser.Semi_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bid_vas.
    def visitBid_vas(self, ctx:D96Parser.Bid_vasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bid_va.
    def visitBid_va(self, ctx:D96Parser.Bid_vaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bvaldecl.
    def visitBvaldecl(self, ctx:D96Parser.BvaldeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#bvardecl.
    def visitBvardecl(self, ctx:D96Parser.BvardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_lhs.
    def visitIndex_lhs(self, ctx:D96Parser.Index_lhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#varass.
    def visitVarass(self, ctx:D96Parser.VarassContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#func.
    def visitFunc(self, ctx:D96Parser.FuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#dollarfunc.
    def visitDollarfunc(self, ctx:D96Parser.DollarfuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#funccall.
    def visitFunccall(self, ctx:D96Parser.FunccallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#rcb.
    def visitRcb(self, ctx:D96Parser.RcbContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#foreachstmt.
    def visitForeachstmt(self, ctx:D96Parser.ForeachstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifstmt.
    def visitIfstmt(self, ctx:D96Parser.IfstmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#ifpart.
    def visitIfpart(self, ctx:D96Parser.IfpartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#elseif_part.
    def visitElseif_part(self, ctx:D96Parser.Elseif_partContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#datatype.
    def visitDatatype(self, ctx:D96Parser.DatatypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#dttype.
    def visitDttype(self, ctx:D96Parser.DttypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#dttyp.
    def visitDttyp(self, ctx:D96Parser.DttypContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term1.
    def visitTerm1(self, ctx:D96Parser.Term1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term2.
    def visitTerm2(self, ctx:D96Parser.Term2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term3.
    def visitTerm3(self, ctx:D96Parser.Term3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term4.
    def visitTerm4(self, ctx:D96Parser.Term4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term5.
    def visitTerm5(self, ctx:D96Parser.Term5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term6.
    def visitTerm6(self, ctx:D96Parser.Term6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term7.
    def visitTerm7(self, ctx:D96Parser.Term7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#index_operators.
    def visitIndex_operators(self, ctx:D96Parser.Index_operatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term8.
    def visitTerm8(self, ctx:D96Parser.Term8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term9.
    def visitTerm9(self, ctx:D96Parser.Term9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#term10.
    def visitTerm10(self, ctx:D96Parser.Term10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#arrayCell.
    def visitArrayCell(self, ctx:D96Parser.ArrayCellContext):
        return self.visitChildren(ctx)



del D96Parser