n=int(input("enter the number..."))
s=int(input("enter the number..."))
c=0
i=0
while i<=s:
    m=i%10
    if m==2 or m==3 or m==9:
        c=c+1
    i+=1
print(i)