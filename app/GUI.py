import PySimpleGUIQt as sg
import pyperclip as pc

from converting import englishToMorse, decrypt

# link to different theme colors https://user-images.githubusercontent.com/46163555/70382042-796da500-1923-11ea-8432-80d08cd5f503.jpg
sg.theme('DarkBlue2')
layout = [[sg.Text('Welcome to the Morse Code Translator!')],
          [sg.Text(
              'Input English text to be translated to Morse Code. Spaces will be replaced with the | key.'),
              sg.InputText(key='-IN-')],
          [sg.Text(key='-OUTPUT-')], [sg.Button('Translate'), sg.Button('Copy')],
    [sg.Button('Exit')]]
     #     [sg.Text('Input morse code that you want translated to English. Please have a space between each.'), sg.InputText(key='-INPUT-')],
      #    [sg.Text(key='-EnglishOutput-')],
       #   [sg.Button('Translate'), sg.Button('Exit')]]
# Create the window
window = sg.Window("Morse Code Translator", layout)

# Create an event loop
while True:
    event, values = window.read()
    x = values['-IN-']
    y = ""
    if x:
        y = englishToMorse(x)
   # z = values['-INPUT-']
   # abc = ""
   # if z:
    #    abc = decrypt(z)


    if event in (None, 'Exit'):
        break

    # if user presses "translate"
    if event == 'Translate':
        if x:
            window['-OUTPUT-'].update(y)
      #  if z:
       #     window['-EnglishOutput'].update(abc)

    # if user clicks Copy
    if event == 'Copy':
        pc.copy(y)
    # End program if user closes window or
    # presses the Exit button
    if event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()
