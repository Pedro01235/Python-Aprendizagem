# Introdução
# É muito comum na programação, precisarmos que determinado bloco de código seja executado apenas se determinada condição for satisfeita.
# Para esses casos, Python disponibiliza formas de se controlar o fluxo de execução de programas: são as chamadas Estruturas Condicionais IF/ELIF/ELSE.

# Estrutura Condicional if

# Agora que já está craque com os Operadores do Python, vamos aprender sobre nossa primeira estrutura condicional.
# Sua sintaxe é bem simples, bastando utilizarmos if seguido pela condicao seguido por dois pontos:

# # Veja o exemplo a seguir:

valor = 10

if valor > 5:
    print('O valor é maior que 5.')


# Neste caso, a condição está testando se o valor presente na variável valor é maior que 5.
# Caso isso aconteça, a linha de código abaixo será executada (nesse exemplo, a chamada à função

# Caso você precise que um bloco de código seja sempre executado, basta adicionar True à condição:

if True:
    print("Este bloco sempre irá ser executado.")


# Estrutura Condicional if/else

# Vimos na seção acima que o if executa um bloco de código se sua condição for atendida, mas e se ela não for atendida e você deseja realizar outra ação? :thinking:
# Bom, basta utilizarmos a estrutura condicional else!
# Com ela, toda vez que uma condição não for atendida, o Python executará o bloco de código definido abaixo da cláusula else.

# Vamos esclarecer no exemplo abaixo:

idade = 20

if idade < 17:
    print('A idade é MENOR que 17')
else:
    print('A idade é MAIOR que 17')


# Estrutura Condicional if-elif-else
# O elif é utilizando quando mais de uma condição if precisa ser testada. Exemplo:

linguagem = "Python"

if linguagem == "C++":
    print('C++ é uma linguagem de programação compilada.')
elif linguagem == "Python":
    print("Python é uma linguagem de programação de alto nível")
elif linguagem == "Java":
    print("Java é uma linguagem de programação amplamante utilizada no mercado")
else:
    print('Não é nenhuma das duas opções')

# Neste exemplo, estamos verificando o valor da variável linguagem em diversos testes.
# Note que a saída abaixo é exatamente o resultado da execução do elif, ja que a o valor da variável linguagem é igual à “Python”:


# Estrutura Condicional Ternária (if em uma linha)

# Python provê uma forma concisa de se testar valores com apenas uma linha de código
# São os chamados if-ternários, ou condições ternárias, ou operadores ternários: os nomes são diversos!

# Veja um exemplo:

velocidade = 75
resultado = 'Multado' if velocidade > 60 else 'Dentro do limite'

print(resultado)


velocidade = 55
resultado = 'Multado' if velocidade > 60 else 'Dentro do limite'

print(resultado)

# Nesse caso, está sendo verificado se o valor da variável velocidade é maior que 60 e:
#     Caso a condição seja verdadeira a variável resultado receberá o valor Multado;
#     Caso a condição seja falsa, a variável resultado receberá o valor Dentro do limite.
# Bem, pelo resultado abaixo parece que alguém foi multado


# Estruturas de Repetição com Estruturas Condicionais

# Podemos juntar as Estruturas de Repetição com as Estruturas Condicionais, que alias trabalham muito bem juntas.
# Se você quer aprender mais sobre estruturas de repetição, loops, for, while e muito mais acesse nosso post feito especialmente para este tema: Loops e estruturas de repetição no Python.

# Veja um exemplo dessas estruturas trabalhando em conjunto:


for numero in range(1, 5):
    if numero % 2 == 0:
        print(f'O número {numero} é par')
    else:
        print(f'O número {numero} é impar')

# Nota: O operador % retorna o resto da divisão.


# List Comprehensions com if

# Outro lugar onde podemos utilizar as Estruturas Condicionais são nas chamadas List Comprehensions do Python.
# Suponha que te peçam para: escrever um código que retorne apenas os números pares de uma sequência de 0 a 10.

# Veja como isto poderia ser feito em apenas 1 linha de código!

list_comp = [numero for numero in range(0, 11) if numero % 2 == 0]
print(list_comp)
