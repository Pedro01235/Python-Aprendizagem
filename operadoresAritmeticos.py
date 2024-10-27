# Operadores em Python
# Os Operadores em Python possibilitam que o desenvolvedor consiga transcrever a lógica para código.
# Python disponibiliza uma série desses operadores para os desenvolvedores e é muito importante dominá-los se você quiser se tornar um verdadeiro Pythonista!
# Veremos todos em detalhes agora, começando pelos Operadores Aritméticos!

# Operadores Aritméticos
# Esses operadores são utilizados para criarmos expressões matemáticas comuns, como soma, subtração, multiplicação e divisão.

n1 = 4
n2 = 2

soma = n1 + n2
print('Resultado = ',soma)  # Resultado: 6

subtracao = n1 - n2
print('Resultado = ',subtracao)  # Resultado: 2

multiplicacao = n1 * n2
print('Resultado = ', multiplicacao)  # Resultado: 8

divisao = n1 / n2
print('Resultado = ',divisao)  # Resultado: 2.0

divisao_interna = n1 // n2
print('Resultado = ',divisao_interna)  # Resultado: 2

modulo = n1 % n2
print('Resultado = ',modulo)  # Resultado: 0

exponenciacao = n1 ** n2
print('Resultado = ',exponenciacao)  # Resultado: 16

# Operadores de Comparação
# Como o nome já diz, esses Operadores são usados para comparar dois valores:

# == 	Igual a 	    Verifica se um valor é igual ao outro
# != 	Diferente de 	Verifica se um valor é diferente ao outro
# > 	Maior que 	    Verifica se um valor é maior que outro
# >= 	Maior ou igual 	Verifica se um valor é maior ou igual ao outro
# < 	Menor que 	    Verifica se um valor é menor que outro
# <= 	Menor ou igual 	Verifica se um valor é menor ou igual ao outro

# Vamos ver exemplos da utilização de cada operador de comparação mencionado acima.
# Para facilitar o entendimento, todas as operações estão retornando um valor igual a True, para que você entenda como cada condição é aceita:

var = 5

if var == 5:
    print('Os valores são iguais')

if var != 7:
    print('O valor não é igual a 7')

if var > 2:
    print('O valor da variável é maior de 2')

if var >= 5:
    print('O valor da variável é maior ou igual a 5')

if var < 7:
    print('O valor da variável é menor que 7')

if var <= 5:
    print('O valor da variável é menor ou igual a 5')

# Operadores de Atribuição

# = 	x = 1
# += 	x = x + 1
# -= 	x = x - 1
# *= 	x = x * 1
# /= 	x = x / 1
# %= 	x = x % 1

# Exemplo da utilização de cada operador de atribuição mencionado acima:

# Operador +=
numero = 5
numero += 7
print(numero)  # Resultado será 10

# Operador -=
numero = 5
numero -= 3
print(numero)  # Resultado será 2

# Operador *=
numero = 5
numero *= 2
print(numero)  # Resultado será 10

# Operador /=
numero = 5
numero /= 4
print(numero)  # Resultado será 1.25

# Operador -=
numero = 5
numero %= 2
print(numero)  # Resultado será 1


# Operadores Lógicos
# Esses Operadores nos possibilitam construir um tipo de teste muito útil e muito utilizado em qualquer programa Python: os testes lógicos.
# Python nos disponibiliza três tipos de Operadores Lógicos: o and, o or e o not.

# and 	Retorna True se ambas as afirmações forem verdadeiras
# or 	Retorna True se uma das afirmações for verdadeira
# not 	retorna Falso se o resultado for verdadeiro

num1 = 7
num2 = 4

# Exemplo and
if num1 > 3 and num2 < 8:
    print("As Duas condições são verdadeiras")

# Exemplo or
if num1 > 4 or num2 <= 8:
    print("Uma ou duas das condições são verdadeiras")

# Exemplo not
if not (num1 < 30 and num2 < 8):
    print('Inverte o resultado da condição entre os parânteses')


# Operadores de Identidade
# Estes Operadores são utilizados para comparar objetos, verificando se os objetos testados referenciam o mesmo objeto (is) ou não (is not).

# is 	    Retorna True se ambas as variáveis são o mesmo objeto
# is not 	Retorna True se ambas as variáveis não forem o mesmo objeto

lista = [1, 2, 3]
outra_lista = [1, 2, 3]
recebe_lista = lista

# Recebe True, pois são o mesmo objeto
print(f"São o mesmo objeto? {lista is recebe_lista}")

# Retorna False, pois são objetos diferentes
print(f"São o mesmo objeto? {lista is outra_lista}")

# Exemplo do operador is not:
tupla = (1, 2, 3)
outra_tupla = (1, 2, 3)

print(f"Os objetos são diferentes? {outra_tupla is tupla}")

# Muitas vezes programadores Python ficam na dúvida em quando utilizar o operador de igualdade == ou o operador de identidade is.
# Mas agora que você já conhece os dois sabe que o operador == verifica os valores testados, enquanto o operador is testa a referência dos valores testados! 

# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------

# Operadores de Associação
# Por último, temos os Operadores de Associação.

# Eles servem para verificar se determinado objeto está associado ou pertence a determinada estrutura de dados.

# in 	    Retorna True caso o valor seja encontrado na sequência
# not in 	Retorna True caso o valor não seja encontrado na sequência

# Exemplo da utilização de cada operador de associação mencionado acima:
lista = ["Python", 'Academy', "Operadores", 'Condições']

# Verifica se existe a string dentro da lista
print('Python' in lista)  # Saída: True

# Verifica se não existe a string dentro da lista
print('SQL' not in lista) # Saída: True
