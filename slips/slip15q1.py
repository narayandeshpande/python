 # Q.1) Write a python program to check if a string is a Palindrome or not. 
str1=input("Enter your strimg:")
str2=str1[::-1]
if str1==str2:
    print("Yes")
else:
    print("No")