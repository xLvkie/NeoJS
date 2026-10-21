// Generated from c:/Trabajos U/Codigos/NeoJS/NeoJS.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class NeoJSParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		TK_ITEM=1, TK_BOSS=2, TK_PHASE=3, TK_LOOT=4, TK_DROP=5, TK_MODIFY=6, TK_CONDITION=7, 
		TRUE=8, FALSE=9, OP_REL=10, LBRACE=11, RBRACE=12, SEMI=13, COLON=14, TIME_LITERAL=15, 
		PERCENTAGE=16, NUMBER=17, STRING=18, ID=19, WS=20;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_itemDecl = 2, RULE_bossDecl = 3, 
		RULE_lootDecl = 4, RULE_modifyDecl = 5, RULE_dropList = 6, RULE_dropDecl = 7, 
		RULE_attrList = 8, RULE_attr = 9, RULE_value = 10, RULE_condition = 11;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "itemDecl", "bossDecl", "lootDecl", "modifyDecl", 
			"dropList", "dropDecl", "attrList", "attr", "value", "condition"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'item'", "'boss'", "'phase'", "'loot'", "'drop'", "'modify'", 
			"'condition'", "'true'", "'false'", null, "'{'", "'}'", "';'", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "TK_ITEM", "TK_BOSS", "TK_PHASE", "TK_LOOT", "TK_DROP", "TK_MODIFY", 
			"TK_CONDITION", "TRUE", "FALSE", "OP_REL", "LBRACE", "RBRACE", "SEMI", 
			"COLON", "TIME_LITERAL", "PERCENTAGE", "NUMBER", "STRING", "ID", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "NeoJS.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public NeoJSParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgramContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(NeoJSParser.EOF, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_program);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(27);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 94L) != 0)) {
				{
				{
				setState(24);
				declaration();
				}
				}
				setState(29);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(30);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationContext extends ParserRuleContext {
		public ItemDeclContext itemDecl() {
			return getRuleContext(ItemDeclContext.class,0);
		}
		public BossDeclContext bossDecl() {
			return getRuleContext(BossDeclContext.class,0);
		}
		public LootDeclContext lootDecl() {
			return getRuleContext(LootDeclContext.class,0);
		}
		public ModifyDeclContext modifyDecl() {
			return getRuleContext(ModifyDeclContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_declaration);
		try {
			setState(36);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TK_ITEM:
				enterOuterAlt(_localctx, 1);
				{
				setState(32);
				itemDecl();
				}
				break;
			case TK_BOSS:
			case TK_PHASE:
				enterOuterAlt(_localctx, 2);
				{
				setState(33);
				bossDecl();
				}
				break;
			case TK_LOOT:
				enterOuterAlt(_localctx, 3);
				{
				setState(34);
				lootDecl();
				}
				break;
			case TK_MODIFY:
				enterOuterAlt(_localctx, 4);
				{
				setState(35);
				modifyDecl();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ItemDeclContext extends ParserRuleContext {
		public TerminalNode TK_ITEM() { return getToken(NeoJSParser.TK_ITEM, 0); }
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(NeoJSParser.LBRACE, 0); }
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(NeoJSParser.RBRACE, 0); }
		public ItemDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_itemDecl; }
	}

	public final ItemDeclContext itemDecl() throws RecognitionException {
		ItemDeclContext _localctx = new ItemDeclContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_itemDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(38);
			match(TK_ITEM);
			setState(39);
			match(ID);
			setState(40);
			match(LBRACE);
			setState(41);
			attrList();
			setState(42);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BossDeclContext extends ParserRuleContext {
		public TerminalNode TK_BOSS() { return getToken(NeoJSParser.TK_BOSS, 0); }
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(NeoJSParser.LBRACE, 0); }
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(NeoJSParser.RBRACE, 0); }
		public TerminalNode TK_PHASE() { return getToken(NeoJSParser.TK_PHASE, 0); }
		public BossDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bossDecl; }
	}

	public final BossDeclContext bossDecl() throws RecognitionException {
		BossDeclContext _localctx = new BossDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_bossDecl);
		try {
			setState(56);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TK_BOSS:
				enterOuterAlt(_localctx, 1);
				{
				setState(44);
				match(TK_BOSS);
				setState(45);
				match(ID);
				setState(46);
				match(LBRACE);
				setState(47);
				attrList();
				setState(48);
				match(RBRACE);
				}
				break;
			case TK_PHASE:
				enterOuterAlt(_localctx, 2);
				{
				setState(50);
				match(TK_PHASE);
				setState(51);
				match(ID);
				setState(52);
				match(LBRACE);
				setState(53);
				attrList();
				setState(54);
				match(RBRACE);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LootDeclContext extends ParserRuleContext {
		public TerminalNode TK_LOOT() { return getToken(NeoJSParser.TK_LOOT, 0); }
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(NeoJSParser.LBRACE, 0); }
		public DropListContext dropList() {
			return getRuleContext(DropListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(NeoJSParser.RBRACE, 0); }
		public LootDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_lootDecl; }
	}

	public final LootDeclContext lootDecl() throws RecognitionException {
		LootDeclContext _localctx = new LootDeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_lootDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(TK_LOOT);
			setState(59);
			match(ID);
			setState(60);
			match(LBRACE);
			setState(61);
			dropList();
			setState(62);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ModifyDeclContext extends ParserRuleContext {
		public TerminalNode TK_MODIFY() { return getToken(NeoJSParser.TK_MODIFY, 0); }
		public TerminalNode TK_ITEM() { return getToken(NeoJSParser.TK_ITEM, 0); }
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(NeoJSParser.LBRACE, 0); }
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(NeoJSParser.RBRACE, 0); }
		public ModifyDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modifyDecl; }
	}

	public final ModifyDeclContext modifyDecl() throws RecognitionException {
		ModifyDeclContext _localctx = new ModifyDeclContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_modifyDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(TK_MODIFY);
			setState(65);
			match(TK_ITEM);
			setState(66);
			match(ID);
			setState(67);
			match(LBRACE);
			setState(68);
			attrList();
			setState(69);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DropListContext extends ParserRuleContext {
		public List<DropDeclContext> dropDecl() {
			return getRuleContexts(DropDeclContext.class);
		}
		public DropDeclContext dropDecl(int i) {
			return getRuleContext(DropDeclContext.class,i);
		}
		public DropListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dropList; }
	}

	public final DropListContext dropList() throws RecognitionException {
		DropListContext _localctx = new DropListContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_dropList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(72); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(71);
				dropDecl();
				}
				}
				setState(74); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==TK_DROP );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DropDeclContext extends ParserRuleContext {
		public TerminalNode TK_DROP() { return getToken(NeoJSParser.TK_DROP, 0); }
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(NeoJSParser.LBRACE, 0); }
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(NeoJSParser.RBRACE, 0); }
		public DropDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dropDecl; }
	}

	public final DropDeclContext dropDecl() throws RecognitionException {
		DropDeclContext _localctx = new DropDeclContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_dropDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(76);
			match(TK_DROP);
			setState(77);
			match(ID);
			setState(78);
			match(LBRACE);
			setState(79);
			attrList();
			setState(80);
			match(RBRACE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttrListContext extends ParserRuleContext {
		public List<AttrContext> attr() {
			return getRuleContexts(AttrContext.class);
		}
		public AttrContext attr(int i) {
			return getRuleContext(AttrContext.class,i);
		}
		public List<TerminalNode> SEMI() { return getTokens(NeoJSParser.SEMI); }
		public TerminalNode SEMI(int i) {
			return getToken(NeoJSParser.SEMI, i);
		}
		public AttrListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attrList; }
	}

	public final AttrListContext attrList() throws RecognitionException {
		AttrListContext _localctx = new AttrListContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_attrList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(82);
				attr();
				setState(83);
				match(SEMI);
				}
				}
				setState(87); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==TK_CONDITION || _la==ID );
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AttrContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public TerminalNode COLON() { return getToken(NeoJSParser.COLON, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public TerminalNode TK_CONDITION() { return getToken(NeoJSParser.TK_CONDITION, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public AttrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attr; }
	}

	public final AttrContext attr() throws RecognitionException {
		AttrContext _localctx = new AttrContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_attr);
		try {
			setState(95);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(89);
				match(ID);
				setState(90);
				match(COLON);
				setState(91);
				value();
				}
				break;
			case TK_CONDITION:
				enterOuterAlt(_localctx, 2);
				{
				setState(92);
				match(TK_CONDITION);
				setState(93);
				match(COLON);
				setState(94);
				condition();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(NeoJSParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(NeoJSParser.STRING, 0); }
		public TerminalNode PERCENTAGE() { return getToken(NeoJSParser.PERCENTAGE, 0); }
		public TerminalNode TIME_LITERAL() { return getToken(NeoJSParser.TIME_LITERAL, 0); }
		public TerminalNode TRUE() { return getToken(NeoJSParser.TRUE, 0); }
		public TerminalNode FALSE() { return getToken(NeoJSParser.FALSE, 0); }
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public ValueContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_value; }
	}

	public final ValueContext value() throws RecognitionException {
		ValueContext _localctx = new ValueContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1016576L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public TerminalNode OP_REL() { return getToken(NeoJSParser.OP_REL, 0); }
		public ValueContext value() {
			return getRuleContext(ValueContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(99);
			match(ID);
			setState(100);
			match(OP_REL);
			setState(101);
			value();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\u0004\u0001\u0014h\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0001"+
		"\u0000\u0005\u0000\u001a\b\u0000\n\u0000\f\u0000\u001d\t\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001"+
		"%\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0003\u00039\b\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0004\u0006"+
		"I\b\u0006\u000b\u0006\f\u0006J\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0004\bV\b\b\u000b"+
		"\b\f\bW\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0003\t`\b\t\u0001"+
		"\n\u0001\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0000\u0000\f\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016"+
		"\u0000\u0001\u0002\u0000\b\t\u000f\u0013c\u0000\u001b\u0001\u0000\u0000"+
		"\u0000\u0002$\u0001\u0000\u0000\u0000\u0004&\u0001\u0000\u0000\u0000\u0006"+
		"8\u0001\u0000\u0000\u0000\b:\u0001\u0000\u0000\u0000\n@\u0001\u0000\u0000"+
		"\u0000\fH\u0001\u0000\u0000\u0000\u000eL\u0001\u0000\u0000\u0000\u0010"+
		"U\u0001\u0000\u0000\u0000\u0012_\u0001\u0000\u0000\u0000\u0014a\u0001"+
		"\u0000\u0000\u0000\u0016c\u0001\u0000\u0000\u0000\u0018\u001a\u0003\u0002"+
		"\u0001\u0000\u0019\u0018\u0001\u0000\u0000\u0000\u001a\u001d\u0001\u0000"+
		"\u0000\u0000\u001b\u0019\u0001\u0000\u0000\u0000\u001b\u001c\u0001\u0000"+
		"\u0000\u0000\u001c\u001e\u0001\u0000\u0000\u0000\u001d\u001b\u0001\u0000"+
		"\u0000\u0000\u001e\u001f\u0005\u0000\u0000\u0001\u001f\u0001\u0001\u0000"+
		"\u0000\u0000 %\u0003\u0004\u0002\u0000!%\u0003\u0006\u0003\u0000\"%\u0003"+
		"\b\u0004\u0000#%\u0003\n\u0005\u0000$ \u0001\u0000\u0000\u0000$!\u0001"+
		"\u0000\u0000\u0000$\"\u0001\u0000\u0000\u0000$#\u0001\u0000\u0000\u0000"+
		"%\u0003\u0001\u0000\u0000\u0000&\'\u0005\u0001\u0000\u0000\'(\u0005\u0013"+
		"\u0000\u0000()\u0005\u000b\u0000\u0000)*\u0003\u0010\b\u0000*+\u0005\f"+
		"\u0000\u0000+\u0005\u0001\u0000\u0000\u0000,-\u0005\u0002\u0000\u0000"+
		"-.\u0005\u0013\u0000\u0000./\u0005\u000b\u0000\u0000/0\u0003\u0010\b\u0000"+
		"01\u0005\f\u0000\u000019\u0001\u0000\u0000\u000023\u0005\u0003\u0000\u0000"+
		"34\u0005\u0013\u0000\u000045\u0005\u000b\u0000\u000056\u0003\u0010\b\u0000"+
		"67\u0005\f\u0000\u000079\u0001\u0000\u0000\u00008,\u0001\u0000\u0000\u0000"+
		"82\u0001\u0000\u0000\u00009\u0007\u0001\u0000\u0000\u0000:;\u0005\u0004"+
		"\u0000\u0000;<\u0005\u0013\u0000\u0000<=\u0005\u000b\u0000\u0000=>\u0003"+
		"\f\u0006\u0000>?\u0005\f\u0000\u0000?\t\u0001\u0000\u0000\u0000@A\u0005"+
		"\u0006\u0000\u0000AB\u0005\u0001\u0000\u0000BC\u0005\u0013\u0000\u0000"+
		"CD\u0005\u000b\u0000\u0000DE\u0003\u0010\b\u0000EF\u0005\f\u0000\u0000"+
		"F\u000b\u0001\u0000\u0000\u0000GI\u0003\u000e\u0007\u0000HG\u0001\u0000"+
		"\u0000\u0000IJ\u0001\u0000\u0000\u0000JH\u0001\u0000\u0000\u0000JK\u0001"+
		"\u0000\u0000\u0000K\r\u0001\u0000\u0000\u0000LM\u0005\u0005\u0000\u0000"+
		"MN\u0005\u0013\u0000\u0000NO\u0005\u000b\u0000\u0000OP\u0003\u0010\b\u0000"+
		"PQ\u0005\f\u0000\u0000Q\u000f\u0001\u0000\u0000\u0000RS\u0003\u0012\t"+
		"\u0000ST\u0005\r\u0000\u0000TV\u0001\u0000\u0000\u0000UR\u0001\u0000\u0000"+
		"\u0000VW\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000WX\u0001\u0000"+
		"\u0000\u0000X\u0011\u0001\u0000\u0000\u0000YZ\u0005\u0013\u0000\u0000"+
		"Z[\u0005\u000e\u0000\u0000[`\u0003\u0014\n\u0000\\]\u0005\u0007\u0000"+
		"\u0000]^\u0005\u000e\u0000\u0000^`\u0003\u0016\u000b\u0000_Y\u0001\u0000"+
		"\u0000\u0000_\\\u0001\u0000\u0000\u0000`\u0013\u0001\u0000\u0000\u0000"+
		"ab\u0007\u0000\u0000\u0000b\u0015\u0001\u0000\u0000\u0000cd\u0005\u0013"+
		"\u0000\u0000de\u0005\n\u0000\u0000ef\u0003\u0014\n\u0000f\u0017\u0001"+
		"\u0000\u0000\u0000\u0006\u001b$8JW_";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}