import arcade
import food

class Snake(arcade.Sprite):
    def __init__(self, game,fries,burger,cabbage):
        super().__init__("source/face.png")
        self.width = 55
        self.height = 55
        self.radius = 20
        self.body = []
        self.center_x = game.width // 2
        self.center_y = game.height // 2 
        self.colors = [arcade.color.DARK_KHAKI, arcade.color.LIGHT_KHAKI]
        self.change_x = 0
        self.change_y = 0
        self.speed = 8
        self.score = 0
        self.game = game
        self.eaten_food = []

    def draws(self):

        for part in self.body:
            arcade.draw_circle_filled(part['x'], part['y'], self.radius, self.colors[part['color']])
        self.draw()

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed
        
        if self.body:
            self.body.insert(0, {'x': self.center_x, 'y': self.center_y, 'color': 1 - self.body[0]['color']})
        
            while len(self.body) > self.score:
                self.body.pop()

        else:
            self.body.append({'x': self.center_x, 'y': self.center_y, 'color': 1})


    def eat(self, food_items):
        eaten_food = []
        for food_item in food_items:
            if arcade.check_for_collision(self, food_item):
                if isinstance(food_item, food.Fries):
                    self.score += 1
                elif isinstance(food_item, food.Burger):
                    self.score += 2
                elif isinstance(food_item, food.Cabbage):
                    self.score -= 1
                eaten_food.append(food_item)

        for item in eaten_food:
            self.game.food_items.remove(item)

        for item in eaten_food:
            if isinstance(item, food.Fries):
                self.game.food_items.append(food.Fries())
            elif isinstance(item, food.Burger):
                self.game.food_items.append(food.Burger())
            elif isinstance(item, food.Cabbage):
                self.game.food_items.append(food.Cabbage())
