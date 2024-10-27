#Funções
#Modularização de código, reutilização de código e abstração de código, estrutura de dados e legiibilidade.

#Definindo uma função (def = definir)

#Estrutura
# def <nome_funcao> ([<argumentos>]):
#     <bloco de código>

def mensagem():
    print('Hello World!')
mensagem()

#Função com argumentos
def soma(a, b):
    return a + b
soma = soma(12, 7)
print(soma)

def mult(x, y ):
    
    return x * y
a = 5 
b = 6
c = mult(a, b)
print(c)

def div(k , l):
    if l == 0:
        return 'Impossível dividir por 0'
    else:
        return k / l
    
if __name__ == '__main__':
    k = int(input('Primeiro valor: '))
    l = int(input('Segundo valor: '))
    c = div(k, l)

print(c)


def quadrado(val):
    quadrados = []
    for x in val:
        quadrados.append(x**2)
    return quadrados

if __name__ == '__main__':
    valores = [2, 5, 7, 9 ,12]
    resultados = quadrado(valores)
    for x in resultados:    
        print('Valor:',x)

#funções com parametros opcionais, de valor padrão e com multiplos argumentos

def contar(num=11, caracter='+'):
    for x in range(1, num):
        print(caracter)

if __name__ == '__main__':
    contar(caracter='*')


x = 5
y = 6
z = 3

def soma_multiplos(x, y, z = 0):
    if z == 0:
        return x + y
    else:
        return x + y + z

if __name__ == '__main__':
    res = soma_multiplos(x, y)
    print(res)




# Exercícios

# Aqui estão alguns exercícios básicos de funções em Python sem as respostas:

# 1. **Função de saudação**
#    - Crie uma função chamada `saudacao` que recebe um nome como argumento e exibe uma saudação personalizada.

def saudacao(name):
    print('Ola', name)
saudacao('Pedro')

# 2. **Função de soma**
#    - Crie uma função chamada `soma` que recebe dois números como parâmetros e retorna a soma deles.

def somar(x, y):
    return x + y
somar = somar(3, 2)
print(somar)

# 3. **Função para verificar par ou ímpar**
#    - Crie uma função chamada `par_ou_impar` que recebe um número como argumento e retorna se o número é par ou ímpar.

def par_ou_impar(n1):
    if n1 % 2 == 0:
        print('Par')
    else:
        print('Impar')

if __name__ == '__main__':
    n1 = int(input('Digite um número: '))
    par_ou_impar(n1)

# 4. **Função de fatorial**
#    - Crie uma função chamada `fatorial` que recebe um número inteiro positivo e retorna o fatorial desse número.

def fatorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

if __name__ == '__main__':
    n = int(input('Digite um número: '))
    print(fatorial(n))

# 5. **Função para calcular a média**
#    - Crie uma função chamada `calcular_media` que recebe uma lista de números e retorna a média dos valores.

def media(valores):
    return sum(valores) / len(valores)

if __name__ == '__main__':
    valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(media(valores))

# 6. **Função para verificar maior de idade**
#    - Crie uma função chamada `maior_de_idade` que recebe a idade de uma pessoa e retorna se ela é maior de idade (18 anos ou mais).

def maior_de_idade(idade):
    if idade >= 18:
        return True
    else:
        return False
    
if __name__ == '__main__':
    idade = int(input('Digite sua idade: '))
    print(maior_de_idade(idade))

# 7. **Função para inverter uma string**
#    - Crie uma função chamada `inverter_string` que recebe uma string como argumento e retorna a string invertida.

def inverter_string(string):
    return string[::-1]

if __name__ == '__main__':
    string = input('Digite uma string: ')
    print(inverter_string(string))  

# 8. **Função que retorna o maior valor**
#    - Crie uma função chamada `maior_valor` que recebe três números como parâmetros e retorna o maior deles.

def maior_valor(a, b, c):
    return max(a, b, c) 

if __name__ == '__main__': 
    a = int(input('Primeiro valor: '))
    b = int(input('Segundo valor: '))
    c = int(input('Terceiro valor: '))
    print(maior_valor(a, b, c))

# 9. **Função de contagem regressiva**
#    - Crie uma função chamada `contagem_regressiva` que recebe um número como argumento e imprime uma contagem regressiva de N até 0.

def contagem_regressiva(n):
    for i in range(n, -1, -1):
        print(i)

if __name__ == '__main__':
    n = int(input('Digite um número: '))
    contagem_regressiva(n)

# 10. **Função para encontrar a palavra mais longa**
#     - Crie uma função chamada `palavra_mais_longa` que recebe uma lista de palavras e retorna a palavra com o maior número de caracteres.

def palavra_mais_longa(palavras):
    return max(palavras, key=len)

if __name__ == '__main__':
    palavras = input('Palavras: ').split()
    print(palavra_mais_longa(palavras))

# Esses exercícios são ótimos para praticar o uso de funções em Python!


# Aqui estão alguns exercícios ainda mais simples sobre funções em Python:

# 1. **Função que imprime "Olá, Mundo!"**
#    - Crie uma função chamada `ola_mundo` que imprime "Olá, Mundo!" quando for chamada.

def ola_mundo():
    print('Olá, Mundo')
ola_mundo()

# 2. **Função que soma dois números**
#    - Crie uma função chamada `soma` que recebe dois números como parâmetros e imprime a soma deles.

def soma(a, b):
    print(a + b)
soma(5, 6)

# 3. **Função que multiplica um número por 10**
#    - Crie uma função chamada `multiplica_por_10` que recebe um número como argumento e imprime o resultado da multiplicação por 10.

def multiplica_por_10(n):
    print(n * 10)
multiplica_por_10(5)

# 4. **Função que verifica se um número é positivo**
#    - Crie uma função chamada `numero_positivo` que recebe um número como parâmetro e imprime "Positivo" se o número for maior que zero, ou "Não é positivo" caso contrário.

def numero_positivo(n):
    if n > 0:
        print('Positivo')
    else:
        print('Não é positivo')
numero_positivo(5)

# 5. **Função que imprime o dobro de um número**
#    - Crie uma função chamada `dobro` que recebe um número e imprime o dobro desse número.

def dobro(n):
    print(n * 2)
dobro(5)

# 6. **Função que dá bom dia com nome**
#    - Crie uma função chamada `bom_dia` que recebe um nome e imprime "Bom dia, [nome]!"

def bom_dia(nome):
    print(f'Bom dia, {nome}!')
bom_dia('Pedro')

# 7. **Função que exibe um número ao quadrado**
#    - Crie uma função chamada `ao_quadrado` que recebe um número e imprime o valor desse número ao quadrado.

def ao_quadrado(n):
    print(n**2)
ao_quadrado(5)

# 8. **Função que imprime "Par" ou "Ímpar"**
#    - Crie uma função chamada `verificar_par` que recebe um número e imprime "Par" se for par e "Ímpar" se for ímpar.

def verificar_par(n):
    if n % 2 == 0:
        print('Par')
    else:
        print('Ímpar')
verificar_par(5)

# Esses exercícios são bem simples e ajudam a fixar os conceitos básicos de criação e uso de funções!