from Lesson04.Exercise3_List.Athlete_Ver2 import Athlete_Ver2


class AthleteTest_Ver3:
    @staticmethod
    def main():
        # Ask the user how many athletes to create
        number = int(input("How many athletes would you like to create? "))

        athletes = []

        # Create athletes based on user input
        for i in range(number):
            name = input(f"Enter name of athlete #{i + 1}: ")
            sport = input(f"Enter sport for {name}: ")

            athletes.append(Athlete_Ver2(name, sport))
            print()

        print("=== START EVENT ===\n")

        # Run the event
        for athlete in athletes:
            athlete.warm_up()
            athlete.compete()
            athlete.celebrate()
            print()  # Empty line between athletes


if __name__ == "__main__":
    AthleteTest_Ver3.main()