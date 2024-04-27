# Q.2) Write a Python program to accept n numbers in list. Find average of list and sort it in 
# descending order. 
l=[]
num=int(input("Enter length of list\n"))
for i in range(0,num):
    a=int(input("Enter your elemet\n"))
    l.append(a)
sum=0
for i in l:
    sum+=i
avg=sum/num

print("Avrage is ",avg)

print(sorted(l,reverse=True))
