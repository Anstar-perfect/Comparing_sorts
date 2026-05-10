def intersection_array(a1,a2,m,n):
    for i in range(0,m):
        for j in range(0,n):
            if a1[i] == a2[j]:
                print(a1[i],end=' ')
a1=[]
a2=[]
m = int(input('Enter the number of values for the first array:'))
for k in range(m):
    value = int(input('Enter the integer values(one at a time):'))
    a1.append(value)
n = int(input('Enter the number of values for the second array:'))
for k in range(n):
    value = int(input('Enter the integer values(one at a time):'))
    a2.append(value)    
intersection_array(a1,a2,m,n)

