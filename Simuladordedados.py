# Simulador de dados
import random
import PySimpleGui

class SimuladordeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Gerar novo valor ?"
        #layout
        self.layout = [
            [sg.Text('Jogar o dado ?')],
            [sg.Button('sim'),sg.Button('Não')]
        ]

    def Iniciar(self):
        #criar interface
        self.interface = sg.Window('Simulador de Dado', Layout=self.layout)
        #ler eventos e valores
        self.eventos, self.valores = self.interface.Read()
        #tratamento dos dados
        try:
            if self.eventos == "y":
                self.GerarValordoDado()
            elif self.eventos == "n":
                print("Adeus!")
            else:
                print("digitar 'y' ou 'n'")
        except:
            print("erro")

    def GerarValordoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
Simulador = SimuladordeDado()
Simulador.Iniciar()
