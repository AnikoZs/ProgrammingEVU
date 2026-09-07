from Lesson04.Exercise4_MiniProjekt_Cat.Cat_Solution import Cat


class CatTest:

    @staticmethod
    def main():
        # Create a list of cats
        cats = [
            Cat("Luna"),
            Cat("Simba"),
            Cat("Milo")
        ]

        # Use the list to call methods
        for cat in cats:
            cat.eat()
            cat.chase_mouse()
            cat.sleep()
            print()  # Empty line for readability


if __name__ == "__main__":
    CatTest.main()