# importing built in python libary for reading json
import json


# function that will retrieve dictionary value and then add it to the final_output
def englishToMorse(user_input):
    # importing json file and loading it in memory as a python dictionary
    with open("morsecode.json", "r") as rf:
        decoded_data = json.load(rf)

    # breaking string into a list of characters

    # converting string to lower case since the dict is lowercase, no uppercase letters
    lower_cased = user_input.lower()
    character_list = list(lower_cased)
    length = len(character_list)
    i = 0

    # string that will represents the final value
    final_output = ""

    # will run until all the characters are iterated over
    # sets the current index in the length (a letter) to a char variable which will then test if that character is
    # present in the dictionary made from the JSON file
    # Then, if it's present, the if statement will run. The program will get the value for that key and add it to
    # the final output variable
    # If the else runs, then that character is discarded

    while i < length:
        try:
            working_on = character_list[i]
            in_dict = working_on in character_list
            if in_dict:
                dict_value = decoded_data.get(working_on)
                # adding space because after every character there is a space
                final_output = final_output + dict_value + " "
            # else statement is run if a value such as a space is detected that's not in the JSON
            else:
                final_output = final_output + "|"
            i = i + 1
        except BaseException:
            i = i + 1
    return final_output


def morseToEnglish(user_input):
    # importing json file and loading it in memory as a python dictionary
    with open("morsecode.json", "r") as rf:
        decoded_data = json.load(rf)

    # breaking string into a list of characters
    # converting string to lower case since the dict is lowercase, no uppercase letters
    lower_cased = user_input.lower()
    character_list = list(lower_cased)
    length = len(character_list)
    i = 0

    # string that will represent the final value
    final_output = ""

    # will run until all the characters are iterated over
    # sets the current index in the length (a letter) to a char variable which will then test if that character is
    # present in the dictionary made from the JSON file
    # Then, if it's present, the if statement will run. The program will get the value for that key and add it to
    # the final output variable
    # If the else runs, then that character is discarded

    while i < length:
        try:
            working_on = character_list[i]
            in_dict = working_on in character_list
            if in_dict:
                dict_value = decoded_data.get(working_on)
                # adding space because after every character there is a space
                final_output = final_output + dict_value + " "
            # else statement is run if a value such as a space is detected that's not in the JSON
            else:
                final_output = final_output + "|"
            i = i + 1
        except BaseException:
            i = i + 1
    return final_output


def decrypt(message):
    # loading json file as a dictonary
    with open("morseToEnglish.json", "r") as rf:
        decoded_data = json.load(rf)

    # extra space added at the end to access the
    # last morse code
    message += ' '

    decipher = ''
    citext = ''
    for letter in message:

        # checks for space
        if (letter != ' '):

            # counter to keep track of space
            i = 0

            # storing morse code of a single character
            citext += letter

        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1

            # if i = 2 that indicates a new word
            if i == 2:

                # adding space to separate words
                decipher += ' '
            else:
                # accessing the keys using their values
                decipher += list(decoded_data.keys())[list(decoded_data.values()).index(citext)]
                citext = ''

    return decipher
