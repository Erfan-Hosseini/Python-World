import arcade

class BlueEmerald(arcade.Sprite):
    def __init__(self):
        super().__init__("Assignment 13/source/Blue.png")
        self.width = 20
        self.height = 20

class RedEmerald(arcade.Sprite):
    def __init__(self):
        super().__init__("Assignment 13/source/Red.png")
        self.width = 20
        self.height = 20

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=800, title="Emerald")
        arcade.set_background_color(arcade.color.WHITE)
        self.blue = BlueEmerald()
        self.red = RedEmerald()
        self.emerald_size = 20 
        self.spacing = 5  
        self.grid_size = 10  
        
        self.start_x = (self.width - (self.grid_size * (self.emerald_size + self.spacing) - self.spacing)) / 2
        self.start_y = (self.height - (self.grid_size * (self.emerald_size + self.spacing) - self.spacing)) / 2

    def on_draw(self):
        arcade.start_render()
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                x = self.start_x + (self.emerald_size + self.spacing) * i + self.emerald_size / 2
                y = self.start_y + (self.emerald_size + self.spacing) * j + self.emerald_size / 2
                if (i + j) % 2 == 0:
                    self.blue.center_x = x
                    self.blue.center_y = y
                    self.blue.draw()
                else:
                    self.red.center_x = x
                    self.red.center_y = y
                    self.red.draw()

window = Game()
arcade.run()
