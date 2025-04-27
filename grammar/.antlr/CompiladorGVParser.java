// Generated from /Users/ogeorgehenrique/Desktop/Faculdade/Compiladores/compiladorGV/grammar/CompiladorGV.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CompiladorGVParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		LEIA=1, ESCREVA=2, SE=3, SENAO=4, PARA=5, ENQUANTO=6, RETORNA=7, TIPO_INT=8, 
		TIPO_STRING=9, ABRE_PAR=10, FECHA_PAR=11, ABRE_CHAVE=12, FECHA_CHAVE=13, 
		VIRGULA=14, FINAL=15, RECEBE=16, INCREMENTO=17, DECREMENTO=18, PLUS=19, 
		MINUS=20, MULT=21, DIV=22, IGUAL_EXATO=23, DIFERENTE=24, MAIOR_Q=25, MENOR_Q=26, 
		MENOR_IGUAL_Q=27, MAIOR_IGUAL_Q=28, AND=29, OR=30, NOT=31, STRING=32, 
		INTEIRO=33, FLOAT=34, ID=35, WS=36, ERRO=37;
	public static final int
		RULE_inicio = 0, RULE_comandos = 1, RULE_comando_declaracao_funcao = 2, 
		RULE_comando_chamada_funcao = 3, RULE_parametros = 4, RULE_parametro = 5, 
		RULE_argumentos = 6, RULE_comando_retorno = 7, RULE_comando_ler = 8, RULE_comando_escrever = 9, 
		RULE_comando_se = 10, RULE_comando_para = 11, RULE_comando_enquanto = 12, 
		RULE_comando_atribuicao = 13, RULE_comando_declaracao = 14, RULE_atribuicao = 15, 
		RULE_incremento = 16, RULE_condicao = 17, RULE_operador = 18, RULE_expressao = 19, 
		RULE_bloco = 20, RULE_bloco_funcao = 21;
	private static String[] makeRuleNames() {
		return new String[] {
			"inicio", "comandos", "comando_declaracao_funcao", "comando_chamada_funcao", 
			"parametros", "parametro", "argumentos", "comando_retorno", "comando_ler", 
			"comando_escrever", "comando_se", "comando_para", "comando_enquanto", 
			"comando_atribuicao", "comando_declaracao", "atribuicao", "incremento", 
			"condicao", "operador", "expressao", "bloco", "bloco_funcao"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'leia'", "'escreva'", "'se'", "'senao'", "'para'", "'enquanto'", 
			"'retorna'", "'int'", "'string'", "'('", "')'", "'{'", "'}'", "','", 
			"';'", "'='", "'++'", "'--'", "'+'", "'-'", "'*'", "'/'", "'=='", "'!='", 
			"'>'", "'<'", "'<='", "'>='", "'&&'", "'||'", "'!'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "LEIA", "ESCREVA", "SE", "SENAO", "PARA", "ENQUANTO", "RETORNA", 
			"TIPO_INT", "TIPO_STRING", "ABRE_PAR", "FECHA_PAR", "ABRE_CHAVE", "FECHA_CHAVE", 
			"VIRGULA", "FINAL", "RECEBE", "INCREMENTO", "DECREMENTO", "PLUS", "MINUS", 
			"MULT", "DIV", "IGUAL_EXATO", "DIFERENTE", "MAIOR_Q", "MENOR_Q", "MENOR_IGUAL_Q", 
			"MAIOR_IGUAL_Q", "AND", "OR", "NOT", "STRING", "INTEIRO", "FLOAT", "ID", 
			"WS", "ERRO"
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
	public String getGrammarFileName() { return "CompiladorGV.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CompiladorGVParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class InicioContext extends ParserRuleContext {
		public List<ComandosContext> comandos() {
			return getRuleContexts(ComandosContext.class);
		}
		public ComandosContext comandos(int i) {
			return getRuleContext(ComandosContext.class,i);
		}
		public InicioContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_inicio; }
	}

	public final InicioContext inicio() throws RecognitionException {
		InicioContext _localctx = new InicioContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_inicio);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(45); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(44);
				comandos();
				}
				}
				setState(47); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 34359739374L) != 0) );
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
	public static class ComandosContext extends ParserRuleContext {
		public Comando_declaracao_funcaoContext comando_declaracao_funcao() {
			return getRuleContext(Comando_declaracao_funcaoContext.class,0);
		}
		public Comando_chamada_funcaoContext comando_chamada_funcao() {
			return getRuleContext(Comando_chamada_funcaoContext.class,0);
		}
		public Comando_retornoContext comando_retorno() {
			return getRuleContext(Comando_retornoContext.class,0);
		}
		public Comando_lerContext comando_ler() {
			return getRuleContext(Comando_lerContext.class,0);
		}
		public Comando_escreverContext comando_escrever() {
			return getRuleContext(Comando_escreverContext.class,0);
		}
		public Comando_seContext comando_se() {
			return getRuleContext(Comando_seContext.class,0);
		}
		public Comando_paraContext comando_para() {
			return getRuleContext(Comando_paraContext.class,0);
		}
		public Comando_enquantoContext comando_enquanto() {
			return getRuleContext(Comando_enquantoContext.class,0);
		}
		public Comando_atribuicaoContext comando_atribuicao() {
			return getRuleContext(Comando_atribuicaoContext.class,0);
		}
		public Comando_declaracaoContext comando_declaracao() {
			return getRuleContext(Comando_declaracaoContext.class,0);
		}
		public ComandosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comandos; }
	}

	public final ComandosContext comandos() throws RecognitionException {
		ComandosContext _localctx = new ComandosContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_comandos);
		try {
			setState(59);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,1,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(49);
				comando_declaracao_funcao();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(50);
				comando_chamada_funcao();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(51);
				comando_retorno();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(52);
				comando_ler();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(53);
				comando_escrever();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(54);
				comando_se();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(55);
				comando_para();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(56);
				comando_enquanto();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(57);
				comando_atribuicao();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(58);
				comando_declaracao();
				}
				break;
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
	public static class Comando_declaracao_funcaoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CompiladorGVParser.ID, 0); }
		public TerminalNode ABRE_PAR() { return getToken(CompiladorGVParser.ABRE_PAR, 0); }
		public TerminalNode FECHA_PAR() { return getToken(CompiladorGVParser.FECHA_PAR, 0); }
		public Bloco_funcaoContext bloco_funcao() {
			return getRuleContext(Bloco_funcaoContext.class,0);
		}
		public TerminalNode TIPO_INT() { return getToken(CompiladorGVParser.TIPO_INT, 0); }
		public TerminalNode TIPO_STRING() { return getToken(CompiladorGVParser.TIPO_STRING, 0); }
		public ParametrosContext parametros() {
			return getRuleContext(ParametrosContext.class,0);
		}
		public Comando_declaracao_funcaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_declaracao_funcao; }
	}

	public final Comando_declaracao_funcaoContext comando_declaracao_funcao() throws RecognitionException {
		Comando_declaracao_funcaoContext _localctx = new Comando_declaracao_funcaoContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_comando_declaracao_funcao);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(61);
			_la = _input.LA(1);
			if ( !(_la==TIPO_INT || _la==TIPO_STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(62);
			match(ID);
			setState(63);
			match(ABRE_PAR);
			setState(65);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==TIPO_INT || _la==TIPO_STRING) {
				{
				setState(64);
				parametros();
				}
			}

			setState(67);
			match(FECHA_PAR);
			setState(68);
			bloco_funcao();
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
	public static class Comando_chamada_funcaoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CompiladorGVParser.ID, 0); }
		public TerminalNode ABRE_PAR() { return getToken(CompiladorGVParser.ABRE_PAR, 0); }
		public TerminalNode FECHA_PAR() { return getToken(CompiladorGVParser.FECHA_PAR, 0); }
		public TerminalNode FINAL() { return getToken(CompiladorGVParser.FINAL, 0); }
		public ArgumentosContext argumentos() {
			return getRuleContext(ArgumentosContext.class,0);
		}
		public Comando_chamada_funcaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_chamada_funcao; }
	}

	public final Comando_chamada_funcaoContext comando_chamada_funcao() throws RecognitionException {
		Comando_chamada_funcaoContext _localctx = new Comando_chamada_funcaoContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_comando_chamada_funcao);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(70);
			match(ID);
			setState(71);
			match(ABRE_PAR);
			setState(73);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 64424510464L) != 0)) {
				{
				setState(72);
				argumentos();
				}
			}

			setState(75);
			match(FECHA_PAR);
			setState(76);
			match(FINAL);
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
	public static class ParametrosContext extends ParserRuleContext {
		public List<ParametroContext> parametro() {
			return getRuleContexts(ParametroContext.class);
		}
		public ParametroContext parametro(int i) {
			return getRuleContext(ParametroContext.class,i);
		}
		public List<TerminalNode> VIRGULA() { return getTokens(CompiladorGVParser.VIRGULA); }
		public TerminalNode VIRGULA(int i) {
			return getToken(CompiladorGVParser.VIRGULA, i);
		}
		public ParametrosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametros; }
	}

	public final ParametrosContext parametros() throws RecognitionException {
		ParametrosContext _localctx = new ParametrosContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_parametros);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(78);
			parametro();
			setState(83);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VIRGULA) {
				{
				{
				setState(79);
				match(VIRGULA);
				setState(80);
				parametro();
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
	public static class ParametroContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CompiladorGVParser.ID, 0); }
		public TerminalNode TIPO_INT() { return getToken(CompiladorGVParser.TIPO_INT, 0); }
		public TerminalNode TIPO_STRING() { return getToken(CompiladorGVParser.TIPO_STRING, 0); }
		public ParametroContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parametro; }
	}

	public final ParametroContext parametro() throws RecognitionException {
		ParametroContext _localctx = new ParametroContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_parametro);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(86);
			_la = _input.LA(1);
			if ( !(_la==TIPO_INT || _la==TIPO_STRING) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			setState(87);
			match(ID);
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
	public static class ArgumentosContext extends ParserRuleContext {
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public List<TerminalNode> VIRGULA() { return getTokens(CompiladorGVParser.VIRGULA); }
		public TerminalNode VIRGULA(int i) {
			return getToken(CompiladorGVParser.VIRGULA, i);
		}
		public ArgumentosContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentos; }
	}

	public final ArgumentosContext argumentos() throws RecognitionException {
		ArgumentosContext _localctx = new ArgumentosContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_argumentos);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(89);
			expressao(0);
			setState(94);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==VIRGULA) {
				{
				{
				setState(90);
				match(VIRGULA);
				setState(91);
				expressao(0);
				}
				}
				setState(96);
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
	public static class Comando_retornoContext extends ParserRuleContext {
		public TerminalNode RETORNA() { return getToken(CompiladorGVParser.RETORNA, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode FINAL() { return getToken(CompiladorGVParser.FINAL, 0); }
		public Comando_retornoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_retorno; }
	}

	public final Comando_retornoContext comando_retorno() throws RecognitionException {
		Comando_retornoContext _localctx = new Comando_retornoContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_comando_retorno);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(97);
			match(RETORNA);
			setState(98);
			expressao(0);
			setState(99);
			match(FINAL);
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
	public static class Comando_lerContext extends ParserRuleContext {
		public TerminalNode LEIA() { return getToken(CompiladorGVParser.LEIA, 0); }
		public TerminalNode ABRE_PAR() { return getToken(CompiladorGVParser.ABRE_PAR, 0); }
		public TerminalNode ID() { return getToken(CompiladorGVParser.ID, 0); }
		public TerminalNode FECHA_PAR() { return getToken(CompiladorGVParser.FECHA_PAR, 0); }
		public TerminalNode FINAL() { return getToken(CompiladorGVParser.FINAL, 0); }
		public Comando_lerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_ler; }
	}

	public final Comando_lerContext comando_ler() throws RecognitionException {
		Comando_lerContext _localctx = new Comando_lerContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_comando_ler);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(101);
			match(LEIA);
			setState(102);
			match(ABRE_PAR);
			setState(103);
			match(ID);
			setState(104);
			match(FECHA_PAR);
			setState(105);
			match(FINAL);
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
	public static class Comando_escreverContext extends ParserRuleContext {
		public TerminalNode ESCREVA() { return getToken(CompiladorGVParser.ESCREVA, 0); }
		public TerminalNode ABRE_PAR() { return getToken(CompiladorGVParser.ABRE_PAR, 0); }
		public TerminalNode FECHA_PAR() { return getToken(CompiladorGVParser.FECHA_PAR, 0); }
		public TerminalNode FINAL() { return getToken(CompiladorGVParser.FINAL, 0); }
		public TerminalNode STRING() { return getToken(CompiladorGVParser.STRING, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public Comando_escreverContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_escrever; }
	}

	public final Comando_escreverContext comando_escrever() throws RecognitionException {
		Comando_escreverContext _localctx = new Comando_escreverContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_comando_escrever);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			match(ESCREVA);
			setState(108);
			match(ABRE_PAR);
			setState(111);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				{
				setState(109);
				match(STRING);
				}
				break;
			case 2:
				{
				setState(110);
				expressao(0);
				}
				break;
			}
			setState(113);
			match(FECHA_PAR);
			setState(114);
			match(FINAL);
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
	public static class Comando_seContext extends ParserRuleContext {
		public TerminalNode SE() { return getToken(CompiladorGVParser.SE, 0); }
		public TerminalNode ABRE_PAR() { return getToken(CompiladorGVParser.ABRE_PAR, 0); }
		public CondicaoContext condicao() {
			return getRuleContext(CondicaoContext.class,0);
		}
		public TerminalNode FECHA_PAR() { return getToken(CompiladorGVParser.FECHA_PAR, 0); }
		public List<BlocoContext> bloco() {
			return getRuleContexts(BlocoContext.class);
		}
		public BlocoContext bloco(int i) {
			return getRuleContext(BlocoContext.class,i);
		}
		public TerminalNode SENAO() { return getToken(CompiladorGVParser.SENAO, 0); }
		public Comando_seContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_se; }
	}

	public final Comando_seContext comando_se() throws RecognitionException {
		Comando_seContext _localctx = new Comando_seContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_comando_se);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(116);
			match(SE);
			setState(117);
			match(ABRE_PAR);
			setState(118);
			condicao(0);
			setState(119);
			match(FECHA_PAR);
			setState(120);
			bloco();
			setState(123);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==SENAO) {
				{
				setState(121);
				match(SENAO);
				setState(122);
				bloco();
				}
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
	public static class Comando_paraContext extends ParserRuleContext {
		public TerminalNode PARA() { return getToken(CompiladorGVParser.PARA, 0); }
		public TerminalNode ABRE_PAR() { return getToken(CompiladorGVParser.ABRE_PAR, 0); }
		public AtribuicaoContext atribuicao() {
			return getRuleContext(AtribuicaoContext.class,0);
		}
		public List<TerminalNode> FINAL() { return getTokens(CompiladorGVParser.FINAL); }
		public TerminalNode FINAL(int i) {
			return getToken(CompiladorGVParser.FINAL, i);
		}
		public CondicaoContext condicao() {
			return getRuleContext(CondicaoContext.class,0);
		}
		public IncrementoContext incremento() {
			return getRuleContext(IncrementoContext.class,0);
		}
		public TerminalNode FECHA_PAR() { return getToken(CompiladorGVParser.FECHA_PAR, 0); }
		public BlocoContext bloco() {
			return getRuleContext(BlocoContext.class,0);
		}
		public Comando_paraContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_para; }
	}

	public final Comando_paraContext comando_para() throws RecognitionException {
		Comando_paraContext _localctx = new Comando_paraContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_comando_para);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(125);
			match(PARA);
			setState(126);
			match(ABRE_PAR);
			setState(127);
			atribuicao();
			setState(128);
			match(FINAL);
			setState(129);
			condicao(0);
			setState(130);
			match(FINAL);
			setState(131);
			incremento();
			setState(132);
			match(FECHA_PAR);
			setState(133);
			bloco();
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
	public static class Comando_enquantoContext extends ParserRuleContext {
		public TerminalNode ENQUANTO() { return getToken(CompiladorGVParser.ENQUANTO, 0); }
		public TerminalNode ABRE_PAR() { return getToken(CompiladorGVParser.ABRE_PAR, 0); }
		public CondicaoContext condicao() {
			return getRuleContext(CondicaoContext.class,0);
		}
		public TerminalNode FECHA_PAR() { return getToken(CompiladorGVParser.FECHA_PAR, 0); }
		public BlocoContext bloco() {
			return getRuleContext(BlocoContext.class,0);
		}
		public Comando_enquantoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_enquanto; }
	}

	public final Comando_enquantoContext comando_enquanto() throws RecognitionException {
		Comando_enquantoContext _localctx = new Comando_enquantoContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_comando_enquanto);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(135);
			match(ENQUANTO);
			setState(136);
			match(ABRE_PAR);
			setState(137);
			condicao(0);
			setState(138);
			match(FECHA_PAR);
			setState(139);
			bloco();
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
	public static class Comando_atribuicaoContext extends ParserRuleContext {
		public AtribuicaoContext atribuicao() {
			return getRuleContext(AtribuicaoContext.class,0);
		}
		public TerminalNode FINAL() { return getToken(CompiladorGVParser.FINAL, 0); }
		public Comando_atribuicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_atribuicao; }
	}

	public final Comando_atribuicaoContext comando_atribuicao() throws RecognitionException {
		Comando_atribuicaoContext _localctx = new Comando_atribuicaoContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_comando_atribuicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(141);
			atribuicao();
			setState(142);
			match(FINAL);
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
	public static class Comando_declaracaoContext extends ParserRuleContext {
		public TerminalNode TIPO_INT() { return getToken(CompiladorGVParser.TIPO_INT, 0); }
		public TerminalNode ID() { return getToken(CompiladorGVParser.ID, 0); }
		public TerminalNode FINAL() { return getToken(CompiladorGVParser.FINAL, 0); }
		public TerminalNode RECEBE() { return getToken(CompiladorGVParser.RECEBE, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public TerminalNode TIPO_STRING() { return getToken(CompiladorGVParser.TIPO_STRING, 0); }
		public Comando_declaracaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comando_declaracao; }
	}

	public final Comando_declaracaoContext comando_declaracao() throws RecognitionException {
		Comando_declaracaoContext _localctx = new Comando_declaracaoContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_comando_declaracao);
		int _la;
		try {
			setState(158);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case TIPO_INT:
				enterOuterAlt(_localctx, 1);
				{
				setState(144);
				match(TIPO_INT);
				setState(145);
				match(ID);
				setState(148);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==RECEBE) {
					{
					setState(146);
					match(RECEBE);
					setState(147);
					expressao(0);
					}
				}

				setState(150);
				match(FINAL);
				}
				break;
			case TIPO_STRING:
				enterOuterAlt(_localctx, 2);
				{
				setState(151);
				match(TIPO_STRING);
				setState(152);
				match(ID);
				setState(155);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==RECEBE) {
					{
					setState(153);
					match(RECEBE);
					setState(154);
					expressao(0);
					}
				}

				setState(157);
				match(FINAL);
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
	public static class AtribuicaoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CompiladorGVParser.ID, 0); }
		public TerminalNode RECEBE() { return getToken(CompiladorGVParser.RECEBE, 0); }
		public ExpressaoContext expressao() {
			return getRuleContext(ExpressaoContext.class,0);
		}
		public AtribuicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_atribuicao; }
	}

	public final AtribuicaoContext atribuicao() throws RecognitionException {
		AtribuicaoContext _localctx = new AtribuicaoContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_atribuicao);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			match(ID);
			setState(161);
			match(RECEBE);
			setState(162);
			expressao(0);
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
	public static class IncrementoContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CompiladorGVParser.ID, 0); }
		public TerminalNode INCREMENTO() { return getToken(CompiladorGVParser.INCREMENTO, 0); }
		public TerminalNode DECREMENTO() { return getToken(CompiladorGVParser.DECREMENTO, 0); }
		public AtribuicaoContext atribuicao() {
			return getRuleContext(AtribuicaoContext.class,0);
		}
		public IncrementoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_incremento; }
	}

	public final IncrementoContext incremento() throws RecognitionException {
		IncrementoContext _localctx = new IncrementoContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_incremento);
		try {
			setState(169);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(164);
				match(ID);
				setState(165);
				match(INCREMENTO);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(166);
				match(ID);
				setState(167);
				match(DECREMENTO);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(168);
				atribuicao();
				}
				break;
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
	public static class CondicaoContext extends ParserRuleContext {
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public OperadorContext operador() {
			return getRuleContext(OperadorContext.class,0);
		}
		public TerminalNode ABRE_PAR() { return getToken(CompiladorGVParser.ABRE_PAR, 0); }
		public List<CondicaoContext> condicao() {
			return getRuleContexts(CondicaoContext.class);
		}
		public CondicaoContext condicao(int i) {
			return getRuleContext(CondicaoContext.class,i);
		}
		public TerminalNode FECHA_PAR() { return getToken(CompiladorGVParser.FECHA_PAR, 0); }
		public TerminalNode AND() { return getToken(CompiladorGVParser.AND, 0); }
		public TerminalNode OR() { return getToken(CompiladorGVParser.OR, 0); }
		public CondicaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condicao; }
	}

	public final CondicaoContext condicao() throws RecognitionException {
		return condicao(0);
	}

	private CondicaoContext condicao(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		CondicaoContext _localctx = new CondicaoContext(_ctx, _parentState);
		CondicaoContext _prevctx = _localctx;
		int _startState = 34;
		enterRecursionRule(_localctx, 34, RULE_condicao, _p);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(172);
				expressao(0);
				setState(173);
				operador();
				setState(174);
				expressao(0);
				}
				break;
			case 2:
				{
				setState(176);
				match(ABRE_PAR);
				setState(177);
				condicao(0);
				setState(178);
				match(FECHA_PAR);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(190);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(188);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
					case 1:
						{
						_localctx = new CondicaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_condicao);
						setState(182);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(183);
						match(AND);
						setState(184);
						condicao(4);
						}
						break;
					case 2:
						{
						_localctx = new CondicaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_condicao);
						setState(185);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(186);
						match(OR);
						setState(187);
						condicao(3);
						}
						break;
					}
					} 
				}
				setState(192);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperadorContext extends ParserRuleContext {
		public TerminalNode IGUAL_EXATO() { return getToken(CompiladorGVParser.IGUAL_EXATO, 0); }
		public TerminalNode DIFERENTE() { return getToken(CompiladorGVParser.DIFERENTE, 0); }
		public TerminalNode MAIOR_Q() { return getToken(CompiladorGVParser.MAIOR_Q, 0); }
		public TerminalNode MENOR_Q() { return getToken(CompiladorGVParser.MENOR_Q, 0); }
		public TerminalNode MAIOR_IGUAL_Q() { return getToken(CompiladorGVParser.MAIOR_IGUAL_Q, 0); }
		public TerminalNode MENOR_IGUAL_Q() { return getToken(CompiladorGVParser.MENOR_IGUAL_Q, 0); }
		public TerminalNode RECEBE() { return getToken(CompiladorGVParser.RECEBE, 0); }
		public OperadorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operador; }
	}

	public final OperadorContext operador() throws RecognitionException {
		OperadorContext _localctx = new OperadorContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_operador);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(193);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 528547840L) != 0)) ) {
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
	public static class ExpressaoContext extends ParserRuleContext {
		public Token op;
		public TerminalNode ABRE_PAR() { return getToken(CompiladorGVParser.ABRE_PAR, 0); }
		public List<ExpressaoContext> expressao() {
			return getRuleContexts(ExpressaoContext.class);
		}
		public ExpressaoContext expressao(int i) {
			return getRuleContext(ExpressaoContext.class,i);
		}
		public TerminalNode FECHA_PAR() { return getToken(CompiladorGVParser.FECHA_PAR, 0); }
		public TerminalNode INTEIRO() { return getToken(CompiladorGVParser.INTEIRO, 0); }
		public TerminalNode FLOAT() { return getToken(CompiladorGVParser.FLOAT, 0); }
		public TerminalNode STRING() { return getToken(CompiladorGVParser.STRING, 0); }
		public TerminalNode ID() { return getToken(CompiladorGVParser.ID, 0); }
		public TerminalNode MULT() { return getToken(CompiladorGVParser.MULT, 0); }
		public TerminalNode DIV() { return getToken(CompiladorGVParser.DIV, 0); }
		public TerminalNode PLUS() { return getToken(CompiladorGVParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(CompiladorGVParser.MINUS, 0); }
		public ExpressaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressao; }
	}

	public final ExpressaoContext expressao() throws RecognitionException {
		return expressao(0);
	}

	private ExpressaoContext expressao(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExpressaoContext _localctx = new ExpressaoContext(_ctx, _parentState);
		ExpressaoContext _prevctx = _localctx;
		int _startState = 38;
		enterRecursionRule(_localctx, 38, RULE_expressao, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(204);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case ABRE_PAR:
				{
				setState(196);
				match(ABRE_PAR);
				setState(197);
				expressao(0);
				setState(198);
				match(FECHA_PAR);
				}
				break;
			case INTEIRO:
				{
				setState(200);
				match(INTEIRO);
				}
				break;
			case FLOAT:
				{
				setState(201);
				match(FLOAT);
				}
				break;
			case STRING:
				{
				setState(202);
				match(STRING);
				}
				break;
			case ID:
				{
				setState(203);
				match(ID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(214);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(212);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
					case 1:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(206);
						if (!(precpred(_ctx, 7))) throw new FailedPredicateException(this, "precpred(_ctx, 7)");
						setState(207);
						((ExpressaoContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==MULT || _la==DIV) ) {
							((ExpressaoContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(208);
						expressao(8);
						}
						break;
					case 2:
						{
						_localctx = new ExpressaoContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_expressao);
						setState(209);
						if (!(precpred(_ctx, 6))) throw new FailedPredicateException(this, "precpred(_ctx, 6)");
						setState(210);
						((ExpressaoContext)_localctx).op = _input.LT(1);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
							((ExpressaoContext)_localctx).op = (Token)_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(211);
						expressao(7);
						}
						break;
					}
					} 
				}
				setState(216);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,17,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BlocoContext extends ParserRuleContext {
		public TerminalNode ABRE_CHAVE() { return getToken(CompiladorGVParser.ABRE_CHAVE, 0); }
		public TerminalNode FECHA_CHAVE() { return getToken(CompiladorGVParser.FECHA_CHAVE, 0); }
		public List<ComandosContext> comandos() {
			return getRuleContexts(ComandosContext.class);
		}
		public ComandosContext comandos(int i) {
			return getRuleContext(ComandosContext.class,i);
		}
		public BlocoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloco; }
	}

	public final BlocoContext bloco() throws RecognitionException {
		BlocoContext _localctx = new BlocoContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_bloco);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(217);
			match(ABRE_CHAVE);
			setState(219); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(218);
				comandos();
				}
				}
				setState(221); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 34359739374L) != 0) );
			setState(223);
			match(FECHA_CHAVE);
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
	public static class Bloco_funcaoContext extends ParserRuleContext {
		public TerminalNode ABRE_CHAVE() { return getToken(CompiladorGVParser.ABRE_CHAVE, 0); }
		public Comando_retornoContext comando_retorno() {
			return getRuleContext(Comando_retornoContext.class,0);
		}
		public TerminalNode FECHA_CHAVE() { return getToken(CompiladorGVParser.FECHA_CHAVE, 0); }
		public List<ComandosContext> comandos() {
			return getRuleContexts(ComandosContext.class);
		}
		public ComandosContext comandos(int i) {
			return getRuleContext(ComandosContext.class,i);
		}
		public Bloco_funcaoContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_bloco_funcao; }
	}

	public final Bloco_funcaoContext bloco_funcao() throws RecognitionException {
		Bloco_funcaoContext _localctx = new Bloco_funcaoContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_bloco_funcao);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(225);
			match(ABRE_CHAVE);
			setState(229);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(226);
					comandos();
					}
					} 
				}
				setState(231);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,19,_ctx);
			}
			setState(232);
			comando_retorno();
			setState(233);
			match(FECHA_CHAVE);
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

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 17:
			return condicao_sempred((CondicaoContext)_localctx, predIndex);
		case 19:
			return expressao_sempred((ExpressaoContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean condicao_sempred(CondicaoContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		case 1:
			return precpred(_ctx, 2);
		}
		return true;
	}
	private boolean expressao_sempred(ExpressaoContext _localctx, int predIndex) {
		switch (predIndex) {
		case 2:
			return precpred(_ctx, 7);
		case 3:
			return precpred(_ctx, 6);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001%\u00ec\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0001\u0000\u0004\u0000.\b\u0000\u000b\u0000\f\u0000/\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0003\u0001<\b\u0001\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0003\u0002B\b\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003J\b"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0005\u0004R\b\u0004\n\u0004\f\u0004U\t\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006]\b"+
		"\u0006\n\u0006\f\u0006`\t\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t"+
		"\u0001\t\u0001\t\u0003\tp\b\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001\n"+
		"\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n|\b\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0001\f"+
		"\u0001\f\u0001\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0003\u000e\u0095\b\u000e\u0001\u000e\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0001\u000e\u0003\u000e\u009c\b\u000e\u0001\u000e\u0003\u000e\u009f"+
		"\b\u000e\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u00aa\b\u0010\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0003\u0011\u00b5\b\u0011\u0001\u0011\u0001"+
		"\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u00bd"+
		"\b\u0011\n\u0011\f\u0011\u00c0\t\u0011\u0001\u0012\u0001\u0012\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0003\u0013\u00cd\b\u0013\u0001\u0013\u0001\u0013"+
		"\u0001\u0013\u0001\u0013\u0001\u0013\u0001\u0013\u0005\u0013\u00d5\b\u0013"+
		"\n\u0013\f\u0013\u00d8\t\u0013\u0001\u0014\u0001\u0014\u0004\u0014\u00dc"+
		"\b\u0014\u000b\u0014\f\u0014\u00dd\u0001\u0014\u0001\u0014\u0001\u0015"+
		"\u0001\u0015\u0005\u0015\u00e4\b\u0015\n\u0015\f\u0015\u00e7\t\u0015\u0001"+
		"\u0015\u0001\u0015\u0001\u0015\u0001\u0015\u0000\u0002\"&\u0016\u0000"+
		"\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u001a\u001c"+
		"\u001e \"$&(*\u0000\u0004\u0001\u0000\b\t\u0002\u0000\u0010\u0010\u0017"+
		"\u001c\u0001\u0000\u0015\u0016\u0001\u0000\u0013\u0014\u00f5\u0000-\u0001"+
		"\u0000\u0000\u0000\u0002;\u0001\u0000\u0000\u0000\u0004=\u0001\u0000\u0000"+
		"\u0000\u0006F\u0001\u0000\u0000\u0000\bN\u0001\u0000\u0000\u0000\nV\u0001"+
		"\u0000\u0000\u0000\fY\u0001\u0000\u0000\u0000\u000ea\u0001\u0000\u0000"+
		"\u0000\u0010e\u0001\u0000\u0000\u0000\u0012k\u0001\u0000\u0000\u0000\u0014"+
		"t\u0001\u0000\u0000\u0000\u0016}\u0001\u0000\u0000\u0000\u0018\u0087\u0001"+
		"\u0000\u0000\u0000\u001a\u008d\u0001\u0000\u0000\u0000\u001c\u009e\u0001"+
		"\u0000\u0000\u0000\u001e\u00a0\u0001\u0000\u0000\u0000 \u00a9\u0001\u0000"+
		"\u0000\u0000\"\u00b4\u0001\u0000\u0000\u0000$\u00c1\u0001\u0000\u0000"+
		"\u0000&\u00cc\u0001\u0000\u0000\u0000(\u00d9\u0001\u0000\u0000\u0000*"+
		"\u00e1\u0001\u0000\u0000\u0000,.\u0003\u0002\u0001\u0000-,\u0001\u0000"+
		"\u0000\u0000./\u0001\u0000\u0000\u0000/-\u0001\u0000\u0000\u0000/0\u0001"+
		"\u0000\u0000\u00000\u0001\u0001\u0000\u0000\u00001<\u0003\u0004\u0002"+
		"\u00002<\u0003\u0006\u0003\u00003<\u0003\u000e\u0007\u00004<\u0003\u0010"+
		"\b\u00005<\u0003\u0012\t\u00006<\u0003\u0014\n\u00007<\u0003\u0016\u000b"+
		"\u00008<\u0003\u0018\f\u00009<\u0003\u001a\r\u0000:<\u0003\u001c\u000e"+
		"\u0000;1\u0001\u0000\u0000\u0000;2\u0001\u0000\u0000\u0000;3\u0001\u0000"+
		"\u0000\u0000;4\u0001\u0000\u0000\u0000;5\u0001\u0000\u0000\u0000;6\u0001"+
		"\u0000\u0000\u0000;7\u0001\u0000\u0000\u0000;8\u0001\u0000\u0000\u0000"+
		";9\u0001\u0000\u0000\u0000;:\u0001\u0000\u0000\u0000<\u0003\u0001\u0000"+
		"\u0000\u0000=>\u0007\u0000\u0000\u0000>?\u0005#\u0000\u0000?A\u0005\n"+
		"\u0000\u0000@B\u0003\b\u0004\u0000A@\u0001\u0000\u0000\u0000AB\u0001\u0000"+
		"\u0000\u0000BC\u0001\u0000\u0000\u0000CD\u0005\u000b\u0000\u0000DE\u0003"+
		"*\u0015\u0000E\u0005\u0001\u0000\u0000\u0000FG\u0005#\u0000\u0000GI\u0005"+
		"\n\u0000\u0000HJ\u0003\f\u0006\u0000IH\u0001\u0000\u0000\u0000IJ\u0001"+
		"\u0000\u0000\u0000JK\u0001\u0000\u0000\u0000KL\u0005\u000b\u0000\u0000"+
		"LM\u0005\u000f\u0000\u0000M\u0007\u0001\u0000\u0000\u0000NS\u0003\n\u0005"+
		"\u0000OP\u0005\u000e\u0000\u0000PR\u0003\n\u0005\u0000QO\u0001\u0000\u0000"+
		"\u0000RU\u0001\u0000\u0000\u0000SQ\u0001\u0000\u0000\u0000ST\u0001\u0000"+
		"\u0000\u0000T\t\u0001\u0000\u0000\u0000US\u0001\u0000\u0000\u0000VW\u0007"+
		"\u0000\u0000\u0000WX\u0005#\u0000\u0000X\u000b\u0001\u0000\u0000\u0000"+
		"Y^\u0003&\u0013\u0000Z[\u0005\u000e\u0000\u0000[]\u0003&\u0013\u0000\\"+
		"Z\u0001\u0000\u0000\u0000]`\u0001\u0000\u0000\u0000^\\\u0001\u0000\u0000"+
		"\u0000^_\u0001\u0000\u0000\u0000_\r\u0001\u0000\u0000\u0000`^\u0001\u0000"+
		"\u0000\u0000ab\u0005\u0007\u0000\u0000bc\u0003&\u0013\u0000cd\u0005\u000f"+
		"\u0000\u0000d\u000f\u0001\u0000\u0000\u0000ef\u0005\u0001\u0000\u0000"+
		"fg\u0005\n\u0000\u0000gh\u0005#\u0000\u0000hi\u0005\u000b\u0000\u0000"+
		"ij\u0005\u000f\u0000\u0000j\u0011\u0001\u0000\u0000\u0000kl\u0005\u0002"+
		"\u0000\u0000lo\u0005\n\u0000\u0000mp\u0005 \u0000\u0000np\u0003&\u0013"+
		"\u0000om\u0001\u0000\u0000\u0000on\u0001\u0000\u0000\u0000pq\u0001\u0000"+
		"\u0000\u0000qr\u0005\u000b\u0000\u0000rs\u0005\u000f\u0000\u0000s\u0013"+
		"\u0001\u0000\u0000\u0000tu\u0005\u0003\u0000\u0000uv\u0005\n\u0000\u0000"+
		"vw\u0003\"\u0011\u0000wx\u0005\u000b\u0000\u0000x{\u0003(\u0014\u0000"+
		"yz\u0005\u0004\u0000\u0000z|\u0003(\u0014\u0000{y\u0001\u0000\u0000\u0000"+
		"{|\u0001\u0000\u0000\u0000|\u0015\u0001\u0000\u0000\u0000}~\u0005\u0005"+
		"\u0000\u0000~\u007f\u0005\n\u0000\u0000\u007f\u0080\u0003\u001e\u000f"+
		"\u0000\u0080\u0081\u0005\u000f\u0000\u0000\u0081\u0082\u0003\"\u0011\u0000"+
		"\u0082\u0083\u0005\u000f\u0000\u0000\u0083\u0084\u0003 \u0010\u0000\u0084"+
		"\u0085\u0005\u000b\u0000\u0000\u0085\u0086\u0003(\u0014\u0000\u0086\u0017"+
		"\u0001\u0000\u0000\u0000\u0087\u0088\u0005\u0006\u0000\u0000\u0088\u0089"+
		"\u0005\n\u0000\u0000\u0089\u008a\u0003\"\u0011\u0000\u008a\u008b\u0005"+
		"\u000b\u0000\u0000\u008b\u008c\u0003(\u0014\u0000\u008c\u0019\u0001\u0000"+
		"\u0000\u0000\u008d\u008e\u0003\u001e\u000f\u0000\u008e\u008f\u0005\u000f"+
		"\u0000\u0000\u008f\u001b\u0001\u0000\u0000\u0000\u0090\u0091\u0005\b\u0000"+
		"\u0000\u0091\u0094\u0005#\u0000\u0000\u0092\u0093\u0005\u0010\u0000\u0000"+
		"\u0093\u0095\u0003&\u0013\u0000\u0094\u0092\u0001\u0000\u0000\u0000\u0094"+
		"\u0095\u0001\u0000\u0000\u0000\u0095\u0096\u0001\u0000\u0000\u0000\u0096"+
		"\u009f\u0005\u000f\u0000\u0000\u0097\u0098\u0005\t\u0000\u0000\u0098\u009b"+
		"\u0005#\u0000\u0000\u0099\u009a\u0005\u0010\u0000\u0000\u009a\u009c\u0003"+
		"&\u0013\u0000\u009b\u0099\u0001\u0000\u0000\u0000\u009b\u009c\u0001\u0000"+
		"\u0000\u0000\u009c\u009d\u0001\u0000\u0000\u0000\u009d\u009f\u0005\u000f"+
		"\u0000\u0000\u009e\u0090\u0001\u0000\u0000\u0000\u009e\u0097\u0001\u0000"+
		"\u0000\u0000\u009f\u001d\u0001\u0000\u0000\u0000\u00a0\u00a1\u0005#\u0000"+
		"\u0000\u00a1\u00a2\u0005\u0010\u0000\u0000\u00a2\u00a3\u0003&\u0013\u0000"+
		"\u00a3\u001f\u0001\u0000\u0000\u0000\u00a4\u00a5\u0005#\u0000\u0000\u00a5"+
		"\u00aa\u0005\u0011\u0000\u0000\u00a6\u00a7\u0005#\u0000\u0000\u00a7\u00aa"+
		"\u0005\u0012\u0000\u0000\u00a8\u00aa\u0003\u001e\u000f\u0000\u00a9\u00a4"+
		"\u0001\u0000\u0000\u0000\u00a9\u00a6\u0001\u0000\u0000\u0000\u00a9\u00a8"+
		"\u0001\u0000\u0000\u0000\u00aa!\u0001\u0000\u0000\u0000\u00ab\u00ac\u0006"+
		"\u0011\uffff\uffff\u0000\u00ac\u00ad\u0003&\u0013\u0000\u00ad\u00ae\u0003"+
		"$\u0012\u0000\u00ae\u00af\u0003&\u0013\u0000\u00af\u00b5\u0001\u0000\u0000"+
		"\u0000\u00b0\u00b1\u0005\n\u0000\u0000\u00b1\u00b2\u0003\"\u0011\u0000"+
		"\u00b2\u00b3\u0005\u000b\u0000\u0000\u00b3\u00b5\u0001\u0000\u0000\u0000"+
		"\u00b4\u00ab\u0001\u0000\u0000\u0000\u00b4\u00b0\u0001\u0000\u0000\u0000"+
		"\u00b5\u00be\u0001\u0000\u0000\u0000\u00b6\u00b7\n\u0003\u0000\u0000\u00b7"+
		"\u00b8\u0005\u001d\u0000\u0000\u00b8\u00bd\u0003\"\u0011\u0004\u00b9\u00ba"+
		"\n\u0002\u0000\u0000\u00ba\u00bb\u0005\u001e\u0000\u0000\u00bb\u00bd\u0003"+
		"\"\u0011\u0003\u00bc\u00b6\u0001\u0000\u0000\u0000\u00bc\u00b9\u0001\u0000"+
		"\u0000\u0000\u00bd\u00c0\u0001\u0000\u0000\u0000\u00be\u00bc\u0001\u0000"+
		"\u0000\u0000\u00be\u00bf\u0001\u0000\u0000\u0000\u00bf#\u0001\u0000\u0000"+
		"\u0000\u00c0\u00be\u0001\u0000\u0000\u0000\u00c1\u00c2\u0007\u0001\u0000"+
		"\u0000\u00c2%\u0001\u0000\u0000\u0000\u00c3\u00c4\u0006\u0013\uffff\uffff"+
		"\u0000\u00c4\u00c5\u0005\n\u0000\u0000\u00c5\u00c6\u0003&\u0013\u0000"+
		"\u00c6\u00c7\u0005\u000b\u0000\u0000\u00c7\u00cd\u0001\u0000\u0000\u0000"+
		"\u00c8\u00cd\u0005!\u0000\u0000\u00c9\u00cd\u0005\"\u0000\u0000\u00ca"+
		"\u00cd\u0005 \u0000\u0000\u00cb\u00cd\u0005#\u0000\u0000\u00cc\u00c3\u0001"+
		"\u0000\u0000\u0000\u00cc\u00c8\u0001\u0000\u0000\u0000\u00cc\u00c9\u0001"+
		"\u0000\u0000\u0000\u00cc\u00ca\u0001\u0000\u0000\u0000\u00cc\u00cb\u0001"+
		"\u0000\u0000\u0000\u00cd\u00d6\u0001\u0000\u0000\u0000\u00ce\u00cf\n\u0007"+
		"\u0000\u0000\u00cf\u00d0\u0007\u0002\u0000\u0000\u00d0\u00d5\u0003&\u0013"+
		"\b\u00d1\u00d2\n\u0006\u0000\u0000\u00d2\u00d3\u0007\u0003\u0000\u0000"+
		"\u00d3\u00d5\u0003&\u0013\u0007\u00d4\u00ce\u0001\u0000\u0000\u0000\u00d4"+
		"\u00d1\u0001\u0000\u0000\u0000\u00d5\u00d8\u0001\u0000\u0000\u0000\u00d6"+
		"\u00d4\u0001\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7"+
		"\'\u0001\u0000\u0000\u0000\u00d8\u00d6\u0001\u0000\u0000\u0000\u00d9\u00db"+
		"\u0005\f\u0000\u0000\u00da\u00dc\u0003\u0002\u0001\u0000\u00db\u00da\u0001"+
		"\u0000\u0000\u0000\u00dc\u00dd\u0001\u0000\u0000\u0000\u00dd\u00db\u0001"+
		"\u0000\u0000\u0000\u00dd\u00de\u0001\u0000\u0000\u0000\u00de\u00df\u0001"+
		"\u0000\u0000\u0000\u00df\u00e0\u0005\r\u0000\u0000\u00e0)\u0001\u0000"+
		"\u0000\u0000\u00e1\u00e5\u0005\f\u0000\u0000\u00e2\u00e4\u0003\u0002\u0001"+
		"\u0000\u00e3\u00e2\u0001\u0000\u0000\u0000\u00e4\u00e7\u0001\u0000\u0000"+
		"\u0000\u00e5\u00e3\u0001\u0000\u0000\u0000\u00e5\u00e6\u0001\u0000\u0000"+
		"\u0000\u00e6\u00e8\u0001\u0000\u0000\u0000\u00e7\u00e5\u0001\u0000\u0000"+
		"\u0000\u00e8\u00e9\u0003\u000e\u0007\u0000\u00e9\u00ea\u0005\r\u0000\u0000"+
		"\u00ea+\u0001\u0000\u0000\u0000\u0014/;AIS^o{\u0094\u009b\u009e\u00a9"+
		"\u00b4\u00bc\u00be\u00cc\u00d4\u00d6\u00dd\u00e5";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}