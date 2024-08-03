from abc import ABC, abstractmethod

class dog(ABC):
    def barking(self,breed):
        print("Your dog is a",breed)

    @abstractmethod
    def loud(self, breed):
        pass

class barker(dog):
    def loud(self, breed):
        print('Your {} is barking loudly at me from the balcony'.format(breed))
    

if __name__ == "__main__":
    obj = barker()
    obj.barking("Chihuahua")
    obj.loud("Chihuahua")
