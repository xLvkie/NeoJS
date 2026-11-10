# Generated from NeoJS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .NeoJSParser import NeoJSParser
else:
    from NeoJSParser import NeoJSParser

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


    # Visit a parse tree produced by NeoJSParser#weaponDecl.
    def visitWeaponDecl(self, ctx:NeoJSParser.WeaponDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#recipeDecl.
    def visitRecipeDecl(self, ctx:NeoJSParser.RecipeDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#mobDecl.
    def visitMobDecl(self, ctx:NeoJSParser.MobDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by NeoJSParser#modifyDecl.
    def visitModifyDecl(self, ctx:NeoJSParser.ModifyDeclContext):
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



del NeoJSParser