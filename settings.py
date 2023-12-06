from level_maps import level_maps

tile_size = 64
SCREEN_WIDTH = 1200
#SCREEN_HEIGHT = tile_size * len(level_maps["Level 1 Map"])
SCREEN_HEIGHT = 700

#set max FPS
global FPS
FPS = 60

#player/level speed
global SPEED
SPEED = 5
JUMP_SPEED = -16

#Gravity Variable
global GRAVITY
GRAVITY = 0.8

#Color variables
Colors = {
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "Green": (8, 135, 26),
    "Sky Blue": (91, 188, 253),
    "Red": (235, 25, 75)
}