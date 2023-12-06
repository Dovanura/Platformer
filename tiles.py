import pygame
from settings import tile_size
from settings import Colors



class Ground(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.size = tile_size
        self.image = pygame.Surface((self.size, self.size))
        self.rect = self.image.get_rect(topleft = pos)
        self.image.fill(Colors["Green"])

    def update(self, x_shift):
        self.rect.x += x_shift
        

    