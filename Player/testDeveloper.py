import random
import unittest
import Developer
import IncorrectPasswordException

class TestDeveloper(unittest.TestCase):
    '''Unit testing Developer class methods.'''
    def test_setPermission(self):
        dev = Developer()
        dev.setPermission(374666)
        self.assertEqual(dev.getPermission(), 2)

        with self.assertRaises(IncorrectPasswordException):
            dev.setPermission(123456)
            
        print("Developer tests passed")

if __name__ == '__main__':
    unittest.main()

