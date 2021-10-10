import PySimpleGUIQt as sg
from converting import *
# link to different theme colors https://user-images.githubusercontent.com/46163555/70382042-796da500-1923-11ea-8432-80d08cd5f503.jpg
sg.theme('DarkBlue2')
layout = [[sg.Text('Welcome to the Morse Code Translator!')],
          [sg.Text('Input the word or sentence that you would like to be converted to morse code.\nPlease note that the space key will be replaced with the \"|" key'), sg.InputText()],
          [sg.OK(), sg.Cancel()]]
# Create the window
window = sg.Window("Morse Code Translator", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break

window.close()
