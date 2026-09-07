class Broccoli:

    # Constructor with default values
    def __init__(self, color="Green", diameter=20.0, weight=500.0):
        self.color = color
        self.diameter = diameter
        self.weight = weight

    # Getter for color
    def get_color(self):
        return self.color

    # Setter for color
    def set_color(self, color):
        self.color = color

    # Getter for diameter
    def get_diameter(self):
        return self.diameter

    # Setter for diameter
    def set_diameter(self, diameter):
        self.diameter = diameter

    # Getter for weight
    def get_weight(self):
        return self.weight

    # Setter for weight
    def set_weight(self, weight):
        self.weight = weight

    # Return a string representation of the object
    def __str__(self):
        return (
            f"Broccoli [color={self.color}, "
            f"diameter={self.diameter} cm, "
            f"weight={self.weight} g]"
        )
