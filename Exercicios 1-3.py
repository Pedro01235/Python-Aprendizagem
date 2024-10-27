# Aqui estão 10 exercícios básicos de Python com variáveis, operadores e condicionais:

# 1. **Exercício 1: Cálculo de Média**
#    - Escreva um programa que solicite ao usuário três notas (valores de 0 a 10). Calcule a média e exiba se o aluno foi aprovado ou reprovado. A média para aprovação é 7.

n1 = int(input('Nota 1: '))
n2 = int(input('Nota 2: '))
n3 = int(input('Nota 3: '))

media = (n1 + n2 + n3) / 3
print('Media:', media)

if media > 7:
    print('Aprovado')
else:
    print('Reprovado')

# 2. **Exercício 2: Verificar Número Par ou Ímpar**
#    - Solicite ao usuário um número inteiro e verifique se ele é par ou ímpar. Mostre o resultado na tela.

n1 = int(input('Número = '))

if n1 % 2 == 0:
    print('Par')
else:
    print('Impar')

# 3. **Exercício 3: Conversão de Celsius para Fahrenheit**
#    - Crie um programa que solicite uma temperatura em graus Celsius e converta para Fahrenheit. A fórmula é `F = (C * 9/5) + 32`.

tempC = float(input('Temperatura Cº = '))  
F = (tempC * 9/5) + 32

print('Temperatura Fº =', F)

# 4. **Exercício 4: Calculadora Simples**
#    - Solicite ao usuário dois números e uma operação matemática (+, -, *, /). Realize a operação escolhida e exiba o resultado.

n1 = int(input('Número 1 = '))
n2 = int(input('Número 2 = '))

soma = n1 + n2 
subtracao = n1 - n2 
multiplicacao = n1 * n2 
divisao = n1 / n2 

print('Soma = ', soma)
print('Soma = ', subtracao)
print('Soma = ', multiplicacao)
print('Soma = ', divisao)

# 5. **Exercício 5: Maior de Três Números**
#    - Peça ao usuário para inserir três números e exiba o maior deles.

n1 = int(input('Número 1 = '))
n2 = int(input('Número 2 = '))
n3 = int(input('Número 3 = '))

print('O maior número é:', max(n1, n2, n3))

# 6. **Exercício 6: Verificação de Idade**
#    - Solicite a idade de uma pessoa e diga se ela é menor de idade (menos de 18 anos), adulta (18 a 60 anos) ou idosa (acima de 60 anos).

idade = int(input('Digite sua idade: '))

if idade > 0 and idade < 18:
    print('Menor de idade')
elif idade >= 18 and idade <= 60:
    print('Adulta')
else:
    print('Idosa')

# 7. **Exercício 7: Verificar Divisibilidade por 5**
#    - Crie um programa que peça ao usuário um número inteiro e verifique se ele é divisível por 5. Mostre uma mensagem adequada.

n1 = int(input('Número = '))

if n1 % 5 == 0:
    print('O número é divisível por 5')
else:
    print('O número não é divisível por 5')

# 8. **Exercício 8: Cálculo do IMC**
#    - Peça ao usuário seu peso e altura. Calcule o Índice de Massa Corporal (IMC) usando a fórmula `IMC = peso / (altura ** 2)` e mostre a faixa de peso (abaixo do peso, normal, sobrepeso ou obeso).

peso = float(input('Qual seu peso: '))
altura = float(input('Qual sua altura: '))

imc = peso / (altura ** 2 )

if imc < 18.5:
    print('Abaixo do normal')
elif imc > 18.6 and imc < 24.9:
    print('Normal') 
elif imc > 25.0 and imc < 29.9:
    print('Sobrepeso') 
elif imc > 30.0 and imc < 34.9:
    print('Obesidade grau I') 
elif imc > 35.0 and imc < 39.9:
    print('Obesidade grau II') 
else: 
    print('Obesidade grau III') 

# 9. **Exercício 9: Comparação de Números**
#    - Escreva um programa que peça ao usuário dois números e informe se eles são iguais ou, caso contrário, qual é o maior.

n1 = int(input('X: '))
n2 = int(input('Y: '))

if n1 == n2:
    print('Os valores são iguais')
elif n1 > n2:
    print('Número maior é: ', n1)
else:
    print('Número maior é: ', n2)

# 10. **Exercício 10: Desconto de Produtos**
#    - Crie um programa que peça o valor de um produto e a forma de pagamento (à vista ou parcelado). Se for à vista, aplique 10% de desconto.  Se for parcelado, exiba o preço normal sem desconto.


price = float(input('Valor Produto: '))

print('1: À vista: 10% de desconto')
print('2: Parcelado')

payment = input('Qual a forma de pagamento: ')

if payment == '1':
    discount = 10
    discountPrice = (discount / 100) * price
    finalPrice = price - discountPrice
    print('Valor à vista: ', finalPrice)
elif payment == '2':
    print('Valor parcelado: ', price)

# Esses exercícios ajudarão a praticar o uso de variáveis, 
# operadores matemáticos e condicionais (`if`, `else`, `elif`) em Python!

# -----------------------------------------------------------------------------------------------------

# Claro! Aqui estão mais 10 exercícios básicos de Python com variáveis, operadores e condicionais:

# 11. **Exercício 1: Tabuada**
#    - Crie um programa que solicite ao usuário um número inteiro e exiba a tabuada desse número de 1 a 10.

n1 = int(input('num: '))
print(f'Tabuada do {n1}: \n')

for i in range(10): 
    print(f'{n1} x {i} = {i * n1}') 

# 12. **Exercício 2: Calculadora de Juros Simples**
#    - Peça ao usuário o valor principal, a taxa de juros e o tempo (em anos). Calcule e exiba o montante total após o tempo usando a fórmula `M = P(1 + rt)`.

valorP = float(input('Valor Principal: '))
taxajuros = float(input('Juros: '))
anos = int(input('Anos: '))

montanteTotal = valorP * (1 + taxajuros * anos)
print(f"O montante total após {anos} anos será: {montanteTotal:.2f}")

# 13. **Exercício 3: Verificação de Senha**
#    - Solicite ao usuário que insira uma senha e verifique se a 
# senha correta é "123456". Exiba uma mensagem de sucesso ou erro.

password = (input('Password: '))

while password != '12345':
    print('Try again:')
    password = (input('Password: '))
print('Senha correta')

# 14. **Exercício 4: Classificação de Notas**
#    - Peça ao usuário para inserir uma nota de 0 a 100 e 
# classifique a nota como "A", "B", "C", "D" ou "F" de acordo com a seguinte tabela:
#      - A: 90 a 100
#      - B: 80 a 89
#      - C: 70 a 79
#      - D: 60 a 69
#      - F: abaixo de 60

nota = int(input('Nota: '))

if nota >= 90 and nota <=100:
    print('A: 90 a 100')
elif nota >= 80 and nota <=89:
    print('B: 80 a 89')
elif nota >= 70 and nota <=79:
    print('C: 70 a 79')
elif nota >= 60 and nota <=69:
    print('D: 60 a 69')
elif nota <= 59 and nota >=0:
    print('F: abaixo de 60')
else:
    print('Fora do padrão')
    

# 15. **Exercício 5: Contagem Regressiva**
#    - Escreva um programa que solicite ao usuário um número inteiro e 
# exiba uma contagem regressiva a partir desse número até 0.

n1 = int(input('Número: '))

for n in range(n1, -1, -1): 
    print(n)

n1 = int(input('Número: '))
for n in range (n1):    
    print(n)

# 16. **Exercício 6: Verificação de Triângulo**
#    - Solicite ao usuário três lados de um triângulo e verifique se os lados formam um triângulo válido (a soma de dois lados deve ser maior que o terceiro).

lado1 = float(input('Lado 1: '))
lado2 = float(input('Lado 2: '))
lado3 = float(input('Lado 3: '))

soma = lado1 + lado2

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print('Triângulo válido')
else:
    print('Triângulo inválido')


# 17. **Exercício 7: Nome e Sobrenome**
#    - Peça ao usuário que insira seu nome completo e exiba uma mensagem dizendo quantos caracteres tem o nome e quantas palavras 
# (separadas por espaços).

nome = input("Insira seu nome completo: ")

numCaracteres = len(nome.replace(" ", ""))
num_palavras = len(nome.split())

print(f"O nome inserido contém {numCaracteres} caracteres e {num_palavras} palavras.")

# 18. **Exercício 8: Conversão de Moedas**
#    - Crie um programa que converta um valor em Reais (BRL) para Dólares (USD) e Euros (EUR). Use uma taxa fixa para as conversões (por exemplo, 1 USD = 5 BRL e 1 EUR = 6 BRL).

print('1: Dolar')
print('2: Euro ')
enchangeSelect = input('Qual moeda deseja trocar: ')

reais = float(input('Qual valor em reais: '))

if enchangeSelect == '1':
    dolar = 5
    valorConvertidoUS = reais * dolar 
    print(f'Valor em dólar: {valorConvertidoUS:.2f}')
elif enchangeSelect == '2':
    euro = 6
    valorConvertidoEU = reais * euro 
    print(f'Valor em dólar: {valorConvertidoEU:.2f}')

# 19. **Exercício 9: Média Ponderada**
#    - Solicite ao usuário duas notas e os pesos correspondentes. Calcule a média ponderada e exiba o resultado. A fórmula é `media_ponderada = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)`.

nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))

peso1 = float(input('Peso 1: '))
peso2 = float(input('Peso 2: '))

mediaPonderada = (nota1 * peso1 + nota2 * peso2) / (peso1 + peso2)

print('A média ponderada é: ', mediaPonderada)

# 20. **Exercício 10: Par ou Múltiplo de 3**
#     - Peça ao usuário um número inteiro e verifique se ele é par ou um múltiplo de 3. 
# Exiba uma mensagem adequada para cada condição.

num = int(input('Número: '))

if num % 2 == 0:
    print("O número é par.")
elif num % 3 == 0:
    print("O número é múltiplo de 3.")
else:
    print("O número é igual a zero.")

# Esses exercícios também ajudarão a praticar e reforçar o uso de variáveis, operadores e condicionais em Python! Se precisar de soluções para algum deles, é só avisar!


# Claro! Aqui estão mais 10 exercícios para você praticar Python:

# 1. **Exercício 1: Contagem de Vogais**
#    - Crie um programa que solicite uma frase ao usuário e conte quantas vogais (a, e, i, o, u) existem na frase.

frase = input('Frase: ')
print('Tem A: ', frase.count('a'))
print('Tem E: ', frase.count('e'))
print('Tem I: ', frase.count('i'))
print('Tem O: ', frase.count('o'))
print('Tem U: ', frase.count('u'))

# 2. **Exercício 2: Soma de Números Pares**
#    - Escreva um programa que calcule a soma de todos os números pares de 1 a 100.

for x in range(0, 100, 2):
    print(x)
print('Soma: ', sum(range(0, 100, 2)))

# 3. **Exercício 3: Inversão de String**
#    - Solicite ao usuário uma string e imprima a string invertida.

palavra = input('Palavra: ')
palavraInvertida = ''.join(reversed(palavra))
print('Palavra invertida', palavraInvertida)

# 4. **Exercício 4: Fatorial de um Número**
#    - Peça ao usuário um número inteiro e calcule o fatorial desse número. O fatorial de n (n!) é o produto de todos os inteiros de 1 a n.

import math

n1 = int(input('Numero: '))
fatorial = math.factorial(n1)
print('Fatorial: ', fatorial)

# 5. **Exercício 5: Número Primo**
#    - Crie um programa que peça um número inteiro e verifique se ele é primo (um número maior que 1 que não é divisível por nenhum número além de 1 e ele mesmo).

n1 = int(input('Numero: '))

if n1 > 1:
   for i in range(2,n1):
       if (n1 % i) == 0:
           print('Não Primo')
           break
   else:
       print('Primo')
else:
   print('Não Primo')

# 6. **Exercício 6: Geração de Lista de Quadrados**
#    - Crie uma lista com os quadrados dos números de 1 a 10 e imprima a lista.

quadrados = [x**2 for x in range(1, 11)]
print('Quadrados: ', quadrados)

# 7. **Exercício 7: Jogo da Adivinhação**
#    - Desenvolva um jogo simples onde o usuário deve adivinhar um número gerado aleatoriamente entre 1 e 100. Dê dicas se o palpite é maior ou menor que o número gerado.

import random

numeroSorteado = random.randint(1, 100)
numero = int(input('Adivinhe o número: '))

while numero != numeroSorteado:
    if numero < numeroSorteado:
        print('Muito baixo!')
    else:
        print('Muito alto!')
    numero = int(input('Tente de novo: '))

# 8. **Exercício 8: Anagrama**
#    - Solicite ao usuário duas palavras e verifique se uma é um 
# anagrama da outra (ou seja, se podem ser formadas reorganizando as letras).

palavra1 = input('Palavra 1: ')
palavra2 = input('Palavra 2: ')

if sorted(palavra1) == sorted(palavra2):
    print('Anagrama')
else:
    print('Não Anagrama')

# 9. **Exercício 9: Soma de Dígitos**
#    - Peça ao usuário um número inteiro e calcule a soma de seus dígitos. Por exemplo, para o número 123, a soma é 1 + 2 + 3 = 6.

n1 = int(input('Números: '))
soma = 0

while n1 > 0:
    digito = n1 % 10
    soma += digito
    n1 //= 10       
print('Soma: ', soma)

# 10. **Exercício 10: Conversor de Horas**
#     - Crie um programa que converta um tempo em horas e minutos para segundos. 
# Por exemplo, 1 hora e 30 minutos devem ser convertidos para 5400 segundos.

hora = int(input('Horas: '))
minuto = 60
segundos = hora * minuto

print('Segundos: ', segundos)


# Esses exercícios cobrem uma variedade de tópicos e ajudarão a fortalecer suas habilidades em Python! Se precisar de ajuda com algum deles, é só avisar!


# Aqui estão 10 exercícios básicos de Python que utilizam loops `for`:

# 1. **Exercício 1: Números de 1 a 10**
#    - Crie um programa que imprima todos os números de 1 a 10.

for x in range(1, 11):
    print(x)

# 2. **Exercício 2: Números Pares de 1 a 20**
#    - Escreva um programa que imprima todos os números pares de 1 a 20.

for x in range (2, 20, 2):
    print(x)

# 3. **Exercício 3: Tabela de Multiplicação**
#    - Crie um programa que peça ao usuário um número e exiba sua tabela de multiplicação de 1 a 10.

n1 = int(input('num: '))
print(f'Tabuada do {n1}: \n')

for i in range(10): 
    print(f'{n1} x {i} = {i * n1}') 

# 4. **Exercício 4: Soma de Números**
#    - Solicite ao usuário quantos números ele deseja somar e use um loop `for` para calcular a soma.

n1 = int(input('Quantos números: '))
soma = 0

for x in range(n1):
    num = int(input('Número: '))
    soma += num
print('Soma: ', soma)

# 5. **Exercício 5: Listagem de Nomes**
#    - Crie uma lista com os nomes de cinco amigos e use um loop `for` para imprimir cada nome.

lista = ['João', 'Maria', 'Pedro', 'Ana', 'Luiz']

for x in lista:
    print('Nomes: ', x)

# 6. **Exercício 6: Contagem Regressiva**
#    - Crie um programa que imprima uma contagem regressiva de 10 a 1.

for x in range(10, 0, -1):
    print(x)

# 7. **Exercício 7: Fatorial com Loop**
#    - Peça ao usuário um número e calcule seu fatorial usando um loop `for`.

n1 = int(input('Número: '))
fatorial = 1

for i in range(1, n1 + 1):  
    fatorial *= i
print('Fatorial: ', fatorial)

# 8. **Exercício 8: Lista de Quadrados**
#    - Gere uma lista com os quadrados dos números de 1 a 10 e imprima essa lista.

listaQuadrados = [x**2 for x in range(1, 11)]
print('Quadrados: ', listaQuadrados)

# 9. **Exercício 9: Contar Letras**
#    - Solicite ao usuário uma palavra e conte quantas letras 'a' existem nela, usando um loop `for`.

palavra = input('Palavra: ')
conta = 0

for x in palavra:
    if x == 'a':
        conta += 1
print('A: ', conta)

# 10. **Exercício 10: Sequência de Fibonacci**
#     - Crie um programa que imprima os primeiros 10 números da sequência de Fibonacci.

n1 = int(input('Quantos números: '))
fibonacci = [0, 1]

for i in range(2, n1):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
print('Fibonacci: ', fibonacci)

# Esses exercícios ajudarão a praticar o uso de loops `for` e reforçar sua compreensão. Se precisar de dicas ou soluções para algum deles, estou aqui para ajudar!