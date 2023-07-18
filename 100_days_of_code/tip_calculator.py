print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, 15? "))
people = int(input("How many people to split the bill? "))

tip_in_percentage = tip/100
total_bill = bill * tip_in_percentage
total_bill_and_tips = bill + total_bill
total_after_tip = total_bill_and_tips / people
final_amount = round(total_after_tip, 2)
final_amount = "{:.2f}".format(total_after_tip)

print(f"Each person should pay: ${final_amount}")
