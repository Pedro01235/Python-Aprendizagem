# Estruturas de repetição
# Loops utilizando o for 

# O for é utilizado para percorrer ou iterar sobre uma sequência de dados (podendo ser uma lista, uma tupla, uma string), 
# executando um conjunto de instruções em cada item.

# for {nome variável} in {variável iteração}:
#     {código}

# Agora vamos à explicação:

#     {variável iteração}: é o nome da variável que vai receber os elementos do iterável a cada iteração
#     {iterável}: é o container de dados sobre o qual vamos iterar, podendo ser: uma lista, uma tupla, um dicionário, entre outros.
#     {código}: é o bloco de código que será executado a cada iteração (loop).

# Vamos à um exemplo:
lista = [1, 2, 3, 4, 5]
for item in lista:
    print(item)

    # Vamos entender o passo a passo:

    # Na primeira iteração, a variável item vai receber o valor do primeiro elemento da lista, que é 1. Portanto print(item) vai mostrar o valor 1.
    # Na segunda iteração, item vai receber o valor do segundo elemento da lista lista, que é 2. Portanto print(item) vai mostrar o valor 2.
    # E assim por diante até o último valor da lista, que é 5.

# Vamos à outro exemplo:
palavra = 'Python'
for item in palavra:
    print(item)

# Vamos à outro exemplo:
for numero in range(1, 11):
    print(numero)

# Vamos à outro exemplo:
for x in range(2, 20, 2):
    print(x)

# Vamos à outro exemplo:
pedras = ('Rubi', 'Esmeralda', 'Quartzo', 'Safira', 'Diamante', 'Turmalina')
for pedra in pedras:
    if pedra == 'Quartzo':
        continue
    print(pedra)
    
# Vamos à outro exemplo:
lista = [2,6,9,4,0,12,3,7]
for item in lista:
    print(item)

# O break e o continue 

# Existem duas palavras reservadas da linguagem que servem para auxiliar no controle de fluxo da estrutura de repetição. São elas: break e continue!

# O comando break
# Começando pelo break, nós o utilizamos para parar a execução de um loop.

# Veja um exemplo:
for item in [1, 2, 3, 4, 5]:
    if item == 3:
        break
    else:
        print(item)

# O comando continue
# Já o continue serve para pular todo código que estiver abaixo da cláusula continue, dando sequência a próxima iteração do loop.

# Veja como será a saída do código abaixo:
for item in [1, 2, 3, 4, 5]:
    if item == 3:
        continue
    else:
        print(item)

# Perceba que o número 3 não aparece!

# Loops utilizando for e else 

# Você sabia que podemos usar o else em loops for?
# E a resposta é: SIM!

# Pois é, esse é um fato que poucos Pythonistas conhecem.

# O else nos possibilita executar um bloco de código após o iterável ter sido completamente percorrido.
# Contudo, o else não é executado quando o for encontra uma cláusula break!

# Vamos entender melhor no exemplo:
for item in [1, 2, 3, 4, 5]:
    if item == 6:
        print('Encontramos o 6 ')
        break
    else:
        print('Elemento 6 não encontrado')

# Como o número 6 não está presente na lista, o código em else será executado!


# A função range()

# Essa função é de grande ajuda quando o tema é repetição, laços, for etc.
# Ela permite especificar o inicio de uma sequência, o passo (ou pulo) e valor final.
# Com isso, o Python nos retorna uma sequência de números para que possamos iterar!

# Sua sintaxe pode ter as seguintes três formas, sendo que seu único parâmetro obrigatório é o fim:

# range(fim)                  # range(stop) 
# range(inicio, fim)          # range(start, stop)
# range(inicio, fim, passo)   # range(start, stop, step)

# É importante ressaltar que na versão 3.x do Python, a função range() retorna um objeto iterável e não mais uma lista com elementos, por essa razão devemos converter o retorno para listas com a função list().

# Veja alguns exemplos de como criar listas com range:

# Gerar lista com (fim)
print(list(range(5)))

# Gerar com (inicio, fim)
print(list(range(5, 10)))

# Gerar com (inicio, fim, passo)
print(list(range(0, 10, 2)))

# Utilizando range
# Sabendo que a estrutura de repetição for executa um ciclo para cada elemento de um iterável, e a função range é um iterável, podemos criar uma harmonia perfeita entre esses dois:
for num in range(4):
    print(num)

# O range não se aplica diretamente ao while, porém um exemplo um pouco mais complexo pode demonstrar eles juntos:
lista = list(range(6))
comprimento = 6

while len(lista) == comprimento:
    print(lista)
    lista.append('item')
else:
    print(f'O comprimento da Lista é {len(lista)} e ultrapassou {comprimento}!')
    print(lista)

# Explicando: basicamente ele verifica se o tamanho da lista é igual a 6 itens. Após a primeira verificação ele adiciona mais um item (item), assim modificando seu comprimento e encerrando o laço!

