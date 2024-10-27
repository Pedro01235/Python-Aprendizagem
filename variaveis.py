# Introdução
# Python é uma linguagem dinamicamente tipada, o que significa que não é necessário declarar o tipo de variável ou fazer casting (mudar o tipo de variável), 
# pois o Interpretador se encarrega disso para nós!
# Isso significa também que o tipo da variável poder variar durante a execução do programa.
# Os tipos de dados padrão do Python são:

#     Inteiro (int)
#     Ponto Flutuante ou Decimal (float)
#     Tipo Complexo (complex)
#     String (str)
#     Boolean (bool)
#     List (list)
#     Tuple
#     Dictionary (dic)

# ----------------------------------------------------

# ----------------------------------------------------

# Tipo Inteiro(int)
# Por exemplo, 21, 4, 0, e −2048 são números inteiros, enquanto 9.75, 1/2, 1.5 não são.
idade = 18
ano = 2002

print(type(idade))
print(type(ano))

# Ponto Flutuante ou Decimal (float)
# O famoso ponto flutuante é um tipo usado para números racionais (números que podem ser representados por uma fração) informalmente conhecido como “número quebrado”.
altura = 1.80
peso = 73.55

print(type(peso))
print(type(altura))

# Complexo (complex)
# Tipo de dado usado para representar números complexos (isso mesmo, aquilo que provavelmente estudou no terceiro ano do ensino médio).
# Esse tipo normalmente é usado em cálculos geométricos e científicos.
# Um tipo complexo contem duas partes: a parte real e a parte imaginária, sendo que a parte imaginária contem um j no sufixo.
a = 5+2j
b = 20+6j

print(type(a))
print(type(b))
print(complex(2, 5))

# String (str)
# É um conjunto de caracteres dispostos numa determinada ordem, geralmente utilizada para representar palavras, frases ou textos.
nome = 'Pedro'
profissao = 'Engenheiro de Software'

print(type(nome))
print(type(profissao))


# Boolean (bool)
# Tipo de dado lógico que pode assumir apenas dois valores: falso ou verdadeiro (False ou True em Python).
# Na lógica computacional, podem ser considerados como 0 ou 1.
fim_de_semana = True
feriado = False

print(type(fim_de_semana))
print(type(feriado))


# Listas (list)
# Tipo de dado muito importante e que é muito utilizado no dia a dia do desenvolvedor Python!
# Listas agrupam um conjunto de elementos variados, podendo conter: inteiros, floats, strings, outras listas e outros tipos.
# Elas são definidas utilizando-se colchetes para delimitar a lista e vírgulas para separar os elementos, veja alguns exemplo abaixo:

alunos = ['Amanda', 'Ana', 'Bruno', 'João']
notas = [10, 8.5, 7.8, 8.0] 

print(type(alunos))
print(type(notas))


# Tuplas (tuple)    
# Assim como Lista, Tupla é um tipo que agrupa um conjunto de elementos.
# Porém sua forma de definição é diferente: utilizamos parênteses e também separado por vírgula.
# A diferença para Lista é que Tuplas são imutáveis, ou seja, após sua definição, Tuplas não podem ser modificadas.

valores = (90, 79, 54, 32, 21)
pontos = (100, 94.05, 86.8, 62)

print(type(valores))
print(type(pontos))

# Caso haja uma tentativa de alterar os itens de uma tupla após sua definição, como no código a seguir:

tuple = (0, 1, 2, 3)
tuple [0] = 4

# O seguinte erro do tipo TypeError será lançado pelo interpretador do Python:

# Dicionários (dict)
# Dict é um tipo de dado muito flexível do Python.
# Eles são utilizados para agrupar elementos através da estrutura de chave e valor, onde a chave é o primeiro elemento seguido por dois pontos e pelo valor.

altura = {'Amanda': 1.65, 'Ana': 1.60, 'João': 1.70}
peso = {'Amanda': 60, 'Ana': 58, 'João': 68}

print(type(altura))
print(type(peso))

# Dicionários possibilitam um tipo de manipulação muito poderosa, chamada de Dict Comprehensions! 

# ----------------------------------------------------

# ----------------------------------------------------

# Como mudar o tipo de uma variável

# Em determinados cenários pode ser necessário mudar o tipo de uma variável e no Python isso é muito fácil, uma das vantagens de uma linguagem dinamicamente tipada.
# Abaixo veremos exemplos de como trocar o tipo de variáveis.

# ----------------------------------------------------
# Decimal (float) para String (str)

# Antes da conversão
altura = 1.80
print(type(altura))

# Conversão do tipo
altura = str(altura)

# Depois da conversão
type(altura)
print(altura)
# ----------------------------------------------------

# Inteiro (int) para Decimal (float):

# Antes da conversão
idade = 18
print(type(idade))

# Conversão do tipo
idade = float(idade)

# Depois da conversão
print(type(idade))
print(idade)
# ----------------------------------------------------

# Booleano (bool) para Inteiro (int)

# Antes da conversão
fim_de_semana = True
print(type(fim_de_semana))

# Conversão do tipo
fim_de_semana = int(fim_de_semana)

# Depois da conversão
print(type(fim_de_semana))
print(fim_de_semana)
# ----------------------------------------------------

#Calculo IMC 

peso = 65.55
altura = 1.7
imc = peso/altura**2
print(imc)