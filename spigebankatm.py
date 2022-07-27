print("Welcome to 'Spige Banking' ")
print(' Please press "Y"  to continue.... else press "N" to cancel   ')

choise  = input("> ")

attempt = 3


if choise == "Y" :

    print("Please enter your 4 digit Banking pin ")

    while attempt >= 0  :
        pin = int(input(">>> Pin : "))
        if pin != 7899 :
            print("Incorrect PIN ")
        elif pin == 7899:
            print("""
               Press 1 for cash withdrawal
                 Press 2 for Balance enquiry
                 Press 3 for to deposit cash
                 Press 4 for exit
             """)
            break
        attempt = attempt - 1

        if attempt == 0:
            print("Oopse ! no more chance left ")
            break



elif choise == "N":
    print("""
          
                         Thanks for using  "Spige Banking"
                          please visit again....

    """)

Options = int(input(">>> Select the input : "))

if Options == 1 :
    print("Please enter the ammount to withdraw ")
    withdraw_ammount = int(input(">>  "))



