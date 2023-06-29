#import statements
import pygame
import LobbyScreenCode
#main loop code
pygame.init()

#initialize screen window size
screen_height = 600
screen_width = 800

#origin and screen dimensions as tuple for efficiency
background_size = (screen_width, screen_height)
topLeft = (0,0)
mapPick_size = (200, 100)

#initialize game state to main aka lobby screen
menuState = "main"


#menu background
menu_background = pygame.image.load("menu_background.jpg")
menu_background = pygame.transform.scale(menu_background,background_size)

#load images
start_button = pygame.image.load("startButton.png")
difficulty_button = pygame.image.load("difficultyButton.png")
map_button = pygame.image.load("mapButton.png")
back_button = pygame.image.load("backButton.png")
exit_button = pygame.image.load("exitButton.png")
resume_button = pygame.image.load("resumeButton.png")

#call buttons into button class
start_img = LobbyScreenCode.Button(330, 30, start_button, 2)
difficulty_img = LobbyScreenCode.Button(300, 130, difficulty_button, 2)
map_img = LobbyScreenCode.Button(330, 230, map_button, 2)
back_img = LobbyScreenCode.Button(330, 500, back_button, 2)
exit_img = LobbyScreenCode.Button(330,330, exit_button, 2)
resume_img = LobbyScreenCode.Button(310,90, resume_button, 2.5)

#winter game background
winter_game_background = pygame.image.load("winter_game_background.jpg")
winter_mapPick = pygame.transform.scale(winter_game_background, mapPick_size)
winter_game_background = pygame.transform.scale(winter_game_background, background_size)

#volcano game background
volcano_game_background = pygame.image.load("volcano_game_background.webp")
volcano_mapPick = pygame.transform.scale(volcano_game_background, mapPick_size)
volcano_game_background = pygame.transform.scale(volcano_game_background, background_size)

#desert game background
desert_game_background = pygame.image.load("desert_game_background.jpg")
desert_mapPick = pygame.transform.scale(desert_game_background, mapPick_size)
desert_game_background = pygame.transform.scale(desert_game_background, background_size)

#grassy game background
grassy_game_background = pygame.image.load("grassy_game_background.jpg")
grassy_mapPick = pygame.transform.scale(grassy_game_background, mapPick_size)
grassy_game_background = pygame.transform.scale(grassy_game_background, background_size)

#call maps to button class and change maps for game
winter_game = LobbyScreenCode.Button(430,100, winter_mapPick, 1)
volcano_game = LobbyScreenCode.Button(430,300, volcano_mapPick, 1)
desert_game = LobbyScreenCode.Button(150,300, desert_mapPick, 1)
grassy_game = LobbyScreenCode.Button(150,100, grassy_mapPick, 1)

#game background, default is grassy
background = grassy_game_background

#create window and title
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Dodge Game")

#Set up font settings
color = (52,78,91)
textColor = (255,255,255)
pausedFont = pygame.font.SysFont("Arial", 36)
UnpauseTxt= pausedFont.render("Press SPACE BAR to resume the game.", True, textColor)
Or = pausedFont.render("OR", True, textColor)
EscTxt= pausedFont.render("Press ESC to exit the application.", True, textColor)
mainTxt = pausedFont.render("Press TAB to pause the game.", True, textColor)
MapTxt= pausedFont.render("Select A Map", True, textColor)

#game loop
run = True
while run:

    #in lobby screen 
    if menuState == "main":
        screen.blit(menu_background,topLeft)
        screen.blit(mainTxt, (screen_width //2 - 4.5 *mainTxt.get_height() , 500))

        #handle the various button presses on the lobby screen
        if start_img.lobbyScreen(screen):
            print("Game Starting")
            menuState = "game"
        elif difficulty_img.lobbyScreen(screen):
            print("Difficulty")
        elif map_img.lobbyScreen(screen):
            menuState = "map"
        elif exit_img.lobbyScreen(screen):
            run = False
    #in game 
    elif menuState == "game":
        screen.blit(background, topLeft)

    #in pause menu
    elif menuState == "gamePaused":
        screen.fill(color)
        screen.blit(UnpauseTxt, (screen_width //2 - 6 *mainTxt.get_height() , 450))
        screen.blit(EscTxt, (screen_width //2 - 5 *mainTxt.get_height() , 500))
        screen.blit(Or, (screen_width //2 - 0.6 * mainTxt.get_height() , 300))

        #handle resume button being pressed
        if resume_img.lobbyScreen(screen):
            print("Game Resumed")
            menuState = "game"

    elif menuState == "map":
        screen.fill(color)
        screen.blit(MapTxt, (screen_width //2 - 2.2 *MapTxt.get_height() , 225))

        if back_img.lobbyScreen(screen):
            menuState = "main"
        if winter_game.lobbyScreen(screen):
            print("Successful Map Change")
            background = winter_game_background
        elif volcano_game.lobbyScreen(screen):
            print("Successful Map Change")
            background = volcano_game_background
        elif grassy_game.lobbyScreen(screen):
            print("Successful Map Change")
            background = grassy_game_background
        elif desert_game.lobbyScreen(screen):
            print("Successful Map Change")
            background = desert_game_background


    #check key pressings and handle accordingly
    for event in pygame.event.get():

        #tab pressed so pause current game
        if event.type == pygame.KEYDOWN and menuState == "game":
            if event.key == pygame.K_TAB:
                menuState = "gamePaused"
                break

        #space pressed so resume game from being paused
        if event.type == pygame.KEYDOWN and menuState == "gamePaused":
            if event.key == pygame.K_SPACE:
                menuState = "game"
                break
        
        #ESC pressed in pause screen so close entire application
        if menuState == "gamePaused" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        #quit application
        if event.type == pygame.QUIT:
            run = False

    #update screen
    pygame.display.update()

#close window
pygame.quit()


