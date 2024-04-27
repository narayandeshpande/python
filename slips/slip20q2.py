# Q.2) Write a Python program to remove special symbols/Punctuation from a given string. 
str1="Narayan Deshpande!"
for i in str1:
    if(i=='!' or i=='?' or i=='$' or i=='*' or i==',' or i=='?' or i=='(' or i==')' or i=='{' or i=='}'):
        # print(i)
        str1=str1.replace(i,'')
print(str1)
