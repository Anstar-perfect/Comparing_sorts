def intersection(a1,a2,m,n):
    for i in range(0,m):
        for j in range(0,n):
            if a1[i]==a2[j]:
                print(a1[i],end=' ')

a1 = [1,3,5,7]
a2 = [2,3,5,9]
m = len(a1)
n = len(a2)
intersection(a1,a2,m,n)