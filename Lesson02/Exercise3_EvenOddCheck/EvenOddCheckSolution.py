# Exercise 1-5: Even and Odd Number Checker


class EvenOddCheck:
    def __init__(self, number):
        # Store the number
        self.number = number

    # Exercise 2:
    # Return True if the number is even, otherwise False.
    def is_even(self):
        return self.number % 2 == 0

    # Exercise 3:
    # Return the stored number.
    def get_number(self):
        return self.number

    # Exercise 4:
    # Return True if the number is positive.
    def is_positive(self):
        return self.number > 0

    # Exercise 5:
    # Return True if the number is divisible by 5.
    def is_divisible_by_5(self):
        return self.number % 5 == 0

    # Exercise 1:
    # Change the output text if you want.
    def print_result(self):
        if self.is_even():
            print(f"{self.number} is an even number.")
        else:
            print(f"{self.number} is an odd number.")


class EvenOddCheckTest:

    @staticmethod
    def run_program():

        # Repeat three times
        for i in range(3):

            print(f"\nNumber {i + 1}")

            # Read a number from the user
            number = int(input("Enter a number: "))

            # Create an object
            checker = EvenOddCheck(number)

            # Exercise 1
            checker.print_result()

            # Exercise 2
            print("Even:", checker.is_even())

            # Exercise 3
            print("Stored number:", checker.get_number())

            # Exercise 4
            print("Positive:", checker.is_positive())

            # Exercise 5
            print("Divisible by 5:", checker.is_divisible_by_5())

    @staticmethod
    def main():
        # Start the program
        EvenOddCheckTest.run_program()


if __name__ == "__main__":
    EvenOddCheckTest.main()