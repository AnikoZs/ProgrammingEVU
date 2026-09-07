# Carrot.py
class Carrot:

    # Constructor with default values
    def __init__(self, color="Orange", length=15.0, weight=80.0):
        self.color = color
        self.length = length
        self.weight = weight

    # Getters
    def get_color(self):
        return self.color

    def get_length(self):
        return self.length

    def get_weight(self):
        return self.weight

    # Setters
    def set_color(self, color):
        self.color = color

    def set_length(self, length):
        self.length = length

    def set_weight(self, weight):
        self.weight = weight

    # toString()
    def __str__(self):
        return (
            f"Carrot [color={self.color}, "
            f"length={self.length} cm, "
            f"weight={self.weight} g]"
        )


# Cabbage.py
class Cabbage:

    # Constructor with default values
    def __init__(self, color="Green", diameter=20.0, weight=1200.0):
        self.color = color
        self.diameter = diameter
        self.weight = weight

    # Getters
    def get_color(self):
        return self.color

    def get_diameter(self):
        return self.diameter

    def get_weight(self):
        return self.weight

    # Setters
    def set_color(self, color):
        self.color = color

    def set_diameter(self, diameter):
        self.diameter = diameter

    def set_weight(self, weight):
        self.weight = weight

    # toString()
    def __str__(self):
        return (
            f"Cabbage [color={self.color}, "
            f"diameter={self.diameter} cm, "
            f"weight={self.weight} g]"
        )


# Beans.py
class Beans:

    # Constructor with default values
    def __init__(self, variety="Green Bean", pods=10, length=8.0):
        self.variety = variety
        self.pods = pods
        self.length = length

    # Getters
    def get_variety(self):
        return self.variety

    def get_pods(self):
        return self.pods

    def get_length(self):
        return self.length

    # Setters
    def set_variety(self, variety):
        self.variety = variety

    def set_pods(self, pods):
        self.pods = pods

    def set_length(self, length):
        self.length = length

    # toString()
    def __str__(self):
        return (
            f"Beans [variety={self.variety}, "
            f"pods={self.pods}, "
            f"length={self.length} cm]"
        )


# Salad.py
class Salad:

    # Constructor with default values
    def __init__(self, type="Lettuce", leaves=20, weight=200.0):
        self.type = type
        self.leaves = leaves
        self.weight = weight

    # Getters
    def get_type(self):
        return self.type

    def get_leaves(self):
        return self.leaves

    def get_weight(self):
        return self.weight

    # Setters
    def set_type(self, type):
        self.type = type

    def set_leaves(self, leaves):
        self.leaves = leaves

    def set_weight(self, weight):
        self.weight = weight

    # toString()
    def __str__(self):
        return (
            f"Salad [type={self.type}, "
            f"leaves={self.leaves}, "
            f"weight={self.weight} g]"
        )


# KitchenGarden.py
class KitchenGarden:

    @staticmethod
    def test():

        # Create Carrot objects
        carrot1 = Carrot()
        carrot2 = Carrot("Purple", 12.5, 60.0)

        # Create Cabbage objects
        cabbage1 = Cabbage()
        cabbage2 = Cabbage("Red", 18.0, 900.0)

        # Create Beans objects
        beans1 = Beans()
        beans2 = Beans("French Bean", 15, 10.0)

        # Create Salad objects
        salad1 = Salad()
        salad2 = Salad("Spinach", 30, 150.0)

        # Print all objects
        print(carrot1)
        print(carrot2)

        print(cabbage1)
        print(cabbage2)

        print(beans1)
        print(beans2)

        print(salad1)
        print(salad2)


# Start program
KitchenGarden.test()