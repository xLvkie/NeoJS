# Generated from NeoJS.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,3,1,34,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,
        1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,
        1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,4,7,70,8,7,11,7,12,7,71,
        1,8,1,8,1,8,1,8,1,9,1,9,1,9,0,0,10,0,2,4,6,8,10,12,14,16,18,0,2,
        2,0,1,1,4,4,2,0,6,7,12,15,75,0,23,1,0,0,0,2,33,1,0,0,0,4,35,1,0,
        0,0,6,41,1,0,0,0,8,47,1,0,0,0,10,53,1,0,0,0,12,59,1,0,0,0,14,69,
        1,0,0,0,16,73,1,0,0,0,18,77,1,0,0,0,20,22,3,2,1,0,21,20,1,0,0,0,
        22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,0,25,23,1,
        0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,34,3,4,2,0,29,34,3,6,3,0,30,
        34,3,8,4,0,31,34,3,10,5,0,32,34,3,12,6,0,33,28,1,0,0,0,33,29,1,0,
        0,0,33,30,1,0,0,0,33,31,1,0,0,0,33,32,1,0,0,0,34,3,1,0,0,0,35,36,
        5,1,0,0,36,37,5,15,0,0,37,38,5,8,0,0,38,39,3,14,7,0,39,40,5,9,0,
        0,40,5,1,0,0,0,41,42,5,2,0,0,42,43,5,15,0,0,43,44,5,8,0,0,44,45,
        3,14,7,0,45,46,5,9,0,0,46,7,1,0,0,0,47,48,5,3,0,0,48,49,5,15,0,0,
        49,50,5,8,0,0,50,51,3,14,7,0,51,52,5,9,0,0,52,9,1,0,0,0,53,54,5,
        4,0,0,54,55,5,15,0,0,55,56,5,8,0,0,56,57,3,14,7,0,57,58,5,9,0,0,
        58,11,1,0,0,0,59,60,5,5,0,0,60,61,7,0,0,0,61,62,5,15,0,0,62,63,5,
        8,0,0,63,64,3,14,7,0,64,65,5,9,0,0,65,13,1,0,0,0,66,67,3,16,8,0,
        67,68,5,10,0,0,68,70,1,0,0,0,69,66,1,0,0,0,70,71,1,0,0,0,71,69,1,
        0,0,0,71,72,1,0,0,0,72,15,1,0,0,0,73,74,5,15,0,0,74,75,5,11,0,0,
        75,76,3,18,9,0,76,17,1,0,0,0,77,78,7,1,0,0,78,19,1,0,0,0,3,23,33,
        71
    ]

class NeoJSParser ( Parser ):

    grammarFileName = "NeoJS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'item'", "'weapon'", "'recipe'", "'mob'", 
                     "'modify'", "'true'", "'false'", "'{'", "'}'", "';'", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "TK_ITEM", "TK_WEAPON", "TK_RECIPE", 
                      "TK_MOB", "TK_MODIFY", "TRUE", "FALSE", "LBRACE", 
                      "RBRACE", "SEMI", "COLON", "PERCENTAGE", "NUMBER", 
                      "STRING", "ID", "COMMENT", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_itemDecl = 2
    RULE_weaponDecl = 3
    RULE_recipeDecl = 4
    RULE_mobDecl = 5
    RULE_modifyDecl = 6
    RULE_attrList = 7
    RULE_attr = 8
    RULE_value = 9

    ruleNames =  [ "program", "declaration", "itemDecl", "weaponDecl", "recipeDecl", 
                   "mobDecl", "modifyDecl", "attrList", "attr", "value" ]

    EOF = Token.EOF
    TK_ITEM=1
    TK_WEAPON=2
    TK_RECIPE=3
    TK_MOB=4
    TK_MODIFY=5
    TRUE=6
    FALSE=7
    LBRACE=8
    RBRACE=9
    SEMI=10
    COLON=11
    PERCENTAGE=12
    NUMBER=13
    STRING=14
    ID=15
    COMMENT=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(NeoJSParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NeoJSParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(NeoJSParser.DeclarationContext,i)


        def getRuleIndex(self):
            return NeoJSParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = NeoJSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0):
                self.state = 20
                self.declaration()
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(NeoJSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def itemDecl(self):
            return self.getTypedRuleContext(NeoJSParser.ItemDeclContext,0)


        def weaponDecl(self):
            return self.getTypedRuleContext(NeoJSParser.WeaponDeclContext,0)


        def recipeDecl(self):
            return self.getTypedRuleContext(NeoJSParser.RecipeDeclContext,0)


        def mobDecl(self):
            return self.getTypedRuleContext(NeoJSParser.MobDeclContext,0)


        def modifyDecl(self):
            return self.getTypedRuleContext(NeoJSParser.ModifyDeclContext,0)


        def getRuleIndex(self):
            return NeoJSParser.RULE_declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = NeoJSParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.itemDecl()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                self.weaponDecl()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                self.recipeDecl()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.mobDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 5)
                self.state = 32
                self.modifyDecl()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ItemDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_ITEM(self):
            return self.getToken(NeoJSParser.TK_ITEM, 0)

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def LBRACE(self):
            return self.getToken(NeoJSParser.LBRACE, 0)

        def attrList(self):
            return self.getTypedRuleContext(NeoJSParser.AttrListContext,0)


        def RBRACE(self):
            return self.getToken(NeoJSParser.RBRACE, 0)

        def getRuleIndex(self):
            return NeoJSParser.RULE_itemDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitItemDecl" ):
                return visitor.visitItemDecl(self)
            else:
                return visitor.visitChildren(self)




    def itemDecl(self):

        localctx = NeoJSParser.ItemDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_itemDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(NeoJSParser.TK_ITEM)
            self.state = 36
            self.match(NeoJSParser.ID)
            self.state = 37
            self.match(NeoJSParser.LBRACE)
            self.state = 38
            self.attrList()
            self.state = 39
            self.match(NeoJSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WeaponDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_WEAPON(self):
            return self.getToken(NeoJSParser.TK_WEAPON, 0)

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def LBRACE(self):
            return self.getToken(NeoJSParser.LBRACE, 0)

        def attrList(self):
            return self.getTypedRuleContext(NeoJSParser.AttrListContext,0)


        def RBRACE(self):
            return self.getToken(NeoJSParser.RBRACE, 0)

        def getRuleIndex(self):
            return NeoJSParser.RULE_weaponDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWeaponDecl" ):
                return visitor.visitWeaponDecl(self)
            else:
                return visitor.visitChildren(self)




    def weaponDecl(self):

        localctx = NeoJSParser.WeaponDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_weaponDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(NeoJSParser.TK_WEAPON)
            self.state = 42
            self.match(NeoJSParser.ID)
            self.state = 43
            self.match(NeoJSParser.LBRACE)
            self.state = 44
            self.attrList()
            self.state = 45
            self.match(NeoJSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RecipeDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_RECIPE(self):
            return self.getToken(NeoJSParser.TK_RECIPE, 0)

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def LBRACE(self):
            return self.getToken(NeoJSParser.LBRACE, 0)

        def attrList(self):
            return self.getTypedRuleContext(NeoJSParser.AttrListContext,0)


        def RBRACE(self):
            return self.getToken(NeoJSParser.RBRACE, 0)

        def getRuleIndex(self):
            return NeoJSParser.RULE_recipeDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRecipeDecl" ):
                return visitor.visitRecipeDecl(self)
            else:
                return visitor.visitChildren(self)




    def recipeDecl(self):

        localctx = NeoJSParser.RecipeDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_recipeDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(NeoJSParser.TK_RECIPE)
            self.state = 48
            self.match(NeoJSParser.ID)
            self.state = 49
            self.match(NeoJSParser.LBRACE)
            self.state = 50
            self.attrList()
            self.state = 51
            self.match(NeoJSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MobDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_MOB(self):
            return self.getToken(NeoJSParser.TK_MOB, 0)

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def LBRACE(self):
            return self.getToken(NeoJSParser.LBRACE, 0)

        def attrList(self):
            return self.getTypedRuleContext(NeoJSParser.AttrListContext,0)


        def RBRACE(self):
            return self.getToken(NeoJSParser.RBRACE, 0)

        def getRuleIndex(self):
            return NeoJSParser.RULE_mobDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMobDecl" ):
                return visitor.visitMobDecl(self)
            else:
                return visitor.visitChildren(self)




    def mobDecl(self):

        localctx = NeoJSParser.MobDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_mobDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(NeoJSParser.TK_MOB)
            self.state = 54
            self.match(NeoJSParser.ID)
            self.state = 55
            self.match(NeoJSParser.LBRACE)
            self.state = 56
            self.attrList()
            self.state = 57
            self.match(NeoJSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifyDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_MODIFY(self):
            return self.getToken(NeoJSParser.TK_MODIFY, 0)

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def LBRACE(self):
            return self.getToken(NeoJSParser.LBRACE, 0)

        def attrList(self):
            return self.getTypedRuleContext(NeoJSParser.AttrListContext,0)


        def RBRACE(self):
            return self.getToken(NeoJSParser.RBRACE, 0)

        def TK_ITEM(self):
            return self.getToken(NeoJSParser.TK_ITEM, 0)

        def TK_MOB(self):
            return self.getToken(NeoJSParser.TK_MOB, 0)

        def getRuleIndex(self):
            return NeoJSParser.RULE_modifyDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifyDecl" ):
                return visitor.visitModifyDecl(self)
            else:
                return visitor.visitChildren(self)




    def modifyDecl(self):

        localctx = NeoJSParser.ModifyDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_modifyDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.match(NeoJSParser.TK_MODIFY)
            self.state = 60
            _la = self._input.LA(1)
            if not(_la==1 or _la==4):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 61
            self.match(NeoJSParser.ID)
            self.state = 62
            self.match(NeoJSParser.LBRACE)
            self.state = 63
            self.attrList()
            self.state = 64
            self.match(NeoJSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NeoJSParser.AttrContext)
            else:
                return self.getTypedRuleContext(NeoJSParser.AttrContext,i)


        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(NeoJSParser.SEMI)
            else:
                return self.getToken(NeoJSParser.SEMI, i)

        def getRuleIndex(self):
            return NeoJSParser.RULE_attrList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrList" ):
                return visitor.visitAttrList(self)
            else:
                return visitor.visitChildren(self)




    def attrList(self):

        localctx = NeoJSParser.AttrListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_attrList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.attr()
                self.state = 67
                self.match(NeoJSParser.SEMI)
                self.state = 71 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==15):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AttrContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def COLON(self):
            return self.getToken(NeoJSParser.COLON, 0)

        def value(self):
            return self.getTypedRuleContext(NeoJSParser.ValueContext,0)


        def getRuleIndex(self):
            return NeoJSParser.RULE_attr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr" ):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)




    def attr(self):

        localctx = NeoJSParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.match(NeoJSParser.ID)
            self.state = 74
            self.match(NeoJSParser.COLON)
            self.state = 75
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(NeoJSParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(NeoJSParser.STRING, 0)

        def PERCENTAGE(self):
            return self.getToken(NeoJSParser.PERCENTAGE, 0)

        def TRUE(self):
            return self.getToken(NeoJSParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(NeoJSParser.FALSE, 0)

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def getRuleIndex(self):
            return NeoJSParser.RULE_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = NeoJSParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61632) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





