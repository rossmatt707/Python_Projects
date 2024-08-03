

class Encap:
    # Construct / Initiate class variables
    def __init__(self):
        self._protectVar = 0
        self.__privateVar = 0
        
    # Method setting value of private variable
    def privateVarSet(self, private):
        self.__privateVar = private
        
    # Method to get value of private variable and print
    def privateVarGet(self):
        print(self.__privateVar)

if __name__ == "__main__":
    # Instance of encap class. Accesses and modifies protected variable.
    obj = Encap()
    obj._protectVar = 99
    print(obj._protectVar)

    # Instance of encap class. Gets and prints initial privateVar value. Sets new value for privateVar and prints that.
    obj = Encap()
    obj.privateVarGet()
    obj.privateVarSet(23)
    obj.privateVarGet()
    
    

        
