# Importing abc module for creating abstract base classes
from abc import ABC, abstractmethod

# Defining an abstract base class named dog
class dog(ABC):
    # Method to print the breed of the dog
    def barking(self, breed):
        print("Your dog is a", breed)

    # Abstract method that must be implemented by subclasses
    @abstractmethod
    def loud(self, breed):
        pass

# Defining a subclass named barker that inherits from dog
class barker(dog):
    # Implementing the abstract method loud
    def loud(self, breed):
        print('Your {} is barking loudly at me from the balcony'.format(breed))

# Main block to create an instance of barker and call its methods
if __name__ == "__main__":
    obj = barker()  # Creating an instance of barker
    obj.barking("Chihuahua")  # Calling the barking method
    obj.loud("Chihuahua")  # Calling the loud method
