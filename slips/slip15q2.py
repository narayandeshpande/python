# Q.2) Write a Sequential search function which searches an item in a sorted list. The function 
# should return the index of element to be searched in the list. 
def search(a,num):
    for i in range(0,len(a)):
        if(a[i]==num):
            return i
    return -1
a=[1,22,3,4,5,6,7,8,9]
num=int(input("Enter your number"))
print(search(a,num))
