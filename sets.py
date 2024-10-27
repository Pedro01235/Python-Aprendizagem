#Sets (conjunto)
#não armazena elementos duplicados
#conjunto = {1, 2, 3, 4, 5}

planeta = {'Mercu', 'Venus', 'Terra', 'Marte', 'Jupiter', 'Saturno', 'Urano', 'Netuno'}
print(planeta)

#tamanho de conjunto (sets)
print(len(planeta))
#verifica se um elemento existe no conjunto
print('Mercu' in planeta)
#verifica se um elemento não existe no conjunto
print('Moon' not in planeta)

#percorrendo o conjunto
for astro in planeta:
    print(astro) 

#removendo elementos
planeta.remove('Venus')
print(planeta)

#removendo o conjunto inteiro
planeta.clear()
print(planeta)

#removendo o conjunto inteiro
del planeta
print(planeta)

#lista de cores
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'amarelo']
print(cores)

cores_sets = set(cores)
print(cores_sets)

frutas1 = {'maca', 'banana', 'jaca', 'melão', 'abacaxi'}
frutas2 = {'maca', 'banana', 'jaca', 'melão', 'abacaxi', 'limão'}
print(frutas1)
print(frutas2)
#verifica se dois conjuntos sao iguais
print(frutas1 == frutas2)
#verifica se dois conjuntos sao diferentes
print(frutas1 != frutas2)
#uniao de conjuntos
print(frutas1 | frutas2)
#interseccao de conjuntos
print(frutas1 & frutas2)
#diferenca de conjuntos
print(frutas1 - frutas2)
#diferenca simetrica de conjuntos
print(frutas1 ^ frutas2)


times = {'vasco', 'flamengo', 'botafogo', 'fluminense'}
print(times)
#adicionando elementos
times.add('palmeiras')
print(times)
#removendo elementos
times.remove('vasco')
print(times)
#removendo elementos com o discard
times.discard('flamengo')
print(times)
#removendo elementos com o pop
times.pop()
print(times)
#removendo elementos com o clear
times.clear()
print(times)


# 1. Criando um set simples
# Crie um set com cinco carros: 'Golf', 'Corolla', 'Civic', 'Jetta', 'Fusca'. Em seguida, exiba o set.

carros = {'Golf', 'Corolla', 'Civic', 'Jetta', 'Fusca'}
print('Sets: ', carros) 

# 2. Adicionando elementos a um set
# Adicione o carro "911" ao set de carros. Em seguida, exiba o set atualizado.

carros.add('911')
print('Adicionado: ', carros)

# 3. Removendo elementos de um set
# Remova o carro "Golf" do set. Exiba o set após a remoção.

carros.remove('Golf')
print('Removido: ', carros)

# 4. Verificando a presença de um elemento no set
# Verifique se o carro "Corolla" está no set e exiba uma mensagem confirmando ou negando.

if 'Corolla' in carros:
    print('Corolla existe')
else:
    print('Corolla não existe')

# 5. Unindo dois sets
# Crie um segundo set com as marcas "Toyota", "Volkswagen", "Nissan", "Honda", "Porsche". 
# Em seguida, una os dois sets em um único set e exiba o resultado.

marcas = {'Toyota', 'Volkswagen', 'Nissan', 'Honda', 'Porsche'}
carros_e_marcas = carros.union(marcas)
print('Carros e Marcas: ', carros_e_marcas)

# 6. Encontrando a interseção de dois sets
# Crie um set com as marcas "Honda" e "Porsche", e encontre as marcas que estão presentes em ambos os sets.

marcas_comum = {'Honda', 'Porsche'}
interseccao = marcas.intersection(marcas_comum)
print('Interseção: ', interseccao)

# 7. Diferença entre sets
# Encontre as marcas que estão no set original de marcas, mas não no set com as marcas "Honda" e "Porsche".

diferenca = marcas.difference(marcas_comum)
print('Diferença: ', diferenca)

# 8. Limpar um set
# Remova todos os elementos do set de carros, deixando-o vazio.

carros.clear()
print('Carros após limpar: ', carros)




