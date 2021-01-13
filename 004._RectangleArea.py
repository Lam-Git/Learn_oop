class RectangleArea:
    def __init__(self):  # user can input their own numbers when variable = 0
        self.length = 0
        self.width = 0

    def set_parameters(
        self, input_length, input_width
    ):  # instance method with the set rules
        self.length = float(input_length)
        self.width = float(input_width)

    def get_area(self):  # getter
        return self.length * self.width


if __name__ == "__main__":
    input_length = input("Please key in the length:")
    input_width = input("Please key in the width:")
    rectangle = RectangleArea()  # assigning the variable to the Class
    rectangle.set_parameters(
        input_length, input_width
    )  # assigning the dot-notion to the new variable to the setter method
    print(rectangle.get_area())  # print
