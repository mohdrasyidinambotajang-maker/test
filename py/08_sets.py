fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}

# Set Operations
fruits.add("grape")                 # Add element
fruits.remove("banana")             # Remove element (error if doesnt exist)
fruits.discard("kiwi")              # Remove if exist (no error)

print(fruits)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))             # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))      # {3, 4}
print(set1.difference(set2))        # {1, 2}



#exercise

grades = [
("Alice", "Math", 85),
("Bob", "Science", 92),
("Alice", "Science", 78),
("Charlie", "Math", 90),
("Bob", "Math", 88),
("Alice", "English", 95)
]

student = set()
subject = set()
data_student = []
find_student = input("Enter student name to find: ").title()

for grade in grades:
    student.add(grade[0])           # Add unique student
    subject.add(grade[1])           # Add unique subject

    if grade[0] == find_student:    # Find subject & grade for selected student
        data_student.append((grade[1], grade[2]))

print(f"Student list: {student}")
print(f"Subject list: {subject}")
print(f"{find_student}: {data_student}")