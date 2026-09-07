# Superclass
class Instrument:

    def __init__(self, name, instrument_type):
        self.name = name
        self.type = instrument_type

    def __str__(self):
        return f"Instrument: {self.name}, type: {self.type}"

    def play(self):
        print(f"{self.name} is being played...")


# Subclass
class Guitar(Instrument):

    def __init__(self, name, number_of_strings):
        super().__init__(name, "String")
        self.number_of_strings = number_of_strings

    def __str__(self):
        return f"Guitar: {self.name}, strings: {self.number_of_strings}"

    def strum(self):
        print(f"{self.name} is strummed: Strum Strum!")


# Subclass
class Drum(Instrument):

    def __init__(self, name, has_cymbal):
        super().__init__(name, "Percussion")
        self.has_cymbal = has_cymbal

    def __str__(self):
        cymbal = "Yes" if self.has_cymbal else "No"
        return f"Drum: {self.name}, cymbal: {cymbal}"

    def hit(self):
        print(f"{self.name} is being hit: Boom Boom!")


# NEW SUBCLASS
class Flute(Instrument):

    def __init__(self, name, material):
        super().__init__(name, "Wind")
        self.material = material

    def __str__(self):
        return f"Flute: {self.name}, material: {self.material}"

    def blow(self):
        print(f"{self.name} is playing: Tuu Tuu 🎵")


# Main Class
class MusicTest:

    @staticmethod
    def test():

        instruments = [
            Guitar("Fender", 6),
            Drum("Yamaha", True),
            Flute("Yamaha Flute", "Silver")
        ]

        for instrument in instruments:

            print(instrument)

            instrument.play()

            if isinstance(instrument, Guitar):
                instrument.strum()

            elif isinstance(instrument, Drum):
                instrument.hit()

            elif isinstance(instrument, Flute):
                instrument.blow()

            print()


if __name__ == "__main__":
    MusicTest.test()