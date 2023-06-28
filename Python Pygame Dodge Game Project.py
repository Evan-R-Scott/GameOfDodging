import pygame
##import Button
#main loop code
pygame.init()

#initialize screen window size
screen_height = 500
screen_width = 800

background_size = (screen_width, screen_height)

#button calculations
start_locX = screen_width / 2 - screen_width
start_locY = screen_height * 1/3
menuState = "main"

#menu background
menu_background = pygame.image.load("menu_background.jpg")
menu_background = pygame.transform.scale(menu_background,background_size)

#button
start_button = pygame.image.load("start_button-removebg-preview.png")
difficulty_button = pygame.image.load("difficulty_button.png")
map_button = pygame.image.load("map_button.jfif")
back_button = pygame.image.load("back_button.jfif")



#winter game background
winter_game_background = pygame.image.load("winter_game_background.jpg")
winter_game_background = pygame.transform.scale(winter_game_background, background_size)

#volcano game background
volcano_game_background = pygame.image.load("volcano_game_background.webp")
volcano_game_background = pygame.transform.scale(volcano_game_background, background_size)

#desert game background
desert_game_background = pygame.image.load("desert_game_background.jpg")
desert_game_background = pygame.transform.scale(desert_game_background, background_size)

#grassy game background
grassy_game_background = pygame.image.load("grassy_game_background.jpg")
grassy_game_background = pygame.transform.scale(grassy_game_background, background_size)

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodge Game")

#game loop
run = True
while run:
    if menuState == "main":
        screen.blit(menu_background,(0,0))
        screen.blit(start_button,(start_locX , start_locY))
    elif menuState == "game":
        screen.blit(grassy_game_background, (0,0))

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                menuState = "game"
                break
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()

pygame.quit()


