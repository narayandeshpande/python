# Q.2) Write a program to display following pattern.
# 1 2 3 4 
# 1 2 3  
# 1 2   
# 1 
k=4
for i in range(1,5):
    for j in range(1,k+1):
        print(j,end=" ")
    k=k-1
    print("\n")

    