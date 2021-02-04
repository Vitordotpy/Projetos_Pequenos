# Simulador de dados
import random

class SimuladordeDado:
    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = "Gerar novo valor ?"

    def Iniciar(self):
        resposta = input(self.mensagem)
        if resposta == "y":
            self.GerarValordoDado()
        elif resposta == "n":
            print("Adeus!")
        else:
            print("digitar 'y' ou 'n'")

    def GerarValordoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))
Simulador = SimuladordeDado()
Simulador.Iniciar()
