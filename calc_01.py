class Calculator_01:
    def add(self, a, b):
        return (a + b)
    def sub(self, a, b):
        return (a - b)
    def mul(self, a, b):
        return (a * b)
    def div(self, a, b):
        try:
            return (a / b)
        except:
            print("ERROR : DIV by ZERO !  ", end="`)

calc = Calculator_01()  ### do not forget ()  ()  ()  !! 
print(calc.add(3, 78))
print(calc.sub(79, 35))
print(calc.mul(31, 7))
print(calc.div(4,0))
print(calc.div(24, 4))
