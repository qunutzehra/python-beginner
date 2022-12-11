print("Welcom to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10,12, or 15? "))
person = int(input("How many people to split the bill? "))

bill_with_tip = bill * (1 + tip / 100)

print("Each person should pay: $", round(bill_with_tip, 2))