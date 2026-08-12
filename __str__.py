class EEquip_01:
    def __init__(self, brand):
        self.brand = brand

Oscilloscope = EEquip_01("Siglent")
print(Oscilloscope)

########################################

class EEquip_02:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return f"{self.brand}"
    
Oscilloscope = EEquip_02("Siglent")
print(Oscilloscope)

###########################################

class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    temp = self.width * self.height
    return f"{temp}"

  def area(self):
    __str__(self)

r1 = Rectangle(5, 3)
print(r1)
