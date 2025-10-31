print("Welcome to Tip Calculator")
number_of_guests = int(input("How many people are splitting the bill?"))
guests = []
while len(guests) < number_of_guests:
    guests.append(input("What is the guest name? Please enter each guest separately."))

receipt = float(input("How much was your total receipt?"))
tip = int(input("How much percent did you tip?"))
if tip > 20:
    print('Wow! Thank you for your generosity!')
tip_amount = (tip / 100) * receipt
total = tip_amount + receipt

print("The tip amount is $" + str(tip_amount))
print("Your total receipt is $" + str(total))
per_person = str(total / number_of_guests)

for guest in guests:
    print(guest + " should pay: $" + per_person)