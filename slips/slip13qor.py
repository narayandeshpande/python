#Q.2) Write a Python program to generate and print a dictionary that contains a number (between 
#1 and n) in the form (x, x*x). 
#Sample Dictionary (n = 5) 
# Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
num=int(input("Eenter you number"))
squ={}
for i in range(1,num+1):
    s=i*i
    squ[i]=s
print(squ)