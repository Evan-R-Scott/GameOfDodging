import pygame
import LobbyScreenCode
#main loop code
pygame.init()

#initialize screen window size
screen_height = 500
screen_width = 800

background_size = (screen_width, screen_height)
topLeft = (0,0)

menuState = "main"

#menu background
menu_background = pygame.image.load("menu_background.jpg")
menu_background = pygame.transform.scale(menu_background,background_size)

#button
start_button = pygame.image.load("start_button-removebg-preview.png")
difficulty_button = pygame.image.load("difficulty_button.png")
map_button = pygame.image.load("map_button-removebg-preview.png")
back_button = pygame.image.load("back_button-removebg-preview.png")

start_img = LobbyScreenCode.Button(50, 50, start_button, 0.5)
difficulty_img = LobbyScreenCode.Button(50, 50, difficulty_button, 0.5)
map_img = LobbyScreenCode.Button(50, 50, map_button, 0.5)
back_img = LobbyScreenCode.Button(50, 50, back_button, 0.5)

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
        screen.blit(menu_background,topLeft)

        start_img.lobbyScreen(screen)
        difficulty_img.lobbyScreen(screen)
        map_img.lobbyScreen(screen)
        back_img.lobbyScreen(screen)
        
    elif menuState == "game":
        screen.blit(grassy_game_background, topLeft)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_TAB:
                menuState = "main"
                break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menuState = "game"
                break
        if event.type == pygame.QUIT:
            run = False
        
    pygame.display.update()

pygame.quit()


