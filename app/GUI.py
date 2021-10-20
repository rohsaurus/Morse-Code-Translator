import PySimpleGUIQt as sg
from converting import *

# link to different theme colors https://user-images.githubusercontent.com/46163555/70382042-796da500-1923-11ea-8432-80d08cd5f503.jpg
sg.theme('DarkBlue2')
layout = [[sg.Text('Welcome to the Morse Code Translator!')],
          [sg.Text(
              'Input the word or sentence that you would like to be converted to morse code.\nPlease note that the space key will be replaced with the \"|" key'),
              sg.InputText(key='-IN-')],
          [sg.Text(key='-OUTPUT-')],
          [sg.Button('Translate'), sg.Button('Exit')]]
# Create the window
window = sg.Window("Morse Code Translator", layout)

# Create an event loop
while True:
    event, values = window.read()
    x = values['-IN-']
    y = conversion(x)

    if event in (None, 'Exit'):
        break

    # if user presses "translate"
    if event == 'Translate':
        window['-OUTPUT-'].update(y)
    # End program if user closes window or
    # presses the OK button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()
