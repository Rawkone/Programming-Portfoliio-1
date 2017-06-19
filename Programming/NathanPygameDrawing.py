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

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("My Game")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
 
    pygame.draw.line(screen, BLUE, [350, 400], [350, 0], 1000)
    pygame.draw.line(screen, DARKGREEN, [350, 4000], [350, 400], 1000)
    
    for x_offset in range(50, 3000, 50):
         pygame.draw.line(screen,WHITE,[x_offset,100],[x_offset-10,90],2)
         pygame.draw.line(screen,WHITE,[x_offset,90],[x_offset-10,100],2) 
    for x_offset in range(50, 3000, 50):
     pygame.draw.line(screen,WHITE,[x_offset,100],[x_offset-10,200],2)
     pygame.draw.line(screen,WHITE,[x_offset,90],[x_offset-10,100],2)       
    
    pygame.draw.line(screen, BROWN, [350, 400], [350, 50], 50)
    
    pygame.draw.line(screen, GREEN, [350, 50], [250, 250], 50)
    pygame.draw.line(screen, GREEN, [350, 50], [450, 250], 50)
    pygame.draw.line(screen, GREEN, [350, 100], [460, 300], 50)
    pygame.draw.line(screen, GREEN, [350, 100], [240, 300], 50)
    pygame.draw.line(screen, GREEN, [350, 150], [470, 350], 50)
    pygame.draw.line(screen, GREEN, [350, 150], [230, 350], 50)
    pygame.draw.polygon(screen, GREEN, [[450,350], [350,100], [250,350]],)
    
    pygame.draw.arc(screen, RED, [260,200,50,50],  PI/2,     PI,24)
    pygame.draw.arc(screen, RED, [260,200,50,50],     0,   PI/2,24)
    pygame.draw.arc(screen, RED, [260,200,50,50],3*PI/2,   2*PI,24)
    pygame.draw.arc(screen, RED, [260,200,50,50],    PI, 3*PI/2,24)
    
    pygame.draw.arc(screen, BLACK, [260,295,50,50],  PI/2,     PI,24)
    pygame.draw.arc(screen, BLACK, [260,295,50,50],     0,   PI/2,24)
    pygame.draw.arc(screen, BLACK, [260,295,50,50],3*PI/2,   2*PI,24)
    pygame.draw.arc(screen, BLACK, [260,295,50,50],    PI, 3*PI/2,24)    
    
    pygame.draw.arc(screen, PINK, [330,240,50,50],  PI/2,     PI,24)
    pygame.draw.arc(screen, PINK, [330,240,50,50],     0,   PI/2,24)
    pygame.draw.arc(screen, PINK, [330,240,50,50],3*PI/2,   2*PI,24)
    pygame.draw.arc(screen, PINK, [330,240,50,50],    PI, 3*PI/2,24)    
    
    pygame.draw.arc(screen, BLUE, [310,100,50,50],  PI/2,     PI,24)
    pygame.draw.arc(screen, BLUE, [310,100,50,50],     0,   PI/2,24)
    pygame.draw.arc(screen, BLUE, [310,100,50,50],3*PI/2,   2*PI,24)
    pygame.draw.arc(screen, BLUE, [310,100,50,50],    PI, 3*PI/2,24)  
    
    pygame.draw.arc(screen, ORANGE, [400,250,50,50],  PI/2,     PI,24)
    pygame.draw.arc(screen, ORANGE, [400,250,50,50],     0,   PI/2,24)
    pygame.draw.arc(screen, ORANGE, [400,250,50,50],3*PI/2,   2*PI,24)
    pygame.draw.arc(screen, ORANGE, [400,250,50,50],    PI, 3*PI/2,24)
    
    pygame.draw.arc(screen, PINK, [370,130,50,50],  PI/2,     PI,24)
    pygame.draw.arc(screen, PINK, [370,130,50,50],     0,   PI/2,24)
    pygame.draw.arc(screen, PINK, [370,130,50,50],3*PI/2,   2*PI,24)
    pygame.draw.arc(screen, PINK, [370,130,50,50],    PI, 3*PI/2,24)     
    
    pygame.draw.line(screen, RED, [310, 80], [400, 100], 5)
    pygame.draw.line(screen, RED, [265, 170], [450, 200], 5)
    pygame.draw.line(screen, RED, [227, 280], [477, 320], 5)
    
    pygame.draw.line(screen, RED, [340, 0], [310, 70], 10)
    pygame.draw.line(screen, RED, [310, 70], [400, 25], 10)
    pygame.draw.line(screen, RED, [400, 25], [300, 25], 10)
    pygame.draw.line(screen, RED, [300, 25], [390, 70], 10)
    pygame.draw.line(screen, RED, [390, 70], [360, 0], 10)
    
    
    
    
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)
  
# Close the window and quit.
pygame.quit()
