import pygame
import math
import random 

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BROWN = (132,75,9)
PI = 3.141592653
BLUE = (60,0,255)
ORANGE = (243,133,7)
DARKGREEN = (3,119,3)
PINK = (255,0,205)
 
 

def draw_tree(screen, x, y):
    
    pygame.draw.line(screen, BROWN, [350 + x, 400 + y], [350 + x, 50 + y], 50)
    
    pygame.draw.line(screen, GREEN, [350+ x, 50 + y], [250+ x, 250 + y], 50)
    pygame.draw.line(screen, GREEN, [350+ x, 50 + y], [450+ x, 250 + y], 50)
    pygame.draw.line(screen, GREEN, [350+ x, 100 + y], [460+ x, 300 + y], 50)
    pygame.draw.line(screen, GREEN, [350+ x, 100 + y], [240+ x, 300 + y], 50)
    pygame.draw.line(screen, GREEN, [350+ x, 150 + y], [470+ x, 350 + y], 50)
    pygame.draw.line(screen, GREEN, [350+ x, 150 + y], [230+ x, 350 + y], 50)
    pygame.draw.polygon(screen, GREEN, [[450+ x,350 + y], [350+ x,100 + y], [250+ x,350 + y]],)
    
screen = pygame.display.set_mode((1000, 1000))
screen_rect=screen.get_rect() 
player=pygame.Rect(180, 180, 20, 20)

# Setup
pygame.init()
 
# Set the width and height of the screen [width,height]
size = [1000, 1000]
screen_rect=screen.get_rect() 
player=draw_tree
screen = pygame.display.set_mode((1000, 1000))
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# Hide the mouse cursor
pygame.mouse.set_visible(0)
 
# Speed in pixels per frame
x_speed = 0
y_speed = 0
 
# Current position
x_coord = 100
y_coord = 100
 
# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            # User pressed down on a key
 
        elif event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_a:
                player.move_ip(-1, 0)
            elif event.key == pygame.K_d:
                player.move_ip(1, 0)
            elif event.key == pygame.K_w:
                player.move_ip(0, -1)
            elif event.key == pygame.K_s:
                player.move_ip(0, 1)
 
        # User let up on a key
        elif event.type == pygame.KEYUP:
            # If it is an arrow key, reset vector back to zero
            if event.key == pygame.K_a or event.key == pygame.K_d:
                x_speed = 0
            elif event.key == pygame.K_w or event.key == pygame.K_s:
                y_speed = 0
 
    # --- Game Logic
 
    # Move the object according to the speed vector.
    x_coord = x_coord + x_speed
    y_coord = y_coord + y_speed
 
    # --- Drawing Code
 
    # First, clear the screen to WHITE. Don't put other drawing commands
    # above this, or they will be erased with this command.
    
    draw_tree(screen, x_coord, y_coord)
    
    player.clamp_ip(screen_rect)
    
    screen.fill(WHITE)
    
    pygame.draw.rect(screen, (0,0,0), player)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # Limit frames per second
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()