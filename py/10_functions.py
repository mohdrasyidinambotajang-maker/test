# def add_numbers(a, b):
#     return a + b

# result = add_numbers(5, 3)
# print(result)                   #8


# def greet_w_title(name, title=" Mr."):
#     return f"Hello, {title} {name}!"

# print(greet_w_title("Smith"))           # Hello, Mr. Smith!
# print(greet_w_title("John", "Dr."))     # Hello, Dr. John!


# # *args - variable number of arguments
# def sum_all(*args):
#     return sum(args)

# print(sum_all(1,2,3,4,5))       #15


# # **kwargs - keyword arguments
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=25, city="New York")


# # Combining *args and **kwargs
# def flexible_function(*args, **kwargs):
#     print("Positional arguments:", args)
#     print("Keyword arguments:", kwargs)

# flexible_function(1,2,3, name="JoJo", age=21)


# # Lambda functions (anonymous functions)
# square = lambda x: x**2
# print(square(5))            #25

# add = lambda x, y: x + y
# print(add(3,4))             #7



# Exercise 1

def is_prime(number):
    if number < 2:
        return f"{number} is not prime"
    for i in range(2, number):
        if number % i == 0:
            return f"{number} is not prime"
    return f"{number} is prime"

number = int(input("Enter a number: "))
print(is_prime(number))

# Exercise 2
def celcius_to_fahrenheit(celcius):
    fahrenheit = celcius * 9/5 +32
    return fahrenheit

celcius = float(input("Enter temperature: "))
print(f"{celcius} Celcius is {celcius_to_fahrenheit(celcius)} Fahrenheit")