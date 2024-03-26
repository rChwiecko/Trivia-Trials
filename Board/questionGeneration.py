# Description: This file contains the questionGeneration class and its subclasses

import random
import math
# import sympy
# import numpy as np

class questionGeneration:
    '''Class questionGeneration is used to generate math questions
    Subclasses of questionGeneration are used to generate questions of different types
    Subclasses of questionGeneration include:
        - addition
        - subtraction
        - multiplication
        - division
        - exponentiation for bit manipulation // scrapped
        - quadratic equations
        - linear equations

    '''
    def __init__(self, questionType, difficulty):
        '''Initializes the questionGeneration class with the questionType and difficulty'''
        self.questionType = questionType
        self.difficulty = difficulty

    def generateQuestion(self):
        '''Generates a math question based on the questionType and difficulty'''
        if self.questionType == "addition":
            return self.addition()
        elif self.questionType == "subtraction":
            return self.subtraction()
        elif self.questionType == "multiplication":
            return self.multiplication()
        elif self.questionType == "division":
            return self.division()
        elif self.questionType == "exponentiation":
            return self.exponentiation()
        elif self.questionType == "quadratic":
            return self.quadratic()
        elif self.questionType == "linear":
            return self.linear()

    def addition(self):
        '''Generates an addition question based on the difficulty'''
        if self.difficulty == "easy":
            return [random.randint(0, 10), random.randint(0, 10)]
        elif self.difficulty == "medium":
            return [random.randint(0, 100), random.randint(0, 100)]
        elif self.difficulty == "hard":
            return [random.randint(0, 1000), random.randint(0, 1000)]

    def subtraction(self):
        '''Generates a subtraction question based on the difficulty'''
        if self.difficulty == "easy":
            return [random.randint(0, 10), random.randint(0, 10)]
        elif self.difficulty == "medium":
            return [random.randint(0, 100), random.randint(0, 100)]
        elif self.difficulty == "hard":
            return [random.randint(0, 1000), random.randint(0, 1000)]

    def multiplication(self):
        '''Generates a multiplication question based on the difficulty'''
        if self.difficulty == "easy":
            return [random.randint(0, 10), random.randint(0,10)]
        elif self.difficulty == "medium":
            return [random.randint(0, 100), random.randint(0, 100)]
        elif self.difficulty == "hard":
            return [random.randint(0, 1000), random.randint(0, 1000)]
        
    def division(self):
        '''Generates a division question based on the difficulty'''
        if self.difficulty == "easy":
            return [random.randint(0, 10), random.randint(1,10)]
        elif self.difficulty == "medium":
            return [random.randint(0, 100), random.randint(1, 100)]
        elif self.difficulty == "hard":
            return [random.randint(0, 1000), random.randint(1, 1000)]
        
    def quadratic(self):
        '''Generates a quadratic question based on the difficulty'''
        if self.difficulty == "easy":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
        elif self.difficulty == "medium":
            a = random.randint(1, 100)
            b = random.randint(1, 100)
            c = random.randint(1, 100)
        elif self.difficulty == "hard":
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
            c = random.randint(1, 1000)

        
        return f"Find the roots of the function given by {a}x^2 + {b}x + {c}"
    
    def linear(self):
        '''Generates a linear question based on the difficulty'''
        if self.difficulty == "easy":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
        elif self.difficulty == "medium":
            a = random.randint(1, 100)
            b = random.randint(1, 100)
        elif self.difficulty == "hard":
            a = random.randint(1, 1000)
            b = random.randint(1, 1000)
        return [a, b]
    
class addition(questionGeneration):
    '''Subclass of questionGeneration that generates addition questions'''
    def __init__(self, difficulty):
        '''Initializes the addition class with the difficulty'''
        super().__init__("addition", difficulty)

class subtraction(questionGeneration):
    '''Subclass of questionGeneration that generates subtraction questions'''
    def __init__(self, difficulty):
        '''Initializes the subtraction class with the difficulty'''
        super().__init__("subtraction", difficulty)

class multiplication(questionGeneration):
    '''Subclass of questionGeneration that generates multiplication questions'''
    def __init__(self, difficulty):
        '''Initializes the multiplication class with the difficulty'''
        super().__init__("multiplication", difficulty)

class division(questionGeneration):
    '''Subclass of questionGeneration that generates division questions'''
    def __init__(self, difficulty):
        '''Initializes the division class with the difficulty'''
        super().__init__("division", difficulty)


# scrapped idea
# class exponentiation(questionGeneration):
#     '''Subclass of questionGeneration that generates exponentiation questions'''
#     def __init__(self, difficulty):
#         '''Initializes the exponentiation class with the difficulty'''
#         super().__init__("exponentiation", difficulty)
        

class quadratic(questionGeneration):
    '''Subclass of questionGeneration that generates quadratic questions'''
    def __init__(self, difficulty):
        '''Initializes the quadratic class with the difficulty'''
        super().__init__("quadratic", difficulty)

class linear(questionGeneration):
    '''Subclass of questionGeneration that generates linear questions'''
    def __init__(self, difficulty):
        '''Initializes the linear class with the difficulty'''
        super().__init__("linear", difficulty)


q = questionGeneration("addition", "easy")
print(q.generateQuestion())

        
