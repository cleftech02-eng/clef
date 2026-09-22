balance = 1000000
name = input("Enter your name: ")
bank = input(f"{name}, check balance(CB) or make deposit(MD) or make withdrawal(MW) : ")

if bank.upper() == "CB" :
    balance = 1000000
    print(f"{name}, your balance is: {balance}")    

    if balance == 0 :
            print("Insufficient funds.")   
    
elif bank.upper() == "MD":
    deposit = int(input("Enter the amount you want to deposit: "))
    balance = balance + deposit

    if deposit < balance :
            print("too much money detected .")   
    
    else:
        print(f"{name}, your new balance is: {balance}")

elif bank.upper() == "MW":
    withdrawal = int(input("Enter the amount you want to withdraw: "))   
    balance = balance - withdrawal

    if withdrawal > balance :
        print("Insufficient funds.")   

    else:
        print(f"{name}, your new balance is: {balance}")

else:
    print("Invalid option. Please choose CB, MD, or MW.")   
