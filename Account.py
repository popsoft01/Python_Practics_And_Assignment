
listOfUserName = ["Popsoft", "Oris_Kenny","Budoo" ]
listOfUserPassword = ["popsoftpass","oriskennypass","budoopass"]
balance = 0
userName = input("Enter your user name? \n")
if userName in listOfUserName:
    userPassword = input("Enter the user password")
    userDetails = listOfUserName.index(userName)
    if userPassword in listOfUserPassword.index[userDetails]:
            print("Welcome to POPLAND Bank %s" ,userName)
            print("Select the an option")
            print(" press 2 for cash Deposit \n press 1 for Withdrawal \n press 3 for Complaint")

            optionSelected = int(input("please select an option"))

            if optionSelected == 1:
                print("selected option is %s ", optionSelected)
                deposit = int(input("Enter the deposit amount"))
                balance = balance + deposit

            elif optionSelected == 2:
                print("selected option is %s ", optionSelected)
                withdrawAmount = int(input("Enter the withdraw amount"))
                if withdrawAmount < balance:
                    balance = balance - withdrawAmount
                else:
                    print("insufficient fund")

            elif (optionSelected == 3):
                print("selected option is %s ", optionSelected)
                withdrawAmount = input("Please enter your complaint here and our again will get back to you")

    else:
        print("Wrong Password, Please try again")

else:
    print("Wrong UserName, Please Enter the correct User Name")
