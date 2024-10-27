
#compreensão de listas

#exemplo 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = [x**2 for x in numeros]
print(quadrados)

#exemplo 2 (lista de pares 0, 10)
pares = [x for x in range(0, 11) if x % 2 == 0]
print(pares)

#exemplo 3 (contar vogais)
frase = 'O rato roeu a roupa do rei de Roma, e a roupa do rei de Roma'
vogais = [letra for letra in frase if letra in 'aeiouáéíóú']
print(f'Quantidade de vogais: {len(vogais)}', vogais)

#exemplo 4 (dois laços for para realizar a multiplicação das duas listas)
distributiva = [k * l for k in [2, 6, 9] for l in [3, 1, 7]]
print(distributiva)