class SpaceMissionSolution:

    # The main "method" (entry point in our program)
    def run(self):
        # Create an object of the class
        mission = self

        # Call methods
        mission.print_title()
        mission.print_astronaut_info()

    # This method prints a title
    def print_title(self):
        # Print lines
        print("================================")
        print("  Andreas Mogensen's Space Trip ")
        print("================================")

        # Print empty line
        print()

    # This method prints astronaut information
    def print_astronaut_info(self):

        # Variables with astronaut information
        name = "Andreas Mogensen"
        nationality = "Danish"
        mission = "International Space Station (ISS)"

        # Print data
        print("Astronaut name:", name)
        print("Nationality:", nationality)
        print('Mission: "' + mission + '"')

        print()  # empty line

        print("Message from space:")
        print('"Hello Earth! I am coding from space!"')


# Start program
app = SpaceMissionSolution()
app.run()
