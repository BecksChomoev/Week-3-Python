print("Welcome to Calculator")
number_of_guests = int(input("How many guests do you have? "))
receipt = float(input("How much was your total receipt?"))
tip = int(input("How much percent did you tip?"))
tip_amount = (tip / 100) * receipt
total = tip_amount + receipt

print("The tip amount is $" + str(tip_amount))
print("Your total receipt is $" + str(total))
print("Each one of you should pay $" + str(total / number_of_guests))