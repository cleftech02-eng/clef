

balance = 1000000
name = input("Enter your name: ")
bank = input(f"{name}, check balance(CB) or make deposit(MD) or make withdrawal(MW) : ")

#balance.
if bank.upper() == "CB" :
    balance = 1000000
    print(f"{name}, your balance is: {balance}")    

    if balance == 0 :
            print("Insufficient funds.")   

#make depoist.    
elif bank.upper() == "MD":
    deposit = int(input("Enter the amount you want to deposit: "))
    balance = balance + deposit

    if deposit > balance:
            print("too much money detected .")   

    elif deposit == 0:
                print("invaild funds")   


    elif deposit < 500:
         print("deposit is from 500 above")
    
    else:
        print(f"{name}, your new balance is: {balance}")

#make withdrwal.
elif bank.upper() == "MW":
    withdrawal = int(input("Enter the amount you want to withdraw: "))   
    balance = balance - withdrawal

    if withdrawal > balance or withdrawal > 500 :
        print("Insufficient funds.")   

    elif withdrawal < 500:
        print("withdrawal is from 500 above")

    elif withdrawal == 0:
            print("invaild funds")
    
    else:
        print(f"{name}, your new balance is: {balance}")

else:
    print("Invalid option. Please choose CB, MD, or MW.")   
