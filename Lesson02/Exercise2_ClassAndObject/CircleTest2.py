from Lesson02.Exercise2_ClassAndObject.Circle import Circle01


# "main" funktion
def main():
    opret_cirkler()


def opret_cirkler():
    # Opret cirkler
    c1 = Circle01(5)
    udskriv_arealer(c1)

    c2 = Circle01(10)
    udskriv_arealer(c2)


def udskriv_arealer(c):
    # Udskriv arealer
    print("Areal af cirkel:", c.beregn_areal())


# Kør programmet
if __name__ == "__main__":
    main()
