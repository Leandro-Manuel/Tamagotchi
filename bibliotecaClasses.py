class Tamagotchi:
    def __init__(self,nome,peso,idade):
        self.nome = nome
        self.idade = idade
        self.peso = peso

        self.comendo = False
        self.falando = False
        self.dormindo = True
        self.acordado = False


    def brincar(self):
        if self.dormindo == True:
            print(f'{self.nome} está dormindo, acorde-o primeiro.')

        elif self.comendo == False:
            print(f'{self.nome} está com fome. Alimente-o primeiro.')

        else:
            print(f'{self.nome} foi brincar.')


    def falar(self):
        if self.falando == True:
            print(f'{self.nome} já disse o que quis fazer.')
        else:
            print(f'{self.nome} falou que quer brincar.')
            self.falando = True
    def pararFalar(self):
        if self.falando == True:
            print(f'{self.nome} parou de falar.')
            self.falando = False
        else:
            print(f'{self.nome} não falou.')

    def comer(self,comida):
        if self.comendo == True:
            print(f'{self.nome} está comendo.')
        else:
            print(f'{self.nome} foi comer {comida}.')
            self.comendo = True

    def pararComer(self):
        if self.comendo == True:
            print(f'{self.nome} parou de comer.')
            self.comendo = False
        else:
            print(f'{self.nome} não estava comendo.')

    def dormir(self):
        if self.dormindo == True:
            print(f'{self.nome} já está dormindo.')
        else:
            print(f'{self.nome} foi dormir.')
            self.dormindo = True


    def acordar(self):
        if self.acordado == True:
            print(f'{self.nome} está acordado.')
        else:
            print(f'{self.nome} acordou.')
            self.dormindo = False