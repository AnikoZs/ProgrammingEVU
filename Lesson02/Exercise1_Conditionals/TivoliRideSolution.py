class TivoliRide:
    def __init__(self, min_height):
        self.min_height = min_height

    def check_height(self, height):

        # Øvelse 2:
        # Skift navnet på forlystelsen fra
        # "LoopMaster 3000" til "Vilde Vulkan!"
        print("Velkommen til Vilde Vulkan!")

        # Kontroller om gæsten er høj nok
        if height >= self.min_height:

            print("Du er høj nok! Hop ombord")

            # Øvelse 3:
            # Tilføj en ekstra besked til gæster,
            # der får lov til at prøve forlystelsen
            print("God tur!")

            # Øvelse 4:
            # Hvis gæsten er mellem 120 og 150 cm
            # (begge tal inklusive), skal der vises
            # en ekstra besked om et grønt armbånd.
            if 120 <= height <= 150:
                print("Du får et grønt armbånd!")

            # Øvelse 6:
            # Hvis gæsten er mindst 180 cm høj,
            # skal der vises en VIP-besked.
            if height >= 180:
                print("Du får en VIP-plads!")

        else:
            print(f"Beklager, du skal være mindst {self.min_height} cm høj")


# Øvelse 5:
# Spørg brugeren om navn.
name = input("Indtast dit navn: ")

# Vis en personlig velkomst.
print(f"Velkommen {name}!")


# Øvelse 1:
# Ændr minimumshøjden fra 140 cm til 120 cm.
ride = TivoliRide(120)


# Spørg brugeren om højden.
height = int(input("Indtast din højde i cm: "))

# Kør højdekontrollen.
ride.check_height(height)