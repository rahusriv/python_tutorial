class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    def get_temperature(self):
        print("Getting value")
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        print("Setting value")
        self._temperature = value

    temperature = property(get_temperature,set_temperature)

if __name__ == '__main__':
    c = Celsius()
    print(c.temperature)
    c.temperature = 37
    print(c.to_fahrenheit())
    #c._temperature = -300
    #print(c.get_temperature())

