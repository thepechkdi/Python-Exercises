# Create a class called Person

class Person:
    def __init__(self, name, age, city, birth_year):
        self.name = name
        self.age = age
        self.city = city
        self.birth_year = birth_year

    # Add a method that displays an introduction message
    def introduce_yourself(self):
        print(f"Hello, my name is {self.name}, I am {self.age} years old, and I live in {self.city}.")


# Create objects and call the method
person_1 = Person("Yahya", 24, "Tangier", 2000)
person_1.introduce_yourself()

person_2 = Person("Ali", 18, "Tetouan", 2002)
person_2.introduce_yourself()

person_3 = Person("Sara", 22, "Rabat", 1998)
person_3.introduce_yourself()

person_4 = Person("Lina", 20, "Casablanca", 2003)
person_4.introduce_yourself()

person_5 = Person("Omar", 30, "Marrakech", 1994)
person_5.introduce_yourself()
