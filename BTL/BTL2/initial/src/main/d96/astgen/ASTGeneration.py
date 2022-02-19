from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    ###
    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return Program(self.visit(ctx.bclasses()))

    ###
    # Visit a parse tree produced by D96Parser#bclasses.
    def visitBclasses(self, ctx:D96Parser.BclassesContext):
        if ctx.getChildCount() == 2:
            return self.visit(ctx.bclass()) + self.visit(ctx.bclasses())
        else:
            return self.visit(ctx.bclass())

    ###
    # Visit a parse tree produced by D96Parser#bclass.
    def visitBclass(self, ctx:D96Parser.BclassContext):
        body = self.visit(ctx.class_body())
        if ctx.getChildCount() == 3:
            return [ClassDecl(Id(ctx.ID(0).getText()), body)]
        else:
            return [ClassDecl(Id(ctx.ID(0).getText()), body, Id(ctx.ID(1).getText()))]

    ###
    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        if ctx.class_stmt_list():
            return self.visit(ctx.class_stmt_list())
        else:
            return []

    ###
    # Visit a parse tree produced by D96Parser#class_stmt_list.
    def visitClass_stmt_list(self, ctx:D96Parser.Class_stmt_listContext):
        if ctx.class_stmt_list():
            return self.visit(ctx.class_stmt()) + self.visit(ctx.class_stmt_list())
        else:
            return self.visit(ctx.class_stmt())

    ###
    # Visit a parse tree produced by D96Parser#class_stmt.
    def visitClass_stmt(self, ctx:D96Parser.Class_stmtContext):
        if ctx.constructor():
            return [self.visit(ctx.constructor())]
        elif ctx.destructor():
            return [self.visit(ctx.destructor())]
        elif ctx.funcdecl():
            return [self.visit(ctx.funcdecl())]
        elif ctx.valdecl():
            return self.visit(ctx.valdecl())
        else:
            return self.visit(ctx.vardecl())
    
    ### 
    # Visit a parse tree produced by D96Parser#funcdecl.
    def visitFuncdecl(self, ctx:D96Parser.FuncdeclContext):
        if ctx.ID():
            if ctx.paramlist():
                return MethodDecl(Instance(), Id(ctx.ID().getText()), self.visit(ctx.paramlist()), self.visit(ctx.blockstmt()))
            else:
                return MethodDecl(Instance(), Id(ctx.ID().getText()), [], self.visit(ctx.blockstmt()))
        else:
            if ctx.paramlist():
                return MethodDecl(Static(), Id(ctx.ID().getText()), self.visit(ctx.paramlist()), self.visit(ctx.blockstmt()))
            else:
                return MethodDecl(Static(), Id(ctx.ID().getText()), [], self.visit(ctx.blockstmt()))

    ### Return Bundles of ID and Expr (but mismatched) 
    # Visit a parse tree produced by D96Parser#id_vas.
    def visitId_vas(self, ctx:D96Parser.Id_vasContext):
        if ctx.ID():
            return [(Id(ctx.ID().getText()), self.visit(ctx.expr()), "I")] + self.visit(ctx.id_va())
        else:
            return [(Id(ctx.DOLLARID().getText()), self.visit(ctx.expr()), "S")] + self.visit(ctx.id_va())

    ### 
    # Visit a parse tree produced by D96Parser#id_va.
    def visitId_va(self, ctx:D96Parser.Id_vaContext):
        if ctx.dttyp():
            return [(self.visit(ctx.dttyp()))]
        elif ctx.ID():
            return [(Id(ctx.ID().getText()), self.visit(ctx.expr()), "I")] + self.visit(ctx.id_va())
        else:
            return [(Id(ctx.DOLLARID().getText()), self.visit(ctx.expr()), "S")] + self.visit(ctx.id_va())
            
    ###
    # Visit a parse tree produced by D96Parser#valdecl.
    def visitValdecl(self, ctx:D96Parser.ValdeclContext):
        if ctx.id_vas():
            v = self.visit(ctx.id_vas())
            ids = []
            expr = []
            SIK = []
            result = []
            tp = v[-1]
            for i in v[:-1]:
                ids = ids + [ i[0] ]
                expr = [ i[1] ] + expr
                SIK = SIK + [ i[2] ]
            for i in range(len(ids)):
                if SIK[i] == "I":
                    result += [AttributeDecl(Instance() , ConstDecl(ids[i], tp, expr[i]))]
                else:
                    result += [AttributeDecl(Static()   , ConstDecl(ids[i], tp, expr[i]))]
            return result
        else:
            var = self.visit(ctx.idlist())
            tp = self.visit(ctx.dttyp())
            result = []
            for i in var:
                if i[1] == "I":
                    result += [AttributeDecl(Instance() , ConstDecl(i[0], tp))]
                else:
                    result += [AttributeDecl(Static()   , ConstDecl(i[0], tp))]
            return result
            

    ### 
    # Visit a parse tree produced by D96Parser#vardecl.
    def visitVardecl(self, ctx:D96Parser.VardeclContext):
        if ctx.id_vas():
            v = self.visit(ctx.id_vas())
            ids = []
            expr = []
            SIK = []
            result = []
            tp = v[-1]
            for i in v[:-1]:
                ids = ids + [ i[0] ]
                expr = [ i[1] ] + expr
                SIK = SIK + [ i[2] ]
            for i in range(len(ids)):
                if SIK[i] == "I":
                    result += [AttributeDecl(Instance() , VarDecl(ids[i], tp, expr[i]))]
                else:
                    result += [AttributeDecl(Static()   , VarDecl(ids[i], tp, expr[i]))]
            return result
        else:
            var = self.visit(ctx.idlist())
            tp = self.visit(ctx.dttyp())
            result = []
            for i in var:
                if i[1] == "I":
                    result += [AttributeDecl(Instance() , VarDecl(i[0], tp))]
                else:
                    result += [AttributeDecl(Static()   , VarDecl(i[0], tp))]
            return result

    ###
    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        return MethodDecl(Instance(), Id(ctx.CONSTRUCTOR().getText()), self.visit(ctx.paramlist()), self.visit(ctx.blockstmt()))

    ###
    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return MethodDecl(Instance(), Id(ctx.DESTRUCTOR().getText()), [], self.visit(ctx.blockstmt()))

    ###
    # Visit a parse tree produced by D96Parser#datatype.
    def visitDatatype(self, ctx:D96Parser.DatatypeContext):
        if ctx.INT():
            return IntType()
        elif ctx.STRING():
            return StringType()
        elif ctx.BOOLEAN():
            return BoolType()
        else:
            return FloatType()

    ###
    # Visit a parse tree produced by D96Parser#dttype.
    def visitDttype(self, ctx:D96Parser.DttypeContext):
        if ctx.datatype():
            return self.visit(ctx.datatype())
        else:
            return ArrayType(self.changeToInt(ctx.INTLIT().getText()),self.visit(ctx.dttype()))

    ###
    # Visit a parse tree produced by D96Parser#dttyp.
    def visitDttyp(self, ctx:D96Parser.DttypContext):
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        else:
            return self.visit(ctx.dttype())

    ###
    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        ids = self.visit(ctx.bidlist())
        tp = self.visit(ctx.dttyp())
        return list(map(lambda x: VarDecl(x, tp), ids))

    ###
    # Visit a parse tree produced by D96Parser#paramlist.
    def visitParamlist(self, ctx:D96Parser.ParamlistContext):
        if ctx.paramlist():
            return self.visit(ctx.param()) + self.visit(ctx.paramlist())
        else:
            return self.visit(ctx.param())

    ###
    # Visit a parse tree produced by D96Parser#bidlist.
    def visitBidlist(self, ctx:D96Parser.BidlistContext):
        if ctx.bidlist():
            return [Id(ctx.ID().getText())] + self.visit(ctx.bidlist())
        else:
            return [Id(ctx.ID().getText())]

    ###
    # Visit a parse tree produced by D96Parser#idlist.
    def visitIdlist(self, ctx:D96Parser.IdlistContext):
        if ctx.idlist():
            if ctx.ID():
                return [(Id(ctx.ID().getText()), "I")] + self.visit(ctx.idlist())
            else:
                return [(Id(ctx.DOLLARID().getText()), "S")] + self.visit(ctx.idlist())
        else:
            if ctx.ID():
                return [(Id(ctx.ID().getText()), "I")]
            else:
                return [(Id(ctx.DOLLARID().getText()), "S")]
            
    # Visit a parse tree produced by D96Parser#lit.
    def visitLit(self, ctx:D96Parser.LitContext):
        if ctx.NULL():
            return NullLiteral()
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.INTLIT():
            return IntLiteral(self.changeToInt(ctx.INTLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.ZERO():
            return IntLiteral(0)
        else:
            return self.visit(ctx.array())

    ###
    # Visit a parse tree produced by D96Parser#valuelist.
    def visitValuelist(self, ctx:D96Parser.ValuelistContext):
        if ctx.valuelist():
            return [self.visit(ctx.expr())] + self.visit(ctx.valuelist())
        else:
            return [self.visit(ctx.expr())]

    ###
    # Visit a parse tree produced by D96Parser#blockstmt.
    def visitBlockstmt(self, ctx:D96Parser.BlockstmtContext):
        if ctx.stmtlist():
            lst = self.visit(ctx.stmtlist())
            return Block(lst)
        else:
            return Block([])

    ###
    # Visit a parse tree produced by D96Parser#stmtlist.
    def visitStmtlist(self, ctx:D96Parser.StmtlistContext):
        if ctx.stmtlist():
            return self.visit(ctx.stmt()) + self.visit(ctx.stmtlist())
        else:
            return self.visit(ctx.stmt())

    ###
    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        if ctx.forstmt():
            return [self.visit(ctx.forstmt())]
        elif ctx.ifstmt():
            return [self.visit(ctx.ifstmt())]
        elif ctx.blockstmt():
            return [self.visit(ctx.blockstmt())]
        else: 
            return self.visit(ctx.semi_stmt())

    ###
    # Visit a parse tree produced by D96Parser#semi_stmt.
    def visitSemi_stmt(self, ctx:D96Parser.Semi_stmtContext):
        if ctx.bvaldecl():
            return self.visit(ctx.bvaldecl())
        elif ctx.bvardecl():
            return self.visit(ctx.bvardecl())
        elif ctx.varass():
            return [self.visit(ctx.varass())]
        elif ctx.returnal():
            return [self.visit(ctx.returnal())]
        elif ctx.funccall():
            return [self.visit(ctx.funccall())]
        elif ctx.brk():
            return [self.visit(ctx.brk())]
        else: 
            return [self.visit(ctx.cont())]
        

    ###
    # Visit a parse tree produced by D96Parser#bid_vas.
    def visitBid_vas(self, ctx:D96Parser.Bid_vasContext):
        return [( Id(ctx.ID().getText()), self.visit(ctx.expr()) )] + self.visit(ctx.bid_va())

    ###
    # Visit a parse tree produced by D96Parser#bid_va.
    def visitBid_va(self, ctx:D96Parser.Bid_vaContext):
        if ctx.dttyp():
            return [(self.visit(ctx.dttyp()))]
        else:
            return [( Id(ctx.ID().getText()), self.visit(ctx.expr()) )] + self.visit(ctx.bid_va())

    ###
    # Visit a parse tree produced by D96Parser#bvardecl.
    def visitBvardecl(self, ctx:D96Parser.BvardeclContext):
        if ctx.bid_vas():
            v = self.visit(ctx.bid_vas())
            ids = []
            expr = []
            result = []
            tp = v[-1]
            for i in v[:-1]:
                ids = ids + [i[0]]
                expr = [i[1]] + expr
            for i in range(len(ids)):
                result += [VarDecl(ids[i], tp, expr[i])]
            return result
        else:
            var = self.visit(ctx.bidlist())
            tp = self.visit(ctx.dttyp())
            result = []
            for i in var:
                result += [VarDecl(i, tp)]
            return result

    ###
    # Visit a parse tree produced by D96Parser#bvaldecl.
    def visitBvaldecl(self, ctx:D96Parser.BvaldeclContext):
        if ctx.bid_vas():
            v = self.visit(ctx.bid_vas())
            ids = []
            expr = []
            result = []
            tp = v[-1]
            for i in v[:-1]:
                ids = ids + [ i[0] ]
                expr = [ i[1] ] + expr
            for i in range(len(ids)):
                result += [ConstDecl(ids[i], tp, expr[i])]
            return result
        else:
            val = self.visit(ctx.bidlist())
            tp = self.visit(ctx.dttyp())
            result = []
            for i in val:
                result += [ConstDecl(i, tp)]
            return result
        

    ###
    # Visit a parse tree produced by D96Parser#scalar.
    def visitScalar(self, ctx:D96Parser.ScalarContext):
        if ctx.DOT():
            return FieldAccess(self.visit(ctx.scalar()),Id(ctx.ID().getText()))
        elif ctx.DCOLON():
            return FieldAccess(Id(ctx.ID().getText()), Id(ctx.DOLLARID().getText()))
        elif ctx.sd():
            return FieldAccess(SelfLiteral(), Id(ctx.ID().getText()))
        else:
            return Id(ctx.ID().getText())

    ###
    # Visit a parse tree produced by D96Parser#index_scalar.
    def visitIndex_scalar(self, ctx:D96Parser.Index_scalarContext):
        return ArrayCell(self.visit(ctx.scalar()), self.visit(ctx.index_operators()))
    
    ###
    # Visit a parse tree produced by D96Parser#index_operators.
    def visitIndex_operators(self, ctx:D96Parser.Index_operatorsContext):
        if ctx.index_operators():
            return [self.visit(ctx.expr())] + self.visit(ctx.index_operators())
        else:
            return [self.visit(ctx.expr())]

    ###
    # Visit a parse tree produced by D96Parser#varass.
    def visitVarass(self, ctx:D96Parser.VarassContext):
        if ctx.index_scalar():
            return Assign(self.visit(ctx.index_scalar()), self.visit(ctx.expr()))
        else:
            return Assign(self.visit(ctx.scalar()), self.visit(ctx.expr()))

    ###
    # Visit a parse tree produced by D96Parser#func.
    def visitFunc(self, ctx:D96Parser.FuncContext):
        if ctx.valuelist():
            return Id(ctx.ID().getText()), self.visit(ctx.valuelist())
        else:
            return Id(ctx.ID().getText()), []

    ###
    # Visit a parse tree produced by D96Parser#dollarfunc.
    def visitDollarfunc(self, ctx:D96Parser.DollarfuncContext):
        if ctx.valuelist():
            return Id(ctx.DOLLARID().getText()), self.visit(ctx.valuelist())
        else:
            return Id(ctx.DOLLARID().getText()), []

    ###
    # Visit a parse tree produced by D96Parser#funccall.
    def visitFunccall(self, ctx:D96Parser.FunccallContext):
        if ctx.expr():
            v = self.visit(ctx.func())
            return CallStmt(self.visit(ctx.expr()), v[0], v[1])
        elif ctx.dollarfunc():
            v = self.visit(ctx.dollarfunc())
            return CallStmt(self.visit(ctx.expr()), v[0], v[1])
        else:
            v = self.visit(ctx.func())
            return CallStmt(SelfLiteral(), v[0], v[1])
            
    ###
    # Visit a parse tree produced by D96Parser#returnal.
    def visitReturnal(self, ctx:D96Parser.ReturnalContext):
        if ctx.expr():
            return Return(self.visit(ctx.expr()))
        else:
            return Return()

    ###
    # Visit a parse tree produced by D96Parser#cont.
    def visitCont(self, ctx:D96Parser.ContContext):
        return Continue()


    ###
    # Visit a parse tree produced by D96Parser#brk.
    def visitBrk(self, ctx:D96Parser.BrkContext):
        return Break()

    ###
    # Visit a parse tree produced by D96Parser#forstmt.
    def visitForstmt(self, ctx:D96Parser.ForstmtContext):
        if ctx.BY():
            return
        else:
            return

    ###
    # Visit a parse tree produced by D96Parser#ifstmt.
    def visitIfstmt(self, ctx:D96Parser.IfstmtContext):
        if ctx.elseif_part():
            v = self.visit(ctx.ifpart())
            return If(v[0], v[1], self.visit(ctx.elseif_part()))
        else:
            v = self.visit(ctx.ifpart())
            return If(v[0], v[1])

    ###
    # Visit a parse tree produced by D96Parser#ifpart.
    def visitIfpart(self, ctx:D96Parser.IfpartContext):
        return self.visit(ctx.expr()), self.visit(ctx.blockstmt())

    ###
    # Visit a parse tree produced by D96Parser#elseif_part.
    def visitElseif_part(self, ctx:D96Parser.Elseif_partContext):
        if ctx.elseif_part():
            expr = self.visit(ctx.expr())
            then = self.visit(ctx.blockstmt())
            return If(expr, then, self.visit(ctx.elseif_part()))
        elif ctx.ESLEIF():
            expr = self.visit(ctx.expr())
            then = self.visit(ctx.blockstmt())
            return If(expr, then)
        else:
            return self.visit(ctx.blockstmt())

    ###
    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        if ctx.STR():
            left = self.visit(ctx.term1(0))
            right = self.visit(ctx.term1(1))
            return BinaryOp(ctx.STR().getText(), left, right)
        else:
            return self.visit(ctx.term1(0))

    ###
    # Visit a parse tree produced by D96Parser#term1.
    def visitTerm1(self, ctx:D96Parser.Term1Context):
        if ctx.RELOP():
            left = self.visit(ctx.term2(0))
            right = self.visit(ctx.term2(1))
            return BinaryOp(ctx.RELOP().getText(), left, right)
        else:
            return self.visit(ctx.term2(0))

    ###
    # Visit a parse tree produced by D96Parser#term2.
    def visitTerm2(self, ctx:D96Parser.Term2Context):
        if ctx.ANDOP():
            left = self.visit(ctx.term2())
            right = self.visit(ctx.term3())
            return BinaryOp(ctx.ANDOP().getText(), left, right)
        if ctx.OROP():
            left = self.visit(ctx.term2())
            right = self.visit(ctx.term3())
            return BinaryOp(ctx.OROP().getText(), left, right)
        else:
            return self.visit(ctx.term3())

    ###
    # Visit a parse tree produced by D96Parser#term3.
    def visitTerm3(self, ctx:D96Parser.Term3Context):
        if ctx.ADDOP():
            left = self.visit(ctx.term3())
            right = self.visit(ctx.term4())
            return BinaryOp(ctx.ADDOP().getText(), left, right)
        if ctx.MINOP():
            left = self.visit(ctx.term3())
            right = self.visit(ctx.term4())
            return BinaryOp(ctx.MINOP().getText(), left, right)
        else:
            return self.visit(ctx.term4())

    ###
    # Visit a parse tree produced by D96Parser#term4.
    def visitTerm4(self, ctx:D96Parser.Term4Context):
        if ctx.MULOP():
            left = self.visit(ctx.term4())
            right = self.visit(ctx.term5())
            return BinaryOp(ctx.MULOP().getText(), left, right)
        if ctx.DIVOP():
            left = self.visit(ctx.term4())
            right = self.visit(ctx.term5())
            return BinaryOp(ctx.DIVOP().getText(), left, right)
        if ctx.REMOP():
            left = self.visit(ctx.term4())
            right = self.visit(ctx.term5())
            return BinaryOp(ctx.REMOP().getText(), left, right)
        else:
            return self.visit(ctx.term5())

    ###
    # Visit a parse tree produced by D96Parser#term5.
    def visitTerm5(self, ctx:D96Parser.Term5Context):
        if ctx.term5():
            return UnaryOp(ctx.NOTOP().getText(), self.visit(ctx.term5()))
        else:
            return self.visit(ctx.term6())

    ###
    # Visit a parse tree produced by D96Parser#term6.
    def visitTerm6(self, ctx:D96Parser.Term6Context):
        if ctx.term6():
            return UnaryOp(ctx.NOTOP().getText(), self.visit(ctx.term6()))
        else:
            return self.visit(ctx.term7())

    ###
    # Visit a parse tree produced by D96Parser#term7.
    def visitTerm7(self, ctx:D96Parser.Term7Context):
        if ctx.index_operators():
            a = self.visit(ctx.term8())
            i = self.visit(ctx.index_operators())
            return ArrayCell(a, i)
        else:
            return self.visit(ctx.term8())

    ###
    # Visit a parse tree produced by D96Parser#term8.
    def visitTerm8(self, ctx:D96Parser.Term8Context):
        if ctx.term8():
            if ctx.ID():
                return FieldAccess(self.visit(ctx.term8()), Id(ctx.ID().getText()))
            else:
                v = self.visit(ctx.func())
                return CallExpr(self.visit(ctx.term8()), v[0], v[1])
        elif ctx.sd():
            if ctx.ID():
                return FieldAccess(self.visit(ctx.sd()), Id(ctx.ID().getText()))
            else:
                v = self.visit(ctx.func())
                return CallExpr(self.visit(ctx.sd()), v[0], v[1])
        else:
            return self.visit(ctx.term9())

    ###
    # Visit a parse tree produced by D96Parser#term9.
    def visitTerm9(self, ctx:D96Parser.Term9Context):
        if ctx.ID():
            if ctx.DOLLARID():
                return FieldAccess(Id(ctx.ID().getText()), Id(ctx.DOLLARID().getText()))
            else:
                v = self.visit(ctx.dollarfunc())
                return CallExpr(Id(ctx.ID().getText()), v[0], v[1])
        else:
            return self.visit(ctx.term10())

    def changeToInt(self, string):
        if string[0] == "0":
            if string[1] == "b" or string[1] == "B":
                return int(string, base = 2)
            if string[1] == "x" or string[1] == "C":
                return int(string, base = 16)
            else:
                return int(string, base = 8)
        else:
            return int(string)

    ###
    # Visit a parse tree produced by D96Parser#term10.
    def visitTerm10(self, ctx:D96Parser.Term10Context):
        if ctx.NEW():
            if ctx.valuelist():
                return NewExpr(Id(ctx.ID().getText()), self.visit(ctx.valuelist()))
            else:
                return NewExpr(Id(ctx.ID().getText()), [])
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.expr():
            return self.visit(ctx.expr())
        else: 
            return self.visit(ctx.lit())
        
    ###
    # Visit a parse tree produced by D96Parser#sd.
    def visitSd(self, ctx:D96Parser.SdContext):
        return SelfLiteral()

    ###
    # Visit a parse tree produced by D96Parser#array.
    def visitArray(self, ctx:D96Parser.ArrayContext):
        if ctx.valuelist():
            return ArrayLiteral(self.visit(ctx.valuelist()))
        else:
            return ArrayLiteral([])

    

