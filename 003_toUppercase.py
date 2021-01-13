class ToUpperCase:
    def __init__(self, input_string="hello world"):
        self.input_string = input_String

    def set_String(self, inputString):  # this is setter
        self.input_string = inputString

    def print_String(self):
        return self.input_string.upper()


if __name__ == "__main__":
    input_String = input(
        "Please key in your string: "
    )  # variable and function use snake_to_case
    toUpperString = ToUpperCase()  # instance use camelCase
    toUpperString.set_String(input_String)
    print(toUpperString.print_String())
