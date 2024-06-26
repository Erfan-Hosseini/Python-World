import arcade
import arcade.key
import rocket
import ball

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 1200,height = 600, title = "King Pong")
        self.rocket_1 = rocket.Rocket_1(self) 
        self.rocket_2 = rocket.Rocket_2(self)
        self.ball = ball.Ball(self)
        self.background_music = arcade.Sound("Pong/source/music.mp3")
        self.background_music.play(loop=True)
        arcade.set_background_color(arcade.color.LIGHT_SEA_GREEN)

    def on_draw(self):
        arcade.start_render()
        self.rocket_1.draws()
        self.rocket_2.draws()
        self.ball.draws()
        arcade.draw_rectangle_outline(self.width // 2, self.height // 2, self.width - 30, self.height - 30, arcade.color.ALLOY_ORANGE,5)
        arcade.draw_line(self.width // 2, 30, self.width // 2, self.height - 30, arcade.color.ALLOY_ORANGE, 5)
        arcade.draw_text(f"Score: {self.rocket_1.score}",20 ,self.height - 40, arcade.color.ALABAMA_CRIMSON)
        arcade.draw_text(f"Score: {self.rocket_2.score}",self.width - 85 ,self.height - 40, arcade.color.ALABAMA_CRIMSON)
        arcade.finish_render()

    def new_ball(self):
        del self.ball
        self.ball = ball.Ball(game)

    def on_update(self, delta_time: float):
        self.rocket_1.move()
        self.rocket_2.move()
        self.ball.move()
        if 40 > self.ball.center_y or self.ball.center_y > self.height - 40:
            self.ball.change_y *= -1
        if self.rocket_1.height - 10 > self.rocket_1.center_y or self.rocket_1.center_y > self.height - (self.rocket_1.height - 10):
            self.rocket_1.change_y = 0
        if self.rocket_2.height - 10 > self.rocket_2.center_y or self.rocket_2.center_y > self.height - (self.rocket_2.height - 10):
            self.rocket_2.change_y = 0
        
        if arcade.check_for_collision(self.rocket_1, self.ball) or arcade.check_for_collision(self.rocket_2, self.ball):
            self.ball.change_x *= -1
            self.background_music = arcade.Sound("Pong/source/ball.mp3", streaming=True)
            self.background_music.play(volume=1)
        if self.ball.center_x == 0:
            self.new_ball()
            self.rocket_2.score += 1
            self.background_music = arcade.Sound("Pong/source/goal.mp3", streaming=True)
            self.background_music.play(volume=1)
        if self.ball.center_x == self.width:
            self.new_ball()
            self.rocket_1.score += 1
            self.background_music = arcade.Sound("Pong/source/goal.mp3", streaming=True)
            self.background_music.play(volume=1)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.rocket_1.change_y = 1
        if symbol == arcade.key.S:
            self.rocket_1.change_y = -1
        if symbol == arcade.key.UP:
            self.rocket_2.change_y = 1
        if symbol == arcade.key.DOWN:
            self.rocket_2.change_y = -1
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.W:
            self.rocket_1.change_y =0
        if symbol == arcade.key.S:
            self.rocket_1.change_y = 0
        if symbol == arcade.key.UP:
            self.rocket_2.change_y = 0
        if symbol == arcade.key.DOWN:
            self.rocket_2.change_y = 0

        
if __name__ == "__main__":
    game = Game()
    arcade.run()

