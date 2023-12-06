import pygame
from settings import Colors, SPEED, JUMP_SPEED, GRAVITY


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, speed=SPEED):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill(Colors["Red"])
        self.rect = self.image.get_rect(topleft = pos)
        

        #player movement
        self.speed = speed
        self.direction = pygame.math.Vector2(0, 0)
        self.gravity = GRAVITY
        self.jump_speed = JUMP_SPEED
        self.disable_jump = False

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE] and self.direction.y == 0 and self.disable_jump == False:
            #move up (jump)
            self.jump()

        if keys[pygame.K_s]:
            #move down (crouch?)
            pass

        if keys[pygame.K_a]:
            #move left
            self.direction.x = -1
        elif keys[pygame.K_d]:
            #move right
            self.direction.x = 1
        else:
            #stop moving
            self.direction.x = 0

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()
        