import random


class Game:
    """
    Responsible for:
    - Generating a random number
    - Checking guesses
    - Returning feedback
    """

    def __init__(self):
        # Generate a random number between 1 and 100
        self.secret_number = random.randint(1, 100)

    def check_guess(self, guess):
        """
        Compare the player's guess with the secret number.
        """

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

        guess = int(input("Enter your guess: "))
        return guess


class GuessNumberApp:
    """
    Main application class.

    Responsible for:
    - Starting the game
    - Creating objects
    - Running the game loop
    """

    @staticmethod
    def main():

        # Create objects
        game = Game()
        player = Player()

        # Controls the loop
        game_finished = False

        print("🎮 Welcome to Guess the Number!")
        print("I am thinking of a number between 1 and 100.")

        while not game_finished:

            guess = player.get_guess()

            result = game.check_guess(guess)

            print(result)

            if result == "Correct!":
                game_finished = True

        print("🎉 You won!")


if __name__ == "__main__":
    GuessNumberApp.main()