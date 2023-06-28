#lobby screen
import pygame

pygame.init()

class Button:
    def __init__(self, x,  y, image, scale):

        width = image.get_width()
        height = image.get_height()
        self.scale = scale
        self.image = pygame.transform.scale(image, int(width * scale), int(height * scale))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
    
    def lobbyScreen(self, window):
        
        inAction = False

        mousePos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mousePos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                inAction = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        check = False

        if check:
            check = True
        
        return check
