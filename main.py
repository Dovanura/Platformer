import pygame
from settings import SCREEN_HEIGHT, SCREEN_WIDTH, Colors, FPS
from tiles import Ground

from level import Level
from level_maps import level_maps


#setup Pygame
pygame.init()
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Platform Game")
clock = pygame.time.Clock()
level_index = 1
#level = Level(level_maps[level_index], SCREEN)


def main():
    replay = True

    while replay:
        run = True
        level = Level(level_maps[level_index], SCREEN)

        while run:
            clock.tick(FPS)

    #-------Draw "function"----------------------------------- 
            SCREEN.fill(Colors["Sky Blue"])

            #this draws and updates both level and player
            level.draw()

            pygame.display.update()
    #-------------------------------------------------------        

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    replay = False
                    break

            #separate key presses not related to the player
            keys = pygame.key.get_pressed()

            if keys[pygame.K_ESCAPE]:
                run = False
                break

    pygame.quit()


if __name__ == "__main__":
    main()

    