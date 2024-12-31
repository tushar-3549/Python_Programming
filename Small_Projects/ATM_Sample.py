print("Welcome to my Bank !")
passw = 1234
username = "admin"
trail = 3
while trail != 0:
    pin = int(input("Enter your password : "))
    user = input("Enter your username : ")
    if pin != passw and user != username:
        trail -= 1
        print("Wrong password and username !",trail,"Trails left")
    else:
        userChoice = input("d : Diposit or w : Withdraw ? : ")
        if userChoice == 'd':
            dip = int(input("Enter amount you would like to deposit : "))
            print(dip," $ You have been deposited into your account .")
        if userChoice == 'w':
            withd = int(input("Enter amount you would like to withdraw : "))
            print(withd," $ You have been withdraw into your account .") 
    Exituser = input("Would you like to continue ! ( Y / N) : ")
    if Exituser == 'N':
        print("Thanks for using the Bank ! ")
        break
    else:
        continue
