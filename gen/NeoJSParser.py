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
        4,1,20,104,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,5,0,26,8,0,10,
        0,12,0,29,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,37,8,1,1,2,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,57,8,
        3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,6,4,6,73,
        8,6,11,6,12,6,74,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,8,4,8,86,8,8,
        11,8,12,8,87,1,9,1,9,1,9,1,9,1,9,1,9,3,9,96,8,9,1,10,1,10,1,11,1,
        11,1,11,1,11,1,11,0,0,12,0,2,4,6,8,10,12,14,16,18,20,22,0,1,2,0,
        8,9,15,19,99,0,27,1,0,0,0,2,36,1,0,0,0,4,38,1,0,0,0,6,56,1,0,0,0,
        8,58,1,0,0,0,10,64,1,0,0,0,12,72,1,0,0,0,14,76,1,0,0,0,16,85,1,0,
        0,0,18,95,1,0,0,0,20,97,1,0,0,0,22,99,1,0,0,0,24,26,3,2,1,0,25,24,
        1,0,0,0,26,29,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,30,1,0,0,0,
        29,27,1,0,0,0,30,31,5,0,0,1,31,1,1,0,0,0,32,37,3,4,2,0,33,37,3,6,
        3,0,34,37,3,8,4,0,35,37,3,10,5,0,36,32,1,0,0,0,36,33,1,0,0,0,36,
        34,1,0,0,0,36,35,1,0,0,0,37,3,1,0,0,0,38,39,5,1,0,0,39,40,5,19,0,
        0,40,41,5,11,0,0,41,42,3,16,8,0,42,43,5,12,0,0,43,5,1,0,0,0,44,45,
        5,2,0,0,45,46,5,19,0,0,46,47,5,11,0,0,47,48,3,16,8,0,48,49,5,12,
        0,0,49,57,1,0,0,0,50,51,5,3,0,0,51,52,5,19,0,0,52,53,5,11,0,0,53,
        54,3,16,8,0,54,55,5,12,0,0,55,57,1,0,0,0,56,44,1,0,0,0,56,50,1,0,
        0,0,57,7,1,0,0,0,58,59,5,4,0,0,59,60,5,19,0,0,60,61,5,11,0,0,61,
        62,3,12,6,0,62,63,5,12,0,0,63,9,1,0,0,0,64,65,5,6,0,0,65,66,5,1,
        0,0,66,67,5,19,0,0,67,68,5,11,0,0,68,69,3,16,8,0,69,70,5,12,0,0,
        70,11,1,0,0,0,71,73,3,14,7,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,1,
        0,0,0,74,75,1,0,0,0,75,13,1,0,0,0,76,77,5,5,0,0,77,78,5,19,0,0,78,
        79,5,11,0,0,79,80,3,16,8,0,80,81,5,12,0,0,81,15,1,0,0,0,82,83,3,
        18,9,0,83,84,5,13,0,0,84,86,1,0,0,0,85,82,1,0,0,0,86,87,1,0,0,0,
        87,85,1,0,0,0,87,88,1,0,0,0,88,17,1,0,0,0,89,90,5,19,0,0,90,91,5,
        14,0,0,91,96,3,20,10,0,92,93,5,7,0,0,93,94,5,14,0,0,94,96,3,22,11,
        0,95,89,1,0,0,0,95,92,1,0,0,0,96,19,1,0,0,0,97,98,7,0,0,0,98,21,
        1,0,0,0,99,100,5,19,0,0,100,101,5,10,0,0,101,102,3,20,10,0,102,23,
        1,0,0,0,6,27,36,56,74,87,95
    ]

class NeoJSParser ( Parser ):

    grammarFileName = "NeoJS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'item'", "'boss'", "'phase'", "'loot'", 
                     "'drop'", "'modify'", "'condition'", "'true'", "'false'", 
                     "<INVALID>", "'{'", "'}'", "';'", "':'" ]

    symbolicNames = [ "<INVALID>", "TK_ITEM", "TK_BOSS", "TK_PHASE", "TK_LOOT", 
                      "TK_DROP", "TK_MODIFY", "TK_CONDITION", "TRUE", "FALSE", 
                      "OP_REL", "LBRACE", "RBRACE", "SEMI", "COLON", "TIME_LITERAL", 
                      "PERCENTAGE", "NUMBER", "STRING", "ID", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_itemDecl = 2
    RULE_bossDecl = 3
    RULE_lootDecl = 4
    RULE_modifyDecl = 5
    RULE_dropList = 6
    RULE_dropDecl = 7
    RULE_attrList = 8
    RULE_attr = 9
    RULE_value = 10
    RULE_condition = 11

    ruleNames =  [ "program", "declaration", "itemDecl", "bossDecl", "lootDecl", 
                   "modifyDecl", "dropList", "dropDecl", "attrList", "attr", 
                   "value", "condition" ]

    EOF = Token.EOF
    TK_ITEM=1
    TK_BOSS=2
    TK_PHASE=3
    TK_LOOT=4
    TK_DROP=5
    TK_MODIFY=6
    TK_CONDITION=7
    TRUE=8
    FALSE=9
    OP_REL=10
    LBRACE=11
    RBRACE=12
    SEMI=13
    COLON=14
    TIME_LITERAL=15
    PERCENTAGE=16
    NUMBER=17
    STRING=18
    ID=19
    WS=20

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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

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
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 94) != 0):
                self.state = 24
                self.declaration()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 30
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


        def bossDecl(self):
            return self.getTypedRuleContext(NeoJSParser.BossDeclContext,0)


        def lootDecl(self):
            return self.getTypedRuleContext(NeoJSParser.LootDeclContext,0)


        def modifyDecl(self):
            return self.getTypedRuleContext(NeoJSParser.ModifyDeclContext,0)


        def getRuleIndex(self):
            return NeoJSParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = NeoJSParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 36
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.itemDecl()
                pass
            elif token in [2, 3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.bossDecl()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.lootDecl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterItemDecl" ):
                listener.enterItemDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitItemDecl" ):
                listener.exitItemDecl(self)

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
            self.state = 38
            self.match(NeoJSParser.TK_ITEM)
            self.state = 39
            self.match(NeoJSParser.ID)
            self.state = 40
            self.match(NeoJSParser.LBRACE)
            self.state = 41
            self.attrList()
            self.state = 42
            self.match(NeoJSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BossDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_BOSS(self):
            return self.getToken(NeoJSParser.TK_BOSS, 0)

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def LBRACE(self):
            return self.getToken(NeoJSParser.LBRACE, 0)

        def attrList(self):
            return self.getTypedRuleContext(NeoJSParser.AttrListContext,0)


        def RBRACE(self):
            return self.getToken(NeoJSParser.RBRACE, 0)

        def TK_PHASE(self):
            return self.getToken(NeoJSParser.TK_PHASE, 0)

        def getRuleIndex(self):
            return NeoJSParser.RULE_bossDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBossDecl" ):
                listener.enterBossDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBossDecl" ):
                listener.exitBossDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBossDecl" ):
                return visitor.visitBossDecl(self)
            else:
                return visitor.visitChildren(self)




    def bossDecl(self):

        localctx = NeoJSParser.BossDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_bossDecl)
        try:
            self.state = 56
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self.match(NeoJSParser.TK_BOSS)
                self.state = 45
                self.match(NeoJSParser.ID)
                self.state = 46
                self.match(NeoJSParser.LBRACE)
                self.state = 47
                self.attrList()
                self.state = 48
                self.match(NeoJSParser.RBRACE)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.match(NeoJSParser.TK_PHASE)
                self.state = 51
                self.match(NeoJSParser.ID)
                self.state = 52
                self.match(NeoJSParser.LBRACE)
                self.state = 53
                self.attrList()
                self.state = 54
                self.match(NeoJSParser.RBRACE)
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


    class LootDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_LOOT(self):
            return self.getToken(NeoJSParser.TK_LOOT, 0)

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def LBRACE(self):
            return self.getToken(NeoJSParser.LBRACE, 0)

        def dropList(self):
            return self.getTypedRuleContext(NeoJSParser.DropListContext,0)


        def RBRACE(self):
            return self.getToken(NeoJSParser.RBRACE, 0)

        def getRuleIndex(self):
            return NeoJSParser.RULE_lootDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLootDecl" ):
                listener.enterLootDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLootDecl" ):
                listener.exitLootDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLootDecl" ):
                return visitor.visitLootDecl(self)
            else:
                return visitor.visitChildren(self)




    def lootDecl(self):

        localctx = NeoJSParser.LootDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lootDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self.match(NeoJSParser.TK_LOOT)
            self.state = 59
            self.match(NeoJSParser.ID)
            self.state = 60
            self.match(NeoJSParser.LBRACE)
            self.state = 61
            self.dropList()
            self.state = 62
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
            return NeoJSParser.RULE_modifyDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifyDecl" ):
                listener.enterModifyDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifyDecl" ):
                listener.exitModifyDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModifyDecl" ):
                return visitor.visitModifyDecl(self)
            else:
                return visitor.visitChildren(self)




    def modifyDecl(self):

        localctx = NeoJSParser.ModifyDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_modifyDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(NeoJSParser.TK_MODIFY)
            self.state = 65
            self.match(NeoJSParser.TK_ITEM)
            self.state = 66
            self.match(NeoJSParser.ID)
            self.state = 67
            self.match(NeoJSParser.LBRACE)
            self.state = 68
            self.attrList()
            self.state = 69
            self.match(NeoJSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dropDecl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(NeoJSParser.DropDeclContext)
            else:
                return self.getTypedRuleContext(NeoJSParser.DropDeclContext,i)


        def getRuleIndex(self):
            return NeoJSParser.RULE_dropList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDropList" ):
                listener.enterDropList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDropList" ):
                listener.exitDropList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropList" ):
                return visitor.visitDropList(self)
            else:
                return visitor.visitChildren(self)




    def dropList(self):

        localctx = NeoJSParser.DropListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_dropList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.dropDecl()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DropDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TK_DROP(self):
            return self.getToken(NeoJSParser.TK_DROP, 0)

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def LBRACE(self):
            return self.getToken(NeoJSParser.LBRACE, 0)

        def attrList(self):
            return self.getTypedRuleContext(NeoJSParser.AttrListContext,0)


        def RBRACE(self):
            return self.getToken(NeoJSParser.RBRACE, 0)

        def getRuleIndex(self):
            return NeoJSParser.RULE_dropDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDropDecl" ):
                listener.enterDropDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDropDecl" ):
                listener.exitDropDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDropDecl" ):
                return visitor.visitDropDecl(self)
            else:
                return visitor.visitChildren(self)




    def dropDecl(self):

        localctx = NeoJSParser.DropDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_dropDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(NeoJSParser.TK_DROP)
            self.state = 77
            self.match(NeoJSParser.ID)
            self.state = 78
            self.match(NeoJSParser.LBRACE)
            self.state = 79
            self.attrList()
            self.state = 80
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

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttrList" ):
                listener.enterAttrList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttrList" ):
                listener.exitAttrList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttrList" ):
                return visitor.visitAttrList(self)
            else:
                return visitor.visitChildren(self)




    def attrList(self):

        localctx = NeoJSParser.AttrListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_attrList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 82
                self.attr()
                self.state = 83
                self.match(NeoJSParser.SEMI)
                self.state = 87 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7 or _la==19):
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


        def TK_CONDITION(self):
            return self.getToken(NeoJSParser.TK_CONDITION, 0)

        def condition(self):
            return self.getTypedRuleContext(NeoJSParser.ConditionContext,0)


        def getRuleIndex(self):
            return NeoJSParser.RULE_attr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAttr" ):
                listener.enterAttr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAttr" ):
                listener.exitAttr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAttr" ):
                return visitor.visitAttr(self)
            else:
                return visitor.visitChildren(self)




    def attr(self):

        localctx = NeoJSParser.AttrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_attr)
        try:
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 89
                self.match(NeoJSParser.ID)
                self.state = 90
                self.match(NeoJSParser.COLON)
                self.state = 91
                self.value()
                pass
            elif token in [7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.match(NeoJSParser.TK_CONDITION)
                self.state = 93
                self.match(NeoJSParser.COLON)
                self.state = 94
                self.condition()
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

        def TIME_LITERAL(self):
            return self.getToken(NeoJSParser.TIME_LITERAL, 0)

        def TRUE(self):
            return self.getToken(NeoJSParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(NeoJSParser.FALSE, 0)

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def getRuleIndex(self):
            return NeoJSParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitValue" ):
                return visitor.visitValue(self)
            else:
                return visitor.visitChildren(self)




    def value(self):

        localctx = NeoJSParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1016576) != 0)):
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


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(NeoJSParser.ID, 0)

        def OP_REL(self):
            return self.getToken(NeoJSParser.OP_REL, 0)

        def value(self):
            return self.getTypedRuleContext(NeoJSParser.ValueContext,0)


        def getRuleIndex(self):
            return NeoJSParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = NeoJSParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(NeoJSParser.ID)
            self.state = 100
            self.match(NeoJSParser.OP_REL)
            self.state = 101
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





