
# execao é um objeto que representa um erro que ocorreu durante a execução de um programa.
#blocos try e except permitem que o Python identifique e trate esses erros.

# try: 
# Bloco de código a ser executado

# except {exceção}:
#Código que será executado caso a {exceção} seja capturada

# else:
#Código que será executado caso nenhuma exceção tenha sido lançada ou capturada

# finally:
#Código que será executado independente se alguma exceção for capturada ou não

# Apenas as cláusulas try e except são obrigatórias, sendo else e finally opcionais!
# Podemos ter múltiplas cláusulas except, capturando Exceções diferentes.

#Exception - classe base para todos os erros
#ArithmeticError - erro de operação aritmética
#OverFlowError - erro de sobreposição de capacidade
#ZeroDivisionError - erro de divisão por zero
#ImportError - erro de importação
#NameError - erro de nome inválido
#IOError - erro de entrada e saida
#IndentationError - erro de indentação
#RecursionError - erro de recursão infinita
#TypeError - erro de tipo

n1 = int(input('n1: '))
n2 = int(input('n1: '))

try:
    r = n1 / n2
except ZeroDivisionError:
    print('Não é possível dividir por zero')
else:
    print('O resultado é:', r)


#dentro do try vai o codigo que pode dar erro
#dentro do except vai o codigo que vai tratar o erro
#dentro do else vai o codigo que vai ser executado se o try der certo
#dentro do finally vai o codigo que vai ser executado sempre

def div(x, y ):
    return round(x / y, 2)

if __name__ == '__main__':
    while True:
        try:
            n3 = int(input('n3: '))
            n4 = int(input('n4: '))
            break
        except ValueError:
            print('Por favor, digite apenas números')

#enquanto o try der certo o except vai ser executado
#se der erro o except vai ser executado

#forçar o erro (exeção)
#só funcionará se o número for positivo

import math
from math import sqrt

if __name__ == '__main__':
    try:
        num = int(input('Digite um numero positivo: '))
        if num < 0:
            raise ArithmeticError('O numero deve ser positivo')
    except ArithmeticError:
        print('Número negativo')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print('Fim do calculo')

#criando minha exceção
class NumeroNegativoError(Exception):
    def __init__(self):
        pass

if __name__ == '__main__':
    try:
        num = int(input('Digite um número positivo: '))
        if num < 0:
            raise NumeroNegativoError
    except NumeroNegativoError:
        print('Numero negativo')
    else:
        print(f'A raiz quadrada de {num} é {sqrt(num)}')
    finally:
        print('Fim do calculo')


# Exemplos de utilização
# Suponha que você queira abrir um arquivo e caso ele não exista, seu programa irá criá-lo.

# Uma forma de fazer isso seria:
nome_arquivo = 'nome_arquivo.txt'
try:
    arquivo = open(nome_arquivo, 'r')
except FileNotFoundError:
    arquivo = open(nome_arquivo, 'a')
else:
    print(f"Arquivo {nome_arquivo} já existe")
finally:
    # Realiza algum processamento no arquivo
#   processa_arquivo(arquivo)

    # Fecha o arquivo
    arquivo.close()

# Dessa forma, caso o arquivo não exista, uma exceção FileNotFoundError será lançada e será capturada na cláusula except.
# Ali dentro, a função open com o parâmetro “a” (de “append”) será chamada, criando então o arquivo.
# Em seguida, temos a cláusula finally, que será executada independentemente de uma exceção ter sido lançada ou não.
# Como se trata de um arquivo, é sempre aconselhado realizar seu fechamento, e um bom lugar para fazer isso é dentro do finally.


# Capturando múltiplas exceções

# Podemos capturar múltiplas exceções de duas formas:
# A primeira, com múltiplas cláusulas except, assim:

try:
    dividendo = int(input("Digite o dividendo: "))
    divisor = int(input("Digite o divisor: "))
    resultado = dividendo/divisor

except ValueError:
    print("Numero digitado inválido")

except ZeroDivisionError:
    print("Divisão por zero não permitida")

# Assim, caso o erro ValueError seja lançado, este será capturado pelo primeiro except.
# E caso haja uma divisão por zero, a exceção ZeroDivisionError será lançada e capturada pelo segundo except.

# Podemos também agrupar exceções! Dessa forma, o mesmo tratamento será dado independente de qual exceção tenha sido lançado, dessa forma:
try:
    dividendo = int(input("Digite o dividendo: "))
    divisor = int(input("Digite o divisor: "))
    resultado = dividendo/divisor

except(ZeroDivisionError, ValueError):
    print("Erro de conversão ou divisor igual à zero")