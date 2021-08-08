def numb():
    a = int(input("Enter 1st value"))
    b = int(input("Enter 2nd value"))
    print (a)
    print (b)
    print ("Enter 1 for addition")
    print ("Enter 2 for subtraction")
    print ("Enter 3 for Multiplication")
    print ("Enter 4 for Division")
    c = int(input("Enter the number :"))
    if c == 1 :
        d = a + b
        print(d)
    elif c == 2 :
            e = a - b
            print(e)
    elif c == 3 :
        f = a * b
        print(f)
    elif c == 4 :
        g = a / b
        print(g)
numb()
h = str(input("Do you wish to continue : Yes or No:"))
if h == "Yes" :
    numb()
elif h == "No" :
    print("Your function has been done.")
    Print("Github Changes")