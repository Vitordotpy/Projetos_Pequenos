# jogo de Terror
# Jogo de terror, respostas somente (Sim) ou (Não), resposta errada resulta em sua morte e no fim do jogo.

import random
import PySimpleGUI as sg

class Game:
    def __init__(self):
        self.itens_disponiveis = [
            'faca',
            'abajour',
            'tesoura',
            'lápis',
            'livro'
        ]
        self.pergunta1 = 'verificar barulho?'
        self.pergunta2 = 'aproximar-se?'
        self.pergunta3 = 'ligar lanterna?'
        self.pergunta4 = f'segurar {random.choice(self.itens_disponiveis)}?'
        self.pergunta5 = 'jogar no monstro?'
        self.pergunta6 = 'fugir ?'

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Button('Começar')],
            [sg.Output(size=(50,10),key='perguntas')],
            [sg.Input(size=(3,0),key='respostas')],
            [sg.Button('Responder')]
        ]
        # screen
        self.screen = sg.Window('Jogo de terror!', layout=layout)
        while True:
            # Data Receive
            self.DataRead()
            # todo
            if self.eventos == 'Começar':
                print(self.pergunta1)
                self.DataRead()
                if self.valores['respostas'] == 'Sim':
                    print('Você abre a porta e visualiza algo se mexendo no escuro...')
                    print(self.pergunta2)
                    self.DataRead()
                    if self.valores['respostas'] == 'Não':
                        print('Você mantém a distancia...')
                        print(self.pergunta3)
                        self.DataRead()
                        if self.valores['respostas'] == 'Sim':
                            print('Você liga a lantera e se depara com uma criatura assutadora, e então, tranca a porta rapidamente...')
                            print(self.pergunta4)
                            self.DataRead()
                            if self.valores['respostas'] == 'Sim':
                                print('Você segura firmemente o objeto, quando a criatura entra pela janela...')
                                print(self.pergunta5)
                                self.DataRead()
                                if self.valores['respostas'] == 'Sim':
                                    print('Você rapidamente joga e tonteia a criatura...')
                                    print(self.pergunta6)
                                    self.DataRead()
                                    if self.valores['respostas'] == 'Sim':
                                        print('Você foge de sua casa e vai até a delegacia, onde conta tudo, os policiais vão investidar a floresta e matam a criatura que foi encontrada ferida.')
                                    if self.valores['respostas'] == 'Não':
                                        print('Você decide ficar, mas a criatura se normaliza e parte pra cima de você...\n Você morreu.')
                                if self.valores['respostas'] == 'Não':
                                    print('A criatura te derruba e te devora \n Você morreu.')
                            if self.valores['respostas'] == 'Não':
                                print('A criatura entra pela janela, e você indefeso, morre.')
                        if self.valores['respostas'] == 'Não':
                            print('O vulto corre em sua direção rapidamente\n Você morreu.')
                    if self.valores['respostas'] == 'Sim':
                        print('O vulto corre em sua direção rapidamente\n Você morreu.')
                if self.valores['respostas'] == 'Não':
                    print('Algo entra pela janela rapidamente e vai em sua direção\n Você morreu.')

    def DataRead(self):
        self.eventos, self.valores = self.screen.Read()

jogo = Game()
jogo.Iniciar()
