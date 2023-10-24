# Lab3
# Author: Terrisha Edwards

"""_summary_
This lab is designed to get you familiar with Python input(), converting data types, and using the round() function.
"""

# 1. Ask the user for their name and assign it to a variable called "name".
name = input("What is your name?")
print(name)
# 2. Ask the user for their age and assign it to a variable called "age".
age = int(input("What is your age?"))
# 3. Ask the user for a balance and assign it to a variable called "balance".
balance = float(input("What is your balance?"))
print(balance)
# 4. Ask the user for a number of years to calculate interest and assign it to a variable called "years".
years = int(input("What is the years?"))
print(years)
# 5. Ask the user for an interest rate and assign it to a variable called "interest_rate".
interest_rate = input("what is the interest_rate?")
print(interest_rate)
# 6. Convert the balance,  years, and interest_rate to float data types.

# Note: This is only necessary if you did not specify the data type in the input() function.

# 7. Calculate the future balance using the formula: balance * (1 + interest_rate/100) ** years
future_balance = (balance * (1 + interest_rate/100) ** 22)
# 8. Round the future balance to 2 decimal places using the round() function.
round = round(future_balance, 2)
# 9. Print the following sentence using string concatenation: "Hello <name>, your balance after <years> years will be $<future_balance>."
print("Hello "+ name +", your balance after " + str(years) + " years will be" + int(future_balance)
