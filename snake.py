import pygame
import pygame.freetype
from controls import Controls
from objects import Objects, Apple
from menu import Menu


pygame.init()
count_x = 60
count_y = 40
max_width = count_x * 20
max_height = count_y * 20
pygame.display.set_caption("Змейка")
win = pygame.display.set_mode((max_width, max_height))


def play():
    def game_over():
        game_font = pygame.freetype.Font("./font.ttf", 24)
        game_font.render_to(win, ((max_width // 2) - 50, max_height // 2), "Game Over", (255, 255, 0))
        game_font.render_to(win, ((max_width // 2) - 90, (max_height // 2) + 25),
                            f"Collected apples: {len(objects.snake) - 3}", (0, 255, 0))
        pygame.display.flip()
        pygame.time.delay(100)

    objects = Objects((0, 0, 255), 40)
    control = Controls()
    apple = Apple(count_x, count_y)
    delay = 0
    while control.run:
        if not apple.apple:
            apple.new_apple(objects, None)
        control.first_player(objects)
        delay += 1
        if delay >= 10:
            delay = 0
            objects.change_lastr_direction()
            objects.move(apple, objects)
            objects.draw(win)
            apple.draw(win)
            win.fill((0, 0, 0))
            if objects.snake[0][0] in range(0, max_width) and objects.snake[0][1] in range(0, max_height):
                objects.draw(win)
                apple.draw(win)
            else:
                control.run = False
            if not objects.its_ok(None):
                control.run = False
        pygame.display.update()
        pygame.time.delay(10)
    game_over()


def two_players():
    def game_over():
        game_font = pygame.freetype.Font("./font.ttf", 24)
        game_font.render_to(win, ((max_width // 2) - 50, max_height // 2), "Game Over", (255, 255, 0))
        game_font.render_to(win, ((max_width // 2) - 90, (max_height // 2) + 25),
                            f"Collected apples: {len(object1.snake) - 3}", (0, 0, 255))
        game_font.render_to(win, ((max_width // 2) - 90, (max_height // 2) + 50),
                            f"Collected apples: {len(object2.snake) - 3}", (0, 255, 0))
        pygame.display.flip()
        pygame.time.delay(100)

    object1 = Objects((0, 0, 255), 40)
    object2 = Objects((0, 255, 0), 120)
    control = Controls()
    apple = Apple(count_x, count_y)
    delay = 0
    while control.run:
        if not apple.apple:
            apple.new_apple(object1, object2)
        delay += 1
        control.two_players(object1, object2)
        if delay >= 10:
            delay = 0
            object1.change_lastr_direction()
            object1.move(apple, object1, object2)
            object2.change_lastr_direction()
            object2.move(apple, object2, object1)
            apple.draw(win)
            win.fill((0, 0, 0))
            if (object1.snake[0][0] in range(0, max_width) and object1.snake[0][1] in range(0, max_height)) \
                    and (object2.snake[0][0] in range(0, max_width) and object2.snake[0][1] in range(0, max_height)):
                object1.draw(win)
                object2.draw(win)
                apple.draw(win)
            else:
                control.run = False
            if not object1.its_ok(object2):
                control.run = False
            if not object2.its_ok(object1):
                control.run = False
        pygame.display.update()
        pygame.time.delay(10)
    game_over()


retry = True
menu = Menu(max_width, max_height)
while retry:
    action = menu.menu(win)
    if action == 0:
        play()
    elif action == 1:
        two_players()
    elif action == 2:
        retry = False
    pygame.time.delay(50)
pygame.quit()
