from random import randint
import PySimpleGUI as sg


class SimuladorDeDado:
    def __init__(self):
        sg.change_look_and_feel('DarkRed1')
        # Layout
        self.layout = [
            [sg.Text('Jogar o dado?')],
            [sg.Button('Sim'), sg.Button('Não')]
        ]
        self.tentar_novamente = True

    def iniciar(self):
        # Criar janela
        self.janela = sg.Window('Simulador De Dado', layout=self.layout)
        # Ler os valores da tela
        try:
            while self.tentar_novamente == True:
                self.eventos, self.valores = self.janela.Read()
                if self.eventos == 'Sim':
                    self.gerarvalordodado()
                elif self.eventos == 'Não':
                    self.tentar_novamente = False
                    print('Programa finalizado.')
                else:
                    self.tentar_novamente = False
                    print('Favor digitar Sim ou Não ')
        except ValueError:
            print('Ocorreu um erro ao receber sua resposta')

    def gerarvalordodado(self):
        print(randint(1, 6))
        self.janela.Read()


simulador = SimuladorDeDado()
simulador.iniciar()


