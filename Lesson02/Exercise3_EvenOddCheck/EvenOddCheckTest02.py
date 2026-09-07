from Lesson02.Exercise3_EvenOddCheck.EvenOddCheck import EvenOddCheck


class EvenOddCheckTest02:
    # A separate method called from main
    @staticmethod
    def run_program():
        # Read a number from the user
        number = int(input("Enter a number: "))

        # Create an object
        checker = EvenOddCheck(number)

        # Call the method
        checker.print_result()

    @staticmethod
    def main():
        # Main only calls run_program()
        EvenOddCheckTest02.run_program()


# Start the program
if __name__ == "__main__":
    EvenOddCheckTest02.main()