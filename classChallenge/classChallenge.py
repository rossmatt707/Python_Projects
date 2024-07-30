


# Parent class with attributes.
class Toy:
    def __init__(self,name,cost,age_requirement,max_players,min_players):
        self.name = name
        self.cost = cost
        self.age_requirement = age_requirement
        self.max_players = max_players
        self.min_players = min_players
        
    # method for parent class
    def funTimes(self):
        print("It's really fun to play with a " + self.name)

# Child class one
class Puzzle(Toy):
    def __init__(self,name,cost,age_requirement,max_players,min_players,pieces,difficulty,theme):
        super().__init__(name,cost,age_requirement,max_players,min_players)
        self.pieces = pieces
        self.difficulty = difficulty
        self.theme = theme

        # inherited method demonstrating polymorphism
    def funTimes(self):
        print("It's really fun to play with the " + self.theme + " puzzle!")
        
        # method for child class one
    def challenging(self):
        print("This puzzle is " + self.difficulty + "... I wonder how long it will take to finish")
        
# Child class two
class Video_Game(Toy):
    def __init__(self,name,cost,age_requirement,max_players,min_players, system_requirements, genre):
        super().__init__(name,cost,age_requirement,max_players,min_players)
        self.system_requirements = system_requirements
        self.genre = genre

        # inherited method demonstrating polymorphism
    def funTimes(self):
        print("It's really fun to play with the " + self.genre + " video game!")

        # method for child class two
    def ageRating(self):
        print("My parents said I have to be at least " + str(self.age_requirement) + " to play this game.")



if __name__ == "__main__":
    # Creating an instance of Puzzle
    puzzle = Puzzle("Great Wall of China Puzzle", 15, 10, 4, 1, 1000, "Hard", "History")
    # Calling both the inhereted method and newly created method
    puzzle.funTimes()
    puzzle.challenging()
    # Creating an instance of Video_Game
    video_game = Video_Game("Mega Man IV", 60, 12, 4, 1, "High", "Platformer")
    # Calling both the inhereted method and newly created method
    video_game.funTimes()
    video_game.ageRating()





    
