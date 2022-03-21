num = [0,1,0,3,12]
i=0
c=[]
p=[]
count=0
while i<len(num):
    if num[i]>0:
        c.append(num[i])
        c.sort()
    else:
        p.append(num[i])
        count=count+1
    d=c+p
    i=i+1
print(d,"zero",count)
