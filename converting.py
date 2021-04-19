import json


# function that will retrieve dictaniary value and then add it to the final_output
def conversion(user_input):
    # importing json file and loading it in memory as a python dictanaroy
    with open("morsecode.json", "r") as rf:
        decoded_data = json.load(rf)
    # breaking string into a list of characters

    # converting string to lower case since the dict is lowercase, no uppercase letters
    lower_cased = user_input.lower()
    character_list = list(lower_cased)
    length = len(character_list)
    i = 0

    # string that will represetn the final value
    final_output = ""

    # will run until all the characters are iterated over
    # sets the current index in the length (a letter) to a char variable which will then test if that character is
    # present in the dictanary made from the JSON file
    # Then, if it's present, the if statement will run. The program will get the value for that key and add it to
    # the final output variable
    # If the else runs, then that character is discarded
    while i < length:
        working_on = character_list[i]
        in_dict = working_on in character_list
        if in_dict:
            dict_value = decoded_data.get(working_on)
            final_output = final_output + dict_value
        else:
            working_on = " "
        i = i + 1
    print(final_output)
