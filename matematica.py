#Função builtin 

valores = [2, 5, 6 ,-1 ,0 ,11 ,3 ,7 ,-6]
print('valor mais alto', max(valores))
print('valor mais baixo', min(valores))

a = -5 
b = 4 
print('Retorna o valor absoluto de um número: ', abs(a))
print('potenciação', pow(a, b))
c = 2.879864
d = 2.2654
print('arrendondamento', round(c,1))
print('arrendondamento', round(d, 2))

import math
print('PI: ', round(math.pi, 2))

x = 8 
y = 100
raiz = math.sqrt(x)
print('Raiz quadrada de', x, 'é:', round(raiz, 1))
raiz = math.sqrt(y)
print('Raiz quadrada de', y, 'é: ', raiz) 

logaritmo = math.log10(y)
print('logaritmo: ',logaritmo)

print(math.factorial(5))
print(x / math.inf)