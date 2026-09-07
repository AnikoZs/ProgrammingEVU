from Lesson04.Exercise4_MiniProjekt_Cat.Cat_Solution import Cat


class CatTestWithInput:

    @staticmethod
    def main():
        # Ask how many cats to create
        number_of_cats = int(input("How many cats would you like to register? "))

        # Create an empty list of cats
        cats = []

        # Ask for cat names and create Cat objects
        for i in range(number_of_cats):
            name = input(f"Enter name for cat {i + 1}: ")
            cats.append(Cat(name))

        # Display the cats in action
        print("\nHere are your cats in action:")

        for cat in cats:
            cat.eat()
            cat.chase_mouse()
            cat.sleep()
            print()  # Empty line for readability


if __name__ == "__main__":
    CatTestWithInput.main()
