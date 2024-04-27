# Q.1) Write a Python program to accept and convert string in uppercase or vice versa. 
def convert_case(string):
    converted_string = ""
    for char in string:
        if char.islower():
            converted_string += char.upper()
        elif char.isupper():
            converted_string += char.lower()
        else:
            converted_string += char
    return converted_string

# Example usage:
input_string = input("Enter a string: ")
converted_string = convert_case(input_string)
print("Converted string:", converted_string)
