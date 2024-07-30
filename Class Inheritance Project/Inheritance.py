# Creates the new class transportation.
# Inludes class attributes and __init__  for initializing new variables.
class Transportation
    def __init__(self, name, capacity, speed, fuel_type):
        self.name = name
        self.capacity = capacity
        self.speed = speed
        self.fuel_type = fuel_type

# Creates child class Car. Transportation becomes parent class.
# Car inherits attributes from parent and has two of its own unique attributes.
class Car(Transportation):
    def __init__(self, name, capacity, speed, fuel_type, doors, trunk_size):
        super().__init__(name, capacity, speed, fuel_type)
        self.doors = doors
        self.trunk_size = trunk_size

# Creates child class Bike. Transportation becomes parent class.
# Bike inherits attributes from parent and has three of its own unique attributes.
class Bike(Transportation):
    def __init__(self, name, capacity, speed, fuel_type, bike_type, seats, gears):
        super().__init__(name, capacity, speed, fuel_type)
        bike_type = bike_type
        seats = seats
        gears = gears

New_Transportation = 
