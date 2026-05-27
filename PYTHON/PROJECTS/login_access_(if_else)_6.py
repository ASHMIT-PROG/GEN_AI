

#------------------------------------------------------------------------

username=input("Enter username: ")

password=input("Enter password: ")

if(password.isdigit()):

    password=int(password)

    username_correct = (username == "raman")
    password_correct = (password == 123)

    if(username_correct == True):

        if(password_correct == True):
            print("Login Successful")

        else:
            print("Wrong Password")

    else:
        print("User Not Found")

else:
    print("INT values only")