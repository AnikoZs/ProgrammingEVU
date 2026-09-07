class Athlete:
    def __init__(self, name):
        # Attribute
        self.name = name

    def warm_up(self):
        """Warm up before the competition."""
        print(f"{self.name} warms up before the competition.")

    def compete(self):
        """Compete in the event."""
        print(f"{self.name} competes in the event.")

    def celebrate(self):
        """Celebrate the achievement."""
        print(f"{self.name} celebrates their achievement with a smile.")
