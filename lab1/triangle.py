import sys

ERROR_MSG = 'Неизвестная ошибка'
NOT_TRIANGLE_MSG = 'Не треугольник'
COMMON_TRIANGLE_MSG = 'Обычный'
ISOSCELES_TRIANGLE_MSG = 'Равнобедренный'
EQUILATERAL_TRIANGLE_MSG = 'Равносторонний'

def is_float(num):
    try:
        num = float(num)
        return True
    except ValueError:
        return False
    
def check_args(args):
    if len(args) < 3 or len(args) > 3:
        return False
    check_type = all([is_float(x) for x in args])
    if not check_type:
        return False
    args = [float(arg) for arg in args]
    check_border_value = all([x < sys.maxsize * 2 + 1 and x > 0.1 for x in args])
    if not check_border_value:
        return False    
    return True

def check_for_triangle(first_line, second_line, third_line):
    if first_line >= (second_line + third_line):
        return False
    if second_line >= (first_line + third_line):
        return False
    if third_line >= (first_line + second_line):
        return False
    return True
   
def get_triangle_type(first_line, second_line, third_line):
    if first_line == second_line == third_line:
        return EQUILATERAL_TRIANGLE_MSG
    if first_line == second_line or second_line == third_line or first_line == third_line:
        return ISOSCELES_TRIANGLE_MSG
    return COMMON_TRIANGLE_MSG

def main(args):
    if not check_args(args):
        return ERROR_MSG
    args = [float(arg) for arg in args]
    if not check_for_triangle(args[0], args[1], args[2]):
        return NOT_TRIANGLE_MSG
    return get_triangle_type(args[0], args[1], args[2])

args = sys.argv
args.pop(0)
print(main(args))