class Flower:
    def __init__(self, name, price, color_code):
        self.name = name
        self.price = price
        self.color_code = color_code

    def __str__(self):
        return f"Flower(name='{self.name}', price={self.price}, color={self.color_code})"

