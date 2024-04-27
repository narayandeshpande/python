#  Q.2) Write a Python program to create a dictionary from a string. 
# Sample String: ’Hello all’ 
# Expected output: {'e': 1, 'o': 1, 'a': 1, 'l': 4, 'H': 1} 
a="hello all"
dic={}
for i in a:
    count=0
    for j in a:
        if(i==j):
            count+=1
    dic[i]=count
print(dic)