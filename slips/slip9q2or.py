 # Q.2) Write a Python program to count the occurrences of each word in a given sentence. 
a="hello my name is narayan narayan"
b=a.split()
# print(b)
dic={}
for i in b:
    count=0
    for j in b:
        if(i==j):
            count+=1
    dic[i]=count
print(dic)