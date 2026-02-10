for i in range(5):          # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 4):       # 1, 2, 3
    print(i)

for i in range(1, 7, 2):    # 1, 3, 5
    print(i)

count = 0
while count < 4:                # 0, 1, 2, 3
    print(count)
    count += 1


for i in range(5):
    if i == 2:
        continue                # skip this
    if i == 4:
        break                   # exit loop
    print(i)                    # 0, 1, 3


for i in range(2):                  # result below
    for j in range(1):              # i,j = 0,0
        print(f"i,j = {i},{j}")     # i,j = 1,0


#excercise

q1 = "build multiplication table"
first = int(input("enter your first number: ")) + 1
second = int(input("enter your second number: ")) + 1

for i in range(1, first):
    for j in range(1, second):
        print(f"{i} * {j} = {i*j}")

q2 ="find prime number, limit 20"
answer = 2, 3, 5, 7, 11, 13, 17, 19

limit = 20
for number in range(2,limit + 1):
    prime = True
    
    for i in range(2, number):
        if number % i == 0:
            prime = False
            break
    if prime:
        print(number)