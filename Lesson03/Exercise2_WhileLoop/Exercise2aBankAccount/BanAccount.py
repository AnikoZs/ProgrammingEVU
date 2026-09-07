class BankAccount:
    # Constructor
    def __init__(self, balance):
        self.balance = balance

    # Method that allows withdrawals until the account is empty
    def withdraw_loop(self):

        # Continue while there is money in the account
        while self.balance > 0:
            print(f"\nBalance: {self.balance}")

            # Ask the user for an amount to withdraw
            amount = float(input("Enter amount to withdraw: "))

            # Check if there is enough money
            if amount > self.balance:
                print("Not enough money!")
            else:
                self.balance -= amount

        print("Account empty!")


class BankAccountTest:

    @staticmethod
    def test():
        # Create a BankAccount object
        account = BankAccount(50.0)

        # Start the withdrawal process
        account.withdraw_loop()


# Start the program
BankAccountTest.test()