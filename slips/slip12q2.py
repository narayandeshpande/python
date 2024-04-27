 # Q.2) Write a Python program to accept string and remove the characters which have odd index 
# values of a given string using user defined function.
def remove_odd_index_chars(input_str):
    return input_str[::2]

# Accepting input string from the user
input_string = input("Enter a string: ")

# Removing characters with odd indices
result_string = remove_odd_index_chars(input_string)

# Printing the result
print("String after removing characters with odd indices:", result_string)
