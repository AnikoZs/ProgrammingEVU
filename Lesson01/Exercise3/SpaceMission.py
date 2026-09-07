class SpaceMission:

    def print_title(self):
        print("================================")
        print("  Andreas Mogensen's Space Trip ")
        print("================================\n")

    def print_astronaut_info(self):
        name = "Andreas Mogensen"
        nationality = "Danish"
        mission = "International Space Station (ISS)"

        print("Astronaut name:", name)
        print("Nationality:", nationality)
        print('Mission: "' + mission + '"')
        print("\nMessage from space:")
        print('"Hello Earth! I am coding from space!"')


# Main program
mission = SpaceMission()

mission.print_title()
mission.print_astronaut_info()