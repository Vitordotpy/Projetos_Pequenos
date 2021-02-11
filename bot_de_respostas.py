#bot de repostas
#faça uma pergunta e receba uma respota
import random
import PySimpleGUI as sg

class Bot:
    def __init__(self):
        self.respostas = [
            'Você com certeza deve fazer isso!',
            'Você que sabe...',
            'Não faz isso!',
            'Então é isto!'
        ]

    def Iniciar(self):
        #layout
        layout = [
            [sg.Text('Faça uma pergunta', size=(15,0))],
            [sg.Input()],
            [sg.Button('Perguntar', size=(15,0))],
            [sg.Output(size=(20,10))]

        ]
        #screen
        self.screen = sg.Window('Bot', layout=layout)
        while True:
            #data receive
            self.eventos, self.valores = self.screen.Read()
            #todo
            if self.eventos == 'Perguntar':
                print(random.choice(self.respostas))

decisao = Bot()
decisao.Iniciar()
