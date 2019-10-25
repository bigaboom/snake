import pygame
import random


class Apple:
    def __init__(self, count_x, count_y):
        self.location = [0, 0]
        self.apple = False
        self.height = 20
        self.width = 20
        self.count_x = count_x
        self.count_y = count_y

    def new_apple(self, object1, object2=None):
        in_snake = False
        self.location = [random.randint(0, self.count_x-1) * 20, random.randint(0, self.count_y-1) * 20]
        if self.location in object1.snake:
            in_snake = True
        if object2 and self.location in object2.snake:
            in_snake = True
        if in_snake:
            self.new_apple(object1, object2)
        self.apple = True

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.location[0] - 1, self.location[1] - 1, self.width - 1, self.height - 1))


class Objects:
    def __init__(self, color, start_y):
        self.snake = [[100, start_y], [80, start_y], [60, start_y]]
        self.height = 20
        self.width = 20
        self.step = 20
        self.go_left = False
        self.go_right = True
        self.go_up = False
        self.go_down = False
        self.color = color
        self.last_direction = "right"

    def stop(self):
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False

    def its_ok(self, second):
        result = True
        if self.snake.count(self.snake[0]) > 1:
            result = False
        if second and self.snake[0] in second.snake:
            result = False
        return result

    def change_lastr_direction(self):
        if self.go_right:
            self.last_direction = "right"
        elif self.go_left:
            self.last_direction = "left"
        elif self.go_up:
            self.last_direction = "up"
        elif self.go_down:
            self.last_direction = "down"

    def direction(self, direction):
        self.stop()
        if direction == "up":
            self.go_up = True
        elif direction == "down":
            self.go_down = True
        elif direction == "left":
            self.go_left = True
        elif direction == "right":
            self.go_right = True

    def draw(self, window):
        for section in self.snake:
            pygame.draw.rect(window, self.color, (section[0] - 1, section[1] - 1, self.width - 1, self.height - 1))

    def move(self, apple, object1, object2=None):
        head_location = [0, 0]
        if self.go_right:
            head_location = [self.snake[0][0] + self.step, self.snake[0][1]]
        if self.go_left:
            head_location = [self.snake[0][0] - self.step, self.snake[0][1]]
        if self.go_up:
            head_location = [self.snake[0][0], self.snake[0][1] - self.step]
        if self.go_down:
            head_location = [self.snake[0][0], self.snake[0][1] + self.step]
        if head_location == apple.location:
            self.snake.insert(0, head_location)
            apple.new_apple(object1, object2)
        else:
            self.snake.insert(0, head_location)
            self.snake.remove(self.snake[len(self.snake) - 1])


