// Generated from /home/bookie/Proyectos/NeoJS/NeoJS.g4 by ANTLR 4.13.1
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
		TK_ITEM=1, TK_WEAPON=2, TK_RECIPE=3, TK_MOB=4, TK_MODIFY=5, TRUE=6, FALSE=7, 
		LBRACE=8, RBRACE=9, SEMI=10, COLON=11, PERCENTAGE=12, NUMBER=13, STRING=14, 
		ID=15, COMMENT=16, WS=17;
	public static final int
		RULE_program = 0, RULE_declaration = 1, RULE_itemDecl = 2, RULE_weaponDecl = 3, 
		RULE_recipeDecl = 4, RULE_mobDecl = 5, RULE_modifyDecl = 6, RULE_attrList = 7, 
		RULE_attr = 8, RULE_value = 9;
	private static String[] makeRuleNames() {
		return new String[] {
			"program", "declaration", "itemDecl", "weaponDecl", "recipeDecl", "mobDecl", 
			"modifyDecl", "attrList", "attr", "value"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'item'", "'weapon'", "'recipe'", "'mob'", "'modify'", "'true'", 
			"'false'", "'{'", "'}'", "';'", "':'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "TK_ITEM", "TK_WEAPON", "TK_RECIPE", "TK_MOB", "TK_MODIFY", "TRUE", 
			"FALSE", "LBRACE", "RBRACE", "SEMI", "COLON", "PERCENTAGE", "NUMBER", 
			"STRING", "ID", "COMMENT", "WS"
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
			setState(23);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 62L) != 0)) {
				{
				{
				setState(20);
				declaration();
				}
				}
				setState(25);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(26);
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
		public WeaponDeclContext weaponDecl() {
			return getRuleContext(WeaponDeclContext.class,0);
		}
		public RecipeDeclContext recipeDecl() {
			return getRuleContext(RecipeDeclContext.class,0);
		}
		public MobDeclContext mobDecl() {
			return getRuleContext(MobDeclContext.class,0);
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
			setState(33);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TK_ITEM:
				enterOuterAlt(_localctx, 1);
				{
				setState(28);
				itemDecl();
				}
				break;
			case TK_WEAPON:
				enterOuterAlt(_localctx, 2);
				{
				setState(29);
				weaponDecl();
				}
				break;
			case TK_RECIPE:
				enterOuterAlt(_localctx, 3);
				{
				setState(30);
				recipeDecl();
				}
				break;
			case TK_MOB:
				enterOuterAlt(_localctx, 4);
				{
				setState(31);
				mobDecl();
				}
				break;
			case TK_MODIFY:
				enterOuterAlt(_localctx, 5);
				{
				setState(32);
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
			setState(35);
			match(TK_ITEM);
			setState(36);
			match(ID);
			setState(37);
			match(LBRACE);
			setState(38);
			attrList();
			setState(39);
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
	public static class WeaponDeclContext extends ParserRuleContext {
		public TerminalNode TK_WEAPON() { return getToken(NeoJSParser.TK_WEAPON, 0); }
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(NeoJSParser.LBRACE, 0); }
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(NeoJSParser.RBRACE, 0); }
		public WeaponDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_weaponDecl; }
	}

	public final WeaponDeclContext weaponDecl() throws RecognitionException {
		WeaponDeclContext _localctx = new WeaponDeclContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_weaponDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(41);
			match(TK_WEAPON);
			setState(42);
			match(ID);
			setState(43);
			match(LBRACE);
			setState(44);
			attrList();
			setState(45);
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
	public static class RecipeDeclContext extends ParserRuleContext {
		public TerminalNode TK_RECIPE() { return getToken(NeoJSParser.TK_RECIPE, 0); }
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(NeoJSParser.LBRACE, 0); }
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(NeoJSParser.RBRACE, 0); }
		public RecipeDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_recipeDecl; }
	}

	public final RecipeDeclContext recipeDecl() throws RecognitionException {
		RecipeDeclContext _localctx = new RecipeDeclContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_recipeDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(TK_RECIPE);
			setState(48);
			match(ID);
			setState(49);
			match(LBRACE);
			setState(50);
			attrList();
			setState(51);
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
	public static class MobDeclContext extends ParserRuleContext {
		public TerminalNode TK_MOB() { return getToken(NeoJSParser.TK_MOB, 0); }
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(NeoJSParser.LBRACE, 0); }
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(NeoJSParser.RBRACE, 0); }
		public MobDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_mobDecl; }
	}

	public final MobDeclContext mobDecl() throws RecognitionException {
		MobDeclContext _localctx = new MobDeclContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_mobDecl);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(TK_MOB);
			setState(54);
			match(ID);
			setState(55);
			match(LBRACE);
			setState(56);
			attrList();
			setState(57);
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
		public TerminalNode ID() { return getToken(NeoJSParser.ID, 0); }
		public TerminalNode LBRACE() { return getToken(NeoJSParser.LBRACE, 0); }
		public AttrListContext attrList() {
			return getRuleContext(AttrListContext.class,0);
		}
		public TerminalNode RBRACE() { return getToken(NeoJSParser.RBRACE, 0); }
		public TerminalNode TK_ITEM() { return getToken(NeoJSParser.TK_ITEM, 0); }
		public TerminalNode TK_MOB() { return getToken(NeoJSParser.TK_MOB, 0); }
		public ModifyDeclContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_modifyDecl; }
	}

	public final ModifyDeclContext modifyDecl() throws RecognitionException {
		ModifyDeclContext _localctx = new ModifyDeclContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_modifyDecl);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(59);
			match(TK_MODIFY);
			setState(60);
			_la = _input.LA(1);
			if ( !(_la==TK_ITEM || _la==TK_MOB) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(61);
			match(ID);
			setState(62);
			match(LBRACE);
			setState(63);
			attrList();
			setState(64);
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
		enterRule(_localctx, 14, RULE_attrList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(69); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(66);
				attr();
				setState(67);
				match(SEMI);
				}
				}
				setState(71); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==ID );
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
		public AttrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_attr; }
	}

	public final AttrContext attr() throws RecognitionException {
		AttrContext _localctx = new AttrContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_attr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(73);
			match(ID);
			setState(74);
			match(COLON);
			setState(75);
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

	@SuppressWarnings("CheckReturnValue")
	public static class ValueContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(NeoJSParser.NUMBER, 0); }
		public TerminalNode STRING() { return getToken(NeoJSParser.STRING, 0); }
		public TerminalNode PERCENTAGE() { return getToken(NeoJSParser.PERCENTAGE, 0); }
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
		enterRule(_localctx, 18, RULE_value);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 61632L) != 0)) ) {
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

	public static final String _serializedATN =
		"\u0004\u0001\u0011P\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0001\u0000\u0005\u0000\u0016\b\u0000\n\u0000"+
		"\f\u0000\u0019\t\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\"\b\u0001\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0007\u0001\u0007\u0001\u0007\u0004\u0007F\b\u0007\u000b\u0007"+
		"\f\u0007G\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0000"+
		"\u0000\n\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0000\u0002\u0002"+
		"\u0000\u0001\u0001\u0004\u0004\u0002\u0000\u0006\u0007\f\u000fK\u0000"+
		"\u0017\u0001\u0000\u0000\u0000\u0002!\u0001\u0000\u0000\u0000\u0004#\u0001"+
		"\u0000\u0000\u0000\u0006)\u0001\u0000\u0000\u0000\b/\u0001\u0000\u0000"+
		"\u0000\n5\u0001\u0000\u0000\u0000\f;\u0001\u0000\u0000\u0000\u000eE\u0001"+
		"\u0000\u0000\u0000\u0010I\u0001\u0000\u0000\u0000\u0012M\u0001\u0000\u0000"+
		"\u0000\u0014\u0016\u0003\u0002\u0001\u0000\u0015\u0014\u0001\u0000\u0000"+
		"\u0000\u0016\u0019\u0001\u0000\u0000\u0000\u0017\u0015\u0001\u0000\u0000"+
		"\u0000\u0017\u0018\u0001\u0000\u0000\u0000\u0018\u001a\u0001\u0000\u0000"+
		"\u0000\u0019\u0017\u0001\u0000\u0000\u0000\u001a\u001b\u0005\u0000\u0000"+
		"\u0001\u001b\u0001\u0001\u0000\u0000\u0000\u001c\"\u0003\u0004\u0002\u0000"+
		"\u001d\"\u0003\u0006\u0003\u0000\u001e\"\u0003\b\u0004\u0000\u001f\"\u0003"+
		"\n\u0005\u0000 \"\u0003\f\u0006\u0000!\u001c\u0001\u0000\u0000\u0000!"+
		"\u001d\u0001\u0000\u0000\u0000!\u001e\u0001\u0000\u0000\u0000!\u001f\u0001"+
		"\u0000\u0000\u0000! \u0001\u0000\u0000\u0000\"\u0003\u0001\u0000\u0000"+
		"\u0000#$\u0005\u0001\u0000\u0000$%\u0005\u000f\u0000\u0000%&\u0005\b\u0000"+
		"\u0000&\'\u0003\u000e\u0007\u0000\'(\u0005\t\u0000\u0000(\u0005\u0001"+
		"\u0000\u0000\u0000)*\u0005\u0002\u0000\u0000*+\u0005\u000f\u0000\u0000"+
		"+,\u0005\b\u0000\u0000,-\u0003\u000e\u0007\u0000-.\u0005\t\u0000\u0000"+
		".\u0007\u0001\u0000\u0000\u0000/0\u0005\u0003\u0000\u000001\u0005\u000f"+
		"\u0000\u000012\u0005\b\u0000\u000023\u0003\u000e\u0007\u000034\u0005\t"+
		"\u0000\u00004\t\u0001\u0000\u0000\u000056\u0005\u0004\u0000\u000067\u0005"+
		"\u000f\u0000\u000078\u0005\b\u0000\u000089\u0003\u000e\u0007\u00009:\u0005"+
		"\t\u0000\u0000:\u000b\u0001\u0000\u0000\u0000;<\u0005\u0005\u0000\u0000"+
		"<=\u0007\u0000\u0000\u0000=>\u0005\u000f\u0000\u0000>?\u0005\b\u0000\u0000"+
		"?@\u0003\u000e\u0007\u0000@A\u0005\t\u0000\u0000A\r\u0001\u0000\u0000"+
		"\u0000BC\u0003\u0010\b\u0000CD\u0005\n\u0000\u0000DF\u0001\u0000\u0000"+
		"\u0000EB\u0001\u0000\u0000\u0000FG\u0001\u0000\u0000\u0000GE\u0001\u0000"+
		"\u0000\u0000GH\u0001\u0000\u0000\u0000H\u000f\u0001\u0000\u0000\u0000"+
		"IJ\u0005\u000f\u0000\u0000JK\u0005\u000b\u0000\u0000KL\u0003\u0012\t\u0000"+
		"L\u0011\u0001\u0000\u0000\u0000MN\u0007\u0001\u0000\u0000N\u0013\u0001"+
		"\u0000\u0000\u0000\u0003\u0017!G";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}