import random
import arcade

class Enemy(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Assignment 13\source\enemy.png")
        self.speed = 5
        self.game = game
        self.height = 70
        self.width = 70
        self.center_x = random.randint(0,game.width)
        self.center_y = game.height 
        self.direction = 1 
        self.game = game

    def update(self):
        self.center_x += self.speed * self.direction
        self.center_y -= self.speed
        if self.center_x <= 0 or self.center_x >= self.game.width:
            self.direction *= -1

        if self.center_y <= 0 or self.center_y >= self.game.height:
            self.speed *= -1
            self.direction *= -1

class Player(arcade.Sprite):
    def __init__(self, game):
        super().__init__("Assignment 13/source/player.png")
        self.center_x = game.width // 2
        self.center_y = 50
        self.width = 70
        self.height = 70
        self.speed = 5

class Bullet(arcade.Sprite):
    def __init__(self, player):
        super().__init__("Assignment 13/source/bullet.png")
        self.speed = 10
        self.center_x = player.center_x
        self.center_y = player.center_y + player.height / 2
        self.width = 40
        self.height = 20
    
    def update(self):
        self.center_y += self.speed

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=800, title="Attack on Swamp")
        self.background = arcade.load_texture("Assignment 13/source/background.png")
        self.player = Player(self)
        self.move_left = False
        self.move_right = False
        self.bullets = []
        self.enemies = []
        self.background_music = arcade.Sound("Assignment 13/source/music.mp3", streaming=True)
        self.background_music.play(volume=0.5)
        self.spawn_enemy()

    def spawn_enemy(self):
        self.enemies.append(Enemy(self))

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.player.draw()
        for bullet in self.bullets:
            bullet.draw()
        for enemy in self.enemies:
            enemy.draw()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == 97:
            self.move_left = True
        elif symbol == 100:
            self.move_right = True
        if symbol == arcade.key.W:
            self.shoot()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == 97:
            self.move_left = False
        elif symbol == 100:
            self.move_right = False

    def shoot(self):
        bullet = Bullet(self.player)
        self.bullets.append(bullet)

    def on_update(self, delta_time):
        if self.move_left:
            self.player.center_x -= self.player.speed
        if self.move_right:
            self.player.center_x += self.player.speed
        for bullet in self.bullets:
            bullet.update()
        for enemy in self.enemies:
            enemy.update()

window = Game()
arcade.run()
