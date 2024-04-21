import arcade

class Bullet(arcade.Sprite):
    def __init__(self, player):
        super().__init__("source/bullet.png")
        self.speed = 10
        self.center_x = player.center_x
        self.center_y = player.center_y + player.height / 2
        self.width = 40
        self.height = 40
        self.angle = 90
        self.background_music = arcade.Sound("source/pew.mp3", streaming=True)
        self.background_music.play(volume=0.5)

    
    def update(self):
        self.center_y += self.speed

