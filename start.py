import pygame
import math

# Set the screen size
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Set the background color to white
screen.fill((255, 255, 255))

# Set the number of rays to cast
num_rays = 360

# Set the field of view
fov = 90

# Set the distance from the viewer to the projection plane
projection_plane_distance = SCREEN_WIDTH / 2 / math.tan(math.radians(fov / 2))

# Set the position of the viewer
viewer_position = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

# Set the color of the walls
wall_color = (0, 0, 0)

# Set the map of the environment
# 0 = empty space
# 1 = wall
# 2 = player
# 3 = goal
map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

# Set the player's position
player_position = (2, 2)

# Set the goal position
goal_position = (8, 8)

# Set the player's direction (in degrees)
player_direction = 0

# Set the player's field of view (in degrees)
player_fov = 60

# Set the player's speed (in pixels per frame)
player_speed = 5

# Set the player's turn speed (in degrees per frame)
player_turn_speed = 5

# Set the maximum distance that a ray can travel
max_distance = SCREEN_WIDTH

# Set the player's viewport (the portion of the screen that the player can see)
viewport_left = viewer_position[0] - SCREEN_WIDTH / 2
viewport_right = viewer_position[0] + SCREEN_WIDTH / 2
viewport_top = viewer_position[1] - SCREEN_HEIGHT / 2
viewport_bottom = viewer_position[1] + SCREEN_HEIGHT / 2
