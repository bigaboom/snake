import pygame


class Controls:
    def __init__(self):
        self.run = True

    def first_player(self, objects):
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

    def two_players(self, object1, object2):
        last_direction = ""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
        if object1.go_down:
            last_direction = "down"
        if object1.go_up:
            last_direction = "up"
        if object1.go_left:
            last_direction = "left"
        if object1.go_right:
            last_direction = "right"
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and last_direction != "right":
            object1.direction("left")
        if keys[pygame.K_RIGHT] and last_direction != "left":
            object1.direction("right")
        if keys[pygame.K_UP] and last_direction != "down":
            object1.direction("up")
        if keys[pygame.K_DOWN] and last_direction != "up":
            object1.direction("down")
        last_direction = ""
        if object2.go_down:
            last_direction = "down"
        if object2.go_up:
            last_direction = "up"
        if object2.go_left:
            last_direction = "left"
        if object2.go_right:
            last_direction = "right"
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and last_direction != "right":
            object2.direction("left")
        if keys[pygame.K_d] and last_direction != "left":
            object2.direction("right")
        if keys[pygame.K_w] and last_direction != "down":
            object2.direction("up")
        if keys[pygame.K_s] and last_direction != "up":
            object2.direction("down")
