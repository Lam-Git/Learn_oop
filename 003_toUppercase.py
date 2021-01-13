class ToUpperCase:  # blueprint
    def __init__(self, input_string="hello world"):  # instancate attribute
        self.input_string = input_String

    def set_String(self, inputString):  # this is setter /instance method
        self.input_string = inputString

    def print_String(self):  # this instance is set to print (.upper)
        return self.input_string.upper()


if __name__ == "__main__":
    # when the interpreter runs a module, the __name__ variable will be set as __main__if the module that is being run is the main program. //// if the code is importing the module from another module, then the __name__ variable will be set to that module's name.

    input_String = input(
        "Please key in your string: "
    )  # variable and function use as the
    toUpperString = ToUpperCase()  # instance use camelCase variable = to the main Class
    toUpperString.set_String(
        input_String
    )  # variable .dot notion with (input_String) Leading question
    print(toUpperString.print_String())  # print
