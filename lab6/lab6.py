class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real_part = real_part
        self.imaginary_part = imaginary_part

    def to_str(self):
        if self.imaginary_part >= 0:
            return f"{self.real_part} + {self.imaginary_part}i"
        else:
            return f"{self.real_part} - {abs(self.imaginary_part)}i"

    def __add__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ArithmeticError('The right operand must be of the type ComplexNumber')
        real_part_sum = self.real_part + other.real_part
        imaginary_part_sum = self.imaginary_part + other.imaginary_part
        return ComplexNumber(real_part_sum, imaginary_part_sum)

    def __sub__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ArithmeticError('The right operand must be of the type ComplexNumber')
        real_part_diff = self.real_part - other.real_part
        imaginary_part_diff = self.imaginary_part - other.imaginary_part
        return ComplexNumber(real_part_diff, imaginary_part_diff)

    def __mul__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ArithmeticError('The right operand must be of the type ComplexNumber')
        real_part = self.real_part * other.real_part - self.imaginary_part * other.imaginary_part
        imaginary_part = self.real_part * other.imaginary_part + self.imaginary_part * other.real_part
        return ComplexNumber(real_part, imaginary_part)
    
    def __truediv__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ArithmeticError('The right operand must be of the type ComplexNumber')
        sum_quadro =  other.real_part**2 + other.imaginary_part**2
        real_part = (self.real_part * other.real_part + self.imaginary_part * other.imaginary_part) / sum_quadro
        imaginary_part = (self.imaginary_part * other.real_part - self.real_part * other.imaginary_part) / sum_quadro
        return ComplexNumber(real_part, imaginary_part)
    
    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            raise ArithmeticError('The right operand must be of the type ComplexNumber')
        return self.real_part == other.real_part and self.imaginary_part == other.imaginary_part