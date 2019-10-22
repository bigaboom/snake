import pygame
import pygame.freetype
import random

pygame.init()
max_width = 500
max_height = 500
pygame.display.set_caption("Змейка")
win = pygame.display.set_mode((max_width, max_height))


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
        self.go_left = False
        self.go_right = True
        self.go_up = False
        self.go_down = False

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


def menu():
    active = True
    menu_start_x = (max_width // 2)
    menu_start_y = (max_height // 4)
    menu_items = [
        "New game",
        "Exit"
    ]
    menu_active = 0
    keys_last = pygame.key.get_pressed()
    while active:
        game_font = pygame.freetype.Font("./font.ttf", 24)
        game_font.render_to(win, (menu_start_x - 60, menu_start_y - 50), "Snake Game", (0, 255, 0))
        for i in range(len(menu_items)):
            if menu_active == i:
                game_font.render_to(win, (menu_start_x - (len(menu_items[i]) // 2)*12, menu_start_y + i * 25),
                                    f"{menu_items[i]}", (255, 255, 0))
            else:
                game_font.render_to(win, (menu_start_x - (len(menu_items[i]) // 2) * 12, menu_start_y + i * 25),
                                    f"{menu_items[i]}", (155, 155, 0))
        pygame.display.flip()
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and not keys_last[pygame.K_UP]:
            if menu_active == 0:
                menu_active = len(menu_items) - 1
            else:
                menu_active -= 1
        if keys[pygame.K_DOWN] and not keys_last[pygame.K_DOWN]:
            if menu_active == len(menu_items) - 1:
                menu_active = 0
            else:
                menu_active += 1
        if keys[pygame.K_RETURN]:
            active = False
        keys_last = keys
    return menu_active


def play():
    def game_over():
        game_font = pygame.freetype.Font("./font.ttf", 24)
        game_font.render_to(win, ((max_width // 2) - 50, max_height // 2), "Game Over", (255, 255, 0))
        game_font.render_to(win, ((max_width // 2) - 90, (max_height // 2) + 25),
                            f"Collected apples: {objects.snake_len - 3}", (0, 255, 0))
        pygame.display.flip()
        pygame.time.delay(100)

    run = True
    objects = Objects()
    while run:
        if not objects.apple:
            objects.new_apple()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        if objects.go_down:
            last_direction = "down"
        if objects.go_up:
            last_direction = "up"
        if objects.go_left:
            last_direction = "left"
        if objects.go_right:
            last_direction = "right"
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and last_direction != "right":
            objects.direction("left")
        if keys[pygame.K_RIGHT] and last_direction != "left":
            objects.direction("right")
        if keys[pygame.K_UP] and last_direction != "down":
            objects.direction("up")
        if keys[pygame.K_DOWN] and last_direction != "up":
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


retry = True
while retry:
    action = menu()
    if action == 0:
        play()
    elif action == 1:
        retry = False
    pygame.time.delay(50)
pygame.quit()
