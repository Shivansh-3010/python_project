print("WELCOME TO OUR ATM")
balance=5000
print("""
      1==Amount
      2==Withdraw balance
      3==Deposit balance
      4==EXIT
      """)

option=int(input("Please enter one of the options above: "))
if option==1:
        print("Name= Mr.John")
        print("Your current balance is",balance,"rupees")
elif option==2:
        withdraw_amount=int(input("Please enter withdraw amount: "))
        print("Name= Mr.John")
        if balance<withdraw_amount:
            print("Transaction Failed")
            print("You do not have sufficient amount")
        else:
            print("Transaction Successful")
            balance=balance-withdraw_amount
            print("Rupees",withdraw_amount,"is debited from your account")
            print("Your current balance is",balance,"rupees")    
elif option==3:
        deposit_amount=int(input("Please enter deposit_amount: "))
        print("Name= Mr.John")
        balance=balance+deposit_amount
        print("Rupees",deposit_amount,"is credited to your account")
        print("Your current balance is",balance,"rupees")
if balance<5000:
    print("Low Balance")
elif option==4:
        'break'
