 # Q.1) Write a Python program to accept the strings which contains all vowels. 
str1=input("Enter your string:\n")
if(('a' in str1 and 'e' in str1 and 'i' in str1 and 'o' in str1 and 'u' in str1 ) or('A' in str1 and 'E' in str1 and 'I' in str1 and 'O' in str1 and 'U' in str1 )):
    print("Accept")
else:
    print("Not accepted")