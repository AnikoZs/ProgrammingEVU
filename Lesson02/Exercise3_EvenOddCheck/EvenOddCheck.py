class EvenOddCheck:
    def __init__(self, number):
        # Store the number
        self.number = number

    # Check if the number is even
    def is_even(self):
        return self.number % 2 == 0

    # Check if the number is odd
    def is_odd(self):
        return not self.is_even()

    # Print the result
    def print_result(self):
        if self.is_even():
            print(f"{self.number} is an even number.")
        else:
            print(f"{self.number} is an odd number.")


