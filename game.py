import pygame
import time
import random
pygame.init()
white =(255,255,255)
black = (0,0,0)
red =(255,0,0)
violet =(123,55,234)
block_size = 10
display_width = 800
display_length = 600
apple_img = pygame.image.load("boy.png")
gameDisplay = pygame.display.set_mode((display_width,display_length))
pygame.display.set_caption('sannnp')
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 75)
def snake(block_size,snakelist):
    for XnY in snakelist:
        
        pygame.draw.rect(gameDisplay,black,[XnY[0],XnY[1],block_size,block_size])
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
        textSurface = medfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)
    return textSurface, textSurface.get_rect()
def msg_to_screen(msg, color,y_displace=0,size ="small"):
    textSurf, textRect = text_objects(msg,color,size)
    #msg_screen = font.render(msg,True,color)
    #gameDisplay.blit(msg_screen ,[round(display_width/3),round(display_length/3)])
    textRect.center = (display_width/2), (display_length/2) + y_displace
    gameDisplay.blit(textSurf, textRect)
    
def gameloop():
    
    gameExit = False
    gameOver = False
    lead_x =round(display_width/2)
    lead_y =round(display_length/2)
    clock = pygame.time.Clock()
    lead_x_change = 0
    lead_y_change = 0
    snakeList =[]
    snakeLength =1
    FPS = 30
    random_x = round(random.randrange(0,display_width - block_size))#/10.0)*10.0
    random_y = round(random.randrange(0,display_length - block_size))#/10.0)*10.0
    
    while not gameExit:
        while gameOver == True:
            gameDisplay.fill(violet)

            msg_to_screen("game Over",red,-50,"large")
            msg_to_screen("press C to continue  and Q to Quit",black,+50,"small")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = False
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0 
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = +block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change =0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = +block_size
                    lead_x_change =0
        if(lead_x>= display_width or lead_x <= 0 or lead_y >=display_length or lead_y <=0):
            gameOver = True
        lead_x += lead_x_change
        lead_y += lead_y_change 
        gameDisplay.fill(violet)
        
        snakeHead =[]
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)
        if len(snakeList)> snakeLength:
            del snakeList[0]
        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                gameOver = True
        snake(block_size,snakeList)
        AppleThickness = 30
        #pygame.draw.rect(gameDisplay,red,[random_x,random_y,AppleThickness,AppleThickness])
        gameDisplay.blit(apple_img,(random_x,random_y))
        pygame.display.update()
        #if lead_x == random_x and lead_y == random_y:
            #random_x = round(random.randrange(0,display_width - block_size)/10.0)*10.0
            #random_y = round(random.randrange(0,display_length - block_size)/10.0)*10.0
           # snakeLength += 1
        
  #      if lead_x >= random_x and lead_x <= random_x + AppleThickness:
   #         if lead_y >= random_y and lead_y <= random_y + AppleThickness:
    #            random_x = round(random.randrange(0,display_width - block_size))#/10.0)*10.0
     #           random_y = round(random.randrange(0,display_length - block_size))#/10.0)*10.0
      #          snakeLength += 1


        if lead_x > random_x and lead_x < random_x + AppleThickness or lead_x + block_size > random_x  and lead_x + block_size < random_x + AppleThickness:
            if lead_y > random_y and lead_y < random_y + AppleThickness or lead_y + block_size > random_y  and lead_y + block_size < random_y + AppleThickness:
                random_x = round(random.randrange(0,display_width - block_size))#/10.0)*10.0
                random_y = round(random.randrange(0,display_length - block_size))#/10.0)*10.0
                snakeLength += 1
        clock.tick(FPS)
    #msg_to_screen('You Lose',red)
    #pygame.display.update() 
    #time.sleep(2)
    pygame.quit()
    quit()
gameloop()
