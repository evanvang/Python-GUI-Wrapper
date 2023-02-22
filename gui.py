import PySimpleGUI as sg

sg.theme('PythonPlus')

#stuff in window
layout = [  [sg.Text("GUI Trial Run!")],
            [sg.Text("Enter your file:"), sg.InputText()],
            [sg.Button('Run MP3 File'),sg.Button("Exit")]   ]

window = sg.Window('CUBE SOFTWARE', layout)

#makes stuff work 
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Exit":
        break
    print("You entered", values[0])

window.close()