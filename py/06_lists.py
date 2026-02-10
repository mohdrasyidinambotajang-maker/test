fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, 3.14, True]
empty_list = []

fruits.append("grape")          # Add to end
fruits.insert(1, "kiwi")        # Insert at index
fruits.remove("banana")         # Remove by value
popped = fruits.pop()           # Remove and return removed value
fruits.sort()                   # Sort in place
fruits.reverse()                # Reverse in place

len(fruits)                     # Length
"apple" in fruits               # Check membership
fruits + ["mango"]              # Cocatenation
fruits * 2                      # Repitition

#exercise 1
# grocery = ["chicken"]
# while True:
#     try:
#         operation = input("Enter operation to do (add, insert, remove, reverse, done): ")
#         if operation.lower() == "add":
#             item = input("Enter item to add in grocery list: ")
#             grocery.append(item)
#             print(f"Current grocery list: {grocery}")
#             continue
#         elif operation.lower() == "remove":
#             item = input("Enter item to remove in grocery list: ")
#             grocery.remove(item)
#             print(f"Current grocery list: {grocery}")
#             continue
#         elif operation.lower() == "insert":
#             idx = int(input("Enter index to insert in grocery list: "))
#             item = input("Enter item to insert in grocery list: ")
#             grocery.insert(idx, item)
#             print(f"Current grocery list: {grocery}")
#             continue
#         elif operation.lower() == "reverse":
#             grocery.reverse()
#             print(f"Current grocery list: {grocery}")
#             continue
#         elif operation.lower() == "done":
#             print(f"Final grocery list: {grocery}")
#             break
#         else:
#             print("Error operation")
#             continue
#     except ValueError:
#         print("Error invalid")


#exercise 2
# the_list = [1,3,4,56,7,88]
# the_list2 = [2, 4, 88, 33, -3]
# the_list.sort()
# print(f"Smallest number: {the_list[0]}")
# print(f"Largest number: {the_list[-1]}")

# print(f"Smallest number: {min(the_list2)}")
# print(f"Largest number: {max(the_list2)}")