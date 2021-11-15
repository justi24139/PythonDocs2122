import basics

app = basics.newProgram()

user = basics.newUser()

app.balance = 1000

app.program = True

while app.program == True:
    userChoice = input('1 deposit, 2 Withdraw, 3 quit')
    if userChoice == '1':
        userDepositAmount = input('How much money do you want to deposit?')
        userDepositAmount = int(userDepositAmount)
        app.balance = app.balance + userDepositAmount
        print('Your current balance is:')
        print(app.balance)

    elif userChoice =='2':
        withdraw = input('How much money do you want to withdraw')
        app.balance = int(app.balance)
        withdraw = int(withdraw)
        if withdraw > app.balance:
            print('You don\'t have enough money.')
        else:
            app.balance =  app.balance - withdraw
            print('Your current balance is')
            print(app.balance)

    elif userChoice =='3':
        app.program = False

    else:
        print('Choice was invaild')
