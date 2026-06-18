class Shape:
    def calculate_area(self, length, width):
        return length * width


# Your original classes stay the same
class parent:
    def __init__(self, bran, model, fuel, color):
        self.bran = bran
        self.model = model
        self.fuel = fuel
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, new_color):
        self.color = new_color
        return self.color

    def showCar(self):
        print("hi i am a car of brand {}, model {}, fuel {}, color {}".format(
            self.bran, self.model, self.fuel, self.color
        ))


class child(parent):
    def __init__(self, bran, model, fuel, color, year, transmission, turbo):
        super().__init__(bran, model, fuel, color)
        self.year = year
        self.transmission = transmission
        self.turbo = turbo

    def showcar(self):
        print("hi i am a car of brand {}, model {}, fuel {}, color {}, year {}, transmission {}, turbo {}".format(
            self.bran, self.model, self.fuel, self.color,
            self.year, self.transmission, self.turbo
        ))


mini = child("mini", "cooper", "petrol", "red", "2018", "automatic", "no")
shape = Shape()

print("Area:", shape.calculate_area(10, 4))
