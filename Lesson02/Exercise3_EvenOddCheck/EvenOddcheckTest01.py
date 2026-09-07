from Lesson02.Exercise3_EvenOddCheck.EvenOddCheck import EvenOddCheck


class EvenOddCheckTest01:
    @staticmethod
    def main():
        # Read a number from the user
        number = int(input("Enter a number: "))

        # Create an object
        checker = EvenOddCheck(number)

        # Call the method
        checker.print_result()


# Start the program
if __name__ == "__main__":
    EvenOddCheckTest01.main()