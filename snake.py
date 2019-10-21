import pygame
import pygame.freetype
import random

pygame.init()

max_width = 500
max_height = 500

run = True

pygame.display.set_caption("Змейка")
win = pygame.display.set_mode((max_width, max_height))

class GameWindow:
    def __init__(self):
        self.max_width = 500
        self.max_height = 500
        self.step = 20


class Objects:
    def __init__(self):
        self.snake_x = [0 for i in range(25 * 25)]
        self.snake_y = [0 for i in range(25 * 25)]
        self.snake_x[0] = 100
        self.snake_y[0] = 40
        self.snake_x[1] = 80
        self.snake_y[1] = 40
        self.snake_x[2] = 60
        self.snake_y[2] = 40
        self.snake_len = 3
        self.height = 20
        self.width = 20
        self.apple = False
        self.apple_x = 0
        self.apple_y = 0
        self.step = 20
        self.goleft = False
        self.goright = True
        self.goup = False
        self.godown = False

    def stop(self):
        self.goleft = False
        self.goright = False
        self.goup = False
        self.godown = False

    def its_ok(self):
        result = True
        for i in range(1, self.snake_len):
            if self.snake_x[i] == self.snake_x[0] and self.snake_y[i] == self.snake_y[0]:
                result = False
        return result

    def direction(self, direct):
        if direct == "up":
            self.goup = True
        elif direct == "down":
            self.godown = True
        elif direct == "left":
            self.goleft = True
        elif direct == "right":
            self.goright = True

    def draw(self):
        for i in range(self.snake_len):
            x = self.snake_x[i]
            y = self.snake_y[i]
            pygame.draw.rect(win, (0, 0, 255), (x - 1, y - 1, self.width - 1, self.height - 1))
        pygame.draw.rect(win, (255, 0, 0), (self.apple_x - 1, self.apple_y - 1, self.width - 1, self.height - 1))

    def new_apple(self):
        in_snake = False
        self.apple_x = random.randint(0, 24) * 20
        self.apple_y = random.randint(0, 24) * 20
        for i in range(self.snake_len):
            if self.apple_x == self.snake_x[i] and self.apple_y == self.snake_y[i]:
                in_snake = True
                break
        if in_snake:
            self.new_apple()
        self.apple = True

    def move(self):
        if self.goright:
            new_x = self.snake_x[0] + self.step
            new_y = self.snake_y[0]
        if self.goleft:
            new_x = self.snake_x[0] - self.step
            new_y = self.snake_y[0]
        if self.goup:
            new_x = self.snake_x[0]
            new_y = self.snake_y[0] - self.step
        if self.godown:
            new_x = self.snake_x[0]
            new_y = self.snake_y[0] + self.step
        if new_x == self.apple_x and new_y == self.apple_y:
            self.new_apple()
            self.snake_len += 1
        for i in reversed(range(self.snake_len)):
            if i != 0:
                self.snake_x[i] = self.snake_x[i - 1]
                self.snake_y[i] = self.snake_y[i - 1]
            else:
                self.snake_x[0] = new_x
                self.snake_y[0] = new_y
        self.draw()


def game_over():
    GAME_FONT = pygame.freetype.Font("./font.ttf", 24)
    GAME_FONT.render_to(win, ((max_width // 2) - 50, max_height // 2), "Game Over", (255, 255, 0))
    pygame.display.flip()
    pygame.time.delay(1000)


def draw_field():
    for i in range(1, max_width, width):
        pygame.draw.line(win, (255, 255, 255), (i, 1), (i, max_height))


objects = Objects()
while run:
    if not objects.apple:
        objects.new_apple()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not objects.goright:
        objects.stop()
        objects.direction("left")
    if keys[pygame.K_RIGHT] and not objects.goleft:
        objects.stop()
        objects.direction("right")
    if keys[pygame.K_UP] and not objects.godown:
        objects.stop()
        objects.direction("up")
    if keys[pygame.K_DOWN] and not objects.goup:
        objects.stop()
        objects.direction("down")
    objects.move()
    win.fill((0, 0, 0))
    if objects.snake_x[0] in range(0, max_width) and objects.snake_y[0] in range(0, max_height):
        objects.draw()
    else:
        run = False
    if not objects.its_ok():
        run = False
    pygame.display.update()
    pygame.time.delay(100)

game_over()
pygame.quit()
