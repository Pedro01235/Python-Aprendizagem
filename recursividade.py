#recursividade 

# formula geral para o fatorial:
# fatorial (num) = 1, se num = 0 ou se num = 1 ('Caso base')
# fatorial (num) = num * fatorial (num - 1), se num > 1 ('Caso recursivo')
# 4! = 4 * fatorial(3) > 4 * 3 * factorial(2) > 4 * 3 * 2 * factorial(1) > 4 * 3 * 2 * 1 = 24) 
#4! = 4 * 3 * 2 * 1 = 24

#Fatorial recursivo (NÃO É OBRIGATORIO)
def fatorial (numero):
    if numero == 0 or numero == 1:
        return 1 
    else:
        return numero * fatorial(numero - 1)

if __name__ == '__main__':
    while True:
        x = int(input('Numero: '))
        try:
            res = fatorial(x)
        except RecursionError:
            print('Numero muito grande ou negativo')
        else:
            print('Fatorial:',res)
            break




