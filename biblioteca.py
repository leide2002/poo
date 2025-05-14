class Pessoa():
    def __init__(self,nome,idade,peso):
        self.nome=nome
        self.peso=peso
        self.idade=idade
    def apresentar(self):
        print(f"ola meu nome e {self.nome}, e tenho{self.idade} anos e peso{self.peso} quilo")

    def dormindo(self):
        self.dormindo = True
        print(f"{self.nome} foi dormir.")

    def acordar(self):
        self.dormindo = False
        print(f"{self.nome} acordou.")

    def comer(self):
        if self.dormindo:
            print(f"{self.nome} está dormindo e não pode comer!")
        else:
            print(f"{self.nome} está comendo. Hmmm!")

class Animal():
            def __init__(self,nome,cor):
                self.nome=nome
                self.cor=cor
            def comer(self):
                print(f"o {self.nome} foi comer")
class Gato(Animal):
            def __init__(self,nome,cor):
                super().__init__(nome,cor)

            def miar (self):
                print(f"o {self.nome} esta miando...")
class Cachorro(Animal):
     def __init__(self,nome,cor):
         super().__init__(nome,cor)

     def latir(self):
         print(f"{self.nome}, esta latindo auau")

class Coelho (Animal):
    def __init__(self,nome,cor):
         super().__init__(nome,cor)

    def grunir(self):
        print(f"{self.nome}, esta grunindo.")
class Vaca (Animal):
    def __init__(self, nome, cor):
        super().__init__(nome,cor)
    def mujir(self):
        print(f"{self.nome} esta mujindo muuuu.")

class Ingresso ():
    def __init__(self, valor): #metodo construtor que vai receber o valor
        self.valor=valor
    def imprimirValor(self):
        print(f"o valor do ingresso e, {self.valor} ")

class Vip (Ingresso):
    def __init__(self, valor):
        super().__init__(valor*1.5)
    def impimeValor(self):
        print(f"O valor do ingresso é R$ {self.valor:.2}")
class Forma():
    def __init__(self):
        self.area=0
        self.perimetro=0

class Triangulo(Forma):
    def __init__(self, altura, base):
        self.base=base
        self.altura=altura

    def calcularArea(self):

        print(f"o valor da area e {self.area}")

        super().calcularArea(self.perimetro*3)
    def calcularPerimetro(self):



