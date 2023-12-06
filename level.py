import pygame
from tiles import Ground
from settings import tile_size, SPEED, SCREEN_WIDTH
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.level_setup(level_data)

        self.world_shift = 0

    def level_setup(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "X":
                    tile = Ground((x, y))
                    self.tiles.add(tile)

                if cell == "P":
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < (.45 * SCREEN_WIDTH) and direction_x < 0:
            self.world_shift = SPEED
            player.speed = 0
        
        elif player_x > (.55 * SCREEN_WIDTH) and direction_x > 0:
            self.world_shift = SPEED * -1
            player.speed = 0

        else:
            self.world_shift = 0
            player.speed = SPEED

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.disable_jump = False
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.disable_jump = True


    def draw(self):
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        #player sprite
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

    