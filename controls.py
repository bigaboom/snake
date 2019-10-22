import pygame


class Controls:
    def __init__(self):
        self.run = True

    def control(self, objects):
        last_direction = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
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
