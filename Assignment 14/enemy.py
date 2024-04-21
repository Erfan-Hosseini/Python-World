import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__("source\enemy.png")
        self.speed = 5  # Initial speed
        self.game = game
        self.height = 70
        self.width = 70
        self.center_x = random.randint(0, game.width)
        self.center_y = game.height 
        self.direction = 1 
        self.game = game
        self.hit = 0
        self.time_elapsed = 0  

    def update(self, delta_time):
     
        self.time_elapsed += delta_time
        
        
        if self.time_elapsed >= 1:  
            self.speed += 1 
            self.time_elapsed = 0 


        self.center_x += self.speed * self.direction
        self.center_y -= self.speed 


        if self.center_x <= 0 or self.center_x >= self.game.width:
            self.direction *= -1
            self.background_music = arcade.Sound("source/ouch.mp3", streaming=True)
            self.background_music.play(volume=0.5)

        if self.center_y <= 0 or self.center_y >= self.game.height or self.hit == 1:
            self.speed *= -1
            self.direction *= -1
            self.background_music = arcade.Sound("source/ouch.mp3", streaming=True)
            self.background_music.play(volume=0.5)
