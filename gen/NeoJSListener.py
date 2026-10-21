# Generated from NeoJS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NeoJSParser import NeoJSParser
else:
    from gen.NeoJSParser import NeoJSParser

# This class defines a complete listener for a parse tree produced by NeoJSParser.
class NeoJSListener(ParseTreeListener):

    # Enter a parse tree produced by NeoJSParser#program.
    def enterProgram(self, ctx:NeoJSParser.ProgramContext):
        pass

    # Exit a parse tree produced by NeoJSParser#program.
    def exitProgram(self, ctx:NeoJSParser.ProgramContext):
        pass


    # Enter a parse tree produced by NeoJSParser#declaration.
    def enterDeclaration(self, ctx:NeoJSParser.DeclarationContext):
        pass

    # Exit a parse tree produced by NeoJSParser#declaration.
    def exitDeclaration(self, ctx:NeoJSParser.DeclarationContext):
        pass


    # Enter a parse tree produced by NeoJSParser#itemDecl.
    def enterItemDecl(self, ctx:NeoJSParser.ItemDeclContext):
        pass

    # Exit a parse tree produced by NeoJSParser#itemDecl.
    def exitItemDecl(self, ctx:NeoJSParser.ItemDeclContext):
        pass


    # Enter a parse tree produced by NeoJSParser#bossDecl.
    def enterBossDecl(self, ctx:NeoJSParser.BossDeclContext):
        pass

    # Exit a parse tree produced by NeoJSParser#bossDecl.
    def exitBossDecl(self, ctx:NeoJSParser.BossDeclContext):
        pass


    # Enter a parse tree produced by NeoJSParser#lootDecl.
    def enterLootDecl(self, ctx:NeoJSParser.LootDeclContext):
        pass

    # Exit a parse tree produced by NeoJSParser#lootDecl.
    def exitLootDecl(self, ctx:NeoJSParser.LootDeclContext):
        pass


    # Enter a parse tree produced by NeoJSParser#modifyDecl.
    def enterModifyDecl(self, ctx:NeoJSParser.ModifyDeclContext):
        pass

    # Exit a parse tree produced by NeoJSParser#modifyDecl.
    def exitModifyDecl(self, ctx:NeoJSParser.ModifyDeclContext):
        pass


    # Enter a parse tree produced by NeoJSParser#dropList.
    def enterDropList(self, ctx:NeoJSParser.DropListContext):
        pass

    # Exit a parse tree produced by NeoJSParser#dropList.
    def exitDropList(self, ctx:NeoJSParser.DropListContext):
        pass


    # Enter a parse tree produced by NeoJSParser#dropDecl.
    def enterDropDecl(self, ctx:NeoJSParser.DropDeclContext):
        pass

    # Exit a parse tree produced by NeoJSParser#dropDecl.
    def exitDropDecl(self, ctx:NeoJSParser.DropDeclContext):
        pass


    # Enter a parse tree produced by NeoJSParser#attrList.
    def enterAttrList(self, ctx:NeoJSParser.AttrListContext):
        pass

    # Exit a parse tree produced by NeoJSParser#attrList.
    def exitAttrList(self, ctx:NeoJSParser.AttrListContext):
        pass


    # Enter a parse tree produced by NeoJSParser#attr.
    def enterAttr(self, ctx:NeoJSParser.AttrContext):
        pass

    # Exit a parse tree produced by NeoJSParser#attr.
    def exitAttr(self, ctx:NeoJSParser.AttrContext):
        pass


    # Enter a parse tree produced by NeoJSParser#value.
    def enterValue(self, ctx:NeoJSParser.ValueContext):
        pass

    # Exit a parse tree produced by NeoJSParser#value.
    def exitValue(self, ctx:NeoJSParser.ValueContext):
        pass


    # Enter a parse tree produced by NeoJSParser#condition.
    def enterCondition(self, ctx:NeoJSParser.ConditionContext):
        pass

    # Exit a parse tree produced by NeoJSParser#condition.
    def exitCondition(self, ctx:NeoJSParser.ConditionContext):
        pass



del NeoJSParser