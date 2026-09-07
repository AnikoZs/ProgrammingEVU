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


# Main Class
class MusicTest:

    @staticmethod
    def test():

        # Polymorphism:
        # Both variables are stored as Instrument objects
        instruments = [
            Guitar("Fender", 6),
            Drum("Yamaha", True)
        ]

        for instrument in instruments:

            print(instrument)

            # Inherited method
            instrument.play()

            # Type checking
            if isinstance(instrument, Guitar):
                instrument.strum()

            elif isinstance(instrument, Drum):
                instrument.hit()

            print()


if __name__ == "__main__":
    MusicTest.test()
