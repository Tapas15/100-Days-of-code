class Dog:
    def __init__(self):
        self.temperament = "loyal"

    def bark(self):
        print("Woof, woof!")

class Labrador(Dog):
    def __init__(self):
        super().__init__()
        self.is_a_good_boy = True
        self.temperament = "gentle"

    def bark(self):
        super().bark()
        print("Greetings, good sir. How do you do?")

    def fetch(self):
        print("Roger that. Retrieving item.")

doggo = Dog()
doggo.bark()
print(f"A dog is {doggo.temperament}")
sparky = Labrador()
print(f"Sparky is {sparky.temperament}")
sparky.bark()

# print(doggo.is_a_good_boy) # Error. No such attribute
# sparky.is_a_good_boy() # Error. Boolean not a function
print(sparky.is_a_good_boy)