from Lesson06.Exercise1_ObjectInAList.Flower import Flower


class FlowerShop:

    @staticmethod
    def display_flowers(flowers):
        """Display all flowers in the list"""
        for flower in flowers:
            print(flower)

    @staticmethod
    def sort_by_price(flowers):
        """Bubble sort by price"""

        for i in range(len(flowers) - 1):

            for j in range(len(flowers) - 1):

                if flowers[j].price > flowers[j + 1].price:

                    temp = flowers[j]
                    flowers[j] = flowers[j + 1]
                    flowers[j + 1] = temp

    @staticmethod
    def count_color(flowers, color):
        """Count flowers with a specific color"""

        count = 0

        for flower in flowers:

            if flower.color_code == color:
                count += 1

        return count


# Creating flower objects
f1 = Flower("Rose", 25.0, 'R')
f2 = Flower("Tulip", 15.0, 'Y')
f3 = Flower("Lily", 30.0, 'W')
f4 = Flower("Daisy", 10.0, 'W')

# Creating a list of Flower objects
bouquet = [f1, f2, f3, f4]

print("🌼 Original bouquet:")
FlowerShop.display_flowers(bouquet)

# Sort by price
FlowerShop.sort_by_price(bouquet)

print("\n🌼 Bouquet sorted by price:")
FlowerShop.display_flowers(bouquet)

# Count white flowers
white_count = FlowerShop.count_color(bouquet, 'W')

print(f"\nNumber of white flowers: {white_count}")