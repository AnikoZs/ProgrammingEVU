from Lesson04.Exercise3_List.Athlete import Athlete


class AthleteTest:

    @staticmethod
    def main():
        # Create a list of athletes
        athletes = [
            Athlete("Alex"),
            Athlete("Maria"),
            Athlete("Jonas")
        ]

        # Use a for loop to call methods
        for athlete in athletes:
            athlete.warm_up()
            athlete.compete()
            athlete.celebrate()
            print()  # Empty line between athletes


# Run the program
if __name__ == "__main__":
    AthleteTest.main()