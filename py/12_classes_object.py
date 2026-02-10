# Basic class definition
class Person:
    # Class attribute (shared by all instance)
    species = "Homo sapiens"

    # Constructor method
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."
    
    # Method with parameters
    def have_birthday(self):
        self.age += 1
        return f"Happy birthday! {self.name} is now {self.age}."
    
    def greet(self, people):
        return f"Hello {people.name}, I'm {self.name} your new neighbour."

# Creating objects (instances)
person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

# Accessing attributes
print(person1.name)         # Alice
print(person1.age)          # 25

# Calling methods
print(person1.introduce())
print(person1.have_birthday())
print(person1.greet(person2))

# Class attributes
print(Person.species)       # Homo sapiens
print(person1.species)      # Homo sapiens



##############################

# Classes and object

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.trasaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.trasaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}"
        else:
            return "Invalid deposit amount"
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.trasaction_history.append(F"Withdrew ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}"
        else:
            return f"Invalid withdrawal amount or insufficient funds"
    
    def get_balance(self):
        return f"Current balance: ${self.balance}"
    
    def get_transaction_history(self):
        return self.trasaction_history
    
# Using the BankAccount class
account = BankAccount(998462, "Alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())
print(account.get_transaction_history())


# Exercise
q="Create game character with health, attack, heal"

class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.current_health = health
        self.max_health = health
        self.attack_power = attack_power

    def attack(self, enemy):
        enemy.current_health -= self.attack_power
        if enemy.current_health < 0:
            enemy.current_health = 0
        return f"{self.name} attacks {enemy.name} for {self.attack_power} damage!"

    def heal(self, amount):
        if (amount + self.current_health) >= self.max_health:
            amount = self.max_health - self.current_health
            self.current_health = self.max_health
            return f"{self.name} has been healed for {amount} health. Current health is {self.current_health}"
        else:
            self.current_health += amount
            return f"{self.name} has been healed for {amount} health. Current health is {self.current_health}"
        
    def status(self):
        return f"{self.name}:\n{self.current_health}/{self.max_health} HP\n{self.attack_power} AP"
    

hero = Character("Hero", 100, 20)
monster = Character("Monster", 50, 15)

print(hero.attack(monster))
print(monster.status())
print(monster.attack(hero))
print(hero.status())
print(hero.heal(30))
print(hero.status())