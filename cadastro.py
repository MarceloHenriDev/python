print('Hello World!')
from PySimpleGUI import PySimpleGUI as sg

#layout

sg.theme('Reddit')
Layout =[
    [sg.Text('Usuário'), sg.Input(key='usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha',password_char='*',size=(20,1))],
    [sg.Checkbox('Salvar o login')],
    [sg.Button('Entrar')]
]
#janela
janela = sg.Window('Tela de login', Layout)
#ler eventos
while True:
    eventos, valores = janela.read()
    if eventos ==sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuario'] == 'marselo' and valores ['senha'] == '1234':
            print('el lobo cuida de su loba!')