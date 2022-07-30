# Tip Calculator Generator

print("Welcome to the Tip Calculator.")
total_bill = float(input("What was the total bill? $"))
tip_percentage_to_add = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
num_of_people = int(input("How many people to split the bill? "))

total_bill_incl_tip = (total_bill * (tip_percentage_to_add / 100)) + total_bill
total_bill_after_split = round((total_bill_incl_tip / num_of_people), 2)
print(f"Each person should pay: ${total_bill_after_split}")