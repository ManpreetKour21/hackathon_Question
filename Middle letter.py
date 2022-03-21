def midal():
    m=input("enter the alp.....")
    n=input("enter the alp.....")
    s=input("enter the alp.....")
    if m>n and m<s:
        print(m,"is midal number")
    elif n>m and n<s:
        print(n,"is midal number")
    elif s>m and s<n:
        print(s,"is midal number")
    else:
        print("no ")
midal()