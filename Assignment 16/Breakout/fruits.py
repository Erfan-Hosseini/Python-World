import arcade

class Fruit(arcade.Sprite):
    def __init__(self, image_path, value):
        super().__init__(image_path)
        self.width = 70
        self.height = 70
        self.change_x = 0
        self.change_y = 0 
        self.value = value

class Apple(Fruit):
    def __init__(self, x, y):
        super().__init__("Breakout/source/apple.png", 1)
        self.center_x = x
        self.center_y = y
        

class Kiwi(Fruit):
    def __init__(self, x, y):
        super().__init__("Breakout/source/Kiwi.png", 2)
        self.center_x = x
        self.center_y = y


class Melon(Fruit):
    def __init__(self, x, y):
        super().__init__("Breakout/source/Melon.png", 3)
        self.center_x = x
        self.center_y = y