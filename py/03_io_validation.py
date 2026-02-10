# name = input("Enter your name: ")

# #input validation
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         height = float(input("Enter your height (cm): "))
#         if age > 0 and height > 0:
#             break
#         else:
#             print("Age and height must be positive!")
#     except ValueError:
#         print("Please enter a valid number!")

# #output after validation
# print(f"Hello, {name}")
# print(f"You're {age} years old and {height} cm tall")

#ChatGPT answer
# def get_number(prompt, min_val, max_val, cast):
#     while True:
#         try:
#             value = cast(input(prompt))
#             if min_val <= value <= max_val:
#                 return value
#             print(f"Enter a value between {min_val} and {max_val}.")
#         except ValueError:
#             print("Invalid input!")

# name = input("Enter your name: ")

# age = get_number("Enter your age: ", 1, 120, int)
# height = get_number("Enter your height (cm): ", 50, 250, float)

# print(f"\nHello, {name}")
# print(f"You're {age} years old and {height} cm tall")



#exercise 
ex1 = "Create a simple calculator that takes two number and an operation from user."

while True:
    try:
        no1 = float(input("Enter first number: "))
        no2 = float(input("Enter second number: "))
        op = input("Enter operation (+,-,*,/): ")

        if(op == "+"):
            result = no1 + no2
        elif(op == "-"):
            result = no1 - no2
        elif(op == "*"):
            result = no1 * no2
        elif(op == "/"):
            if(no2 != 0):
                result = no1 / no2
            else:
                print("Cannot divide by zero")
                continue
        else:
            print("Invalid operation")
            continue
        print(f"Result: {result}")
        break
    except ValueError:
        print("Please enter a valid numbers!")


ex2 = "Create a simple quiz program with 3 questions. At the end of the quiz,display score."

score = 0
# # Question 1
answer1 = input("What is the capital of France? ").lower()
if answer1 == "paris":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Wrong! The answer is Paris.")

# # Question 2
answer2 = input("What is 5 + 3? ")
if answer2 == "8":
    print("Correct!")
    score += 1
    print(score)
else:
    print("Wrong! The answer is 8.")

# # Question 3
answer3 = input("What color do you get when you mix red and blue? ").lower()
if answer3 == "purple":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is purple.")

# Final score
print(f"\nYour final score: {score}/3")
if score == 3:
    print("Perfect score!")
elif score >= 2:
    print("Good job!")
else:
    print("Better luck next time!")