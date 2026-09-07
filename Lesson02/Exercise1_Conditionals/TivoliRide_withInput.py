class TivoliRide:
    def __init__(self, min_height):
        self.min_height = min_height

    def check_height(self, height):
        print("Velkommen til LoopMaster 3000!")

        if height >= self.min_height:
            print("Du er høj nok! Hop ombord")
        else:
            print(f"Beklager, du skal være mindst {self.min_height} cm høj")


ride = TivoliRide(140)

height = int(input("Indtast din højde i cm: "))
ride.check_height(height)