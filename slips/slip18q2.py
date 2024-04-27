# Q.2) Write a Python program to accept n elements in a set and find the length of a set, maximum, 
# minimum value and the sum of values in a set. (Don’t use built-in function) 
def max(a):
    b=list(a)
    maxnum=b[0]
    for i in a:
        if(maxnum>i):
            maxnum=i
    return maxnum

def min(a):
    b=list(a)
    minnum=b[0]
    for i in a:
        if(minnum<i):
            minnum=i
    return minnum

def length(a):
    len=0
    for i in a:
        len+=1
    return len

def sum(a):
    sum1=0
    for i in a:
        sum1+=i
    return sum1

a={1,2,3,4,5,6,7}
print("Max number is: ",max(a))
print("min number is: ",min(a))
print("length of set is: ",length(a))
print("sum of set is: ",sum(a))
