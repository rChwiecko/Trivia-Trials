import unittest
from questionGeneration import *

class TestQuestionGeneration(unittest.TestCase):
    def test_addition(self):
        add = addition('1')
        for i in range(10):
            question = add.generateQuestion()
            print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Addition Easy Tests Passed\n\n")

        add = addition('2')
        for i in range(10):
            question = add.generateQuestion()
            print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Addition Medium Tests Passed\n\n")

        add = addition('3')
        for i in range(10):
            question = add.generateQuestion()
            print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Addition Hard Tests Passed\n\n")

        print("All Addition Test Cases Passed\n\n")

    def test_subtraction(self):
        sub = subtraction('easy')
        for i in range(10):
            question = sub.generateQuestion()
            print(question[0], "Answer should be:", question[3])
            self.assertEqual(question[3], question[1] - question[2], "Test Failed, expected: {} got: {}".format(question[3], question[1] - question[2]))
            i += 1
        print("Subtraction Easy Tests Passed\n\n")

        sub = subtraction('medium')
        for i in range(10):
            question = sub.generateQuestion()
            print(question[0], "Answer should be:", question[3])
            self.assertEqual(question[3], question[1] - question[2], "Test Failed, expected: {} got: {}".format(question[3], question[1] - question[2]))
            i += 1
        print("Subtraction Medium Tests Passed\n\n")

        sub = subtraction('hard')
        for i in range(10):
            question = sub.generateQuestion()
            print(question[0], "Answer should be:", question[3])
            self.assertEqual(question[3], question[1] - question[2], "Test Failed, expected: {} got: {}".format(question[3], question[1] - question[2]))
            i += 1
        print("Subtraction Hard Tests Passed\n\n")

        print("All Subtraction Test Cases Passed\n\n")

    def test_multiplication(self):
        mult = multiplication('easy')
        for i in range(10):
            question = mult.generateQuestion()
            print(question[0], "Answer should be:", question[3])
            self.assertEqual(question[3], question[1] * question[2], "Test Failed, expected: {} got: {}".format(question[3], question[1] * question[2]))
            i += 1
        print("Multiplication Easy Tests Passed\n\n")

        mult = multiplication('medium')
        for i in range(10):
            question = mult.generateQuestion()
            print(question[0], "Answer should be:", question[3])
            self.assertEqual(question[3], question[1] * question[2], "Test Failed, expected: {} got: {}".format(question[3], question[1] * question[2]))
            i += 1
        print("Multiplication Medium Tests Passed\n\n")

        mult = multiplication('hard')
        for i in range(10):
            question = mult.generateQuestion()
            print(question[0], "Answer should be:", question[3])
            self.assertEqual(question[3], question[1] * question[2], "Test Failed, expected: {} got: {}".format(question[3], question[1] * question[2]))
            i += 1
        print("Multiplication Hard Tests Passed\n\n")

        print("All Multiplication Test Cases Passed\n\n")

    def test_division(self):
        div = division('easy')
        for i in range(10):
            question = div.generateQuestion()
            print(question[0], "Answer should be:", question[3])
            self.assertEqual(question[3], round(question[1] / question[2], 2), "Test Failed, expected: {} got: {}".format(question[3], round(question[1] / question[2], 2)))
            i += 1
        print("Division Easy Tests Passed\n\n")

        div = division('medium')
        for i in range(10):
            question = div.generateQuestion()
            print(question[0], "Answer should be:", question[3])
            self.assertEqual(question[3], round(question[1] / question[2], 2), "Test Failed, expected: {} got: {}".format(question[3], round(question[1] / question[2], 2)))
            i += 1
        print("Division Medium Tests Passed\n\n")

        div = division('hard')
        for i in range(10):
            question = div.generateQuestion()
            print(question[0], "Answer should be:", question[3])
            self.assertEqual(question[3], round(question[1] / question[2], 2), "Test Failed, expected: {} got: {}".format(question[3], round(question[1] / question[2], 2)))
            i += 1
        print("Division Hard Tests Passed\n\n")

        print("All Division Test Cases Passed\n\n")

    # Work in progress - define a range of + or -1 for the answer
    # def test_quadratic(self):
    #     quad = quadratic('easy')
    #     for i in range(10):
    #         question = quad.generateQuestion()
    #         print(question[0], "Answer should be:", question[4])
    #         if round(question[1]*question[4][0]*question[4][0] + question[2]*question[4][0] + question[3], 0) != 0.0:
    #             print("Test Failed, expected: {} got: {}".format(0, question[1]*question[4][0]*question[4][0] + question[2]*question[4][0] + question[3]))
    #         if round(question[1]*question[4][1]*question[4][1] + question[2]*question[4][0] + question[3], 0) != 0.0:
    #             print("Test Failed, expected: {} got: {}".format(0, question[1]*question[4][1]*question[4][1] + question[2]*question[4][1] + question[3]))
    #         i += 1
    #     print("Quadratic Easy Tests Passed\n\n")
            


    
            
if __name__ == '__main__':
    unittest.main()