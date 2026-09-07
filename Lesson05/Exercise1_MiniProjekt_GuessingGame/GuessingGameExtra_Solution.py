import random


class Game:
    """
    Responsible for:
    - Generating a random number
    - Checking guesses
    - Giving feedback
    """

    def __init__(self, max_number):
        # Generate a random secret number
        self.secret_number = random.randint(1, max_number)

    def check_guess(self, guess):

        if guess < self.secret_number:
            return "Too low"

        elif guess > self.secret_number:
            return "Too high"

        else:
            return "Correct!"


class Player:
    """
    Responsible for:
    - Reading user input
    - Returning the player's guess
    """

    def get_guess(self):

        while True:

            try:
                # Ask the user for a number
                guess = int(input("Enter your guess: "))
                return guess

            except ValueError:
                # Executed if user types text instead of a number
                print("Invalid input! Please enter a number.")


class GuessNumberApp:
    """
    Main application class

    Responsible for:
    - Starting the program
    - Creating objects
    - Running the game loop
    """

    @staticmethod
    def choose_difficulty():

        print("\nChoose difficulty:")
        print("1. Easy (1-50)")
        print("2. Normal (1-100)")
        print("3. Hard (1-500)")

        choice = input("Enter your choice: ")

        if choice == "1":
            return 50
        elif choice == "3":
            return 500
        else:
            return 100

    @staticmethod
    def main():

        # Controls whether the player wants to play again
        play_again = "yes"

        while play_again == "yes":

            # Let the player choose a difficulty level
            max_number = GuessNumberApp.choose_difficulty()

            # Create objects
            game = Game(max_number)
            player = Player()

            # Counts the number of guesses
            attempts = 0

            # Maximum number of attempts allowed
            max_attempts = 10

            # Used with "while not"
            game_finished = False

            print(f"\nI'm thinking of a number between 1 and {max_number}.")
            print(f"You have {max_attempts} attempts.")

            # Continue while game is not finished
            # AND there are attempts left
            while not game_finished and attempts < max_attempts:

                guess = player.get_guess()

                # Increase attempt counter
                attempts += 1

                result = game.check_guess(guess)

                print(result)

                # Stop loop if the player guessed correctly
                if result == "Correct!":
                    game_finished = True

            # If player guessed the number
            if game_finished:
                print(
                    f"\n🎉 Congratulations! You guessed the number in {attempts} attempts."
                )

            # If player used all attempts
            else:
                print("\n❌ Game Over!")
                print(
                    f"You used all {max_attempts} attempts."
                )
                print(
                    f"The secret number was {game.secret_number}."
                )

            # Ask if the player wants to play again
            play_again = input(
                "\nWould you like to play again? (yes/no): "
            ).lower()

        print("\nThanks for playing!")


if __name__ == "__main__":
    GuessNumberApp.main()