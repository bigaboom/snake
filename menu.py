import pygame
import pygame.freetype


class Menu:
    def __init__(self, max_width, max_height):
        self.active = True
        self.menu_start_x = (max_width // 2)
        self.menu_start_y = (max_height // 4)
        self.menu_items = [
            "One player",
            "Two players",
            "Exit"
        ]

    def menu(self, window):
        self.menu_active = 0
        keys_last = pygame.key.get_pressed()
        self.active = True
        while self.active:
            game_font = pygame.freetype.Font("./font.ttf", 24)
            game_font.render_to(window, (self.menu_start_x - 60, self.menu_start_y - 50), "Snake Game", (0, 255, 0))
            for i in range(len(self.menu_items)):
                if self.menu_active == i:
                    game_font.render_to(window,
                                        (self.menu_start_x - (len(self.menu_items[i]) // 2) * 12,
                                         self.menu_start_y + i * 25), f"{self.menu_items[i]}", (255, 255, 0))
                else:
                    game_font.render_to(window,
                                        (self.menu_start_x - (len(self.menu_items[i]) // 2) * 12,
                                         self.menu_start_y + i * 25), f"{self.menu_items[i]}", (155, 155, 0))
            pygame.display.flip()
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.active = False
                    self.menu_active = 2    # Установка флага Exit
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] and not keys_last[pygame.K_UP]:
                if self.menu_active == 0:
                    self.menu_active = len(self.menu_items) - 1
                else:
                    self.menu_active -= 1
            if keys[pygame.K_DOWN] and not keys_last[pygame.K_DOWN]:
                if self.menu_active == len(self.menu_items) - 1:
                    self.menu_active = 0
                else:
                    self.menu_active += 1
            if keys[pygame.K_RETURN]:
                self.active = False
            keys_last = keys
        return self.menu_active
