 # Q.2) Write a Python program which accept an integer value ‘n’ and display all prime numbers 
# till ‘n’.
num=int(input("Enter your last number:"))
p=[]
for i in range(1,num+1):
    div=0
    for j in range(1,i+1):
        if(i%j==0):
            div+=1
    if div==2:
        p.append(i)
print(p) 