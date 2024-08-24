import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
BULB_OFF_IMAGE = pygame.image.load('bulb_off.png')
BULB_ON_IMAGE = pygame.image.load('bulb_on.png')

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the clock
clock = pygame.time.Clock()

# Set up the initial state
bulb_image = BULB_OFF_IMAGE

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the bulb was clicked
            if 100 <= event.pos[0] <= 300 and 100 <= event.pos[1] <= 300:
                if bulb_image == BULB_OFF_IMAGE:
                    bulb_image = BULB_ON_IMAGE
                else:
                    bulb_image = BULB_OFF_IMAGE

    # Draw everything
    screen.fill((0, 0, 0))
    screen.blit(bulb_image, (100, 100))

    # Flip the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)