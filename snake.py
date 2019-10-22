import pygame
import pygame.freetype
from controls import Controls
from objects import Objects
from menu import Menu

pygame.init()
max_width = 500
max_height = 500
pygame.display.set_caption("Змейка")
win = pygame.display.set_mode((max_width, max_height))


def play():
    def game_over():
        game_font = pygame.freetype.Font("./font.ttf", 24)
        game_font.render_to(win, ((max_width // 2) - 50, max_height // 2), "Game Over", (255, 255, 0))
        game_font.render_to(win, ((max_width // 2) - 90, (max_height // 2) + 25),
                            f"Collected apples: {objects.snake_len - 3}", (0, 255, 0))
        pygame.display.flip()
        pygame.time.delay(100)

    objects = Objects()
    control = Controls()
    while control.run:
        if not objects.apple:
            objects.new_apple()
        control.control(objects)
        objects.move()
        objects.draw(win)
        win.fill((0, 0, 0))
        if objects.snake_x[0] in range(0, max_width) and objects.snake_y[0] in range(0, max_height):
            objects.draw(win)
        else:
            control.run = False
        if not objects.its_ok():
            control.run = False
        pygame.display.update()
        pygame.time.delay(100)
    game_over()


retry = True
menu = Menu(max_width, max_height)
while retry:
    action = menu.menu(win)
    if action == 0:
        play()
    elif action == 1:
        retry = False
    pygame.time.delay(50)
pygame.quit()
