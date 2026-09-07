import random


class Game:
    """
    Responsible for:
    - Generating a random number
    - Checking guesses
    - Returning feedback
    """

    def __init__(self):

        # TODO:
        # Generate and store a random number between 1 and 100.
        #
        # Hint:
        # random.randint(1, 100)
        #
        # Store it in an instance variable called:
        # self.secret_number

        pass

    def check_guess(self, guess):

        # TODO:
        # Compare the player's guess with the secret number.
        #
        # If the guess is lower than the secret number:
        #     return "Too low"
        #
        # If the guess is higher than the secret number:
        #     return "Too high"
        #
        # Otherwise:
        #     return "Correct!"

        pass


class Player:
    """
    Responsible for:
    - Reading user input
    - Returning the player's guess
    """

    def get_guess(self):

        # TODO:
        # Ask the user to enter a number.
        #
        # Convert the input to an integer.
        #
        # Return the value.

        pass


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

        # TODO:
        # Create a Game object.
        #
        # Example:
        # game = Game()

        game = None

        # TODO:
        # Create a Player object.

        player = None

        # This variable controls the game loop.
        # The game starts as NOT finished.
        game_finished = False

        print("🎮 Welcome to Guess the Number!")
        print("I am thinking of a number between 1 and 100.")

        # Continue running while the game is NOT finished.
        #
        # Think:
        # while not game_finished:
        #
        # This means:
        # while game_finished == False
        #
        # The loop should stop when the player guesses correctly.
        while not game_finished:

            # TODO:
            # Ask the player for a guess.
            #
            # Call the get_guess() method.
            #
            # Store the value in a variable named guess.

            guess = None

            # TODO:
            # Send the guess to the Game object.
            #
            # Call check_guess()
            #
            # Store the returned feedback in a variable named result.

            result = None

            # TODO:
            # Display the result to the user.
            #
            # Examples:
            # Too low
            # Too high
            # Correct!

            # TODO:
            # If the result is "Correct!"
            # change game_finished to True.
            #
            # This will stop the while loop.

        print("🎉 You won!")


if __name__ == "__main__":
    GuessNumberApp.main()