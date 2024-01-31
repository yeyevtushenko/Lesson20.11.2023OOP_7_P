class User:
    def __init__(self, name, age):
        self.name = name
        self._age = None
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 0 <= value <= 120:
            self._age = value
        else:
            raise ValueError("Invalid age. Age must be between 0 and 120.")

    def display_user_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


name = input("Enter user name: ")
age = int(input("Enter user age: "))

user = User(name=name, age=age)


try:
    new_age = int(input("Enter new age: "))
    user.age = new_age
except ValueError as e:
    print(e)


user.display_user_info()