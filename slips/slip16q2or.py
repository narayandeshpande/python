# Q.2) Write a Python program to check if a given key already exists in a dictionary. If key exists 
# replace with another key/value pair. 
dicti={'a':1,'b':2,'c':3,'d':4,'e':5}
fkey=input("Enter key to find\n")

if fkey in dicti:
    nkey=input("Enter new key to replace\n")
    nvalue=input("Enter new value\n")
    dicti[nkey]=nvalue
    del dicti[fkey]
print(dicti)
