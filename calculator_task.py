# Calculator Task

class Calculator:
    def __init__(self):
        pass
    def addition(self, int1, int2):
        return int1 + int2
    def subtraction(self, int1, int2):
        return int1 - int2
    def multiplication(self, int1, int2):
        return int1 * int2

    def division(self, int1, int2):
        if int2 != 0:
            return int1 / int2
        else:
            return "Error"

    def modulus(self, int1, int2):
        return int1 % int2

calc = Calculator()
result_add = calc.addition(5, 10)
print("Addition:", result_add)

result_sub = calc.subtraction(12, 5)
print("Subtraction:", result_sub)

result_mul = calc.multiplication(10, 5)
print("multiplication:", result_mul)

result_div = calc.division(12, 6)
print("division:", result_div)

result_mod = calc.modulus(10, 5)
print("modulus:", result_mod)
