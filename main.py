class Multiplier:
    def __init__(self, multiplier):
        self.multiplier = multiplier

    def multiply(self, value):
        return value * self.multiplier


multiplier_instance = Multiplier(5)


result = multiplier_instance.multiply(10)
print(result)