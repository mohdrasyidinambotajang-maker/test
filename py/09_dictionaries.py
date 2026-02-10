student = {
    "name": "Alice",
    "age": 20,
    "grade": "A",
    "course": ["Math", "Science", "English"]
}

print(student["name"])                  # "Alice"
print(student.get("age"))               # 20 , Old method
student["age"] = 21                     # Modify value
student["email"] = "alice@gmail.com"    # Add new key-value
del student["grade"]                    # Delete key-value

keys = student.keys()                   # Get all keys
values = student.values()               # Get all values
items = student.items()                  # Get key-value pairs

print(keys)
print(values)
print(items)


# Iterating Dictionaries
for key in student:
    print(f"{key}: {student[key]}")


for key, value in student.items():
    print(f"{key}: {value}")


# Nested dictionaries
company = {
    "employees": {
        "john": {"age": 30, "department": "IT"},
        "jane": {"age": 25, "department": "HR"}
    },
    "departments": ["IT", "HR", "Finance"]
}

print(company["employees"].items())
print(company["departments"])

for key in company["employees"]:
    print(f"{key}: {company["employees"][key]}")



# Exercises 1
print("--- Exercise 1 ---")
students = [
    {
        "id": "001",
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grade": [85, 92, 78]
    },
    {
        "id": "002",
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grade": [90, 88, 95]
    }
]

# Exercises 2
print("--- Exercise 2 ---")
new_student = {
        "id": "003",
        "name": "Mike",
        "age": 18,
        "major": "Math",
        "grade": [82, 79, 91]
}

students.append(new_student)
for student in students:
    print("ID:", student["id"])
    print("Name:", student["name"])
    print("Age:", student["age"])
    print("Major:", student["major"])
    print("Grades:", student["grade"])
    print("----------------------")


# Exercise 3
print("--- Exercise 3 ---")
for student in students:
    if student["name"] == "John":
        student["age"] = 20
        print("Name:", student["name"])
        print("Age:", student["age"])
        break


# Exercise 4
print("--- Exercise 4 ---")
for student in students:
    print("Student ID:", student["id"])
    print("Name:", student["name"])
    print("Major:", student["major"])
    print("----------------------")