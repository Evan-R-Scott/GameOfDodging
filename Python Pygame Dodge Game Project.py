#import statements
import pygame
import time
import random
import LobbyScreenCode
#main loop code
pygame.init()

#initialize screen window size
screen_height = 600
screen_width = 800

#player dimensions and variable initialization
player_width = 40
player_height = 60
player_velocity = 10
player_location = "grassy"
base = screen_height - player_height -50
player_start = base
player_color = (255,0,0)

#initializing projectiles variables
star_add = 2000
star_count = 0
stars = []
star_width = 10
star_height = 20
star_velocity = 3
hit = False

#origin and screen dimensions as tuple for efficiency
background_size = (screen_width, screen_height)
background_size2 = (screen_width, screen_height +80)
topLeft = (0,0)
mapPick_size = (200, 100)

#initialize game state to main aka lobby screen and difficulty state to easy
menuState = "main"
difficultyState = "easy"

#clock timer
clock = pygame.time.Clock()
elapsedTime = 0

#function to determine the specifics of the player shape based on map
def draw(player_location):

    #adjust starting location and color of the player based on chosen map
    if player_location == "grassy":
        player_start = base 
        player_color = (255,0,0)
    elif player_location == "volcano":
        player_start = base - 118
        player_color = (0,0,255)
    elif player_location == "winter":
        player_start = base - 85 
        player_color = (255,255,0)
    elif player_location == "desert":
        player_start = base - 60 
        player_color = (0,255,0)
    return player_start, player_color

    
#menu background
menu_background = pygame.image.load("PicturesUsed/menu_background.jpg")
menu_background = pygame.transform.scale(menu_background,background_size)

#load images
start_button = pygame.image.load("PicturesUsed/startButton.png")
difficulty_button = pygame.image.load("PicturesUsed/difficultyButton.png")
map_button = pygame.image.load("PicturesUsed/mapButton.png")
back_button = pygame.image.load("PicturesUsed/backButton.png")
exit_button = pygame.image.load("PicturesUsed/exitButton.png")
resume_button = pygame.image.load("PicturesUsed/resumeButton.png")

#call buttons into button class
start_img = LobbyScreenCode.Button(330, 30, start_button, 2)
difficulty_img = LobbyScreenCode.Button(300, 130, difficulty_button, 2)
map_img = LobbyScreenCode.Button(330, 230, map_button, 2)
back_img = LobbyScreenCode.Button(330, 500, back_button, 2)
exit_img = LobbyScreenCode.Button(330,330, exit_button, 2)
resume_img = LobbyScreenCode.Button(310,90, resume_button, 2.5)

#winter game background
winter_game_background = pygame.image.load("PicturesUsed/winter_game_background.jpg")
winter_mapPick = pygame.transform.scale(winter_game_background, mapPick_size)
winter_game_background = pygame.transform.scale(winter_game_background, background_size2)

#volcano game background
volcano_game_background = pygame.image.load("PicturesUsed/volcano_game_background.webp")
volcano_mapPick = pygame.transform.scale(volcano_game_background, mapPick_size)
volcano_game_background = pygame.transform.scale(volcano_game_background, background_size2)

#desert game background
desert_game_background = pygame.image.load("PicturesUsed/desert_game_background.jpg")
desert_mapPick = pygame.transform.scale(desert_game_background, mapPick_size)
desert_game_background = pygame.transform.scale(desert_game_background, background_size)

#grassy game background
grassy_game_background = pygame.image.load("PicturesUsed/grassy_game_background.jpg")
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
TimeFont = pygame.font.SysFont("Arial", 20)
pausedFont = pygame.font.SysFont("Arial", 36)
UnpauseTxt= pausedFont.render("Press SPACE BAR to resume the game.", True, textColor)
BackToMainTxt = pausedFont.render("Press SHIFT to go back to the main menu.", True, textColor)
Or = pausedFont.render("OR", True, textColor)
EscTxt= pausedFont.render("Press ESC to exit the application.", True, textColor)
mainTxt = pausedFont.render("Press TAB to pause the game.", True, textColor)
MapTxt= pausedFont.render("Select A Map", True, textColor)
DifficultyTxt= pausedFont.render("Select A Difficulty", True, textColor)


#game loop
i = 0
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
            startTime = time.time()
        elif difficulty_img.lobbyScreen(screen):
            menuState = "difficulty"
        elif map_img.lobbyScreen(screen):
            menuState = "map"
        elif exit_img.lobbyScreen(screen):
            run = False

    #in game 
    elif menuState == "game":


        #time calculation for timer in game
        star_count += clock.tick(60)
        elapsedTime = time.time() - startTime
        TimeTxt = TimeFont.render(f"Time: {round(elapsedTime)}s", 1, "black")
        
        screen.blit(background, topLeft)
        screen.blit(TimeTxt, (700, 20))

        #easy difficulty
        if star_count > star_add and difficultyState == "easy":
            for _ in range(3):
                star_x = random.randint(0, screen_width - star_width)
                star = pygame.Rect(star_x, -star_height, star_width, star_height)
                stars.append(star)

            star_add = max(1000, star_add - 50)
            star_count = 0

        #medium difficulty
        if star_count > star_add and difficultyState == "medium":
            for _ in range(5):
                star_x = random.randint(0, screen_width - star_width)
                star = pygame.Rect(star_x, -star_height, star_width, star_height)
                stars.append(star)

            star_add = max(400, star_add - 80)
            star_count = 0

        #hard difficulty
        if star_count > star_add and difficultyState == "hard":
            for _ in range(7):
                star_x = random.randint(0, screen_width - star_width)
                star = pygame.Rect(star_x, -star_height, star_width, star_height)
                stars.append(star)

            star_add = max(100, star_add - 100)
            star_count = 0


        for star in stars:
            pygame.draw.rect(screen, (255,255,255), star)
        

    #in difficulty settings
    elif menuState == "difficulty":
        screen.fill(color)
        screen.blit(DifficultyTxt, (screen_width //2 - 2.45 *DifficultyTxt.get_height() , 350))

        if back_img.lobbyScreen(screen):
            menuState = "main"

    #in pause menu
    elif menuState == "gamePaused":
        screen.fill(color)
        screen.blit(UnpauseTxt, (screen_width //2 - 6 *mainTxt.get_height() , 390))
        screen.blit(EscTxt, (screen_width //2 - 5 *mainTxt.get_height() , 500))
        screen.blit(Or, (screen_width //2 - 0.6 * mainTxt.get_height() , 300))
        screen.blit(BackToMainTxt, (screen_width //2 - 6.3 * BackToMainTxt.get_height() , 445))

        #handle resume button being pressed
        if resume_img.lobbyScreen(screen):
            print("Game Resumed")
            menuState = "game"
            
    #in map settings
    elif menuState == "map":
        screen.fill(color)
        screen.blit(MapTxt, (screen_width //2 - 2.2 *MapTxt.get_height() , 225))

        if back_img.lobbyScreen(screen):
            menuState = "main"
        if winter_game.lobbyScreen(screen):
            print("Successful Map Change")
            player_location = "winter"
            background = winter_game_background
        elif volcano_game.lobbyScreen(screen):
            print("Successful Map Change")
            player_location = "volcano"
            print(player_location)
            background = volcano_game_background
        elif grassy_game.lobbyScreen(screen):
            print("Successful Map Change")
            player_location = "grassy"
            background = grassy_game_background
        elif desert_game.lobbyScreen(screen):
            print("Successful Map Change")
            player_location = "desert"
            background = desert_game_background

    player_start, player_color = draw(player_location)

    while i < 1:
        #create player shape
        player = pygame.Rect(200, player_start, player_width, player_height)
        i+=1
    if menuState == "game":
        pygame.draw.rect(screen, player_color, player)

    #check key pressings and handle accordingly
    for event in pygame.event.get():

        #handle A/D keys pressed to move player accordingly
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_velocity >= 0:
                player.x -= player_velocity
        if keys[pygame.K_d] and player.x + player_velocity + player_width <= screen_width:
                player.x += player_velocity
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
            if event.key  == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                menuState = "main"
                break
        
        #ESC pressed in pause screen so close entire application
        if menuState == "gamePaused" and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

        #quit application
        if event.type == pygame.QUIT:
            run = False

    for star in stars[:]:
        star.y += star_velocity
        if star.y > screen_height:
            stars.remove(star)
        elif star.y + star.height >= player.y and star.colliderect(player):
            stars.remove(star)
            hit = True
            break

    #update screen
    pygame.display.update()

#close window
pygame.quit()


