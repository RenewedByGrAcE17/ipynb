# %%
# Accept user's name
user_name = input ("Please enter your name: ")
friend_name = input ("Please enter your friend's name: ")
print(f"Hello, {user_name}! It's great that you and {friend_name} are here together. Have a wonderful day!")

# %%
#Add Two Numbers
num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
result = num1 + num2
print(f"The sum of {num1} and {num2} is {result}.")

# %%
# Simple Age Calculator
from datetime import datetime
current_year = datetime.now().year
birth_year = int(input("Please enter your birth year: "))
age = current_year - birth_year
print(f"You are {age} years old.")


# %%
# Temperature Converter (Celsius to Fahrenheit)
celsius = float(input("Please enter the temperature in Celsius"))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F.")


# %%
# Dollar to naira converter
dollar_amount = float(input("Enter the dollar amount: "))
exchange_rate = 1750
naira_amount = dollar_amount * exchange_rate
print(f"{dollar_amount} USD is equivalent to {naira_amount:.2f} Naira.")

# %%
# Concatenate Two Strings
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
full_name = first_name + " " + last_name
print(f"Your full name is: {full_name}")

# %%
# Calculate the Area of a Rectangle
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area:.2f}")


