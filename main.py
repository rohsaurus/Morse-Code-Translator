# importing method from converting file
from converting import *

# grabbing user input to run the method that will convert
user_input = input("Enter in a sentence that you would like converted into morse code.\nPlease note that entering a "
                   "space will cause in a replacement with the | character. Also note that the backward slash(\) will "
                   "cause the program to break so please refrain from using it.")

# running the function that will convert to morse code and print it out
conversion(user_input)
