import random
import arcade

class Ball(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Pong/source/ball.png")
        self.center_x = game.width // 2
        self.center_y = game.height // 2
        self.change_x = random.choice([-1 , 1])
        self.change_y = random.choice([-1 , 1])
        self.width = 50
        self.height = 50
        self.speed = 6


    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def draws(self):
        self.draw()