import Player
import IncorrectPasswordException

class Instructor:
    '''This class extends the Player class to allow Instructors to view
    additional information i.e. all Player scores and progression.
    
    Attributes:
        instructorPin (int): Instructor pin, check if input pin matches the instructor pin.
    '''

    def __init__(self):
        self.__instructorPin = 666473   # stores the instructor pin

    def setPermission(self, pinInput: int) -> None:
        '''Overwrites Player.setPermission() to give appropriate permission level for Instructor provided
        correct pin is input by user.

        Args:
            pinInput (int): Pin provided by user.

        Raises:
            IncorrectPasswordException(): If user input does not match pin to access Instructor mode
        '''
        if pinInput == self.__instructorPin:
            self.__permissionValue = 1
        else:
            self.__permissionValue = 0
            raise IncorrectPasswordException()
        
    def getPermission(self) -> int:
        '''Gets the permission level of this objects, should be 1.
        
        Returns:
            int: The permission level of this user.
        '''
        return self.__permissionValue
    


    # # verifies whether the pin entered by user matches the instructor pin or not and returns a boolean of the status 
    # def verifyInstructorPin(self, pinInput): # recieve input from user and store it 
    #     if pinInput == self.__instructorPin: # if the input by user matches the pin, run the following code
    #         self.__instructorStatus = True # set the intrusctor status to true, allowing the user to conitnue as an instructior 
    #     else: # else, if the user enters any other input (including strings, space, incorrect pin integers, etc)
    #         self.__instructorStatus = False # set the instructor status to false, to deny access of the instructor mode
    #         raise IncorrectPasswordException()

    #     return self.__instructorStatus # return the instructor status 