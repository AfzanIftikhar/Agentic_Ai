# Task -> Atm System
# Check if the pin Code is correct or not, if matches not correct break and 3 tries max
# Ask the user to enter the desired amount to withdraw
# Check if amount is less then current balance and the amount is multiple of 500 then allow the transaction and reduce the amount from the current balance

pin = 900712
current_balance = 3000
tries = 3

while True:
    user_input = int(input("Enter Your Pin : "))
    if user_input == pin:
        print("Correct Pin !")

        user_amount = int(input("Enter the amount you want to withdraw : "))
        if user_amount < 500:
            print("please enter amount equal or greater then 500")

        elif user_amount > current_balance:
            print("Sorry the entered amount is greater then your current amount")
        else:
            new_balance = current_balance - user_amount
            current_balance = new_balance
            print(f"Your account has been debited with pkr {user_amount}")
            print(f"amount left : {current_balance}")
            break            

        break

    else:
        tries -= 1
        print(f"Try again, you have {tries} chances left")

        if tries == 0:
            print("You Card has been Captured") 
            break