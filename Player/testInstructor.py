import random
import unittest
import Instructor
import IncorrectPasswordException

class TestInstructor(unittest.TestCase):
    '''Unit testing Instructor class methods.'''
    def test_setPermission(self):
        instructor = Instructor()
        instructor.setPermission(666473)
        self.assertEqual(instructor.getPermission(), 1)
        
        with self.assertRaises(IncorrectPasswordException):
            instructor.setPermission(123456)

        print("Instructor tests passed")

if __name__ == '__main__':
    unittest.main()