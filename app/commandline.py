# importing method from converting file
from converting import *



# running the function that will convert to morse code and print it out
# while true loop to give the user the option to run the program again
while True:
# grabbing user input to run the method that will convert to Morse Code
    user_input = input("Enter in a sentence that you would like converted into morse code.\nPlease note that entering a "
                   "space will cause in a replacement with the | character. Also note that the backward slash(\) will "
                   "cause the program to break so please refrain from using it.")
    final_output = conversion(user_input)
    print(final_output)
    user_choice = input("Would you like to run the program again?\n")
    if user_choice == "no":
        break
