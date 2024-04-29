import arcade
import random

class Food(arcade.Sprite):
    def __init__(self, image_path, value):
        super().__init__(image_path)
        self.width = 50
        self.height = 50
        self.center_x = random.randint(20, 1400)
        self.center_y = random.randint(20, 700)
        self.change_x = 0
        self.change_y = 0 
        self.value = value

class Fries(Food):
    def __init__(self):
        super().__init__("source/fry.png", 1)
        

class Burger(Food):
    def __init__(self):
        super().__init__("source/burger.png", 2)


class Cabbage(Food):
    def __init__(self):
        super().__init__("source/cabbage.png", -1)

