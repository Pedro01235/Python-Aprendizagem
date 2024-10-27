# https://pythonacademy.com.br/blog/funcoes-lambda-no-python
#funções lambda (anônimas)

#Sintaxe
#lambda <parametros> : <expressão>

#Exemplo
quadrado = lambda x: x**2
print(quadrado(9))

#Exemplo 2
par = lambda x: x % 2 == 0
print(par(5))

#Exemplo 3
f_c = lambda f: (f - 32) * 5/9
print(f'100°F = {f_c(100):.2f}°C')


# https://pythonacademy.com.br/blog/as-funcoes-map-e-filter-no-python
#função map() função de ordem superior

#Sintaxe
#map(<função>, <iterável>)

#exemplo 
num = [2, 4, 6, 8]
dobro = list(map(lambda x: x * 2, num))
print(dobro)

#exemplo 2
palavras = ['cachorro', 'gato', 'elefante']
maisculas = list(map(lambda x: x.upper(), palavras))
print(maisculas)

#Exemplo 3
soma = lambda x, y: x + y
print(list(map(soma, [1, 2, 3], [4, 5, 6])))


#Função filter() filtra elementos de um iteração

#Sintaxe
#filter(<função>, <iterável>)

#exemplo
num = [2, 4, 6, 7, 5, 3 ,1]
pares = list(filter(lambda x: x % 2 == 0, num))
print(pares)

#exemplo 2
palavras = ['cachorro', 'gato', 'elefante', 'CAVALO', 'GATO']
maiusculas = list(filter(lambda x: x[0].isupper(), palavras))
print(maiusculas)

# Função reduce(função, sequência, valor_inicial) reduz os elementos de um iteração

#Sintaxe
#reduce(<função>, <iterável>)

#exemplo
from functools import reduce
num = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, num)
print(soma)

#exemplo 2
from functools import reduce
def multiplica(x, y):
    return x * y
num = [1, 2, 3, 4, 5]
multiplica = reduce(multiplica, num)
print(multiplica)

#exemplo 3 ((1² + 2²)² + 3²)² + 4²
from functools import reduce
numeros = [1, 2, 3, 4]
soma = reduce(lambda x, y: x + y**2 + x**2, numeros)
print(soma)

