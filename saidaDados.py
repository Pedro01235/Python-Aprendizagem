# Saída de dados com a função print

# A função para imprimir dados em Python é a função print().
# Ela é responsável por mostrar valores em seu terminal:

print('Olá, Mundo!')

# O parâmetro sep= da função print

# Por padrão, quando utilizamos virgula para separar os itens, a função print utiliza espaços para separar cada saída.
# Porém, podemos utilizar o parâmetro sep= para definir um caractere de separação.

# Entenda no exemplo a seguir:

print('Dia', 'Mês', 'Ano', sep='/')
print('ontem', 'Hoje', 'Amanhã', sep='-')
print("B", "n", "n", ".", sep='a')
print('Carro:' , 'Astra', sep=' ')

# O parâmetro end= da função print 

# Por padrão, a função print utiliza a quebra de linha (\n) como último caracter.
# O parâmetro end= é responsável por alterar esse comportamento, possibilitando ao desenvolvedor trocar qual caracter será adicionado ao final do dado impresso no terminal.

# Vamos entender melhor no exemplo a seguir:

# Exemplo com fim de linha sem nenhum caracter
print('Vamos estudar Na ', end='')
print('Python Academy')

# Exemplo com fim de linha igual à ->
print('As rosas são', end=' -> ')
print('Vermelhas')

# Exemplo com fim de linha igual à :
print("Quantidade", end=': ')
print(40)

# Utilizando print para gravar dados em arquivos

# A função print() também funciona para gravar dados em arquivos.
# Para isso, utilizamos o parâmetro file= da função print.
# Também precisamos de um arquivo aberto, o que é feito utilizando-se a função open.

# Veja o exemplo abaixo:

with open('arquivo.txt', 'w') as arquivo:
    print("Escreva isso dentro do arquivo,", file=arquivo)
    print("Escreva outra linha dentro do arquivo.", file=arquivo)

#Formatação de Strings em Python

# Em Python nós não temos muitas formas de formatar strings, graças a um dos Zen’s do Python (não sabe qual? Então já clica aqui pra saber mais).
# Antes do Python 3.6, nós tínhamos basicamente duas formas de formatar strings:

#     Utilizando % ou
#     Utilizando str.format(), a partir do Python 3.0.

# A partir da versão 3.6 do Python, foi introduzido o conceito de f-strings, que veremos AGORA!

# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------

# Formatação com f-strings

# F-strings foram criados para facilitar nossa vida e vieram para ficar!
# Também chamadas de “strings literais formatadas” (formatted string literals), f-strings são strings com a letra f no início e chaves {} para realizar a interpolação de expressões.

# As expressões são processadas em tempo de execução e formatadas utilizadas o protocolo __format__.

nome = 'Python Academy'
print(f"Qual o melhor Blog sobre Python? {nome}!")

# Utilizando funções

# Como f-strings são processadas em tempo de execução, podemos colocar quase todo tipo de código dentro das expressões.
# Aqui um outro exemplo, utilizando chamada de função e mais:

nome = 'python academy'
print(f"Qual o melhor Blog sobre Python? {nome.upper() + '!' * 3}")

# Ou ainda:

import math
x = 0.5
print(f'cos({x}) = {math.cos(x)}')

# Acessando dicionários

dicionario = dict({'nome': 'Vinícius', 'ocupacao': 'Software Engineer'})
print(f"{dicionario['nome']} é um {dicionario['ocupacao']}")

# Strings multi-linha
# Também podemos criar f-strings multilinha:

site = 'Python Academy'
titulo = 'f-string no Python'
dificuldade = 'Básico'

print(
  f"Site: {site}\n"
  f"Título: {titulo}\n"
  f"Dificuldade: {dificuldade}"
)

# Método de classe __str__ vs __repr__

# Você pode até mesmo utilizar objetos instanciados dentro de f-strings. Por exemplo, caso você tenha a seguinte classe:
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def __str__(self):
        return f"{self.marca}/{self.modelo} - Ano {self.ano}"
    
    def __repr__(self):
        return (
            f"Marca: {self.marca}\n"
            f"Modelo: {self.modelo}\n"
            f"Ano: {self.ano}"
        )

# Instanciando um objeto da classe Carro
carro = Carro("Toyota", "Corolla", 2020)

# Exibindo o objeto usando print() (chamará o método __str__)
print(carro)

# Exibindo a representação formal do objeto (chamará o método __repr__)
print(repr(carro))


# Utilizando formatadores especiais
# Cada campo desse possibilita um tipo de modificação na string resultante.

# Vamos de exemplo!
# Um modificador disponível é o símbolo de porcentagem %. Ele serve para formatar saídas numéricas. Veja a mágica:

valor = 5.5 / 40.0

print(
  f'Resultado original: {valor}\n'
  f'Resultado formatado: {valor:.1%}'
)

# Explicando:

#     O .1 diz que a string resultante deve ter apenas uma casa decimal;
#     O % multiplica o valor por 100 e inclui o % ao final.

# Agora um exemplo maluco:

valor = 255
print(f"'{valor:-^10x}'")