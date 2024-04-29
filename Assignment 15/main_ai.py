import arcade
from snake import Snake
from food import Fries, Burger, Cabbage
import random

class AISnakeGame(arcade.Window):
    def __init__(self):
        super().__init__(width=1500, height=700, title="Amoo Masood The Intelligent Snake")
        self.background = arcade.load_texture("source/background.png")
        self.food_items = []
        self.snake = Snake(self, Fries, Burger, Cabbage)
        self.over = False
        self.create_food()
        self.background_music = arcade.Sound("source/music.mp3")
        self.background_music.play(loop=True)

    def spawn_new_food(self, eaten_food):
        food_type = type(eaten_food)
        new_food = food_type()
        self.food_items.append(new_food)

    def create_food(self):
        self.food_items.append(Fries())
        self.food_items.append(Burger())
        self.food_items.append(Cabbage())

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

    def on_update(self, delta_time: float):
        if not self.over:
            self.ai_move()
            self.snake.move()
            self.snake.eat(self.food_items)

            if self.check_game_over():
                self.over = True

    def ai_move(self):
        head_x, head_y = self.snake.center_x, self.snake.center_y
        closest_food = None
        min_distance = float('inf')
        for food in self.food_items:
            distance = abs(food.center_x - head_x) + abs(food.center_y - head_y)
            if distance < min_distance:
                min_distance = distance
                closest_food = food

        if closest_food:
            food_x, food_y = closest_food.center_x, closest_food.center_y
            dx = 1 if food_x > head_x else -1 if food_x < head_x else 0
            dy = 1 if food_y > head_y else -1 if food_y < head_y else 0

            if dx != 0:
                next_x = head_x + dx * self.snake.speed
                if not (self.snake.width / 2 <= next_x <= self.width - self.snake.width / 2):
                    dy = 1 if food_y > head_y else -1 if food_y < head_y else 0
                    dx = 0
                elif dx == -self.snake.change_x:
                    dy = 1 if food_y > head_y else -1 if food_y < head_y else 0
                    dx = 0
            elif dy != 0:
                next_y = head_y + dy * self.snake.speed
                if not (self.snake.height / 2 <= next_y <= self.height - self.snake.height / 2):
                    dx = 1 if food_x > head_x else -1 if food_x < head_x else 0
                    dy = 0
                elif dy == -self.snake.change_y:
                    dx = 1 if food_x > head_x else -1 if food_x < head_x else 0
                    dy = 0

            self.snake.change_x = dx
            self.snake.change_y = dy
        else:
            dx, dy = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
            self.snake.change_x = dx
            self.snake.change_y = dy

        next_x = head_x + self.snake.change_x * self.snake.speed
        next_y = head_y + self.snake.change_y * self.snake.speed

        next_x = head_x + self.snake.change_x * self.snake.speed
        next_y = head_y + self.snake.change_y * self.snake.speed
        if next_x < self.snake.width / 2:
            self.snake.change_x = 1
        elif next_x > self.width - self.snake.width / 2:
            self.snake.change_x = -1
        if next_y < self.snake.height / 2:
            self.snake.change_y = 1
        elif next_y > self.height - self.snake.height / 2:
            self.snake.change_y = -1

    def check_game_over(self):
        if (self.snake.center_x < 0 or self.snake.center_x > self.width or
                self.snake.center_y < 0 or self.snake.center_y > self.height):
            return True
        if self.snake.score < 0:
            return True
        return False

if __name__ == "__main__":
    game = AISnakeGame()
    arcade.run()

