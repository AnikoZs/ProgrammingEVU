class BottleSong:
    # Constructor
    def __init__(self, bottles):
        self.bottles = bottles

    # Method that sings the bottle song
    def sing(self):

        # Continue while there are bottles left
        while self.bottles > 0:
            print(
                f"{self.bottles} bottles of soda on the wall, "
                f"{self.bottles} bottles of soda!"
            )

            # Remove one bottle
            self.bottles -= 1

            print(
                f"Take one down, pass it around, "
                f"{self.bottles} bottles of soda on the wall.\n"
            )

        # No bottles left
        print("No more bottles of soda on the wall!")


class BottleSongTest:

    @staticmethod
    def test():
        # Create a BottleSong object starting with 5 bottles
        song = BottleSong(5)

        # Start singing
        song.sing()


# Start the program
BottleSongTest.test()