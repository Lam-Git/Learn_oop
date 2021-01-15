# single inheritance 1
class Rectangle:  # Blueprint
    def __init__(self, length, width):  # instance attributes #initializer
        self.length = length
        self.width = width

    def area(self):  # instance method
        return self.length * self.width

    def circumstance(self):
        return (self.length + self.width) * 2


class Square(Rectangle):  # inheritance
    def __init__(self, length):  # initialize
        super().__init__(length, length)  # super to call the main parent class

    def isSquare(
        self,
    ):  # instance method to check if the two variable equal one another
        return self.length == self.width


class Cube(Square):
    # don't have an initialize
    def surfaceArea(self):
        self.face_area = super(Cube, self).area()  # super(thisClass,self) = super()
        return self.face_area * 6

    def volume(self):
        return self.length * self.face_area


length = int(input("Please key in the length:"))
square = Square(length)  # instance object
print(square.area())  # dot notation
print(square.circumstance())
print(square.isSquare())
cube = Cube(length)  # instance object for class Cube
print(cube.surfaceArea())
print(cube.volume())
print("------------")
print(Cube.__mro__)  # this is to check method resolution order

