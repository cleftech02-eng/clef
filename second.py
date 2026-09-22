name = input("enter your name: ")
age = input("Enter your age: ")
if int(age) >= 18 and int(age) >= 70:    
    print(f"{name} you may need a medical check.")

elif int(age) < 18:
         print(f"{name} you are too young to drive.")

else:
    print(f"{name} you can apply for a driver's license.")

