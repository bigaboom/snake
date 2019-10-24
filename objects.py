import pygame
import random

class Apple:
    def __init__(self):
        self.apple_x = 0
        self.apple_y = 0
        self.apple = False
        self.height = 20
        self.width = 20

    def new_apple(self, object1, object2=None):
        in_snake = False
        self.apple_x = random.randint(0, 24) * 20
        self.apple_y = random.randint(0, 24) * 20
        for i in range(object1.snake_len):
            if self.apple_x == object1.snake_x[i] and self.apple_y == object1.snake_y[i]:
                in_snake = True
                break
        if object2:
            for i in range(object2.snake_len):
                if self.apple_x == object2.snake_x[i] and self.apple_y == object2.snake_y[i]:
                    in_snake = True
                    break
        if in_snake:
            self.new_apple(object1, object2)
        self.apple = True

    def draw(self, window):
        pygame.draw.rect(window, (255, 0, 0), (self.apple_x - 1, self.apple_y - 1, self.width - 1, self.height - 1))


class Objects:
    def __init__(self, color, start_y):
        self.snake_x = [0 for i in range(25 * 25)]
        self.snake_y = [0 for i in range(25 * 25)]
        self.snake_x[0] = 100
        self.snake_y[0] = start_y
        self.snake_x[1] = 80
        self.snake_y[1] = start_y
        self.snake_x[2] = 60
        self.snake_y[2] = start_y
        self.snake_len = 3
        self.height = 20
        self.width = 20
        self.step = 20
        self.go_left = False
        self.go_right = True
        self.go_up = False
        self.go_down = False
        self.color = color

    def stop(self):
        self.go_left = False
        self.go_right = False
        self.go_up = False
        self.go_down = False

    def its_ok(self):
        result = True
        for i in range(1, self.snake_len):
            if self.snake_x[i] == self.snake_x[0] and self.snake_y[i] == self.snake_y[0]:
                result = False
        return result

    def direction(self, direct):
        self.stop()
        if direct == "up":
            self.go_up = True
        elif direct == "down":
            self.go_down = True
        elif direct == "left":
            self.go_left = True
        elif direct == "right":
            self.go_right = True

    def draw(self, window):
        for i in range(self.snake_len):
            x = self.snake_x[i]
            y = self.snake_y[i]
            pygame.draw.rect(window, self.color, (x - 1, y - 1, self.width - 1, self.height - 1))


    def move(self, apple, object1, object2=None):
        new_x = 0
        new_y = 0
        if self.go_right:
            new_x = self.snake_x[0] + self.step
            new_y = self.snake_y[0]
        if self.go_left:
            new_x = self.snake_x[0] - self.step
            new_y = self.snake_y[0]
        if self.go_up:
            new_x = self.snake_x[0]
            new_y = self.snake_y[0] - self.step
        if self.go_down:
            new_x = self.snake_x[0]
            new_y = self.snake_y[0] + self.step
        if new_x == apple.apple_x and new_y == apple.apple_y:
            apple.new_apple(object1, object2)
            self.snake_len += 1
        for i in reversed(range(self.snake_len)):
            if i != 0:
                self.snake_x[i] = self.snake_x[i - 1]
                self.snake_y[i] = self.snake_y[i - 1]
            else:
                self.snake_x[0] = new_x
                self.snake_y[0] = new_y
