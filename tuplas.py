# são imbutáveis (não pode ser modificada depois de criada)


tupla = (0, 1, 2, 3)
print(tupla)

halogenios = ('Li', 'Na', 'K', 'Rb', 'Cs')
print('elementos 0 a 3: ', halogenios[0:3])
print('tupla: ', halogenios)
print('acessando elemento: ', halogenios[2])
print('tamanho da tupla: ', len(halogenios))
print('L1' in halogenios) #não está no conjunto
print('Li' in halogenios) #está no conjunto


gases_nobre = ('He', 'Ne', 'Ar', 'Kr', 'Xe')
elementos = halogenios + gases_nobre
print(elementos)

t1 = (0, 1, 1, 2, 3 ,5 ,6 ,8 ,9 ,7 ,1 ,1 ,3 ,5 ,53)
print(t1)
print(min(t1))
print(max(t1))
print('quantidade de elementos repetidos: ', t1.count(5))

# Operaçôes não disponíveis em tuplas: .sort(), .append(), .reverse(), .pop() ...

for elemento in elementos:
    print(f'Elemento químico', {elemento})

# lista com tuplas dentro
grupo17 = list(halogenios)
grupo17 [0] = 'H'
print(grupo17)

#tupla criada com lista
grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs']
alcalinos = tuple(grupo1)
print(alcalinos)
# tuplas classicadas
print(sorted(alcalinos))