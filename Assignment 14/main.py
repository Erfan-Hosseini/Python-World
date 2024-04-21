import random
import arcade
from player import Player
from enemy import Enemy
from bullet import Bullet


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1000, height=800, title="Attack on Swamp")
        self.background = arcade.load_texture("source/background.png")
        self.player = Player(self)
        self.move_left = False
        self.move_right = False
        self.game_over_flag = False
        self.enemies = []
        self.bullets = []
        self.background_music = arcade.Sound("source/music.mp3", streaming=True)
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
        self.player.draw_health()
        arcade.draw_text(f"Score: {self.player.score}", 10, 10, arcade.color.WHITE, 16)
        if self.game_over_flag:
            arcade.draw_text("Game Over", self.width // 2, self.height // 2, arcade.color.RED, 36, anchor_x="center", anchor_y="center")
            arcade.draw_text(f"Final Score: {self.player.score}", self.width // 2, self.height // 2 - 50, arcade.color.WHITE, 20, anchor_x="center", anchor_y="center")

        

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.move_left = True
        elif symbol == arcade.key.D:
            self.move_right = True
        if symbol == arcade.key.W:
            self.shoot()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A:
            self.move_left = False
        
        elif symbol == arcade.key.D:
            self.move_right = False

    def shoot(self):
        bullet = Bullet(self.player)
        self.bullets.append(bullet)
    
    def death_sound(self):
        self.background_music = arcade.Sound("source/death.mp3", streaming=True)
        self.background_music.play(volume=0.5)
        



    def on_update(self, delta_time):
        if not self.game_over_flag:
            self.player.update()
            if self.move_left:
                if self.player.center_x > 0:
                    self.player.center_x -= self.player.speed
            if self.move_right:
                if self.player.center_x < self.width:
                    self.player.center_x += self.player.speed
            for bullet in self.bullets:
                bullet.update()
            for enemy in self.enemies:
                enemy.update(delta_time)
            for bullet in self.bullets:
                if bullet.center_y > self.height:
                    self.bullets.remove(bullet)

            if random.randint(1,70) == 50:
                Game.spawn_enemy(self)
            
            for enemy in self.enemies:
                for bullet in self.bullets:
                    if arcade.check_for_collision(enemy, bullet):
                        Game.death_sound(self)
                        self.enemies.remove(enemy)
                        self.bullets.remove(bullet)
                        self.player.score += 1
            for enemy in self.enemies:
                if arcade.check_for_collision(enemy,self.player):
                    self.enemies.remove(enemy)
                    self.player.health_value -= 1

            if self.player.health_value <= 0:
                self.game_over_flag = True


        

window = Game()
arcade.run()