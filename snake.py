import pygame
import pygame.freetype
import random

pygame.init()

max_width = 500
max_height = 500

width = 20
height = 20
speed = 20
run = True

snake_x = [0 for i in range(25*25)]
snake_y = [0 for i in range(25*25)]


snake_x[0] = 100
snake_y[0] = 40
snake_x[1] = 80
snake_y[1] = 40
snake_x[2] = 60
snake_y[2] = 40
snake_len = 3

apple_x = 0
apple_y = 0

left = False
right = True
up = False
down = False
apple = False

pygame.display.set_caption("Змейка")
win = pygame.display.set_mode((max_width, max_height))


def game_over():
    GAME_FONT = pygame.freetype.Font("./font.ttf", 24)
    GAME_FONT.render_to(win, ((max_width // 2) - 50, max_height // 2), "Game Over", (255, 255, 0))
    pygame.display.flip()
    pygame.time.delay(1000)


def draw_snake():
    for i in range(snake_len):
        x = snake_x[i]
        y = snake_y[i]
        pygame.draw.rect(win, (0, 0, 255), (x - 1, y - 1, width - 1, height - 1))
    pygame.draw.rect(win, (255, 0, 0), (apple_x - 1, apple_y - 1, width - 1, height - 1))


def its_ok():
    result = True
    for i in range(1, snake_len):
        if snake_x[i] == snake_x[0] and snake_y[i] == snake_y[0]:
            result =  False
    return result


def move_snake(new_x, new_y):
    global snake_len
    global run
    if new_x == apple_x and new_y == apple_y:
        new_apple()
        snake_len += 1
    for i in reversed(range(snake_len)):
        if i != 0:
            snake_x[i] = snake_x[i-1]
            snake_y[i] = snake_y[i - 1]
        else:
            snake_x[0] = new_x
            snake_y[0] = new_y


def draw_field():
    for i in range(1, max_width, width):
        pygame.draw.line(win, (255, 255, 255), (i, 1), (i, max_height))


def new_apple():
    in_snake = False
    global apple_x
    apple_x = random.randint(0, 24) * 20
    global apple_y
    apple_y = random.randint(0, 24) * 20
    global apple
    for i in range(snake_len):
        if apple_x == snake_x[i] and apple_y == snake_y[i]:
            in_snake = True
            break
    if in_snake:
        new_apple()
    apple = True


while run:
    if not apple:
        new_apple()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and not right:
        left = True
        right = False
        up = False
        down = False
    if keys[pygame.K_RIGHT] and not left:
        left = False
        right = True
        up = False
        down = False
    if keys[pygame.K_UP] and not down:
        left = False
        right = False
        up = True
        down = False
    if keys[pygame.K_DOWN] and not up:
        left = False
        right = False
        up = False
        down = True

    if left:
        move_snake(snake_x[0] - speed, snake_y[0])
    if right:
        move_snake(snake_x[0] + speed, snake_y[0])
    if up:
        move_snake(snake_x[0], snake_y[0] - speed)
    if down:
        move_snake(snake_x[0], snake_y[0] + speed)

    win.fill((0, 0, 0))

    if snake_x[0] in range(0, max_width) and snake_y[0] in range(0, max_height):
        draw_snake()
    else:
        run = False
    if not its_ok():
        run = False
    pygame.display.update()
    pygame.time.delay(100)

game_over()
pygame.quit()
