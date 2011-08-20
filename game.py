# Import a library of functions called 'pygame'
import pygame
import sys
import random
from pygame import * 

# Initialize the game engine
pygame.init()
pygame.font.init()
black = [ 0, 0, 0]
white = [255,255,255]

# Set the height and width of the screen
screen = pygame.display.set_mode([600, 500])
pygame.display.set_caption("My Game")
background = pygame.Surface(screen.get_size())
background.fill(black) 
x_coord=250
y_coord=430
clock = pygame.time.Clock()
score=0
a=pygame.font.Font(None,60)
screen.blit(a.render("Start Playing" ,4,(255,255,255)),(150,220))
pygame.display.flip()
pygame.time.delay(1000)
# Set music
music=pygame.mixer.Sound("music.ogg")
music.play()
# Create empty arrays
rain=[]
bomb=[] 
# Loop and add a Rains and Bombs in a random x,y position
for i in range(7):
    x=random.randrange(0,600)
    y=random.randrange(0,100)
    rain.append([x,y])

for i in range(12):
    x=random.randrange(0,600)
    y=random.randrange(0,500)
    bomb.append([x,y])

 
#Loop until the user clicks the close button or escape key.
done=False
while done==False:
 
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop

	if event.type == KEYUP: 
            if event.key == K_ESCAPE:
	        done = True

        move_x=0
        move_y=0
        if event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so
            # adjust speed.
            if event.key == pygame.K_LEFT:
                move_x=-6
                move_y=0
            if event.key == pygame.K_RIGHT:
                move_x= 6 
                move_y=0
                               
    #Move the object according to the speed vector.
    x_coord=x_coord+move_x
    y_coord=y_coord+move_y
      
    screen.fill(black)

    # Create a red player block
    player=pygame.image.load("28.gif").convert()
    screen.blit(player,[x_coord,y_coord])
    rect1=pygame.Rect(x_coord,y_coord,40,80)
    player.set_colorkey(white)

    pygame.display.flip()
 
    # Process each star in the list
    for i in range(len(rain)):
        # Draw the star
        rain_im=pygame.image.load("rain.gif").convert()
        screen.blit(rain_im,rain[i])
        rain_im.set_colorkey(white)
        
        # Move the star down one pixel
        rain[i][1]+=6
         
        if rect1.collidepoint(rain[i][0],rain[i][1]):
            score=score+1

            y=random.randrange(-500,-10)
            rain[i][1]=y
            # Give it a new x position
            x=random.randrange(0,500)
            rain[i][0]=x

        if rain[i][1]>500:
            y=random.randrange(-500,-10)
            rain[i][1]=y
            # Give it a new x position
            x=random.randrange(0,500)
            rain[i][0]=x
             
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    # Process each star in the list
    for i in range(len(bomb)):
        # Draw the star

        bomb_im=pygame.image.load("b2-17.gif").convert()
        screen.blit(bomb_im,bomb[i])
        bomb_im.set_colorkey(white)

        # Move the star down one pixel
        bomb[i][1]+=8

        if rect1.collidepoint(bomb[i][0],bomb[i][1]):
            score=score-1
            if score==-10:    
                a=pygame.font.Font(None,80)
                screen.blit(a.render("Game Over" ,4,(255,255,255)),(160,200))
                pygame.display.update()
                pygame.time.delay(1000)
                sys.exit(1)
            y=random.randrange(-500,-10)
            bomb[i][1]=y
            # Give it a new x position
            x=random.randrange(0,500)
            bomb[i][0]=x
        if bomb[i][1]>500:
            y=random.randrange(-500,-10)
            bomb[i][1]=y
            # Give it a new x position
            x=random.randrange(0,500)
            bomb[i][0]=x

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    clock.tick(20)
a=pygame.font.Font(None,60)
screen.blit(a.render("Your Score : " +str(score),4,(255,255,255)),(140,220))
pygame.display.flip()
pygame.time.delay(1000)

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit ()
