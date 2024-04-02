import unittest
from lab6 import ComplexNumber

class TestComplexNumber(unittest.TestCase):
    def setUp(self):
        #arrange
        self.num1 = ComplexNumber(3, 4)
        self.num2 = ComplexNumber(2, -3)                   
    def test_addition(self):
        #arrange
        result = None
        #act
        result = self.num1 + self.num2
        #assert
        self.assertEqual(result.to_str(), "5 + 1i", 'error with addition 2 complex numbers')

    def test_mutable_addition(self):
        #arrange
        result = ComplexNumber(4, -5)
        #act
        result += self.num1
        #assert
        self.assertEqual(result.to_str(), "7 - 1i", 'error with addition 2 complex numbers')

    def test_addition_with_exception(self):
        #arrange               
        def sum():
            #act
            result = self.num1 + 12
        #assert
        with self.assertRaises(ArithmeticError, msg='error with exception of addition complex number and non comlex number'):
            sum()

    def test_subtraction(self):        
        #arrange
        result = None
        #act
        result = self.num1 - self.num2
        #assert
        self.assertEqual(result.to_str(), "1 + 7i", 'error with substraction 2 complex numbers')

    def test_mutable_subtraction(self):
        #arrange
        result = ComplexNumber(4, -5)
        #act
        result -= self.num1
        #assert
        self.assertEqual(result.to_str(), "1 - 9i", 'error with substraction 2 complex numbers')

    def test_subtraction_with_exception(self):
        #arrange
        def sub():
            #act
            result = self.num1 - 12
        #assert
        with self.assertRaises(ArithmeticError, msg='error with exception of substraction complex number and non comlex number'):
            sub()

    def test_multiplication(self):
        #arrange
        result = None
        #act
        result = self.num1 * self.num2
        #assert
        self.assertEqual(result.to_str(), "18 - 1i", 'error with multiplication 2 complex numbers')

    def test_mutable_multiplication(self):
        #arrange
        result = ComplexNumber(4, -5)
        #act
        result *= self.num1
        #assert
        self.assertEqual(result.to_str(), "32 + 1i", 'error with multiplication 2 complex numbers')

    def test_multiplication_with_exception(self):
        #arrange        
        def mul():
            #act
            result = self.num1 * 12
        #assert        
        with self.assertRaises(ArithmeticError, msg='error with exception of multiplication complex number and non comlex number'):
            mul()

    def test_divine(self):
        #arrange
        result = None
        #act
        result = self.num1 / self.num2
        #assert        
        self.assertEqual(result.real_part, -6/13, 'error with real part of divine 2 complex numbers')
        self.assertEqual(result.imaginary_part, 17/13, 'error with imaginary part of divine 2 complex numbers')

    def test_mutable_divine(self):
        #arrange
        result = ComplexNumber(4, -5)
        #act
        result /= self.num1
        #assert        
        self.assertEqual(result.real_part, -8/25, 'error with real part of divine 2 complex numbers')
        self.assertEqual(result.imaginary_part, -31/25, 'error with imaginary part of divine 2 complex numbers')
        # self.assertEqual(result.to_str(), " + 1i")

    def test_divine_with_exception(self):
        #arrange
        def div():
            #act
            result = self.num1 / 12
        #assert
        with self.assertRaises(ArithmeticError, msg='error with exception of divine complex number and non comlex number'):
            div()
            
    def test_divine_with_zero_divine_exception(self):
        #arrange
        def div():
            #act
            result = self.num1 / ComplexNumber(0, 0)
        #assert
        with self.assertRaises(ZeroDivisionError, msg='error with exception of divine complex number and zero'):
            div()

    def test_str_representation(self):
        #assert
        self.assertEqual(self.num1.to_str(), "3 + 4i", 'error with str representation of complex number')
        self.assertEqual(self.num2.to_str(), "2 - 3i", 'error with str representation of complex number')

    def test_equality(self):
        #arrange
        num1_copy = ComplexNumber(3, 4)
        #assert
        self.assertEqual(self.num1, num1_copy, 'error with equality 2 complex number')
    
    def test_equality_with_exception(self):
        #arrage
        def eq():
            #act
            result = self.num1 == 12
        #assert
        with self.assertRaises(ArithmeticError, msg='error with exception of equality of complex number and non complex'):
            eq()