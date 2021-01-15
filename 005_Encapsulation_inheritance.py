# encapsulation involving setter/getter as with public/private variable
class Person:
    def __init__(self, fname, email):
        self.first_name = fname  # public variable
        self.__email = email  # private variable ( __ double )

    def update_email(self, email):  # instance method that set a new email
        self.__email = email

    def get_email(self):
        return self.__email


thien = Person("Thien", "Tn@gmail.com")  # instance option
print(thien.first_name, thien.get_email())
thien.update_email("BabyT@apple.com")  # assinging a new email
print(thien.get_email())  # print the new email.

# encapsulation 2


class Person:
    def __init__(self, fname, age):
        self.first_name = fname
        self.age = age

    def show_age(self):  # setter
        return (
            self._get_age()
        )  # here function is private and cannot be reached externally

    def _get_age(self):  # getter
        return self.age


joe = Person("Joe", 20)
print(joe.first_name, joe.show_age())


# example of inheritance
class Car:
    def __init__(self, num_of_wheels, seating_capacity, max_velocity):
        self.num_of_wheels = num_of_wheels
        self.seating_capacity = seating_capacity
        self.max_velocity = max_velocity

    def make_noise(self):
        print("YeeHaaaa!")


class ElectricCar(Car):
    def __init__(self, num_of_wheels, seating_capacity, max_velocity, battery):
        # Car.__init__(self, num_of_wheels, seating_capacity, max_velocity)
        super().__init__(
            num_of_wheels, seating_capacity, max_velocity
        )  # use super() to obtain the class Class
        self.battery = battery
        self.state = ""

    def sold_in_state(self, sold_state):
        self.state = sold_state


electricCar = ElectricCar(4, 5, 250, "1000V")  # the last value goes under the battery.
electricCar.sold_in_state("CA")
electricCar.make_noise()
print(electricCar.num_of_wheels)
print(electricCar.battery)
print(electricCar.state)
