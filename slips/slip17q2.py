# Q.2) Write a Python program to display the following pattern (Floyd's triangle) 
# For n=3 
# 1 
# 2 3 
# 4 5 6 
num=1
for i in range(1,4):
    for j in range(1,i+1):
        print(num,end=" ")
        num+=1
    print("\n")