# Encapsulation 
'''
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return amount
        return "Insufficient amount.."
    def get_balance(self):
        return self.__balance
amount = BankAccount("Tushar", 1000)
amount.deposit(500)
amount.withdraw(400)
print(amount.get_balance())    
'''

# Inheritance  

'''
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks"

dog = Dog("Tommy")
print(dog.speak())
animal = Animal("Animal")
print(animal.speak())
'''

# Polymorphism
'''
class Dog:
    def sound(self):
        return "Ghew Ghew"
class Cat:
    def sound(self):
        return "Meow"
def animal_sound(animal):
    return animal.sound()

dog = Dog()
dog_sound = animal_sound(dog)
print(dog_sound)
cat = Cat()
cat_sound = animal_sound(cat)
print(cat_sound)
'''

# Abstraction

# ABC -> Abstract base class
'''
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def sound(self):
        pass

class Bike(Vehicle):
    def sound(self):
        return "buum buum..."

bike = Bike()
print(bike.sound())    
'''

# OOP [all in one]

from abc import ABC, abstractmethod

# Abstraction + Inheritance
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self):
        pass

# Inheritance + Encapsulation
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.__student_id = student_id  # Encapsulation

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, ID: {self.__student_id}"

# Polymorphism
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}, Teaches: {self.subject}"

# Data Storage
people = []

# Add students and teachers
people.append(Student("Rahim", 20, "S101"))
people.append(Teacher("Karim Sir", 40, "Math"))

# Display info using Polymorphism
for person in people:
    print(person.get_info())

