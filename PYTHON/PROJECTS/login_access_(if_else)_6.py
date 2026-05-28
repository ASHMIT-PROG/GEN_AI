username=input("Enter username: ").strip()#strip() will remove all the spacs from left and right 
password=input("Enter password: ")

if(password.isdigit()):#check that the password entered is digit or not , works only on string

    if(username == "raman" and int(password)==123):
        print("login successful")

    else:
        print("Wrong Password")    


else:
        print("User Not Found")



