'''
Description: This file contains the test cases for the questionGeneration module.
Author: Arjun'''

import unittest
from questionGeneration import *

class TestQuestionGeneration(unittest.TestCase):
    def test_addition(self):
        add = addition('1')
        for i in range(10):
            question = add.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Addition Easy Tests Passed\n\n")

        add = addition('2')
        for i in range(10):
            question = add.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Addition Medium Tests Passed\n\n")

        add = addition('3')
        for i in range(10):
            question = add.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Addition Hard Tests Passed\n\n")

        print("All Addition Test Cases Passed\n\n")

    def test_subtraction(self):
        sub = subtraction('1')
        for i in range(10):
            question = sub.generateQuestion()
            # print(question[0], "Answer is", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Subtraction Easy Tests Passed\n\n")

        sub = subtraction('2')
        for i in range(10):
            question = sub.generateQuestion()
            # print(question[0], "Answer is", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Subtraction Medium Tests Passed\n\n")

        sub = subtraction('3')
        for i in range(10):
            question = sub.generateQuestion()
            # print(question[0], "Answer is", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Subtraction Hard Tests Passed\n\n")

        print("All Subtraction Test Cases Passed\n\n")

    def test_multiplication(self):
        mult = multiplication('1')
        for i in range(10):
            question = mult.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Multiplication Easy Tests Passed\n\n")

        mult = multiplication('2')
        for i in range(10):
            question = mult.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Multiplication Medium Tests Passed\n\n")

        mult = multiplication('3')
        for i in range(10):
            question = mult.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], int, "Test Failed, expected question[3] to be an integer")
            i += 1
        print("Multiplication Hard Tests Passed\n\n")

        print("All Multiplication Test Cases Passed\n\n")

    def test_division(self):
        div = division('1')
        for i in range(10):
            question = div.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], float, "Test Failed, expected question[3] to be a float")
            i += 1
        print("Division Easy Tests Passed\n\n")

        div = division('2')
        for i in range(10):
            question = div.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], float, "Test Failed, expected question[3] to be a float")
            i += 1
        print("Division Medium Tests Passed\n\n")

        div = division('3')
        for i in range(10):
            question = div.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], float, "Test Failed, expected question[3] to be a float")
            i += 1
        print("Division Hard Tests Passed\n\n")

        print("All Division Test Cases Passed\n\n")

    def test_quadratic(self):
        quad = quadratic('1')
        for i in range(10):
            question = quad.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], list, "Test Failed, expected question[3] to be an array")
            i += 1
        print("Quadratic Easy Tests Passed\n\n")

        quad = quadratic('2')
        for i in range(10):
            question = quad.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], list, "Test Failed, expected question[3] to be an array")
            i += 1
        print("Quadratic Medium Tests Passed\n\n")

        quad = quadratic('3')
        for i in range(10):
            question = quad.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], list, "Test Failed, expected question[3] to be an array")
            i += 1
        print("Quadratic Hard Tests Passed\n\n")

        print("All Quadratic Test Cases Passed\n\n")
            
    def test_linear(self):
        linearq = linear("1")
        for i in range(10):
            question = linearq.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], str, "Test Failed, expected question[3] to be an string")
            i += 1
        print("Linear Easy Tests Passed\n\n")

        linearq = linear("2")
        for i in range(10):
            question = linearq.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], str, "Test Failed, expected question[3] to be an string")
            i += 1
        print("Linear Medium Tests Passed\n\n")

        linearq = linear("3")
        for i in range(10):
            question = linearq.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], str, "Test Failed, expected question[3] to be an string")
            i += 1
        print("Linear Hard Tests Passed\n\n")

        print("All Linear Test Cases Passed\n\n")

    def test_superscaryfluidDynamics(self):
        fluid = fluidDynamics("1")
        for i in range(10):
            question = fluid.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], float, "Test Failed, expected question[3] to be a float")
            i += 1
        print("Fluid Dynamics Easy Tests Passed\n\n")

        fluid = fluidDynamics("2")
        for i in range(10):
            question = fluid.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], float, "Test Failed, expected question[3] to be a float")
            self.assertIsInstance(question[4], float, "Test Failed, expected question[4] to be a float")
            i += 1
        print("Fluid Dynamics Medium Tests Passed\n\n")

        fluid = fluidDynamics("3")
        for i in range(10):
            question = fluid.generateQuestion()
            # print(question[0], "Answer is:", question[3])
            self.assertIsInstance(question[0], str, "Test Failed, expected question[0] to be a string")
            self.assertIsInstance(question[1], str, "Test Failed, expected question[1] to be a string")
            self.assertIsInstance(question[2], str, "Test Failed, expected question[2] to be a string")
            self.assertIsInstance(question[3], float, "Test Failed, expected question[3] to be a float")
            i += 1
        print("Fluid Dynamics Hard Tests Passed\n\n")

        print("All Fluid Dynamics Test Cases Passed\n\n")
        
            
if __name__ == '__main__':
    unittest.main()