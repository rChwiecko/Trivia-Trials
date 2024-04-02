'''Author: Jin'''
import random
import unittest
import Instructor
import IncorrectPasswordException

class TestInstructor(unittest.TestCase):
    '''Unit testing Instructor class methods.'''
    def test_setPermission(self):
        instructor = Instructor()       # check if appropriate permission level is given
        instructor.setPermission(666473)
        self.assertEqual(instructor.getPermission(), 1)
        
        with self.assertRaises(IncorrectPasswordException):     # check if appropriate exception is thrown
            instructor.setPermission(123456)
        print("setPermission passed")

    def test_getPermission(self):
        instructor = Instructor()
        self.assertEqual(instructor.getPermission(), 0)
        instructor.setPermission(666473)
        self.assertEqual(instructor.getPermission(), 1)
        print("getPermission passed")
        
    print("Instructor tests passed")

if __name__ == '__main__':
    unittest.main()