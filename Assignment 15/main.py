import arcade
import food
from snake import Snake


class Game(arcade.Window):
    def __init__(self):
        super().__init__(width=1500, height=700, title="Amoo Masood The Big Snake")
        self.background = arcade.load_texture("source/background.png")
        self.food_items = []
        self.snake = Snake(self,food.Fries,food.Burger,food.Cabbage)
        self.score = 1
        self.over = False
        self.create_food()  
        self.background_music = arcade.Sound("source/music.mp3")
        self.background_music.play(loop=True)

    def spawn_new_food(self, eaten_food):
        food_type = type(eaten_food)
        new_food = food_type()
        self.food_items.append(new_food)

    def create_food(self):
        self.food_items.append(food.Fries())
        self.food_items.append(food.Burger())
        self.food_items.append(food.Cabbage())

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, self.width, self.height, self.background)
        if self.over:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("Game Over", self.width // 2, self.height // 2 + 50, arcade.color.RED, font_size=50, anchor_x="center")
            arcade.draw_text(f"Score: {self.snake.score}", self.width // 2, self.height // 2, arcade.color.RED, font_size=30, anchor_x="center")
        else:
            self.snake.draws()
            for food in self.food_items:
                food.draw()
        arcade.finish_render()

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.A and self.snake.change_x != 1:
            self.snake.change_x = -1
            self.snake.change_y = 0

        if symbol == arcade.key.W and self.snake.change_y != -1:
            self.snake.change_x = 0
            self.snake.change_y = 1

        if symbol == arcade.key.D and self.snake.change_x != -1:
            self.snake.change_x = 1
            self.snake.change_y = 0

        if symbol == arcade.key.S and self.snake.change_y != 1:
            self.snake.change_x = 0
            self.snake.change_y = -1

    def on_update(self, delta_time: float):
        if not self.over:
            self.snake.move()
            self.snake.eat(self.food_items)
            for count, part in enumerate(self.snake.body):
                for i in range(count + 1, len(self.snake.body)):
                    if part['x'] == self.snake.body[i]['x'] and part['y'] == self.snake.body[i]['y']:
                        self.over = True
                        break
            if (self.snake.center_x < 0 or self.snake.center_x > self.width or
                    self.snake.center_y < 0 or self.snake.center_y > self.height):
                self.over = True
            if self.snake.score < 0:
                self.over = True
            if self.over:
                arcade.set_background_color(arcade.color.BLACK)
                arcade.draw_text("Game Over", self.width // 2, self.height // 2 + 50, arcade.color.RED, font_size=50, anchor_x="center")
                arcade.draw_text(f"Score: {self.snake.score}", self.width // 2, self.height // 2, arcade.color.RED, font_size=30, anchor_x="center")


if __name__ == "__main__":
    game = Game()
    arcade.run()

