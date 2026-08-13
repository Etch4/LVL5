def addthumpsup(func):
  def myinner():
    return func() + " \U0001F44D"
  return myinner

class EEquip_00:
    pass

Oscilloscope = EEquip_00
@addthumpsup
def dummy():
    EEquip_00 = "Siglent(SDS2104)_00"
    return EEquip_00

print(dummy())

#######################################

class EEquip_01:
    def __init__(self, brand):
        self.brand = brand

@addthumpsup
def dummy():
    Oscilloscope = EEquip_01("Siglent(SDS2104)_01")
    return Oscilloscope.brand

print(dummy())

#######################################

class EEquip_02:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return f"{self.brand}"

@addthumpsup
def dummy():
    Oscilloscope = EEquip_02("Siglent(SDS2104)_02")
    return Oscilloscope.brand
print(dummy())

#######################################

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height
  def area(self):
     return self.width * self.height  
  
@addthumpsup
def dummy():
    r1 = Rectangle(5, 3)
    return f"{r1.area()}"
print(dummy())
