age = int(input("Enter your age: "))
if age:
    if age<=18 and age<21:
        # too young to party
        print("Too young to drink use wrist band")
    elif age>21 or age ==65:
        print("Hurray you free to drink") # older age to party
    else:
        print("you are not allowed")
else:
    print("Please Enter your age")
