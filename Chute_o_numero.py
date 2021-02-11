#chute o numero
import random
import PySimpleGUI as sg

class ChuteoNumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True

    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('Chute um número', size=(20,0))],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(20,10))]
        ]
        #screen
        self.screen = sg.Window('Chute o número!', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                #data receive
                self.evento, self.valores = self.screen.Read()
                #todo
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valroes['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print('Chute um valor mais baixo')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print('Chute um valor mais alto')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Parabens!')
                            break
        except:
            print('Apenas digite números entre 1 e 100')
            self.Iniciar()

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um numero')

    def GerarNumeroALeatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

chute = ChuteoNumero()
chute.Iniciar()
