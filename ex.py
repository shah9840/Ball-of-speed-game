import pygame
import time
import random

pygame.init()

crashed = pygame.mixer.Sound('crash.wav')


pygame.mixer.music.load("bg.wav")


display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

ball_width = 100
block_color = (153,115,255)


win = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()

ball = pygame.image.load('ball.png')
ball = pygame.transform.scale(ball, (100,100))

pygame.display.set_icon(ball)

pause = False

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(win, color, [thingx, thingy, thingw, thingh])

def car(x,y):
    win.blit(ball,(x,y))

def things_dodged(count):
    font = pygame.font.Font(None, 40, bold=False, italic=True)
    text = font.render("Score : "+ str(count), True, black)
    win.blit(text, (2,2))


def best_score(count):
    font = pygame.font.Font(None, 40, bold=False, italic=True)
    text = font.render("Best Score : "+ str(count), True, black)
    win.blit(text, (2,50))

def button(msg, x, y, w, h, ic, ac, action=None):
    
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        # print(mouse)    
        if x+w>mouse[0]>x and y+h>mouse[1]>y:
            pygame.draw.rect(win, ac, (x,y,w,h))
            if click[0] == 1 and action != None:
                # if action == "play":
                #     main_loop()
                # elif action == "quit":
                #     pygame.quit()
                #     quit()
                if action == quit:
                    # pygame.quit()
                    action()
                action()   
                 
                
        else:
            pygame.draw.rect(win, ic, (x,y, w,h))
            
        smallText = pygame.font.Font("freesansbold.ttf", 20)
        textsurf, textrect = text_objects(msg ,smallText)
        textrect.center = (x+(w/2), y+(h/2) )
        win.blit(textsurf, textrect)



def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):

    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    win.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)
    intro()
    
    #main_loop()
 
def unpause():
    global pause
    pause = False 
    pygame.mixer.music.unpause()
 
    
def paused():
    
    pygame.mixer.music.pause()
    
    largeText = pygame.font.Font('freesansbold.ttf',100)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    win.blit(TextSurf, TextRect)  
    
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        #win.fill((255,255,255))
             
        
        
        button("Continue", 100,400,100,50, (0,100,0), (10,255,10), unpause)
        button("QUIT", 550,400,100,50, (0,0,100), (10,10,255), quit)
        
        #pygame.draw.rect(win, (255,0,0), (100,400, 100,50))
       
        
        pygame.display.update()    
        clock.tick(15)
 
 
  
 
    
def intro():
    
    
    intro = True
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
        win.fill((255,255,255))
        largeText = pygame.font.Font('freesansbold.ttf',100)
        TextSurf, TextRect = text_objects("Game of speed", largeText)
        TextRect.center = ((display_width/2),(display_height/2))
        win.blit(TextSurf, TextRect)        
        
        
        button("START", 100,400,100,50, (0,100,0), (10,255,10), main_loop)
        button("QUIT", 550,400,100,50, (0,0,100), (10,10,255), quit)
        
        #pygame.draw.rect(win, (255,0,0), (100,400, 100,50))
       
        
        pygame.display.update()    
        clock.tick(15)

def crash():
    
    pygame.mixer.music.stop()
    
    crashed.play()
  
    message_display('You Crashed')

def main_loop():
    
    pygame.mixer.music.play(-1)
    
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    thing_count = 1

    global pause 
    
    x_change = 0
    dodged = 0
    
    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 6
    thing_width = 100
    thing_height = 100
    
    gameExit = False

    while not gameExit:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -9
                if event.key == pygame.K_RIGHT:
                    x_change = 9
                if event.key == pygame.K_p:
                    pause = True
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        win.fill(white)
        
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, block_color)
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)
        
        if x > display_width - ball_width or x < 0:
            crash()
           
    
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 0.1
            thing_width += 5
            pygame.display.update()
        ####
        if y < thing_starty+thing_height:
            #print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+ball_width > thing_startx and x + ball_width < thing_startx+thing_width:
                #print('x crossover')
                crash()
              
        ####
        thing_count += 1
        pygame.display.update()
        clock.tick(60)

intro()
main_loop()
pygame.quit()
quit()
