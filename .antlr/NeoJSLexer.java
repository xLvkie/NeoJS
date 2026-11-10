// Generated from /home/bookie/Proyectos/NeoJS/NeoJS.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue", "this-escape"})
public class NeoJSLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		TK_ITEM=1, TK_WEAPON=2, TK_RECIPE=3, TK_MOB=4, TK_MODIFY=5, TRUE=6, FALSE=7, 
		LBRACE=8, RBRACE=9, SEMI=10, COLON=11, PERCENTAGE=12, NUMBER=13, STRING=14, 
		ID=15, COMMENT=16, WS=17;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"TK_ITEM", "TK_WEAPON", "TK_RECIPE", "TK_MOB", "TK_MODIFY", "TRUE", "FALSE", 
			"LBRACE", "RBRACE", "SEMI", "COLON", "PERCENTAGE", "NUMBER", "STRING", 
			"ID", "COMMENT", "WS"
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


	public NeoJSLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "NeoJS.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\u0004\u0000\u0011\u00a2\u0006\uffff\uffff\u0002\u0000\u0007\u0000\u0002"+
		"\u0001\u0007\u0001\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002"+
		"\u0004\u0007\u0004\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002"+
		"\u0007\u0007\u0007\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002"+
		"\u000b\u0007\u000b\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e"+
		"\u0002\u000f\u0007\u000f\u0002\u0010\u0007\u0010\u0001\u0000\u0001\u0000"+
		"\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002"+
		"\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001"+
		"\b\u0001\t\u0001\t\u0001\n\u0001\n\u0001\u000b\u0004\u000bV\b\u000b\u000b"+
		"\u000b\f\u000bW\u0001\u000b\u0001\u000b\u0004\u000b\\\b\u000b\u000b\u000b"+
		"\f\u000b]\u0003\u000b`\b\u000b\u0001\u000b\u0001\u000b\u0001\f\u0003\f"+
		"e\b\f\u0001\f\u0004\fh\b\f\u000b\f\f\fi\u0001\f\u0001\f\u0004\fn\b\f\u000b"+
		"\f\f\fo\u0003\fr\b\f\u0001\r\u0001\r\u0005\rv\b\r\n\r\f\ry\t\r\u0001\r"+
		"\u0001\r\u0001\u000e\u0001\u000e\u0005\u000e\u007f\b\u000e\n\u000e\f\u000e"+
		"\u0082\t\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u0087\b"+
		"\u000e\n\u000e\f\u000e\u008a\t\u000e\u0005\u000e\u008c\b\u000e\n\u000e"+
		"\f\u000e\u008f\t\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f"+
		"\u0005\u000f\u0095\b\u000f\n\u000f\f\u000f\u0098\t\u000f\u0001\u000f\u0001"+
		"\u000f\u0001\u0010\u0004\u0010\u009d\b\u0010\u000b\u0010\f\u0010\u009e"+
		"\u0001\u0010\u0001\u0010\u0000\u0000\u0011\u0001\u0001\u0003\u0002\u0005"+
		"\u0003\u0007\u0004\t\u0005\u000b\u0006\r\u0007\u000f\b\u0011\t\u0013\n"+
		"\u0015\u000b\u0017\f\u0019\r\u001b\u000e\u001d\u000f\u001f\u0010!\u0011"+
		"\u0001\u0000\u0006\u0001\u000009\u0003\u0000\n\n\r\r\"\"\u0003\u0000A"+
		"Z__az\u0004\u000009AZ__az\u0002\u0000\n\n\r\r\u0003\u0000\t\n\r\r  \u00ae"+
		"\u0000\u0001\u0001\u0000\u0000\u0000\u0000\u0003\u0001\u0000\u0000\u0000"+
		"\u0000\u0005\u0001\u0000\u0000\u0000\u0000\u0007\u0001\u0000\u0000\u0000"+
		"\u0000\t\u0001\u0000\u0000\u0000\u0000\u000b\u0001\u0000\u0000\u0000\u0000"+
		"\r\u0001\u0000\u0000\u0000\u0000\u000f\u0001\u0000\u0000\u0000\u0000\u0011"+
		"\u0001\u0000\u0000\u0000\u0000\u0013\u0001\u0000\u0000\u0000\u0000\u0015"+
		"\u0001\u0000\u0000\u0000\u0000\u0017\u0001\u0000\u0000\u0000\u0000\u0019"+
		"\u0001\u0000\u0000\u0000\u0000\u001b\u0001\u0000\u0000\u0000\u0000\u001d"+
		"\u0001\u0000\u0000\u0000\u0000\u001f\u0001\u0000\u0000\u0000\u0000!\u0001"+
		"\u0000\u0000\u0000\u0001#\u0001\u0000\u0000\u0000\u0003(\u0001\u0000\u0000"+
		"\u0000\u0005/\u0001\u0000\u0000\u0000\u00076\u0001\u0000\u0000\u0000\t"+
		":\u0001\u0000\u0000\u0000\u000bA\u0001\u0000\u0000\u0000\rF\u0001\u0000"+
		"\u0000\u0000\u000fL\u0001\u0000\u0000\u0000\u0011N\u0001\u0000\u0000\u0000"+
		"\u0013P\u0001\u0000\u0000\u0000\u0015R\u0001\u0000\u0000\u0000\u0017U"+
		"\u0001\u0000\u0000\u0000\u0019d\u0001\u0000\u0000\u0000\u001bs\u0001\u0000"+
		"\u0000\u0000\u001d|\u0001\u0000\u0000\u0000\u001f\u0090\u0001\u0000\u0000"+
		"\u0000!\u009c\u0001\u0000\u0000\u0000#$\u0005i\u0000\u0000$%\u0005t\u0000"+
		"\u0000%&\u0005e\u0000\u0000&\'\u0005m\u0000\u0000\'\u0002\u0001\u0000"+
		"\u0000\u0000()\u0005w\u0000\u0000)*\u0005e\u0000\u0000*+\u0005a\u0000"+
		"\u0000+,\u0005p\u0000\u0000,-\u0005o\u0000\u0000-.\u0005n\u0000\u0000"+
		".\u0004\u0001\u0000\u0000\u0000/0\u0005r\u0000\u000001\u0005e\u0000\u0000"+
		"12\u0005c\u0000\u000023\u0005i\u0000\u000034\u0005p\u0000\u000045\u0005"+
		"e\u0000\u00005\u0006\u0001\u0000\u0000\u000067\u0005m\u0000\u000078\u0005"+
		"o\u0000\u000089\u0005b\u0000\u00009\b\u0001\u0000\u0000\u0000:;\u0005"+
		"m\u0000\u0000;<\u0005o\u0000\u0000<=\u0005d\u0000\u0000=>\u0005i\u0000"+
		"\u0000>?\u0005f\u0000\u0000?@\u0005y\u0000\u0000@\n\u0001\u0000\u0000"+
		"\u0000AB\u0005t\u0000\u0000BC\u0005r\u0000\u0000CD\u0005u\u0000\u0000"+
		"DE\u0005e\u0000\u0000E\f\u0001\u0000\u0000\u0000FG\u0005f\u0000\u0000"+
		"GH\u0005a\u0000\u0000HI\u0005l\u0000\u0000IJ\u0005s\u0000\u0000JK\u0005"+
		"e\u0000\u0000K\u000e\u0001\u0000\u0000\u0000LM\u0005{\u0000\u0000M\u0010"+
		"\u0001\u0000\u0000\u0000NO\u0005}\u0000\u0000O\u0012\u0001\u0000\u0000"+
		"\u0000PQ\u0005;\u0000\u0000Q\u0014\u0001\u0000\u0000\u0000RS\u0005:\u0000"+
		"\u0000S\u0016\u0001\u0000\u0000\u0000TV\u0007\u0000\u0000\u0000UT\u0001"+
		"\u0000\u0000\u0000VW\u0001\u0000\u0000\u0000WU\u0001\u0000\u0000\u0000"+
		"WX\u0001\u0000\u0000\u0000X_\u0001\u0000\u0000\u0000Y[\u0005.\u0000\u0000"+
		"Z\\\u0007\u0000\u0000\u0000[Z\u0001\u0000\u0000\u0000\\]\u0001\u0000\u0000"+
		"\u0000][\u0001\u0000\u0000\u0000]^\u0001\u0000\u0000\u0000^`\u0001\u0000"+
		"\u0000\u0000_Y\u0001\u0000\u0000\u0000_`\u0001\u0000\u0000\u0000`a\u0001"+
		"\u0000\u0000\u0000ab\u0005%\u0000\u0000b\u0018\u0001\u0000\u0000\u0000"+
		"ce\u0005-\u0000\u0000dc\u0001\u0000\u0000\u0000de\u0001\u0000\u0000\u0000"+
		"eg\u0001\u0000\u0000\u0000fh\u0007\u0000\u0000\u0000gf\u0001\u0000\u0000"+
		"\u0000hi\u0001\u0000\u0000\u0000ig\u0001\u0000\u0000\u0000ij\u0001\u0000"+
		"\u0000\u0000jq\u0001\u0000\u0000\u0000km\u0005.\u0000\u0000ln\u0007\u0000"+
		"\u0000\u0000ml\u0001\u0000\u0000\u0000no\u0001\u0000\u0000\u0000om\u0001"+
		"\u0000\u0000\u0000op\u0001\u0000\u0000\u0000pr\u0001\u0000\u0000\u0000"+
		"qk\u0001\u0000\u0000\u0000qr\u0001\u0000\u0000\u0000r\u001a\u0001\u0000"+
		"\u0000\u0000sw\u0005\"\u0000\u0000tv\b\u0001\u0000\u0000ut\u0001\u0000"+
		"\u0000\u0000vy\u0001\u0000\u0000\u0000wu\u0001\u0000\u0000\u0000wx\u0001"+
		"\u0000\u0000\u0000xz\u0001\u0000\u0000\u0000yw\u0001\u0000\u0000\u0000"+
		"z{\u0005\"\u0000\u0000{\u001c\u0001\u0000\u0000\u0000|\u0080\u0007\u0002"+
		"\u0000\u0000}\u007f\u0007\u0003\u0000\u0000~}\u0001\u0000\u0000\u0000"+
		"\u007f\u0082\u0001\u0000\u0000\u0000\u0080~\u0001\u0000\u0000\u0000\u0080"+
		"\u0081\u0001\u0000\u0000\u0000\u0081\u008d\u0001\u0000\u0000\u0000\u0082"+
		"\u0080\u0001\u0000\u0000\u0000\u0083\u0084\u0005:\u0000\u0000\u0084\u0088"+
		"\u0007\u0002\u0000\u0000\u0085\u0087\u0007\u0003\u0000\u0000\u0086\u0085"+
		"\u0001\u0000\u0000\u0000\u0087\u008a\u0001\u0000\u0000\u0000\u0088\u0086"+
		"\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000\u0089\u008c"+
		"\u0001\u0000\u0000\u0000\u008a\u0088\u0001\u0000\u0000\u0000\u008b\u0083"+
		"\u0001\u0000\u0000\u0000\u008c\u008f\u0001\u0000\u0000\u0000\u008d\u008b"+
		"\u0001\u0000\u0000\u0000\u008d\u008e\u0001\u0000\u0000\u0000\u008e\u001e"+
		"\u0001\u0000\u0000\u0000\u008f\u008d\u0001\u0000\u0000\u0000\u0090\u0091"+
		"\u0005/\u0000\u0000\u0091\u0092\u0005/\u0000\u0000\u0092\u0096\u0001\u0000"+
		"\u0000\u0000\u0093\u0095\b\u0004\u0000\u0000\u0094\u0093\u0001\u0000\u0000"+
		"\u0000\u0095\u0098\u0001\u0000\u0000\u0000\u0096\u0094\u0001\u0000\u0000"+
		"\u0000\u0096\u0097\u0001\u0000\u0000\u0000\u0097\u0099\u0001\u0000\u0000"+
		"\u0000\u0098\u0096\u0001\u0000\u0000\u0000\u0099\u009a\u0006\u000f\u0000"+
		"\u0000\u009a \u0001\u0000\u0000\u0000\u009b\u009d\u0007\u0005\u0000\u0000"+
		"\u009c\u009b\u0001\u0000\u0000\u0000\u009d\u009e\u0001\u0000\u0000\u0000"+
		"\u009e\u009c\u0001\u0000\u0000\u0000\u009e\u009f\u0001\u0000\u0000\u0000"+
		"\u009f\u00a0\u0001\u0000\u0000\u0000\u00a0\u00a1\u0006\u0010\u0000\u0000"+
		"\u00a1\"\u0001\u0000\u0000\u0000\u000e\u0000W]_dioqw\u0080\u0088\u008d"+
		"\u0096\u009e\u0001\u0006\u0000\u0000";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}