#Escopo de variáveis (GLOBAL e LOCAL)

#global pode ser usado para variáveis globais
#local pode ser usado para variáveis locais

#Exemplo:

x = 10
def funcao():
    y = 20
    print(x)
    print(y)
funcao()

# Em Python, as variáveis podem ser **locais** ou **globais**, dependendo de onde elas são declaradas e onde podem ser acessadas.

### 1. **Variáveis Globais**:
# Uma variável é **global** quando é declarada fora de qualquer função e pode ser acessada em qualquer lugar do código, inclusive dentro de funções (a menos que seja sobrescrita).

# Variável global
x = 10

def minha_funcao():
    print(x)  # Acessa a variável global

minha_funcao()  # Saída: 10
print(x)  # Saída: 10

### 2. **Variáveis Locais**:
# Uma variável é **local** quando é declarada dentro de uma função. Ela só pode ser acessada dentro dessa função, não fora dela.

def minha_funcao():
    y = 5  # Variável local
    print(y)

minha_funcao()  # Saída: 5
# print(y)  # Erro: NameError, 'y' não é definida fora da função

### 3. **Modificando variáveis globais dentro de uma função**:
# Se você quiser modificar uma variável global dentro de uma função, você precisa usar a palavra-chave `global`.

x = 10  # Variável global

def minha_funcao():
    global x  # Referencia a variável global
    x = 20  # Modifica a variável global

minha_funcao()
print(x)  # Saída: 20

### 4. **Funções com variáveis locais e globais**:
    # É possível ter uma variável local com o mesmo nome de uma variável global. Nesse caso, a variável local "sombra" a global dentro do escopo da função.
x = 10  # Variável global

def minha_funcao():
    x = 5  # Variável local, não afeta a global
    print(x)  # Saída: 5

minha_funcao()
print(x)  # Saída: 10 (a variável global não foi alterada)

### Resumo:
# - **Variáveis globais** são acessíveis em qualquer parte do código.
# - **Variáveis locais** são acessíveis apenas dentro da função onde foram criadas.
# - Para modificar uma variável global dentro de uma função, use `global`.