from Lesson04.Exercise3_List.Athlete_Ver2 import Athlete_Ver2


class AthleteTest_Ver2:

    @staticmethod
    def main():
        athletes = [
            Athlete_Ver2("Alex", "Skiing"),
            Athlete_Ver2("Maria", "Snowboarding"),
            Athlete_Ver2("Jonas", "Shooting")
        ]

        for athlete in athletes:
            athlete.warm_up()
            athlete.compete()
            athlete.celebrate()
            print()  # Empty line between athletes


if __name__ == "__main__":
    AthleteTest_Ver2.main()
