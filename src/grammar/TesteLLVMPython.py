# Importa o módulo de Intermediate Representation (IR) da llvmlite
from llvmlite import ir

# 1. Crie o Módulo
# Um módulo é o contêiner de nível superior para todo o código.
module = ir.Module(name="meu_modulo")

# 2. Defina o tipo da função
# Nossa função não receberá argumentos () e retornará um inteiro de 32 bits (i32).
# ir.IntType(32) representa um inteiro de 32 bits.
func_type = ir.FunctionType(ir.IntType(32), [])

# 3. Crie a Função
# Adicionamos a função 'main' ao nosso módulo.
main_func = ir.Function(module, func_type, name="main")

# 4. Crie o Bloco de Entrada (Entry Block)
# Toda função precisa de pelo menos um bloco básico.
entry_block = main_func.append_basic_block(name="entry")

# 5. Crie o IR Builder
# O builder é um ajudante que nos permite criar e inserir instruções LLVM.
builder = ir.IRBuilder(entry_block)

# 6. Crie as Instruções
# Criamos uma constante do tipo i32 com o valor 42.
return_value = ir.Constant(ir.IntType(32), 42)

# Criamos a instrução de retorno.
builder.ret(return_value)

# 7. Imprima o LLVM IR gerado
with open("main.ll", "w") as f:
    f.write(str(module))
print("Arquivo LLVM IR salvo como main.ll")