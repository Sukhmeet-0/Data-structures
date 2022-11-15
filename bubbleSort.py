a=[2,4,5,5,4,32,20,3,3,392,0,38,1,9,59,99,23]
for i in range(0,len(a)):
    for j in range(1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)