class Athlete_Ver2:
    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

    def warm_up(self):
        sport = self.sport.lower()

        if sport == "skiing":
            print(f"{self.name} stretches legs and skis through the snow. ⛷️")
        elif sport == "snowboarding":
            print(f"{self.name} practices flips and jumps on the snowboard. 🏂")
        elif sport == "shooting":
            print(f"{self.name} focuses eyes and practices breathing. 🎯")
        else:
            print(f"{self.name} does a general warm-up. 💪")

    def compete(self):
        print(f"{self.name} competes in {self.sport}!")

    def celebrate(self):
        sport = self.sport.lower()

        if sport == "skiing":
            print(f"{self.name} sips hot chocolate after skiing. ☕")
        elif sport == "snowboarding":
            print(f"{self.name} does a victory trick on the snowboard! 🏂")
        elif sport == "shooting":
            print(f"{self.name} raises the rifle proudly on the podium. 🏆")
        else:
            print(f"{self.name} celebrates with a big smile! 😄")