# Orientação a Objetos (POO): Paradigmas de programação, multiparadigma

# Classes e objetos (atributos e métodos)
# atributo = valor
# metodo = função
# encapsulamento

# Vamos tratar sobre conceitos muito importante da Programação Orientada a Objetos que todo programador Python DEVE dominar:

    # Classes;
    # Objetos;
    # Herança;
    # Polimorfismo;
    # Encapsulamento e muito mais!

# Programação Orientada a Objetos: Introdução

# A Programação Orientada a Objetos (POO) é ​​um paradigma de programação baseado no conceito de Classes e Objetos.
# Classes podem conter dados e código:

    #Dados na forma de campos (também chamamos de atributos ou propriedades); e
    #Código, na forma de procedimentos (frequentemente conhecido como métodos).

# Uma importante característica dos objetos é que seus próprios métodos podem acessar e frequentemente modificar seus campos de dados: objetos mantém uma referência para si mesmo, o atributo self no Python.
# Na POO, os programas são projetados a partir de objetos que interagem uns com os outros.
# Esse paradigma se concentra nos objetos que os desenvolvedores desejam manipular, ao invés da lógica necessária para manipulá-los.
# Essa abordagem de programação é adequada para programas grandes, complexos e ativamente atualizados ou mantidos.


# Classes, Objetos, Métodos e Atributos

# Esses conceitos são os pilares da Programação Orientada a Objetos então é muito importante que você os DOMINE:


    # As Classes são tipos de dados definidos pelo desenvolvedor que atuam como um modelo para objetos. Pra não esquecer mais: Classes são fôrmas de bolo e bolos são objetos 
    # Objetos são instâncias de uma Classe. Objetos podem modelar entidades do mundo real (Carro, Pessoa, Usuário) ou entidades abstratas (Temperatura, Umidade, Medição, Configuração).
    # Métodos são funções definidas dentro de uma classe que descreve os comportamentos de um objeto. Em Python, o primeiro parâmetro dos métodos é sempre uma referência ao próprio objeto.
    # Os Atributos são definidos na Classe e representam o estado de um objeto. Os objetos terão dados armazenados nos campos de atributos. Também existe o conceito de atributos de classe, mas veremos isso mais pra frente.


# Princípios Básicos de POO
# A programação orientada a objetos é baseada nos seguintes princípios:

# Encapsulamento
# Abstração
# Herança
# Polimorfismo




#Criando uma CLASSE

# Vamos criar uma classe que representa uma entidade do tipo Pessoa!
# Ela deve ter os seguintes campos:

    #Nome como String;
    #Idade como Inteiro;
    #Altura como Decimal.

#Também deve ter métodos para:

    #Dizer “Olá”;
    #Cozinhar;
    #Andar.

# Utilizando POO e Python, podemos modelar a entidade Pessoa da seguinte forma:

# Temos a definição da Classe na primeira linha com class Pessoa. Isso diz ao Python que vamos criar a definição de uma nova classe.
class Pessoa:
    # Em seguida, temos o método __init__. Ele é muito importante e é chamado de Construtor. Ele é chamado ao se instanciar objetos e é nele que geralmente setamos os atributos do objeto.
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

# Em seguida temos a definição dos métodos dizer_ola(), cozinhar() e andar().
    def dizer_ola(self):
        print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} '
              f'anos e minha altura é {self.altura}m.')

    def cozinhar(self, receita: str):
        print(f'Estou cozinhando um(a): {receita}')

    def andar(self, distancia: float):
        print(f'Saí para andar. Volto quando completar {distancia} metros')

# Perceba que no método dizer_ola() referenciamos os atributos do próprio objeto com o argumento self: self.nome, self.idade e self.altura.
# Agora veja como podemos instanciar e interagir com objetos dessa Classe:

# Instancia um objeto da Classe "Pessoa"
pessoa = Pessoa(nome='João', idade=25, altura=1.88)

# Chama os métodos de "Pessoa"
pessoa.dizer_ola()
pessoa.cozinhar('Spaghetti')
pessoa.andar(750.5)
















# Exemplo 1

class Veiculo:
    def movimentar(self):
        print(f'Sou um veiculo que se move')

    def __init__(self, fabricante, modelo):
        self.__fabricante = fabricante
        self.__modelo = modelo
        self.__num_registro = None

    # Setter - permite alterar o atributo privado
    def set_num_registro(self, registro):
        self.__num_registro = registro

    # Getter - permite acessar o atributo privado
    def get_fabr_modelo(self):
        print(f'Veiculo: {self.__fabricante}, Modelo: {self.__modelo} \n')

    def get_num_registro(self):
        return self.__num_registro


# Herança = uma classe herda os atributos e métodos de outra
class Carro(Veiculo):
    # Método __init será heradado de Veiculo
    def movimentar(self):
        print(f'Sou um carro e ando pelas ruas')

class Aviao(Veiculo):
    def movimentar(self):
        print(f'Sou um avião e ando pelo ar')

class Moto(Veiculo):
    def movimentar(self):
        print(f'Sou uma moto e posso correr')

class Bicicleta(Veiculo):
    def __init__(self, fabricante, modelo, categoria):
        self.__cat = categoria
        super().__init__(fabricante, modelo)

    def get_categoria(self):
        return self.__cat

if __name__ == '__main__':
    meu_veiculo = Veiculo('Ford', 'F-150')
    meu_veiculo.movimentar()
    meu_veiculo.get_fabr_modelo()
    meu_veiculo.set_num_registro('509653-12')
    print(f'Registro: {meu_veiculo.get_num_registro()} \n')

    meu_carro = Carro('Toyota', 'Corolla')
    meu_carro.movimentar()
    meu_carro.get_fabr_modelo()

    seu_carro = Carro('Honda', 'Civic')
    seu_carro.movimentar()
    seu_carro.get_fabr_modelo()

    meu_aviao = Aviao('Boeing', '747')
    meu_aviao.movimentar()
    meu_aviao.get_fabr_modelo()

    minha_moto = Moto('Yamaha', 'YBR')
    minha_moto.movimentar()
    minha_moto.get_fabr_modelo()

    minha_bicicleta = Bicicleta('Bike', 'Caloi', 'Mountain')
    minha_bicicleta.movimentar()
    minha_bicicleta.get_categoria()


