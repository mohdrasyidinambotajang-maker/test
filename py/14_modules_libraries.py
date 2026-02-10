########### Import Module ###########
from math_utils import add, multiply, factorial, PI, Calculator

print(f"Addition Result: {add(5, 3)}")
print(f"Multiplication Result: {multiply(5, 3)}")
print(f"Calculator add: {Calculator().calculate("add", 5, 4)}")
print(f"Calculator multiply: {Calculator().calculate("multiply", 5, 4)}")

############# Libraries #############
import os
import sys
import datetime
import random

sys.path.append(os.path.dirname(os.path.abspath(__file__))) # Adjust path for imports to root directory

now = datetime.datetime.now()
today = datetime.date.today()
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Now date: {now}")
print(f"Today's date: {today}")
print(f"Current Date and Time: {formatted_date}")

random_number = random.randint(1,100)
random_choice = random.choice(["apple", "banana", "orange"])
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print(f"Random Number: {random_number}")
print(f"Random Choice: {random_choice}")
print(f"Shuffled List: {numbers}")