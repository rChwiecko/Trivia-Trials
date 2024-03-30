import Instructor

"""This class allows Developers more access to the game for ease of testing,
debugging, and modification.
"""
# developer will not need to explicitly overide any conditions for game progression
# developers must be able to jump between levels, reset highscores, 
# add 'change metrics' button to main menu screen

class Developer:   
    def __init__(self):
        self.__developerStatus = False # give developer status default = False
        self.__developerPin = 374666 # stores the devleoper pin (temporary for now)
        # add parameter for any changes they would make
        # changes to leaderboard
        self.__scoreChange = 0

    
    # verifies whether the pin entered by user matches the developer pin or not and returns a boolean of the status 
    def verifyDeveloperPin(self, pinInput): # recieve input from user and store it 
        if pinInput == self.__developerPin: # if the input by user matches the pin, run the following code
            self.__developerStatus = True # set the intrusctor status to true, allowing the user to conitnue as an instructior 
        else: # else, if the user enters any other input (including strings, space, incorrect pin integers, etc)
            self.__developerStatus = False # set the developer status to false, to deny access of the developer mode 
        return self.__developerStatus # return the developer status 
    
    def setPlayerScore(self, scoreInput):
        self.__scoreChange = scoreInput

    def getplayerScore(self):
        return self.__scoreChange
    
    def changeHighScore(self, newScore):
        return 
    
    def changeCurrlevel(self, level):
        return
    
    # def 