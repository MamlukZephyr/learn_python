# Assume that you live till the age of 90
# In 1 year = 365 days
# In 1 year = 52 weeks
# In 1 year = 12 months

# It will take your current age as the input and output a message with our time left in this format:

# You have x days, y weeks, and z months left.

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")  # 🚨 Don't change the code above 👆

# 🚨 Don't change the code above 👆# Assume that you live till the age of 90

age_as_int = int(age)

remaining_year = 90 - age_as_int
remaining_days = remaining_year * 365
remaining_weeks = remaining_year * 52
remaining_months = remaining_year * 12

message = (
    f"You have {remaining_days}, {remaining_weeks} weeks, and {remaining_months} months left")
print(message)
