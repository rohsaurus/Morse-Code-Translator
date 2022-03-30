import PySimpleGUIQt as sg
from converting import conversion
import pyperclip as pc

# link to different theme colors https://user-images.githubusercontent.com/46163555/70382042-796da500-1923-11ea-8432-80d08cd5f503.jpg
sg.theme('DarkBlue2')
layout = [[sg.Text('Welcome to the Morse Code Translator!')],
          [sg.Text(
              'Input English text to be translated to Morse Code. Spaces will be replaced with the | key.'),
              sg.InputText(key='-IN-')],
         # [sg.Text('Input morse code that you want translated to English. Please space out words with the | key.'),
          # sg.InputText(key='-INPUT-')],
          [sg.Text(key='-OUTPUT-'), sg.Button('Copy')],
          [sg.Button('Translate'), sg.Button('Exit')],
          ]
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

    if event == 'Copy':
        pc.copy(y)
    # End program if user closes window or
    # presses the Exit button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()
