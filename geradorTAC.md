O que é TAC? Conceito e Objetivo

🔹 Definição

TAC (Three Address Code) é uma forma de representação intermediária entre o código fonte e o código de máquina. Cada instrução do TAC realiza no máximo uma operação e trabalha, geralmente, com três operandos: dois de entrada e um de saída.

🧠 Por que usar TAC?
	•	Independência da máquina: Não é ligado à arquitetura física do processador.
	•	Facilidade de otimização: É muito mais simples aplicar otimizações nesta forma intermediária.
	•	Base para geração de código final: Pode ser traduzido para Assembly, bytecode, etc.

🔸 Exemplo simples:

Código em C:
```C
int x = (a + b) * (c - d);
```
Em Tac:
```TAC
_t1 = a + b
_t2 = c - d
x = _t1 * _t2
```
