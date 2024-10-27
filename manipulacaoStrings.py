#manipulacao de strings
nome = 'PEDRO'
letra = nome[2]
print('Letra: ', letra)
print('Tamanho: ', len(nome))

#concatenar
nome = 'Curso de Python'
instrutor = 'Pedrinho'
print(nome + ' ' + instrutor)

#split, criando uma lista de palavras(Strings)
frase = 'Vamos aprender Python hoje'
palavra = frase.split()
print(palavra)
print(palavra[1])
for letra in palavra:
    print(letra)    
for letra in frase:
    print(letra)

#slice
frase = 'Vamos aprender Python hoje'
print(frase[0:5])
print(frase[6:15])

#email 
email = '7KwC6@example.com'
print(email.find('@'))
print(email.split('@'))

#Verificar se uma palavra está contida em uma string ou não
produtos = 'iphone,ipad,imac'   
print('iphone' in produtos)
print('samsung' not in produtos)

#posicao
item = 'ipad'
pos = item.find('pda') #quando retornar -1, não foi encontrado
print(pos)
pos = item.find('pad')
print(pos)

#maiusculas, minusculas e Titulo
objeto1 = 'celular'
print(objeto1.upper())
objeto2 = 'CARRO'
print(objeto2.lower())
titulo = 'Curso de python'
print(titulo.title())

#remover espacos e substituir por outros
frase = '   Vamos aprender Python hoje   '
print(frase.strip())
suplemento = 'Hipercalorico de Uva' 
print(suplemento.replace('Uva', 'Laranja'))

#alinhamento de texto (BOM PARA MENUS)
fruta = 'maca'
print(fruta.rjust(20, '-'))
print(fruta.ljust(20, '-'))
print(fruta.center(20, ' '))


# Termina com algum caractere e começa com algum caractere
p = 'Bom dia, Pedro'
print(p.startswith('B'))
print(p.startswith('b'))
print(p.endswith('o'))
print(p.endswith('O'))

#docString
