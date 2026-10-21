# Generated from NeoJS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NeoJSParser import NeoJSParser
else:
    from gen.NeoJSParser import NeoJSParser

# This class defines a complete generic visitor for a parse tree produced by NeoJSParser.

class NeoJSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by NeoJSParser#program.
    def visitProgram(self, ctx:NeoJSParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#declaration.
    def visitDeclaration(self, ctx:NeoJSParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#itemDecl.
    def visitItemDecl(self, ctx:NeoJSParser.ItemDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#bossDecl.
    def visitBossDecl(self, ctx:NeoJSParser.BossDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#lootDecl.
    def visitLootDecl(self, ctx:NeoJSParser.LootDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#modifyDecl.
    def visitModifyDecl(self, ctx:NeoJSParser.ModifyDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#dropList.
    def visitDropList(self, ctx:NeoJSParser.DropListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#dropDecl.
    def visitDropDecl(self, ctx:NeoJSParser.DropDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#attrList.
    def visitAttrList(self, ctx:NeoJSParser.AttrListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#attr.
    def visitAttr(self, ctx:NeoJSParser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#value.
    def visitValue(self, ctx:NeoJSParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#condition.
    def visitCondition(self, ctx:NeoJSParser.ConditionContext):
        return self.visitChildren(ctx)



del NeoJSParser