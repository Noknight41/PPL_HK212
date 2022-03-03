from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *

class ASTGeneration(D96Visitor):
    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        class_list = [self.visit(x) for x in ctx.bclass()]
        return Program(class_list)

    # Visit a parse tree produced by D96Parser#bclass.
    def visitBclass(self, ctx:D96Parser.BclassContext):
        body = []
        res = self.visit(ctx.class_body())
        if ctx.ID(0).getText() == "Program":
            body = [i[0] for i in res]
        else:
            for i in res:
                if i[1] == "Main":
                    d = i[0]
                    body += [MethodDecl(Instance(), d.name, [], d.body)]
                else:
                    body += [i[0]]
            
        if ctx.getChildCount() == 3:
            return ClassDecl(Id(ctx.ID(0).getText()), body)
        else:
            return ClassDecl(Id(ctx.ID(0).getText()), body, Id(ctx.ID(1).getText()))

    # Visit a parse tree produced by D96Parser#class_body.
    def visitClass_body(self, ctx:D96Parser.Class_bodyContext):
        stmt_list = []
        if ctx.class_stmt():
            for i in ctx.class_stmt():
                stmt_list += self.visit(i)
        return stmt_list

    # Visit a parse tree produced by D96Parser#class_stmt.
    def visitClass_stmt(self, ctx:D96Parser.Class_stmtContext):
        if ctx.constructor():
            return [(self.visit(ctx.constructor()), "Not")]
        elif ctx.destructor():
            return [(self.visit(ctx.destructor()), "Not" )]
        elif ctx.vardecl():
            return self.visit(ctx.vardecl())
        elif ctx.valdecl():
            return self.visit(ctx.valdecl())
        else:
            if ctx.funcdecl().ID():
                if ctx.funcdecl().ID().getText() == "main" and not(ctx.funcdecl().paramlist()):
                    return [(MethodDecl(Static(), Id(ctx.funcdecl().ID().getText()), [], self.visit(ctx.funcdecl().blockstmt())), "Main" )]
            return [(self.visit(ctx.funcdecl()) , "Not")]
            
    # Visit a parse tree produced by D96Parser#funcdecl.
    def visitFuncdecl(self, ctx:D96Parser.FuncdeclContext):
        if ctx.ID():
            if ctx.paramlist():
                return MethodDecl(Instance(), Id(ctx.ID().getText()), self.visit(ctx.paramlist()), self.visit(ctx.blockstmt()))
            else:
                return MethodDecl(Instance(), Id(ctx.ID().getText()), [], self.visit(ctx.blockstmt()))
        else:
            if ctx.paramlist():
                return MethodDecl(Static(), Id(ctx.DOLLARID().getText()), self.visit(ctx.paramlist()), self.visit(ctx.blockstmt()))
            else:
                return MethodDecl(Static(), Id(ctx.DOLLARID().getText()), [], self.visit(ctx.blockstmt()))

    # Visit a parse tree produced by D96Parser#id_vas.
    def visitId_vas(self, ctx:D96Parser.Id_vasContext):
        if ctx.ID():
            return [(Id(ctx.ID().getText()), self.visit(ctx.expr()), "I")] + self.visit(ctx.id_va())
        else:
            return [(Id(ctx.DOLLARID().getText()), self.visit(ctx.expr()), "S")] + self.visit(ctx.id_va())

    # Visit a parse tree produced by D96Parser#id_va.
    def visitId_va(self, ctx:D96Parser.Id_vaContext):
        if ctx.dttyp():
            return [(self.visit(ctx.dttyp()))]
        elif ctx.ID():
            return [(Id(ctx.ID().getText()), self.visit(ctx.expr()), "I")] + self.visit(ctx.id_va())
        else:
            return [(Id(ctx.DOLLARID().getText()), self.visit(ctx.expr()), "S")] + self.visit(ctx.id_va())
            
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
                    result += [(AttributeDecl(Instance() , ConstDecl(ids[i], tp, expr[i])), "Not" )]
                else:
                    result += [(AttributeDecl(Static()   , ConstDecl(ids[i], tp, expr[i])), "Not")]
            return result
        else:
            var = self.visit(ctx.idlist())
            tp = self.visit(ctx.dttyp())
            result = []
            if (ctx.dttyp().ID()):
                for i in var:
                    if i[1] == "I":
                        result += [(AttributeDecl(Instance() , ConstDecl(i[0], tp, NullLiteral())), "Not")]
                    else:
                        result += [(AttributeDecl(Static()   , ConstDecl(i[0], tp, NullLiteral())), "Not")]
            else:
                for i in var:
                    if i[1] == "I":
                        result += [(AttributeDecl(Instance() , ConstDecl(i[0], tp)), "Not")]
                    else:
                        result += [(AttributeDecl(Static()   , ConstDecl(i[0], tp)), "Not")]
            return result
            
    # Visit a parse tree produced by D96Parser#vardecl.
    def visitVardecl(self, ctx:D96Parser.VardeclContext):
        if ctx.id_vas():
            v = self.visit(ctx.id_vas())
            ids = []
            expr = []
            SIK = []
            tp = v[-1]
            for i in v[:-1]:
                ids = ids + [ i[0] ]
                expr = [ i[1] ] + expr
                SIK = SIK + [ i[2] ]
            result = []
            for i in range(len(ids)):
                if SIK[i] == "I":
                    result += [(AttributeDecl(Instance() , VarDecl(ids[i], tp, expr[i])), "Not")]
                else:
                    result += [(AttributeDecl(Static()   , VarDecl(ids[i], tp, expr[i])), "Not")]
            return result
        else:
            var = self.visit(ctx.idlist())
            tp = self.visit(ctx.dttyp())
            result = []
            if (ctx.dttyp().ID()):
                for i in var:
                    if i[1] == "I":
                        result += [(AttributeDecl(Instance() , VarDecl(i[0], tp, NullLiteral())), "Not")]
                    else:
                        result += [(AttributeDecl(Static()   , VarDecl(i[0], tp, NullLiteral())), "Not")]
            else:
                for i in var:
                    if i[1] == "I":
                        result += [(AttributeDecl(Instance() , VarDecl(i[0], tp)), "Not")]
                    else:
                        result += [(AttributeDecl(Static()   , VarDecl(i[0], tp)), "Not")]
            return result

    # Visit a parse tree produced by D96Parser#constructor.
    def visitConstructor(self, ctx:D96Parser.ConstructorContext):
        if ctx.paramlist():
            return MethodDecl(Instance(), Id("Constructor"), self.visit(ctx.paramlist()), self.visit(ctx.blockstmt()))
        else:
            return MethodDecl(Instance(), Id("Constructor"), [], self.visit(ctx.blockstmt()))
            
    # Visit a parse tree produced by D96Parser#destructor.
    def visitDestructor(self, ctx:D96Parser.DestructorContext):
        return MethodDecl(Instance(), Id("Destructor"), [], self.visit(ctx.blockstmt()))

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

    # Visit a parse tree produced by D96Parser#dttype.
    def visitDttype(self, ctx:D96Parser.DttypeContext):
        if ctx.datatype():
            return self.visit(ctx.datatype())
        else:
            return ArrayType(self.changeToInt(ctx.INTLIT().getText()),self.visit(ctx.dttype()))

    # Visit a parse tree produced by D96Parser#dttyp.
    def visitDttyp(self, ctx:D96Parser.DttypContext):
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
        else:
            return self.visit(ctx.dttype())

    # Visit a parse tree produced by D96Parser#param.
    def visitParam(self, ctx:D96Parser.ParamContext):
        ids = self.visit(ctx.bidlist())
        tp = self.visit(ctx.dttyp())
        return list(map(lambda x: VarDecl(x, tp), ids))

    # Visit a parse tree produced by D96Parser#paramlist.
    def visitParamlist(self, ctx:D96Parser.ParamlistContext):
        if ctx.paramlist():
            return self.visit(ctx.param()) + self.visit(ctx.paramlist())
        else:
            return self.visit(ctx.param())

    # Visit a parse tree produced by D96Parser#bidlist.
    def visitBidlist(self, ctx:D96Parser.BidlistContext):
        if ctx.bidlist():
            return [Id(ctx.ID().getText())] + self.visit(ctx.bidlist())
        else:
            return [Id(ctx.ID().getText())]

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

    # Visit a parse tree produced by D96Parser#valuelist.
    def visitValuelist(self, ctx:D96Parser.ValuelistContext):
        if ctx.valuelist():
            return [self.visit(ctx.expr())] + self.visit(ctx.valuelist())
        else:
            return [self.visit(ctx.expr())]

    # Visit a parse tree produced by D96Parser#blockstmt.
    def visitBlockstmt(self, ctx:D96Parser.BlockstmtContext):
        if ctx.stmtlist():
            lst = self.visit(ctx.stmtlist())
            return Block(lst)
        else:
            return Block([])

    # Visit a parse tree produced by D96Parser#stmtlist.
    def visitStmtlist(self, ctx:D96Parser.StmtlistContext):
        if ctx.stmtlist():
            return self.visit(ctx.stmt()) + self.visit(ctx.stmtlist())
        else:
            return self.visit(ctx.stmt())

    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        if ctx.foreachstmt():
            return [self.visit(ctx.foreachstmt())]
        elif ctx.ifstmt():
            return [self.visit(ctx.ifstmt())]
        elif ctx.blockstmt():
            return [self.visit(ctx.blockstmt())]
        else: 
            return self.visit(ctx.semi_stmt())

    # Visit a parse tree produced by D96Parser#semi_stmt.
    def visitSemi_stmt(self, ctx:D96Parser.Semi_stmtContext):
        if ctx.bvaldecl():
            return self.visit(ctx.bvaldecl())
        elif ctx.bvardecl():
            return self.visit(ctx.bvardecl())
        elif ctx.varass():
            return [self.visit(ctx.varass())]
        elif ctx.rcb():
            return [self.visit(ctx.rcb())]
        else: 
            return [self.visit(ctx.funccall())]
        
    # Visit a parse tree produced by D96Parser#block_id_vas.
    def visitBlock_id_vas(self, ctx:D96Parser.Block_id_vasContext):
        return [( Id(ctx.ID().getText()), self.visit(ctx.expr()) )] + self.visit(ctx.block_id_va())

    # Visit a parse tree produced by D96Parser#block_id_va.
    def visitBlock_id_va(self, ctx:D96Parser.Block_id_vaContext):
        if ctx.dttyp():
            return [(self.visit(ctx.dttyp()))]
        else:
            return [( Id(ctx.ID().getText()), self.visit(ctx.expr()) )] + self.visit(ctx.block_id_va())

    # Visit a parse tree produced by D96Parser#bvardecl.
    def visitBvardecl(self, ctx:D96Parser.BvardeclContext):
        if ctx.block_id_vas():
            v = self.visit(ctx.block_id_vas())
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
                if ctx.dttyp().ID():
                    result += [VarDecl(i, tp, NullLiteral())]
                else:    
                    result += [VarDecl(i, tp)]
            return result

    # Visit a parse tree produced by D96Parser#bvaldecl.
    def visitBvaldecl(self, ctx:D96Parser.BvaldeclContext):
        if ctx.block_id_vas():
            v = self.visit(ctx.block_id_vas())
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
                if ctx.dttyp().ID():
                    result += [ConstDecl(i, tp, NullLiteral())]
                else:
                    result += [ConstDecl(i, tp)]
            return result
        
    # Visit a parse tree produced by D96Parser#scalar.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        if ctx.lhs():
            return self.visit(ctx.lhs())
        elif ctx.expr():
            return FieldAccess(self.visit(ctx.expr()),Id(ctx.ID().getText()))
        elif ctx.DCOLON():
            return FieldAccess(Id(ctx.ID().getText()), Id(ctx.DOLLARID().getText()))
        else:
            return Id(ctx.ID().getText())

    # Visit a parse tree produced by D96Parser#index_scalar.
    def visitIndex_lhs(self, ctx:D96Parser.Index_lhsContext):
        if ctx.index_lhs():
            return ArrayCell(self.visit(ctx.index_lhs()), self.visit(ctx.index_operators()))
        else:
            return ArrayCell(self.visit(ctx.lhs()), self.visit(ctx.index_operators()))
    
    # Visit a parse tree produced by D96Parser#index_operators.
    def visitIndex_operators(self, ctx:D96Parser.Index_operatorsContext):
        if ctx.index_operators():
            return [self.visit(ctx.expr())] + self.visit(ctx.index_operators())
        else:
            return [self.visit(ctx.expr())]

    # Visit a parse tree produced by D96Parser#varass.
    def visitVarass(self, ctx:D96Parser.VarassContext):
        if ctx.index_lhs():
            return Assign(self.visit(ctx.index_lhs()), self.visit(ctx.expr()))
        else:
            return Assign(self.visit(ctx.lhs()), self.visit(ctx.expr()))

    # Visit a parse tree produced by D96Parser#func.
    def visitFunc(self, ctx:D96Parser.FuncContext):
        if ctx.valuelist():
            return Id(ctx.ID().getText()), self.visit(ctx.valuelist())
        else:
            return Id(ctx.ID().getText()), []

    # Visit a parse tree produced by D96Parser#dollarfunc.
    def visitDollarfunc(self, ctx:D96Parser.DollarfuncContext):
        if ctx.valuelist():
            return Id(ctx.DOLLARID().getText()), self.visit(ctx.valuelist())
        else:
            return Id(ctx.DOLLARID().getText()), []

    # Visit a parse tree produced by D96Parser#funccall.
    def visitFunccall(self, ctx:D96Parser.FunccallContext):
        if ctx.expr():
            v = self.visit(ctx.func())
            return CallStmt(self.visit(ctx.expr()), v[0], v[1])
        else:
            v = self.visit(ctx.dollarfunc())
            return CallStmt(Id(ctx.ID().getText()), v[0], v[1])
            
    # Visit a parse tree produced by D96Parser#rcb.
    def visitRcb(self, ctx:D96Parser.RcbContext):
        if ctx.CONTINUE():
            return Continue()
        elif ctx.BREAK():
            return Break()
        else:
            if ctx.expr():
                return Return(self.visit(ctx.expr()))
            else:
                return Return()
        
        

    # Visit a parse tree produced by D96Parser#foreachstmt.
    def visitForeachstmt(self, ctx:D96Parser.ForeachstmtContext):
        if ctx.BY():
            return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.blockstmt()), self.visit(ctx.expr(2)))
        else:
            return For(Id(ctx.ID().getText()), self.visit(ctx.expr(0)), self.visit(ctx.expr(1)), self.visit(ctx.blockstmt()), IntLiteral(1))

    # Visit a parse tree produced by D96Parser#ifstmt.
    def visitIfstmt(self, ctx:D96Parser.IfstmtContext):
        res = self.visit(ctx.ifpart())
        if ctx.elseif_part():
            return If(res[0], res[1], self.visit(ctx.elseif_part()))
        else:
            return If(res[0], res[1])

    # Visit a parse tree produced by D96Parser#ifpart.
    def visitIfpart(self, ctx:D96Parser.IfpartContext):
        return self.visit(ctx.expr()), self.visit(ctx.blockstmt())

    # Visit a parse tree produced by D96Parser#elseif_part.
    def visitElseif_part(self, ctx:D96Parser.Elseif_partContext):
        if ctx.elseif_part():
            expr = self.visit(ctx.expr())
            then = self.visit(ctx.blockstmt())
            return If(expr, then, self.visit(ctx.elseif_part()))
        elif ctx.ELSEIF():
            expr = self.visit(ctx.expr())
            then = self.visit(ctx.blockstmt())
            return If(expr, then)
        else:
            return self.visit(ctx.blockstmt())

    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        if ctx.STR():
            left = self.visit(ctx.term1(0))
            right = self.visit(ctx.term1(1))
            return BinaryOp(ctx.STR().getText(), left, right)
        else:
            return self.visit(ctx.term1(0))

    # Visit a parse tree produced by D96Parser#term1.
    def visitTerm1(self, ctx:D96Parser.Term1Context):
        if ctx.RELOP():
            left = self.visit(ctx.term2(0))
            right = self.visit(ctx.term2(1))
            return BinaryOp(ctx.RELOP().getText(), left, right)
        else:
            return self.visit(ctx.term2(0))

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

    # Visit a parse tree produced by D96Parser#term5.
    def visitTerm5(self, ctx:D96Parser.Term5Context):
        if ctx.term5():
            return UnaryOp(ctx.NOTOP().getText(), self.visit(ctx.term5()))
        else:
            return self.visit(ctx.term6())

    # Visit a parse tree produced by D96Parser#term6.
    def visitTerm6(self, ctx:D96Parser.Term6Context):
        if ctx.term6():
            return UnaryOp(ctx.MINOP().getText(), self.visit(ctx.term6()))
        else:
            return self.visit(ctx.term7())

    # Visit a parse tree produced by D96Parser#term7.
    def visitTerm7(self, ctx:D96Parser.Term7Context):
        if ctx.index_operators():
            left = self.visit(ctx.term8())
            right = self.visit(ctx.index_operators())
            return ArrayCell(left, right)
        else:
            return self.visit(ctx.term8())

    # Visit a parse tree produced by D96Parser#term8.
    def visitTerm8(self, ctx:D96Parser.Term8Context):
        if ctx.term8():
            if ctx.ID():
                return FieldAccess(self.visit(ctx.term8()), Id(ctx.ID().getText()))
            else:
                v = self.visit(ctx.func())
                return CallExpr(self.visit(ctx.term8()), v[0], v[1])
        else:
            return self.visit(ctx.term9())

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

    # Visit a parse tree produced by D96Parser#term10.
    def changeToInt(self, string):
        if string[0] == "0":
            if string[1] == "b" or string[1] == "B":
                return int(string, base = 2)
            if string[1] == "x" or string[1] == "X":
                return int(string, base = 16)
            else:
                return int(string, base = 8)
        else:
            return int(string)
    
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
        elif ctx.SELF():
            return SelfLiteral()
        else: 
            return self.visit(ctx.literal())

    # Visit a parse tree produced by D96Parser#literal.
    def visitLiteral(self, ctx:D96Parser.LiteralContext):
        if ctx.NULL():
            return NullLiteral()
        elif ctx.TRUE():
            return BooleanLiteral(True)
        elif ctx.FALSE():
            return BooleanLiteral(False)
        elif ctx.FLOATLIT():
            text = ctx.FLOATLIT().getText()
            if text[0] == "." and (text[1] == "e" or text[1] == "E"):
                return FloatLiteral(0.0)
            return FloatLiteral(float(text))
        elif ctx.INTLIT():
            return IntLiteral(self.changeToInt(ctx.INTLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        elif ctx.ZERO():
            return IntLiteral(0)
        else:
            return self.visit(ctx.arrayCell())

    # Visit a parse tree produced by D96Parser#array.
    def visitArrayCell(self, ctx:D96Parser.ArrayCellContext):
        if ctx.valuelist():
            return ArrayLiteral(self.visit(ctx.valuelist()))
        else:
            return ArrayLiteral([])

    

