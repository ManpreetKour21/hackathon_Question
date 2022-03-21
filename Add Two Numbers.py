a = [2,4,3]
b = [5,6,4]
i=0
while i<len(a):
    j=0
    c=0
    while j<len(a):
        c=a[i]+b[i]
        j+=1
    i+=1
    print(c)



