#clicking handler on buttons/maps

#import statement
import pygame

#initialize pygame
pygame.init()

#initialize class
class Button:
    def __init__(self, x,  y, image, scale):

        width = image.get_width()
        height = image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    #function handle clicking action on buttons and maps
    def lobbyScreen(self, window):
        
        inAction = False

        #get current position of the mouse
        mousePos = pygame.mouse.get_pos()

        #check if mouse location is overlapping button/map
        if self.rect.collidepoint(mousePos):
            #check if click occurred and not already clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                inAction = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        #draw button on screen
        window.blit(self.image, (self.rect.x, self.rect.y))

        #returns true if there was a successful click on a button/map
        #false otherwise
        return inAction
