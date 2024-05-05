import arcade

class Rocket_1(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Pong\source\kong.png")
        self.center_x =  60
        self.center_y = game.height // 2
        self.change_x = 0
        self.change_y = 0
        self.speed = 5
        self.width = 70
        self.height = 70
        self.score = 0
    def move(self):
        self.center_y += self.change_y * self.speed
    
    def draws(self):
        self.draw()

class Rocket_2(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Pong/source/mario.png")
        self.center_x = game.width - 60
        self.center_y = game.height // 2
        self.change_x = 0
        self.change_y = 0
        self.speed = 5
        self.width = 70
        self.height = 70
        self.score = 0

    def move(self):
        self.center_y += self.change_y * self.speed
    
    def draws(self):
        self.draw()
