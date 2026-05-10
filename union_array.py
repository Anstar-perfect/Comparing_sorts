def union_array(a1,a2,m,n):
    i,j = 0,0
    while i<m and j<n :
        if a1[i]<a2[j]:
            print(a1[i],end = ' ')
            i+=1
        if a2[j]<a1[i]:
            print(a2[j],end=' ')
            j+=1
        else:
            print(a2[j],end=' ')
            i+=1
            j+=1
    while i<m :
        print(a1[i],end= ' ')
        i+=1
    while j<n:
        print(a2[j],end=' ')
        j+=1

a1 = [32,13,9,22]
a2 = [13,67,0,22]
m=len(a1)
n=len(a2)
union_array(a1,a2,m,n)