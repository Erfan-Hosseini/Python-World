import arcade

class Player(arcade.Sprite):
    def __init__(self, game):
        super().__init__("source/player.png")
        self.center_x = game.width // 2
        self.center_y = 50
        self.width = 70
        self.height = 70
        self.speed = 5
        self.health_value = 3
        self.score = 0

   

    
    def draw_health(self):
        arcade.draw_text(f"Health: {self.health_value}", self.center_x + 20, self.center_y + 40, arcade.color.RED, 12, align="center", anchor_x="center", width=100)





