import math

class Circle01:
    def __init__(self, radius):
        self.radius = radius  # konstruktør

    # Beregn areal
    def beregn_areal(self):
        return math.pi * self.radius ** 2


