// Generated from c:/Users/vinycius yuji/OneDrive/Documentos/faculdade/Compiladores/compiladorGV/grammar/CompiladorGV.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CompiladorGVParser}.
 */
public interface CompiladorGVListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#inicio}.
	 * @param ctx the parse tree
	 */
	void enterInicio(CompiladorGVParser.InicioContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#inicio}.
	 * @param ctx the parse tree
	 */
	void exitInicio(CompiladorGVParser.InicioContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#comandos}.
	 * @param ctx the parse tree
	 */
	void enterComandos(CompiladorGVParser.ComandosContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#comandos}.
	 * @param ctx the parse tree
	 */
	void exitComandos(CompiladorGVParser.ComandosContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#comando_declaracao_funcao}.
	 * @param ctx the parse tree
	 */
	void enterComando_declaracao_funcao(CompiladorGVParser.Comando_declaracao_funcaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#comando_declaracao_funcao}.
	 * @param ctx the parse tree
	 */
	void exitComando_declaracao_funcao(CompiladorGVParser.Comando_declaracao_funcaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#comando_chamada_funcao}.
	 * @param ctx the parse tree
	 */
	void enterComando_chamada_funcao(CompiladorGVParser.Comando_chamada_funcaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#comando_chamada_funcao}.
	 * @param ctx the parse tree
	 */
	void exitComando_chamada_funcao(CompiladorGVParser.Comando_chamada_funcaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#parametros}.
	 * @param ctx the parse tree
	 */
	void enterParametros(CompiladorGVParser.ParametrosContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#parametros}.
	 * @param ctx the parse tree
	 */
	void exitParametros(CompiladorGVParser.ParametrosContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#parametro}.
	 * @param ctx the parse tree
	 */
	void enterParametro(CompiladorGVParser.ParametroContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#parametro}.
	 * @param ctx the parse tree
	 */
	void exitParametro(CompiladorGVParser.ParametroContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void enterArgumentos(CompiladorGVParser.ArgumentosContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#argumentos}.
	 * @param ctx the parse tree
	 */
	void exitArgumentos(CompiladorGVParser.ArgumentosContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#comando_retorno}.
	 * @param ctx the parse tree
	 */
	void enterComando_retorno(CompiladorGVParser.Comando_retornoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#comando_retorno}.
	 * @param ctx the parse tree
	 */
	void exitComando_retorno(CompiladorGVParser.Comando_retornoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#comando_ler}.
	 * @param ctx the parse tree
	 */
	void enterComando_ler(CompiladorGVParser.Comando_lerContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#comando_ler}.
	 * @param ctx the parse tree
	 */
	void exitComando_ler(CompiladorGVParser.Comando_lerContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#comando_escrever}.
	 * @param ctx the parse tree
	 */
	void enterComando_escrever(CompiladorGVParser.Comando_escreverContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#comando_escrever}.
	 * @param ctx the parse tree
	 */
	void exitComando_escrever(CompiladorGVParser.Comando_escreverContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#comando_se}.
	 * @param ctx the parse tree
	 */
	void enterComando_se(CompiladorGVParser.Comando_seContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#comando_se}.
	 * @param ctx the parse tree
	 */
	void exitComando_se(CompiladorGVParser.Comando_seContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#comando_para}.
	 * @param ctx the parse tree
	 */
	void enterComando_para(CompiladorGVParser.Comando_paraContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#comando_para}.
	 * @param ctx the parse tree
	 */
	void exitComando_para(CompiladorGVParser.Comando_paraContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#comando_enquanto}.
	 * @param ctx the parse tree
	 */
	void enterComando_enquanto(CompiladorGVParser.Comando_enquantoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#comando_enquanto}.
	 * @param ctx the parse tree
	 */
	void exitComando_enquanto(CompiladorGVParser.Comando_enquantoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#comando_atribuicao}.
	 * @param ctx the parse tree
	 */
	void enterComando_atribuicao(CompiladorGVParser.Comando_atribuicaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#comando_atribuicao}.
	 * @param ctx the parse tree
	 */
	void exitComando_atribuicao(CompiladorGVParser.Comando_atribuicaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#comando_declaracao}.
	 * @param ctx the parse tree
	 */
	void enterComando_declaracao(CompiladorGVParser.Comando_declaracaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#comando_declaracao}.
	 * @param ctx the parse tree
	 */
	void exitComando_declaracao(CompiladorGVParser.Comando_declaracaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void enterAtribuicao(CompiladorGVParser.AtribuicaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#atribuicao}.
	 * @param ctx the parse tree
	 */
	void exitAtribuicao(CompiladorGVParser.AtribuicaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#incremento}.
	 * @param ctx the parse tree
	 */
	void enterIncremento(CompiladorGVParser.IncrementoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#incremento}.
	 * @param ctx the parse tree
	 */
	void exitIncremento(CompiladorGVParser.IncrementoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#condicao}.
	 * @param ctx the parse tree
	 */
	void enterCondicao(CompiladorGVParser.CondicaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#condicao}.
	 * @param ctx the parse tree
	 */
	void exitCondicao(CompiladorGVParser.CondicaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#operador}.
	 * @param ctx the parse tree
	 */
	void enterOperador(CompiladorGVParser.OperadorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#operador}.
	 * @param ctx the parse tree
	 */
	void exitOperador(CompiladorGVParser.OperadorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#lista_argumentos}.
	 * @param ctx the parse tree
	 */
	void enterLista_argumentos(CompiladorGVParser.Lista_argumentosContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#lista_argumentos}.
	 * @param ctx the parse tree
	 */
	void exitLista_argumentos(CompiladorGVParser.Lista_argumentosContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#expressao}.
	 * @param ctx the parse tree
	 */
	void enterExpressao(CompiladorGVParser.ExpressaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#expressao}.
	 * @param ctx the parse tree
	 */
	void exitExpressao(CompiladorGVParser.ExpressaoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#bloco}.
	 * @param ctx the parse tree
	 */
	void enterBloco(CompiladorGVParser.BlocoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#bloco}.
	 * @param ctx the parse tree
	 */
	void exitBloco(CompiladorGVParser.BlocoContext ctx);
	/**
	 * Enter a parse tree produced by {@link CompiladorGVParser#bloco_funcao}.
	 * @param ctx the parse tree
	 */
	void enterBloco_funcao(CompiladorGVParser.Bloco_funcaoContext ctx);
	/**
	 * Exit a parse tree produced by {@link CompiladorGVParser#bloco_funcao}.
	 * @param ctx the parse tree
	 */
	void exitBloco_funcao(CompiladorGVParser.Bloco_funcaoContext ctx);
}