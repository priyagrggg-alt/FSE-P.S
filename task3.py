user_input = input("Enter a string with at least 8 characters: ")

if len(user_input) < 8:
    print("Please enter a string with at least 8 characters.")
else:

    ascii_values = [ord(char) for char in user_input]
    print("ASCII values of each character:", ascii_values)

    modified_string = ""

    for i, char in enumerate(user_input):

        if (i + 1) % 2 == 0:
            modified_char = chr(ord(char) - 32) if 'a' <= char <= 'z' else char
            modified_string += modified_char

        else:
            modified_string += char

    print("Final modified string:", modified_string)