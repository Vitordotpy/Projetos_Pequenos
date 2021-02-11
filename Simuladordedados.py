# Simulador de dados
import random
import PySimpleGUI as sg

class SimuladordeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Gerar novo valor ?"

    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('Jogar o dado ?')],
            [sg.Button('Sim'),sg.Button('Não')]
        ]
        #criar interface
        self.interface = sg.Window('Simulador de Dado', layout=layout)
        #ler eventos e valores
        self.eventos, self.valores = self.interface.Read()
        #tratamento dos dados
        try:
            if self.eventos == "Sim":
                self.GerarValordoDado()
            elif self.eventos == "Não":
                print("Adeus!")
            else:
                print("digitar somente 'Sim' ou 'Não'")
        except:
            print("erro")

    def GerarValordoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
Simulador = SimuladordeDado()
Simulador.Iniciar()
