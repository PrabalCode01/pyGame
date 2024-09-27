from operator import truediv
import pygame
# import time
pygame.init()

#creating game window
gamewindow= pygame.display.set_mode((1200,500))

# giving title for game
pygame.display.set_caption("My First Game")


# time.sleep(5)


#game specific variables
exit_game= False
game_over= False

#creating game loop
while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:         # handelling a event
            exit_game= True 


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                print("You have presed right key")    

pygame.quit()
quit()
