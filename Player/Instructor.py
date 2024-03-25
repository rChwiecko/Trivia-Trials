import Player
import IncorrectPasswordException

"""This class extends the Player class to allow Instructors to view
additional information, such as all Player scores and Player progression.
"""

class Instructor:   # needs a pin, and password check
    def __init__(self):
        self.__instructorStatus = True # store whether or not the user can progress as an instructor or not 
        self.__instructorPin = 666473 # stores the instructor pin (temporary for now)

    # where they are in the game
    #def viewPlayerStatus(self, playerID):
        #self.viewPlayerStatus
    
    # scores of players and time 
    #def viewOverall(self):
        #self.viewOverall

    # verifies whether the pin entered by user matches the instructor pin or not and returns a boolean of the status 
    def verifyInstructorPin(self, pinInput): # recieve input from user and store it 
        if pinInput == self.__instructorPin: # if the input by user matches the pin, run the following code
            self.__instructorStatus = True # set the intrusctor status to true, allowing the user to conitnue as an instructior 
        else: # else, if the user enters any other input (including strings, space, incorrect pin integers, etc)
            self.__instructorStatus = False # set the instructor status to false, to deny access of the instructor mode
            raise IncorrectPasswordException()

        return self.__instructorStatus # return the instructor status 