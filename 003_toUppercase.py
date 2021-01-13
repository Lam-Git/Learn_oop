class ToUpperCase:  # blueprint
    def __init__(self, input_string="Hello World"):  # instancate attribute
        self.input_string = input_String

    def set_String(self, input_String):  # setter/ instance method
        self.input_string = input_String

    def print_String(self):
        return self.input_string.upper()


if __name__ == " __main__":
    input_String = input("Please key in your string:")  # variable and function use
    toUpperString = ToUpperCase()  # instance use camelCase
    toUpperString.set_String(input_String)
    print(toUpperString.print_String())
