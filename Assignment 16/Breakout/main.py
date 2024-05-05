import arcade
import ball
import racket
import fruits

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 800,height = 700, title = "Fruit Waster")
        self.background = arcade.load_texture("Breakout/source/background.png")
        self.racket = racket.Racket(self)
        self.ball = ball.Ball(self)
        self.apples = []
        self.kiwis = []
        self.melons = []
        self.create_fruits()
        self.game_over_flag = False
        self.win = False
        self.background_music = arcade.Sound("Breakout/source/music.mp3")
        self.background_music.play(loop=True)


    def create_fruits(self):
        for x in range(80, 800, 80):
            apple = fruits.Apple(x, self.height // 2 + 150)
            self.apples.append(apple)
            kiwi = fruits.Kiwi(x, self.height // 2 + 220)
            self.kiwis.append(kiwi)
            melon = fruits.Melon(x, self.height // 2 + 290)
            self.melons.append(melon)


    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        self.racket.draws()
        self.ball.draws()
        for apple in self.apples:
            apple.draw()
        for kiwi in self.kiwis:
            kiwi.draw()
        for melon in self.melons:
            melon.draw()
        arcade.draw_text(f"Score: {self.racket.score}",10 ,20 , arcade.color.WHITE)
        arcade.draw_text(f"Health: {self.racket.health}",game.width - 80,20 , arcade.color.WHITE)
        
        if self.game_over_flag:
            arcade.draw_text("Game Over", self.width // 2, self.height // 2, arcade.color.RED, 36, anchor_x="center", anchor_y="center")
            arcade.draw_text(f"Final Score: {self.racket.score}", self.width // 2, self.height // 2 - 50, arcade.color.WHITE, 20, anchor_x="center", anchor_y="center")

        if self.win:
            arcade.draw_text("Game Won", self.width // 2, self.height // 2, arcade.color.BABY_BLUE, 36, anchor_x="center", anchor_y="center")
            arcade.draw_text(f"Final Score: {self.racket.score}", self.width // 2, self.height // 2 - 50, arcade.color.WHITE, 20, anchor_x="center", anchor_y="center")


        arcade.finish_render()


    def ball_sound(self):
        self.background_music = arcade.Sound("Breakout/source/ball.mp3", streaming=True)
        self.background_music.play(volume=1)
        
    def eat_sound(self):
        self.background_music = arcade.Sound("Breakout/source/eat.mp3", streaming=True)
        self.background_music.play(volume=1)

    def on_update(self, delta_time: float):
        if not self.game_over_flag and not self.win:
            for apple in self.apples:
                if arcade.check_for_collision(apple, self.ball):
                    self.racket.score += apple.value
                    self.apples.remove(apple)
                    self.ball.change_y *= -1
                    self.eat_sound()
                    

            for kiwi in self.kiwis:
                if arcade.check_for_collision(kiwi, self.ball):
                    self.racket.score += kiwi.value
                    self.kiwis.remove(kiwi)
                    self.ball.change_y *= -1
                    self.eat_sound()

            for melon in self.melons:
                if arcade.check_for_collision(melon, self.ball):
                    self.racket.score += melon.value
                    self.melons.remove(melon)
                    self.ball.change_y *= -1
                    self.eat_sound()

            self.racket.move()
            if self.racket.width - 20 > self.racket.center_x or self.racket.center_x > self.width - (self.racket.width - 20):
                self.racket.change_x = 0
            
            self.ball.move()
            if 20 > self.ball.center_x or self.ball.center_x > self.width - 20:
                self.ball.change_x *= -1
                self.ball_sound()
                

            if self.ball.center_y > self.height - 20:
                self.ball.change_y *= -1
                self.ball_sound()

            if arcade.check_for_collision(self.racket, self.ball):
                self.ball.change_y *= -1
                self.ball_sound()

            if self.ball.center_y < 10:
                del self.ball
                self.ball = ball.Ball(self)
                self.background_music = arcade.Sound("Breakout/source/no.mp3", streaming=True)
                self.background_music.play(volume=1)
                self.racket.health -=1

            if self.racket.health == 0:
                self.game_over_flag = True
            
            if self.racket.score == 54:
                self.win = True

    
    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.racket.width - 20 < x < self.width - (self.racket.width - 20):
            self.racket.center_x = x
    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.racket.change_x = 1
        if symbol == arcade.key.A:
            self.racket.change_x = -1
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.D:
            self.racket.change_x = 0
        if symbol == arcade.key.A:
            self.racket.change_x = 0

if __name__ == "__main__":
    game = Game()
    arcade.run()

