bike=int(input("enter any bike..."))
car=int(input("enter any car..."))
if car>bike:
    print("bike")
elif bike>car:  
    print("car")
elif car==bike:
    print("same")
else:
    print("nathing")