# First class (like your original one)
class WriteToNewLine02:

    def __init__(self, navn, alder):
        self.navn = navn
        self.alder = alder

    def run(self):
        print(f"Hej {self.navn}! Du er {self.alder} år gammel.")
        print("Welcome to Python!")


# Second class that uses the first class
class App:

    def start(self):
        # create an object from the first class
        person_program = WriteToNewLine02("Sofie", 20)

        # call its method
        person_program.run()


# run the program
app = App()
app.start()