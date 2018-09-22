class Celsius:
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

    # new update
    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible")
        self._temperature = value

if __name__ == '__main__':
    #c = Celsius(-277)
    c = Celsius(37)
    print(c.get_temperature())
    c.set_temperature(10)
    #c.set_temperature(-300)
    #c._temperature = -300
    #print(c.get_temperature())