a=[85,25,65,21,84]
i=0
while i<len(a):
    b=a[i]%10
    i=i+1
    print(b,end="")
if b%10==0:
    print("yes")
else:
    print(".:.no")
