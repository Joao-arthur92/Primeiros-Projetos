from random import randint
import PySimpleGUI as sg


class ChuteumNumero:
    def __init__(self):
        sg.change_look_and_feel('DarkRed1')
        self.valor_aleatorio = 0
        self.tentar_novamente = True

    def iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu chute', size=(35, 0))],
            [sg.Button('Chutar!')],
            [sg.Input(size=(18,0), key='ValorChute')],
            [sg.Output(size=(30,10))],
            [sg.Button('Sair')]
        ]
        # Criar Janela
        self.janela = sg.Window('Chute um número entre 1 e 100!', layout=layout)
        # Gerar o valor
        self.gerar_valor_aleatorio()
        try:
            while True:
                # Receber valores
                self.evento, self.valores = self.janela.Read()
                if self.evento == 'Sair':
                    break
                elif self.evento == 'Chutar!':
                    while self.tentar_novamente == True:
                        if self.valor_aleatorio > int(self.valores['ValorChute']):
                            print('Chute um número maior.')
                            break
                        elif self.valor_aleatorio < int(self.valores['ValorChute']):
                            print('Chute um número menor.')
                            break
                        elif self.valor_aleatorio == int(self.valores['ValorChute']):
                            print('Você acertou!!!')
                            self.tentar_novamente = False
                            break
        except:
            print('Digite um número!')
            self.eventos, self.valores = self.janela.Read()

    def gerar_valor_aleatorio(self):
        self.valor_aleatorio = randint(1, 100)


chute = ChuteumNumero()
chute.iniciar()
