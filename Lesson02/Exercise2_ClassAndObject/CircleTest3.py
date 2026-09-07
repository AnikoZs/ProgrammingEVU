import math

class Circle01:
    def __init__(self, radius):
        self.radius = radius

    def beregn_areal(self):
        return math.pi * self.radius ** 2


def main():
    circle_areal()


def circle_areal():
    # Opret cirkler
    c1 = Circle01(5)
    c2 = Circle01(10)

    # Beregn arealer
    areal1 = c1.beregn_areal()
    areal2 = c2.beregn_areal()

    # Udskriv og vurder cirkel 1
    print("Areal af cirkel 1:", areal1)
    if areal1 > 100:
        print("Cirklen 1 er stor!")
    else:
        print("Cirklen 1 er lille.")

    # Udskriv og vurder cirkel 2
    print("Areal af cirkel 2:", areal2)
    if areal2 > 100:
        print("Cirklen 2 er stor!")
    else:
        print("Cirklen 2 er lille.")


if __name__ == "__main__":
    main()
