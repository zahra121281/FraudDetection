// Generated from c:/git/compiler/FraudDetection/grammar/DetectCommands.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class DetectCommandsParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		STRING=18, NUMBER=19, DATE=20, Pass=21, WS=22, NewLine=23;
	public static final int
		RULE_start = 0, RULE_setting = 1, RULE_url = 2, RULE_username = 3, RULE_pass = 4, 
		RULE_dbname = 5, RULE_load_terminal = 6, RULE_load_customer = 7, RULE_load_transaction = 8, 
		RULE_path = 9, RULE_commands = 10, RULE_command = 11, RULE_detect_customer = 12, 
		RULE_detect_terminal = 13, RULE_detect_date_range = 14, RULE_detect_degree_limit = 15, 
		RULE_start_date = 16, RULE_end_date = 17, RULE_limit = 18, RULE_degree = 19;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "setting", "url", "username", "pass", "dbname", "load_terminal", 
			"load_customer", "load_transaction", "path", "commands", "command", "detect_customer", 
			"detect_terminal", "detect_date_range", "detect_degree_limit", "start_date", 
			"end_date", "limit", "degree"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'Setting'", "'url='", "'username='", "'pass='", "'Databasename='", 
			"'LoadTerminal'", "'LoadCustomer'", "'LoadTransaction'", "'Detect'", 
			"'customer'", "'terminal'", "'name3'", "'name4'", "'startdate='", "'enddate='", 
			"'limit='", "'degree='", null, null, null, null, null, "'\\n'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, "STRING", "NUMBER", "DATE", "Pass", 
			"WS", "NewLine"
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
	public String getGrammarFileName() { return "DetectCommands.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public DetectCommandsParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StartContext extends ParserRuleContext {
		public SettingContext setting() {
			return getRuleContext(SettingContext.class,0);
		}
		public Load_terminalContext load_terminal() {
			return getRuleContext(Load_terminalContext.class,0);
		}
		public Load_customerContext load_customer() {
			return getRuleContext(Load_customerContext.class,0);
		}
		public Load_transactionContext load_transaction() {
			return getRuleContext(Load_transactionContext.class,0);
		}
		public CommandsContext commands() {
			return getRuleContext(CommandsContext.class,0);
		}
		public TerminalNode EOF() { return getToken(DetectCommandsParser.EOF, 0); }
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(40);
			setting();
			setState(41);
			load_terminal();
			setState(42);
			load_customer();
			setState(43);
			load_transaction();
			setState(44);
			commands();
			setState(45);
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
	public static class SettingContext extends ParserRuleContext {
		public UrlContext url() {
			return getRuleContext(UrlContext.class,0);
		}
		public UsernameContext username() {
			return getRuleContext(UsernameContext.class,0);
		}
		public PassContext pass() {
			return getRuleContext(PassContext.class,0);
		}
		public DbnameContext dbname() {
			return getRuleContext(DbnameContext.class,0);
		}
		public List<TerminalNode> NewLine() { return getTokens(DetectCommandsParser.NewLine); }
		public TerminalNode NewLine(int i) {
			return getToken(DetectCommandsParser.NewLine, i);
		}
		public SettingContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_setting; }
	}

	public final SettingContext setting() throws RecognitionException {
		SettingContext _localctx = new SettingContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_setting);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(T__0);
			setState(48);
			url();
			setState(49);
			username();
			setState(50);
			pass();
			setState(51);
			dbname();
			setState(55);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NewLine) {
				{
				{
				setState(52);
				match(NewLine);
				}
				}
				setState(57);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class UrlContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(DetectCommandsParser.STRING, 0); }
		public UrlContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_url; }
	}

	public final UrlContext url() throws RecognitionException {
		UrlContext _localctx = new UrlContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_url);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			match(T__1);
			setState(59);
			match(STRING);
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
	public static class UsernameContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(DetectCommandsParser.STRING, 0); }
		public UsernameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_username; }
	}

	public final UsernameContext username() throws RecognitionException {
		UsernameContext _localctx = new UsernameContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_username);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			match(T__2);
			setState(62);
			match(STRING);
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
	public static class PassContext extends ParserRuleContext {
		public TerminalNode Pass() { return getToken(DetectCommandsParser.Pass, 0); }
		public PassContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pass; }
	}

	public final PassContext pass() throws RecognitionException {
		PassContext _localctx = new PassContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_pass);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(64);
			match(T__3);
			setState(65);
			match(Pass);
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
	public static class DbnameContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(DetectCommandsParser.STRING, 0); }
		public DbnameContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_dbname; }
	}

	public final DbnameContext dbname() throws RecognitionException {
		DbnameContext _localctx = new DbnameContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_dbname);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(67);
			match(T__4);
			setState(68);
			match(STRING);
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
	public static class Load_terminalContext extends ParserRuleContext {
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public List<TerminalNode> NewLine() { return getTokens(DetectCommandsParser.NewLine); }
		public TerminalNode NewLine(int i) {
			return getToken(DetectCommandsParser.NewLine, i);
		}
		public Load_terminalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_load_terminal; }
	}

	public final Load_terminalContext load_terminal() throws RecognitionException {
		Load_terminalContext _localctx = new Load_terminalContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_load_terminal);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(T__5);
			setState(71);
			path();
			setState(75);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NewLine) {
				{
				{
				setState(72);
				match(NewLine);
				}
				}
				setState(77);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class Load_customerContext extends ParserRuleContext {
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public List<TerminalNode> NewLine() { return getTokens(DetectCommandsParser.NewLine); }
		public TerminalNode NewLine(int i) {
			return getToken(DetectCommandsParser.NewLine, i);
		}
		public Load_customerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_load_customer; }
	}

	public final Load_customerContext load_customer() throws RecognitionException {
		Load_customerContext _localctx = new Load_customerContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_load_customer);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			match(T__6);
			setState(79);
			path();
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NewLine) {
				{
				{
				setState(80);
				match(NewLine);
				}
				}
				setState(85);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class Load_transactionContext extends ParserRuleContext {
		public PathContext path() {
			return getRuleContext(PathContext.class,0);
		}
		public List<TerminalNode> NewLine() { return getTokens(DetectCommandsParser.NewLine); }
		public TerminalNode NewLine(int i) {
			return getToken(DetectCommandsParser.NewLine, i);
		}
		public Load_transactionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_load_transaction; }
	}

	public final Load_transactionContext load_transaction() throws RecognitionException {
		Load_transactionContext _localctx = new Load_transactionContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_load_transaction);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			match(T__7);
			setState(87);
			path();
			setState(91);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NewLine) {
				{
				{
				setState(88);
				match(NewLine);
				}
				}
				setState(93);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class PathContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(DetectCommandsParser.STRING, 0); }
		public PathContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_path; }
	}

	public final PathContext path() throws RecognitionException {
		PathContext _localctx = new PathContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_path);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(94);
			match(STRING);
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
	public static class CommandsContext extends ParserRuleContext {
		public List<CommandContext> command() {
			return getRuleContexts(CommandContext.class);
		}
		public CommandContext command(int i) {
			return getRuleContext(CommandContext.class,i);
		}
		public CommandsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_commands; }
	}

	public final CommandsContext commands() throws RecognitionException {
		CommandsContext _localctx = new CommandsContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_commands);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(96);
				command();
				}
				}
				setState(99); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==T__8 );
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
	public static class CommandContext extends ParserRuleContext {
		public Detect_customerContext detect_customer() {
			return getRuleContext(Detect_customerContext.class,0);
		}
		public Detect_terminalContext detect_terminal() {
			return getRuleContext(Detect_terminalContext.class,0);
		}
		public Detect_date_rangeContext detect_date_range() {
			return getRuleContext(Detect_date_rangeContext.class,0);
		}
		public Detect_degree_limitContext detect_degree_limit() {
			return getRuleContext(Detect_degree_limitContext.class,0);
		}
		public List<TerminalNode> NewLine() { return getTokens(DetectCommandsParser.NewLine); }
		public TerminalNode NewLine(int i) {
			return getToken(DetectCommandsParser.NewLine, i);
		}
		public CommandContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_command; }
	}

	public final CommandContext command() throws RecognitionException {
		CommandContext _localctx = new CommandContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_command);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(T__8);
			setState(106);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__9:
				{
				setState(102);
				detect_customer();
				}
				break;
			case T__10:
				{
				setState(103);
				detect_terminal();
				}
				break;
			case T__11:
				{
				setState(104);
				detect_date_range();
				}
				break;
			case T__12:
				{
				setState(105);
				detect_degree_limit();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(111);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==NewLine) {
				{
				{
				setState(108);
				match(NewLine);
				}
				}
				setState(113);
				_errHandler.sync(this);
				_la = _input.LA(1);
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
	public static class Detect_customerContext extends ParserRuleContext {
		public Start_dateContext start_date() {
			return getRuleContext(Start_dateContext.class,0);
		}
		public End_dateContext end_date() {
			return getRuleContext(End_dateContext.class,0);
		}
		public LimitContext limit() {
			return getRuleContext(LimitContext.class,0);
		}
		public Detect_customerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_detect_customer; }
	}

	public final Detect_customerContext detect_customer() throws RecognitionException {
		Detect_customerContext _localctx = new Detect_customerContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_detect_customer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(114);
			match(T__9);
			setState(115);
			start_date();
			setState(116);
			end_date();
			setState(117);
			limit();
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
	public static class Detect_terminalContext extends ParserRuleContext {
		public Start_dateContext start_date() {
			return getRuleContext(Start_dateContext.class,0);
		}
		public End_dateContext end_date() {
			return getRuleContext(End_dateContext.class,0);
		}
		public LimitContext limit() {
			return getRuleContext(LimitContext.class,0);
		}
		public Detect_terminalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_detect_terminal; }
	}

	public final Detect_terminalContext detect_terminal() throws RecognitionException {
		Detect_terminalContext _localctx = new Detect_terminalContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_detect_terminal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			match(T__10);
			setState(120);
			start_date();
			setState(121);
			end_date();
			setState(122);
			limit();
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
	public static class Detect_date_rangeContext extends ParserRuleContext {
		public Start_dateContext start_date() {
			return getRuleContext(Start_dateContext.class,0);
		}
		public End_dateContext end_date() {
			return getRuleContext(End_dateContext.class,0);
		}
		public Detect_date_rangeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_detect_date_range; }
	}

	public final Detect_date_rangeContext detect_date_range() throws RecognitionException {
		Detect_date_rangeContext _localctx = new Detect_date_rangeContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_detect_date_range);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(124);
			match(T__11);
			setState(125);
			start_date();
			setState(126);
			end_date();
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
	public static class Detect_degree_limitContext extends ParserRuleContext {
		public DegreeContext degree() {
			return getRuleContext(DegreeContext.class,0);
		}
		public LimitContext limit() {
			return getRuleContext(LimitContext.class,0);
		}
		public Detect_degree_limitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_detect_degree_limit; }
	}

	public final Detect_degree_limitContext detect_degree_limit() throws RecognitionException {
		Detect_degree_limitContext _localctx = new Detect_degree_limitContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_detect_degree_limit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(T__12);
			setState(129);
			degree();
			setState(130);
			limit();
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
	public static class Start_dateContext extends ParserRuleContext {
		public TerminalNode DATE() { return getToken(DetectCommandsParser.DATE, 0); }
		public Start_dateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start_date; }
	}

	public final Start_dateContext start_date() throws RecognitionException {
		Start_dateContext _localctx = new Start_dateContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_start_date);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(T__13);
			setState(133);
			match(DATE);
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
	public static class End_dateContext extends ParserRuleContext {
		public TerminalNode DATE() { return getToken(DetectCommandsParser.DATE, 0); }
		public End_dateContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_end_date; }
	}

	public final End_dateContext end_date() throws RecognitionException {
		End_dateContext _localctx = new End_dateContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_end_date);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(T__14);
			setState(136);
			match(DATE);
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
	public static class LimitContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(DetectCommandsParser.NUMBER, 0); }
		public LimitContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_limit; }
	}

	public final LimitContext limit() throws RecognitionException {
		LimitContext _localctx = new LimitContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_limit);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			match(T__15);
			setState(139);
			match(NUMBER);
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
	public static class DegreeContext extends ParserRuleContext {
		public TerminalNode NUMBER() { return getToken(DetectCommandsParser.NUMBER, 0); }
		public DegreeContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_degree; }
	}

	public final DegreeContext degree() throws RecognitionException {
		DegreeContext _localctx = new DegreeContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_degree);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			match(T__16);
			setState(142);
			match(NUMBER);
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
		"\u0004\u0001\u0017\u0091\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007"+
		"\u000f\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007"+
		"\u0012\u0002\u0013\u0007\u0013\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0005\u00016\b\u0001\n\u0001"+
		"\f\u00019\t\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006J\b"+
		"\u0006\n\u0006\f\u0006M\t\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0005"+
		"\u0007R\b\u0007\n\u0007\f\u0007U\t\u0007\u0001\b\u0001\b\u0001\b\u0005"+
		"\bZ\b\b\n\b\f\b]\t\b\u0001\t\u0001\t\u0001\n\u0004\nb\b\n\u000b\n\f\n"+
		"c\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b"+
		"k\b\u000b\u0001\u000b\u0005\u000bn\b\u000b\n\u000b\f\u000bq\t\u000b\u0001"+
		"\f\u0001\f\u0001\f\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001\u000f"+
		"\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010\u0001\u0011"+
		"\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0000\u0000\u0014\u0000\u0002\u0004"+
		"\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \""+
		"$&\u0000\u0000\u0085\u0000(\u0001\u0000\u0000\u0000\u0002/\u0001\u0000"+
		"\u0000\u0000\u0004:\u0001\u0000\u0000\u0000\u0006=\u0001\u0000\u0000\u0000"+
		"\b@\u0001\u0000\u0000\u0000\nC\u0001\u0000\u0000\u0000\fF\u0001\u0000"+
		"\u0000\u0000\u000eN\u0001\u0000\u0000\u0000\u0010V\u0001\u0000\u0000\u0000"+
		"\u0012^\u0001\u0000\u0000\u0000\u0014a\u0001\u0000\u0000\u0000\u0016e"+
		"\u0001\u0000\u0000\u0000\u0018r\u0001\u0000\u0000\u0000\u001aw\u0001\u0000"+
		"\u0000\u0000\u001c|\u0001\u0000\u0000\u0000\u001e\u0080\u0001\u0000\u0000"+
		"\u0000 \u0084\u0001\u0000\u0000\u0000\"\u0087\u0001\u0000\u0000\u0000"+
		"$\u008a\u0001\u0000\u0000\u0000&\u008d\u0001\u0000\u0000\u0000()\u0003"+
		"\u0002\u0001\u0000)*\u0003\f\u0006\u0000*+\u0003\u000e\u0007\u0000+,\u0003"+
		"\u0010\b\u0000,-\u0003\u0014\n\u0000-.\u0005\u0000\u0000\u0001.\u0001"+
		"\u0001\u0000\u0000\u0000/0\u0005\u0001\u0000\u000001\u0003\u0004\u0002"+
		"\u000012\u0003\u0006\u0003\u000023\u0003\b\u0004\u000037\u0003\n\u0005"+
		"\u000046\u0005\u0017\u0000\u000054\u0001\u0000\u0000\u000069\u0001\u0000"+
		"\u0000\u000075\u0001\u0000\u0000\u000078\u0001\u0000\u0000\u00008\u0003"+
		"\u0001\u0000\u0000\u000097\u0001\u0000\u0000\u0000:;\u0005\u0002\u0000"+
		"\u0000;<\u0005\u0012\u0000\u0000<\u0005\u0001\u0000\u0000\u0000=>\u0005"+
		"\u0003\u0000\u0000>?\u0005\u0012\u0000\u0000?\u0007\u0001\u0000\u0000"+
		"\u0000@A\u0005\u0004\u0000\u0000AB\u0005\u0015\u0000\u0000B\t\u0001\u0000"+
		"\u0000\u0000CD\u0005\u0005\u0000\u0000DE\u0005\u0012\u0000\u0000E\u000b"+
		"\u0001\u0000\u0000\u0000FG\u0005\u0006\u0000\u0000GK\u0003\u0012\t\u0000"+
		"HJ\u0005\u0017\u0000\u0000IH\u0001\u0000\u0000\u0000JM\u0001\u0000\u0000"+
		"\u0000KI\u0001\u0000\u0000\u0000KL\u0001\u0000\u0000\u0000L\r\u0001\u0000"+
		"\u0000\u0000MK\u0001\u0000\u0000\u0000NO\u0005\u0007\u0000\u0000OS\u0003"+
		"\u0012\t\u0000PR\u0005\u0017\u0000\u0000QP\u0001\u0000\u0000\u0000RU\u0001"+
		"\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000ST\u0001\u0000\u0000\u0000"+
		"T\u000f\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000VW\u0005\b\u0000"+
		"\u0000W[\u0003\u0012\t\u0000XZ\u0005\u0017\u0000\u0000YX\u0001\u0000\u0000"+
		"\u0000Z]\u0001\u0000\u0000\u0000[Y\u0001\u0000\u0000\u0000[\\\u0001\u0000"+
		"\u0000\u0000\\\u0011\u0001\u0000\u0000\u0000][\u0001\u0000\u0000\u0000"+
		"^_\u0005\u0012\u0000\u0000_\u0013\u0001\u0000\u0000\u0000`b\u0003\u0016"+
		"\u000b\u0000a`\u0001\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000ca\u0001"+
		"\u0000\u0000\u0000cd\u0001\u0000\u0000\u0000d\u0015\u0001\u0000\u0000"+
		"\u0000ej\u0005\t\u0000\u0000fk\u0003\u0018\f\u0000gk\u0003\u001a\r\u0000"+
		"hk\u0003\u001c\u000e\u0000ik\u0003\u001e\u000f\u0000jf\u0001\u0000\u0000"+
		"\u0000jg\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000ji\u0001\u0000"+
		"\u0000\u0000ko\u0001\u0000\u0000\u0000ln\u0005\u0017\u0000\u0000ml\u0001"+
		"\u0000\u0000\u0000nq\u0001\u0000\u0000\u0000om\u0001\u0000\u0000\u0000"+
		"op\u0001\u0000\u0000\u0000p\u0017\u0001\u0000\u0000\u0000qo\u0001\u0000"+
		"\u0000\u0000rs\u0005\n\u0000\u0000st\u0003 \u0010\u0000tu\u0003\"\u0011"+
		"\u0000uv\u0003$\u0012\u0000v\u0019\u0001\u0000\u0000\u0000wx\u0005\u000b"+
		"\u0000\u0000xy\u0003 \u0010\u0000yz\u0003\"\u0011\u0000z{\u0003$\u0012"+
		"\u0000{\u001b\u0001\u0000\u0000\u0000|}\u0005\f\u0000\u0000}~\u0003 \u0010"+
		"\u0000~\u007f\u0003\"\u0011\u0000\u007f\u001d\u0001\u0000\u0000\u0000"+
		"\u0080\u0081\u0005\r\u0000\u0000\u0081\u0082\u0003&\u0013\u0000\u0082"+
		"\u0083\u0003$\u0012\u0000\u0083\u001f\u0001\u0000\u0000\u0000\u0084\u0085"+
		"\u0005\u000e\u0000\u0000\u0085\u0086\u0005\u0014\u0000\u0000\u0086!\u0001"+
		"\u0000\u0000\u0000\u0087\u0088\u0005\u000f\u0000\u0000\u0088\u0089\u0005"+
		"\u0014\u0000\u0000\u0089#\u0001\u0000\u0000\u0000\u008a\u008b\u0005\u0010"+
		"\u0000\u0000\u008b\u008c\u0005\u0013\u0000\u0000\u008c%\u0001\u0000\u0000"+
		"\u0000\u008d\u008e\u0005\u0011\u0000\u0000\u008e\u008f\u0005\u0013\u0000"+
		"\u0000\u008f\'\u0001\u0000\u0000\u0000\u00077KS[cjo";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}