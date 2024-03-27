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
        #Initializes the questionGeneration class with the questionType and difficulty
        self.questionType = questionType
        self.difficulty = difficulty

    def generateQuestion(self):
        #Generates a math question based on the questionType and difficulty
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
        #Generates an addition question based on the difficulty
        if self.difficulty == "easy":
            a = random.randint(0, 10)
            b = random.randint(0, 10)
        elif self.difficulty == "medium":
            a = random.randint(0, 100)
            b = random.randint(0, 100)
        elif self.difficulty == "hard":
            a = random.randint(0, 1000)
            b = random.randint(0, 1000)

        solution = a + b
        return [f"What is {a} + {b}?",a, b, solution]

    def subtraction(self):
        #Generates a subtraction question based on the difficulty
        if self.difficulty == "easy":
            a = random.randint(0, 10)
            b = random.randint(0, 10)
        elif self.difficulty == "medium":
            a = random.randint(0, 100)
            b = random.randint(0, 100)
        elif self.difficulty == "hard":
            a = random.randint(0, 1000)
            b = random.randint(0, 1000)

        solution = a - b
        return [f"What is {a} - {b}?", a, b, solution]

    def multiplication(self):
        #Generates a multiplication question based on the difficulty
        if self.difficulty == "easy":
            a = random.randint(0, 10)
            b = random.randint(0,10)
        elif self.difficulty == "medium":
            a = random.randint(0, 100)
            b = random.randint(0, 100)
        elif self.difficulty == "hard":
            a = random.randint(0, 1000)
            b = random.randint(0, 1000)

        solution = a * b
        return [f"What is {a} x {b}?", a, b, solution]

    def division(self):
        #Generates a division question based on the difficulty
        if self.difficulty == "easy":
            a = random.randint(0, 10)
            b = random.randint(1,10)
        elif self.difficulty == "medium":
            a = random.randint(0, 100)
            b = random.randint(1, 100)
        elif self.difficulty == "hard":
            a = random.randint(0, 1000)
            b = random.randint(1, 1000)

        solution = round(a / b, 2)
        return [f"What is {a} / {b}?\nRound to 2 decimal places", a, b, solution]
    
    def quadratic(self):
        #Generates a quadratic question based on the difficulty, done in this way to ensure that the roots are real numbers without use of an external library
        if self.difficulty == "easy":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            d = random.randint(1, 10)
        elif self.difficulty == "medium":
            a = random.randint(5, 15)
            b = random.randint(5, 15)
            c = random.randint(5, 15)
            d = random.randint(5, 15)
        elif self.difficulty == "hard":
            a = random.randint(5, 20)
            b = random.randint(5, 20)
            c = random.randint(5, 20)
            d = random.randint(5, 20)

        # from the form (ax + c)(bx + d), expand into ax^2 + bx + cx + d 
        first = a * b
        second = a * d + b * c
        third = c * d

        # roots are the solutions to the equation ax^2 + bx + cx + d = 0
        roots = [round((-c) / a, 2) , round((-d) / b, 2)]

        return [f"Find the roots of the function given by {first}x^2 + {second}x + {third}\nRound to 2 decimal places", first, second, third, roots]
            
    
    def linear(self):
        #Generates a linear question based on the difficulty
        if self.difficulty == "easy":
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = random.randint(1, 10)
            d = random.randint(1, 100)
        elif self.difficulty == "medium":
            a = random.randint(5, 15)
            b = random.randint(5, 15)
            c = random.randint(1, 15)
            d = random.randint(1, 100)
        elif self.difficulty == "hard":
            a = random.randint(5, 20)
            b = random.randint(5, 20)
            c = random.randint(1, 20)
            d = random.randint(1, 100)

        first = a * c * c / 2
        second = b * c
        constant = round(d - (first + second), 2)

        return f"Determine the integral of the function given by {a}x + {b}, use ∫({c}) = {d} to find C\nRound to 2 decimal places",a,b,f"{round(a/2, 2)}x^2, {b}x + {constant}"   
    
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