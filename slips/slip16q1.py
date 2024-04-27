#Q.1) Write a Python program to create tuple of n numbers, print the first half values of tuple in 
#one line and the last half values of tuple on next line. 
a=(10,20,30,40,50,60,70,80)
print("first half value is:\n")
for i in range(0,int(len(a)/2)):
    print(a[i])
print("last half value is:\n")
for i in range(int(len(a)/2),len(a)):
    print(a[i])