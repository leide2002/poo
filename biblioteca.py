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