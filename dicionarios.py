#dicionarios 

elemento = {
    'nome': 'Ferro',
    'simbolo': 'Fe',
    'numero': 26,
    'densidade': 0.534
}
print(elemento)

#Acessando itens do dicionarios
print(f'Simbolo: {elemento["simbolo"]}')
print(f'Nome: {elemento["nome"]}')

#Quantos itens tem no dicionário
print(f'O dicionário possui {len(elemento)} itens')

#Alterando itens
elemento['nome'] = 'Ouro'
elemento['densidade'] = 1.55
print(elemento)

#Adicionando itens
elemento['madeira'] = 'Carvalho'
print(elemento)

#Excluindo itens
del elemento['madeira']
print(elemento)

#Apagar todos os itens
elemento.clear()
print(elemento)

#Apagar o dicionário inteiro
del elemento
print(elemento)

#Verificando se um item existe
if 'madeira' in elemento:
    print('Existe um item chamado madeira')
else:
    print('Não existe um item chamado madeira')



elemento = {
    'nome': 'Ferro',
    'simbolo': 'Fe',
    'numero': 26,
    'densidade': 0.534
}
print(elemento)

#metodo items 
print(elemento.items())
for i in elemento.items():
    print(i) 

#metodo keys (chaves)
print(elemento.keys())
for i in elemento.keys():
    print(i)

#metodos values (valores)
print(elemento.values())
for i in elemento.values():
    print(i)

#metodo items e for 
for i, j in elemento.items():
    print(f'{i}, {j}')


# Exercícios

# 1. Criação de um dicionário
# Crie um dicionário que armazene informações sobre um aluno: nome, idade e as matérias que está cursando.

aluno = {
    'nome': 'Joaquim',
    'idade': 20,
    'materias': ['Matematica', 'Portugues', 'Fisica']
}
print(aluno)

# 2. Acessando valores
# A partir do dicionário criado no exercício anterior, acesse e exiba apenas o nome e a lista de matérias do aluno.

print(aluno['materias'])

# 3. Adicionando e modificando itens
# Adicione ao dicionário do aluno uma chave "nota_final" com o valor 8.5 e depois altere o valor para 9.0.

aluno ['nota_final'] = 10
print(aluno)

# 4. Removendo um item
# Remova a chave "idade" do dicionário e exiba o dicionário atualizado.

del aluno['idade']
print(aluno)

# 5. Iterando sobre um dicionário
# Crie um dicionário com o nome de cinco cidades e suas respectivas populações. Em seguida, itere sobre o dicionário e exiba cada cidade com sua população.

cidades = {
    'São Paulo': 12_000000,
    'Rio de Janeiro': 6_700_000,
    'Belo Horizonte': 2_500_000,
    'Salvador': 2_900_000,
    'Curitiba': 1_900_000
}

for i, j in cidades.items():
    print(f'{i} tem {j} habitantes')

# 6. Verificando a existência de uma chave
# Verifique se a chave "nota_final" está presente no dicionário do aluno. Caso esteja, exiba o valor.

if 'nota_final' in aluno:
    print('Chave existente')
else:
    print('Chave inexistente')

# 7. Dicionário de listas
# Crie um dicionário onde as chaves são nomes de frutas e os valores são listas contendo o preço e a quantidade disponível. Em seguida, acesse o preço de uma fruta específica.

frutas = {
    'maca': [2.00, 5],
    'banana': [4.00, 6],
    'uva': [5.00, 3],
}
print(frutas['banana'][0])

#Crie um dicionário que contenha informações de um aluno, como nome, idade e curso. Em seguida, exiba os dados do dicionário.

alunoF = {
    'nome': 'Pedro',
    'idade': 26,
    'curso': 'Jornalismo'
}
print(alunoF)

# Acessando valores do dicionário
#A partir do dicionário criado no exercício anterior, acesse e exiba o nome e o curso do aluno.

print(alunoF['nome'])
print(alunoF['curso'])

#Adicionando novos pares chave-valor
#Adicione um novo par chave-valor ao dicionário do aluno, como “nota_final” e atribua um valor. Depois, exiba o dicionário atualizado.

alunoF ['nota_final'] = 6
print(alunoF)

#Atualizando valores no dicionário
#Atualize a idade do aluno para 21 anos. Em seguida, exiba o dicionário atualizado.

alunoF ['idade'] = 21
print(alunoF)

#Removendo itens do dicionário
#Remova o campo “nota_final” do dicionário. Mostre o dicionário após a remoção.

del alunoF ['nota_final']
print(alunoF)

#Verificando se uma chave existe
#Verifique se a chave “idade” existe no dicionário. Exiba uma mensagem dizendo se ela existe ou não.

if "idade" in alunoF:
    print("A chave 'idade' existe no dicionário.")
else:
  print("A chave 'idade' não existe no dicionário.")

#Percorrendo um dicionário
#Faça um loop para percorrer todas as chaves e valores no dicionário e exibi-los.

for chave, valor in alunoF.items():
    print(f"{chave}: {valor}")
