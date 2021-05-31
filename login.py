for i in range(3):
    usr = input("Enter username: ")
    psw = input("Enter password: ")
    
    if usr == "username1" and psw == "open123":
        print("Access Granted!")
        break
    else:
        print("Access Denied!")
    print("Try Again!")
else:
    print("No more attemps!")
