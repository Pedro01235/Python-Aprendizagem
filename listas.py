# Introdução

# Uma Lista (list) em Python, nada mais é que uma coleção ordenada de valores, separados por vírgula e dentro de colchetes [].
# Elas são utilizadas para armazenar diversos itens em uma única variável. Entender este conteúdo é de extrema importância para dominar a linguagem por completo!

# Abaixo temos um exemplo de uma lista:

# Exemplo de lista:
lista = ['Python', 'Academy']

print(lista)

# Podemos observar a classe de uma lista com type():

lista = []
print(type(lista))


# Criando listas

# Existem várias maneiras de se criar uma lista.
# # A maneira mais simples é envolver os elementos da lista por colchetes, por exemplo:

# lista com apenas um elemento
lista = ['Python']
print(lista)

# Também podemos criar uma lista vazia:
lista = []
print(lista)

# Para criar uma lista com diversos itens, podemos fazer:
lista = ['Python, Academy', 2024]
print(lista)

# Também podemos utilizar a função list do próprio Python (built-in function):
lista = list(["Python Academy"])
print(lista)

# Podemos ainda criar listas através da função range(), dessa forma:
list(range(10))
print(list(range(10)))


# Acessando dados da lista
# Todos os itens de uma lista são indexados, ou seja para cada item da lista um índice é atribuído da seguinte forma: lista[indice].

# Exemplo com itens:
frutas = ['Maça', 'Banana', 'Jaca', 'Melão', 'Abacaxi']
# Em Python os índices são iniciados em 0.
# Acessando o primeiro item da lista:
print(frutas[0])

# Indexação negativa

# Neste momento entramos no conceito de indexação negativa, que significa começar do fim.
# -1 irá se referir ao último item. Por exemplo:
frutas = ['Maça', 'Banana', 'Jaca', 'Melão', 'Abacaxi']
print(frutas[-1])

# Lista dentro de lista

# Suponha que exista uma lista dentro de uma lista, assim:
lista = ['item1', ['python', 'Academy'], 'item3']
sublista = lista[1]
print(sublista[0])

# Como podemos acessar o primeiro índice do item que é uma lista?
# A resposta é simples, basta selecionar a posição em que se localiza a lista para ter acesso a ela, assim:

# Fatiando uma lista (slicing)
# O fatiamento de listas, do inglês slicing, é a extração de um conjunto de elementos contidos numa lista. Ele é feito da seguinte forma:

# lista [ inicio : fim : passo ]
# Explicando cada elemento:

#     início se refere ao índice de início do fatiamento.
#     fim se refere ao índice final do fatiamento. A lista final não vai conter esse elemento.
#     passo é um parâmetro opcional e é utilizado para se pular elementos da lista original

# Vamos entender melhor em seguida!

# # Se quisermos criar uma fatia de uma lista do índice 2 ao 4, podemos fazer da seguinte forma:

lista = [10, 20, 30, 40, 50, 60]
print(lista[2:5])

# O slicing conta a partir do índice 2 até o índice 5 (mas não o utiliza), pegando os índices 2, 3, 4.

# Percorrendo listas
# A forma mais comum de percorrer os elementos em uma lista é com um loop for elemento in lista, assim:

lista = [10, 20, 30, 40, 50, 60]
for num in lista:
    print(num)

# Com a função enumerate() podemos percorrer também o índice referente a cada valor da lista:
lista = [10, 20, 30, 40, 50, 60]
for indice, valor in enumerate(lista):
    print(f'índice={indice}, valor={valor}')

# ue tal poupar algumas linhas e obter o mesmo resultado com List Comprehension?

[print(num) for num in lista]
# Com enumerate:
[print(f'índice={indice}, valor={valor}') for indice, valor in enumerate(lista)]

# Métodos para manipulação de Listas
# O Python tem vários métodos disponíveis em listas que nos permite manipulá-las.
# Veremos agora quais são os métodos e como utilizá-los!

# Método index
# Utilizado encontrar a posição de um valor especificado. Exemplo:
lista = ['Carro', 'Casa', 'Hotel', 'Casa']
pos = lista.index('Casa')

print(f'O item desejado está na posição: {pos}')

# Método count
# O método count(elemento) retorna o número de vezes que o valor especificado aparece na lista. Exemplo:
lista = ['Carro', 'Casa', 'Hotel', 'Casa']
pos = lista.count('Casa')

print(f'O item desejado aparece: {pos}')

# Método append
# Para adicionar um elemento ao final da lista, use o método append(elemento):
lista = ['Python', 'Academy']
lista.append('adicionado')

print(lista)

# Método insert
# Para adicionar um item em um índice especificado, use o método insert(índice, elemento):
lista = ['Python', 'Academy']
lista.insert(0, 'Blog')

print(lista)

# Método extend
# O método extend(iterável) adiciona os elementos de uma lista especificada (ou qualquer outro iterável) ao final da lista:
sacola = ['Laranja', 'Banana']
legumes = ['Xuxu', 'Batata']

sacola.extend(legumes)
print(sacola)

# É possível concatenar as listas para obter o mesmo resultado em uma nova variável. Exemplo:
sacola = ['Laranja', 'Banana']
legumes = ['Xuxu', 'Batata']

juntos = sacola + legumes
print(juntos)

# E também podemos percorrer uma das listas, adicionando elementos à outra com o método append(), assim:
sacola = ['Laranja', 'Banana']
legumes = ['Xuxu', 'Batata']

for legume in legumes:
    sacola.append(legume)
print(sacola)

# Método remove
# Para remover um item com valor especificado, use o método remove(elemento):
lista = ['Blog', 'Python', 'Academy']
lista.remove('Blog')
print(lista)

lista = [10, 20, 30, 40, 50]
del lista[2]
print(lista)

# Com a del também é possível excluir uma lista completamente:
lista = [10, 20, 40, 50]
del lista
print(lista)

# Método pop
# Para remover um item do índice especificado e ainda retorná-lo, use o método pop(índice), dessa forma:
lista = ['Banana', 'limão', 'Carro', 'Laranja']
item = lista.pop(2)

print('Item:', item)
print('Lista:', lista)

# Método clear
# Esse método é utilizado para remover todos os elementos de uma lista, dessa forma:
lista = [10, 20, 40, 50]
lista.clear()

print(lista)

# Método copy
# Esse método retorna uma cópia da lista especificada.
lista = ['Python', 'Academy']
lista_copiada = lista.copy()

print(lista_copiada)
print(lista)

# Método reverse
# O método reverse é utilizado para reverter a ordem dos elementos de uma lista:
lista = [1, 2, 3, 4, 5]
lista.reverse()

print(lista)

# Método sort
# Esse método é utilizado para ordenar a lista.
# Também é possível criar uma função para definir seus próprios critérios de ordenação com sort(key=funcao).
lista = [1, 4, 5, 2, 4]
lista.sort()

print(lista)

# Adicionando o parâmetro reverse=True, é possível ordenar a lista em ordem decrescente.
# Para deixar do modo padrão basta colocar reverse=False:
lista = [1, 4, 5, 2, 4]
lista.sort(reverse=True)

print(lista)

# Keywords de manipulação de Listas
# Nesta parte veremos algumas Keyword da própria linguagem que utilizam listas como parâmetro, executando alguma ação.
# Keyword len()

# Retorna a quantidade de itens em uma lista, utilizando o método len(iterável):
lista = [10, 20, 30, 40, 50, 60]
print('Quantidade de itens:',  len(lista))
 
# Keyword min()
# A função min(iterável) devolve o item com menor valor da lista ou iterável de entrada:
lista = [2, 4, 8, 1]
print('Menor valor da lista:',  min(lista))

# Keyword max()
# Retorne o maior valor da lista ou iterável especificado mix(iterável):
lista = [2, 4, 8, 1]
print('Maior valor da lista:',  max(lista))

# Keyword sorted()
# A função sorted() é utilizada para ordenar a lista de entrada:
lista = [2, 4, 8, 1]
lista_ord = sorted(lista)
print(lista_ord)

# Keyword reversed()
# A função reversed() reverte a ordem da lista de entrada. Exemplo:
lista = [1, 2, 3, 4, 7]
for item in reversed(lista):
    print(item)



# exemplos de listas
n1 = [4, 6, 7, 8, 0, 3]
n2 = [1, 6, 3, 0, 12, 11]

valores = n1 + n2
valores [0] = 9
print('Contagem: ', len(valores))
print('Crescente: ', sorted(valores))
print('Decrescente: ', sorted(valores, reverse=True))
print('Soma: ', sum(valores))
print('Min: ', min(valores))
print('Max: ', max(valores))
print('Intervalo: ', valores[0:2])
print('Intervalo: ', valores)

valores.append(22)
print('Inserindo um número:', valores)
valores.pop()
print('Removendo um valor:', valores)
valores.pop(3)
print('Removendo de uma posição:', valores)
valores.insert(2, 9)
print('Inserindo em uma posição:', valores)
print('Verificar se o número 3 está na lista:', 3 in valores)
print('Verificar se o número 6 não está na lista:', 3 not in valores)
print('Quantidade de vezes 6: ', valores.count(6))

planetas = ['Mercu', 'Venus', 'Terra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Netuno']
for planeta in planetas:  
    print(planeta)  

# ----------------------

bebidas = []
for i in range(5):
    bebidas.append(input('Bebidas: '))
print(bebidas)


