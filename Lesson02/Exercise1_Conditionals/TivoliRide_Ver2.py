# tivoli_ride.py

class TivoliRide:
    def __init__(self, min_height):
        self.min_height = min_height

    def check_height(self, height):
        print("Velkommen til LoopMaster 3000!")

        if height >= self.min_height:
            print("Du er høj nok! Hop ombord")
        else:
            print(f"Beklager, du skal være mindst {self.min_height} cm høj")


# Test
ride = TivoliRide(140)

ride.check_height(145)  # Test: høj nok
print()

ride.check_height(130)  # Test: ikke høj nok