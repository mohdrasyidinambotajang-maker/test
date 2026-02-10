# user_age = int(input("Enter your age: "))
# has_license = input("Do you have license(y/n): ")

# if user_age >= 17 and has_license == "y":
#     print("You're allowed to drive.")
# else:
#     print("You are not allowed to drive.")


#excercise
question = """Write a program that categorizes BMI (Body Mass Index) into
underweight(<18.5), normal weight(<24.9), overweight(<29.9), and
obesity(<30.0). (formula = kg/m^2)"""

weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height (cm): "))/100

bmi = weight/height**2

if(bmi < 18.5):
    cat = "underweight"
elif(bmi < 24.9):
    cat = "normal weight"
elif(bmi < 29.9):
    cat = "overweight"
else:
    cat = "obesity"

print(f"Your BMI is: {bmi:.3f}")
print(f"Your category is: {cat}")