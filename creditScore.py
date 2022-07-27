Name = input("Enter your name : ")
Age = input("Enter your Age : ")
print(f'Hi '+ Name + "  your aligible for loan please give more details about your credit score ")
Credit_sore = (input("Enter your credit score :  "))
if int(Credit_sore) == 100 :
    print(" Your initial down payment is 20% ")
    print("Thank you " + Name )

elif int(Credit_sore) >= 100:
    print("Your initial downpayment is 10% ")
    print("Thank you " + Name )


else:
    print("Plese enter the right input of credit scrore in numbers ")
    print("Than you " + Name +" for your intrest Better luck next time ! ")
