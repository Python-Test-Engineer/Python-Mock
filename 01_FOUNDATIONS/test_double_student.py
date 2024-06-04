from datetime import date


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def calculate_age(cls, name, birth_year):
        # calculate age an set it as a age
        # return new object
        return cls(name, date.today().year - birth_year)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))


def test_student():
    jessa = Student("Jessa", 20)
    assert jessa.name == "Jessa"
    assert jessa.age == 20


if __name__ == "__main__":

    jessa = Student("Jessa", 20)
    jessa.show()

    # create new object using the factory method
    joy = Student.calculate_age("Joy", 1995)
    joy.show()
