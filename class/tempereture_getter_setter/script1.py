class Celsius:
    def __init__(self, temperature = 0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

if __name__ == '__main__':
    man = Celsius()
    man.temperature = -3457
    print(man.temperature)
    print(man.to_fahrenheit())
    print(man.__dict__)