import arcade

class Racket(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Breakout/source/banana.png")
        self.center_x =  game.width // 2
        self.center_y = 20
        self.change_x = 0
        self.change_y = 0
        self.speed = 8
        self.width = 60
        self.height = 60
        self.angle = -42
        self.score = 0
        self.health = 3

    def move(self):
        self.center_x += self.change_x * self.speed

    
    def draws(self):
        self.draw()