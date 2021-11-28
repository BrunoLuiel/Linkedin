from tkinter.constants import COMMAND
from validate_email import validate_email
import PySimpleGUI as sg
from Linkedin import Linkedin_bot
import os

class Tela_Login:
    def __init__(self):
        sg.change_look_and_feel('DarkPurple')
        layout = [
            [sg.Text('Login', size=(30,1)), sg.Input(size=(30,1), key='login')],
            [sg.Text('Senha', size=(30,1)), sg.Input(size=(30,1), key='senha', password_char='*')],
            [sg.Text('Palavra-chave', size=(30,1)), sg.Input(size=(30,1), key='p_chave')],
            [sg.Text('Deixe sua mensagem personalizada abaixo')],
            [sg.Text('Continue a frase: "Olá (nome da pessoa), tudo bem? "'), sg.Input(size=(100,50), key=('texto'))],
            [sg.Text('Exemplo: "Meu nome é Bruno, sou Contador e estou Bacharelando Engenharia de Software, ficaria muito feliz que fizesse parte do meu network. Desde já, sucesso!"')],
            [sg.Button('Iniciar')]
        ]

        self.janela = sg.Window('Dados para Login').layout(layout)

    def Iniciar(self):
        while True:
            try:
                eventos, valores = self.janela.Read()
                user = self.janela['login'].get()
                p_chave = self.janela['p_chave'].get()
                password = self.janela['senha'].get()
                mensagem = self.janela['texto'].get()

                if eventos == 'Iniciar':
                    if validate_email(user) == True and len(password) > 8 and len(p_chave) > 2:
                        run = Linkedin_bot(user, password)
                        run.login()
                        run.pesquisa(p_chave)
                        run.cria_conexoes(mensagem)
                    elif user == '':
                        sg.popup('Insira seu email!')
                    elif validate_email(user) == False:
                        sg.popup('Email Inválido!\nTente novamente.')
                    elif password == '':
                        sg.popup('Insira sua senha!\nA senha do Linkedin.')
                    elif len(password) < 3:
                        sg.popup('Senha inválida!\nTente novamente.')
                    elif p_chave == '':
                        sg.popup('Insira a Palavra-chave!\nA palavra chave pode ser por exemplo nome, profissão ou empresa a ser buscada, além de outros, claro :)!')
                    else:
                        pass

            except:
                sg.popup('Ocorreu um erro inesperado!\nTente novamente.')
                
            if eventos == sg.WINDOW_CLOSED:
                break
            
if __name__ == '__main__':
    tela = Tela_Login()
    tela.Iniciar()
