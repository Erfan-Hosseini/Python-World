import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Breakout/source/ball.png")
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = random.choice([-1 , 1])
        self.change_y = -1
        self.width = 30
        self.height = 30
        self.speed = 5


    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draws(self):
        self.draw()