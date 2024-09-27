import pygame
import random


pygame.init()

#colours
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
brown=(205,127,50)
green=(0, 255, 0)
forestgrn=(34,139,34)

screen_width= 900
screen_height= 600

#creating game window
gamewindow= pygame.display.set_mode((screen_width,screen_height))

pygame.display.set_caption("Snake Game")
pygame.display.update()




clock= pygame.time.Clock()
font=pygame.font.SysFont(None,55)


def text_screen(text,color,x,y):
    screen_text= font.render(text, True,color)
    gamewindow.blit(screen_text,[x,y])

def  plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow,color,[x,y,snake_size,snake_size])


#game loop
def gameloop():
    #game specific variables
    exit_game= False
    game_over= False
    snake_x=45
    snake_y=55
    velocity_x=0
    velocity_y=0

    snk_list=[]
    snk_length=1

    with open("highscore.txt","r") as f:
      hiiscore= f.read()

    score=0
    food_x=random.randint(0,screen_width/2)
    food_y=random.randint(0,screen_height/2)
    snake_size=30
    fps=60  # frame per seecond
    while not exit_game:

        if game_over:
            with open("highscore.txt","w") as f:
              f.write(str(hiiscore))
            gamewindow.fill(green)
            text_screen("Game Over! Press Enter to Continue",red,100,250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:         # handelling a event
                    exit_game= True 
                if event.type== pygame.KEYDOWN:
                    if event.key== pygame.K_RETURN:
                        gameloop()
        else:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:         # handelling a event
                    exit_game= True 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x =10
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -10
                        velocity_y = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y=  10
                        velocity_x=  0
                    if event.key == pygame.K_UP:
                        velocity_y = -10
                        velocity_x = 0
            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y
            
            if abs(snake_x - food_x)<30 and abs(snake_y- food_y)<30:  #abs= absolute value
                score +=10
                # print("Score: ",score*10)
                food_x=random.randint(0,screen_width/2)
                food_y=random.randint(0,screen_height/2)
                snk_length +=5
                if score>int(hiiscore):
                    hiiscore=score
            

            gamewindow.fill(green)
            text_screen("Score: "+ str(score) + "  HighScore: "+str(hiiscore),red,5,5)
            pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
        #  pygame.draw.rect(gamewindow,black,snake_x,snake_y,snake_size,snake_size)

            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>snk_length :
                del snk_list[0]
            

            if head in snk_list[:-1]:    # it takes all elements of list except 1 by using ':'
                game_over= True
            if snake_x<0 or snake_x>screen_width or snake_y<0 or snake_y>screen_height:
                game_over= True
                

            plot_snake(gamewindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)



    pygame.quit()
    quit()

gameloop()