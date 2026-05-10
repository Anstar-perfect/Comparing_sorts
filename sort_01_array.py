def sort_01_array(a,n):
    count = 0
    for i in range(n):
        if a[i]==0:
            count+=1

    for i in range(count):
        a[i]= 0 
    for i in range(count,n):
        a[i] = 1

a = [1,1,0,1,0,1,0,1,1,0,0]
sort_01_array(a,len(a))
print('Sorted Array is ',end='')
for i in range(len(a)):
    print(a[i],end = ' ')
