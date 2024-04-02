'''Author: Jin, Sonia
'''

import Instructor
import IncorrectPasswordException

class Developer:
    '''This class allows Developers more access to the game for ease of testing,
    debugging, and modification. 

    Attributes:
        developerPin (int): Developer pin, check if input pin matches the developer pin.
    '''   

    def __init__(self):
        self.__developerPin = 374666 # stores the devleoper pin

    def setPermission(self, pinInput: int) -> None:
        '''Overwrites Instructor.setPermission() to give appropriate permission level for Developer provided
        correct pin is input by user.

        Args:
            pinInput (int): Pin provided by user.

        Raises:
            IncorrectPasswordException(): If user input does not match pin to access Instructor mode
        '''
        if pinInput == self.__developerPin:
            self.__permissionValue = 2
        else:
            self.__permissionValue = 0
            raise IncorrectPasswordException()
        
    def getPermission(self) -> int:
        '''Gets the permission level of this objects, should be 2.
        
        Returns:
            int: The permission level of this user.
        '''
        return self.__permissionValue