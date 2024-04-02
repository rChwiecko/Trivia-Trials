'''Author: Jin'''
import random
import unittest
import Developer
import IncorrectPasswordException

class TestDeveloper(unittest.TestCase):
    '''Unit testing Developer class methods.'''
    def test_setPermission(self):       # check if appropriate permission level is given
        dev = Developer()
        dev.setPermission(374666)
        self.assertEqual(dev.getPermission(), 2)

        with self.assertRaises(IncorrectPasswordException):     # check if appropriate exception is thrown
            dev.setPermission(123456)
        print("setPermission passed")

    def test_getPermission(self):
        dev = Developer()
        self.assertEqual(dev.getPermission(), 0)
        dev.setPermission(374666)
        self.assertEqual(dev.getPermission(), 2)
        print("getPermission passed")

    print("Developer tests passed")

if __name__ == '__main__':
    unittest.main()

