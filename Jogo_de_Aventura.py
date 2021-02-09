# jogo de aventura
# a historia caminha de acordo com suas escolhas
import random

class Game:
    def __init__(self):
        self.itens_disponiveis = [
            'faca',
            'abajour',
            'tesoura',
            'lápis',
            'livro'
        ]
        self.pergunta1 = 'verificar barulho?\n'
        self.pergunta2 = 'aproximar-se?\n'
        self.pergunta3 = 'ligar lanterna?\n'
        self.pergunta4 = f'segurar {random.choice(self.itens_disponiveis)}?\n'
        self.pergunta5 = 'jogar no monstro?\n'
        self.pergunta6 = 'fugir ?\n'

    def Iniciar(self):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'Sim':
            print('Você abre a porta e visualiza algo se mexendo no escuro...')
            resposta1B = input(self.pergunta2)
            if resposta1B == 'Não':
                print('Você mantém a distancia...')
                resposta1C = input(self.pergunta3)
                if resposta1C == 'Sim':
                    print('Você liga a lantera e se depara com uma criatura assutadora, e então, tranca a porta rapidamente...')
                    resposta1D = input(self.pergunta4)
                    if resposta1D == 'Sim':
                        print('Você segura firmemente o objeto, quando a criatura entra pela janela...')
                        resposta1E = input(self.pergunta5)
                        if resposta1E == 'Sim':
                            print('Você rapidamente joga e tonteia a criatura...')
                            resposta1F = input(self.pergunta6)
                            if resposta1F == 'Sim':
                                print('Você foge de sua casa e vai até a delegacia, onde conta tudo, os policiais vão investidar a floresta e matam a criatura que foi encontrada ferida.')
                            if resposta1F == 'Não':
                                print('Você decide ficar, mas a criatura se normaliza e parte pra cima de você...\n Você morreu.')
                        if resposta1E == 'Não':
                            print('A criatura te derruba e te devora \n Você morreu.')
                    if resposta1D == 'Não':
                        print('A criatura entra pela janela, e você indefeso, morre.')
                if resposta1C == 'Não':
                    print('O vulto corre em sua direção rapidamente\n Você morreu.')
            if resposta1B == 'Sim':
                print('O vulto corre em sua direção rapidamente\n Você morreu.')
        if resposta1 == 'Não':
            print('Algo entra pela janela rapidamente e vai em sua direção\n Você morreu.')
jogo = Game()
jogo.Iniciar()
