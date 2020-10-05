import PySimpleGUI as sg

sg.theme('darkamber')
mainlayout = [
    [sg.Text('Bem vindo, Faça seu login')],
    [sg.Text('Email/Usuario:'), sg.InputText(key='--user--')],
    [sg.Text('Senha:'), sg.InputText(password_char='#', key='--password--')],
    [sg.Button('Entrar', change_submits=True)]

]


mainwindow = sg.Window('login', mainlayout)

while True:
    event, value = mainwindow.read()
    if event == sg.WINDOW_CLOSED:
        mainwindow.close()
        break

    user = value['--user--']
    password = value['--password--']
    if user == 'Lucasf' or user == 'email@gmail.com' and password == 1234:
        sg.popup('Você entrou')
    else:
        sg.popup('Dados incorretos')
