import PySimpleGUIQt as sg

layout = [[sg.Text("Hello and welcome to the Morse Code Translator!")], [sg.Button("OK")]]

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