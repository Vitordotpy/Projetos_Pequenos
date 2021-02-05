#chute o numero
import random

class ChuteoNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar_novamente == True:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print('Chute um valor mais baixo')
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Chute um valor mais alto')
                    self.PedirValorAleatorio()
                if int(self.valor_do_chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print('Parabens!')
        except:
            print('Apenas digite números entre 1 e 100')
            self.Iniciar()1
    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um numero')

    def GerarNumeroALeatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteoNumero()
chute.Iniciar()
