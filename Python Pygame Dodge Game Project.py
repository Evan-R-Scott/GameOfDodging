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
player_velocityX = 10
player_location = "grassy"
player_start = 490
player_color = (255,0,0)
x = 200

#initializing projectiles variables
star_add = 2000
star_count = 0
stars = []
star_width = 10
star_height = 20
star_velocity = 3
hit = False

#initializing jumping variables
isJumping = False
player_velocityY = 10

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
        player_color = (255,0,0)
    elif player_location == "volcano":
        player_color = (0,0,255)
    elif player_location == "winter":
        player_color = (255,255,0)
    elif player_location == "desert": 
        player_color = (0,255,0)
    return player_color

    
#menu background
menu_background = pygame.image.load("PicturesUsed/menu_background.jpg")
menu_background = pygame.transform.scale(menu_background,background_size)

#load button images
start_button = pygame.image.load("PicturesUsed/startButton.png")
difficulty_button = pygame.image.load("PicturesUsed/difficultyButton.png")
map_button = pygame.image.load("PicturesUsed/mapButton.png")
back_button = pygame.image.load("PicturesUsed/backButton.png")
exit_button = pygame.image.load("PicturesUsed/exitButton.png")
resume_button = pygame.image.load("PicturesUsed/resumeButton.png")
easy_button = pygame.image.load("PicturesUsed/EasyButton.png")
medium_button = pygame.image.load("PicturesUsed/MediumButton.png")
hard_button = pygame.image.load("PicturesUsed/HardButton.png")

#call buttons into button class
start_img = LobbyScreenCode.Button(330, 30, start_button, 2)
difficulty_img = LobbyScreenCode.Button(300, 130, difficulty_button, 2)
map_img = LobbyScreenCode.Button(330, 230, map_button, 2)
back_img = LobbyScreenCode.Button(330, 500, back_button, 2)
exit_img = LobbyScreenCode.Button(330,330, exit_button, 2)
resume_img = LobbyScreenCode.Button(310,90, resume_button, 2.5)
easy_img = LobbyScreenCode.Button(130,150, easy_button, 2)
medium_img = LobbyScreenCode.Button(330,150, medium_button, 2)
hard_img = LobbyScreenCode.Button(530,150, hard_button, 2)

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
Font = pygame.font.SysFont("Arial", 36)
UnpauseTxt= Font.render("Press SPACE BAR to resume the game.", True, textColor)
BackToMainTxt = Font.render("Press SHIFT to go back to the main menu.", True, textColor)
Or = Font.render("OR", True, textColor)
EscTxt= Font.render("Press ESC to exit the application.", True, textColor)
mainTxt = Font.render("Press TAB to pause the game.", True, textColor)
MapTxt= Font.render("Select A Map", True, textColor)
DifficultyTxt= Font.render("Select A Difficulty", True, textColor)
LostText = Font.render("You Lost!", True, textColor)

#game loop
i = 0
run = True
restart = False
while run:
    #in lobby screen 
    if menuState == "main":
        screen.blit(menu_background,topLeft)
        screen.blit(mainTxt, (screen_width //2 - 4.5 *mainTxt.get_height() , 500))

        #resolves freezing issue caused by instantly starting new game after just losing
        if restart:
             pygame.time.delay(2000)
             restart = False

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
            for _ in range(random.randint(2,4)):
                star_x = random.randint(0, screen_width - star_width)
                star = pygame.Rect(star_x, -star_height, star_width, star_height)
                stars.append(star)

            star_add = max(800, star_add - 50)
            star_count = 0

        #medium difficulty
        if star_count > star_add and difficultyState == "medium":
            for _ in range(random.randint(3,6)):
                star_x = random.randint(0, screen_width - star_width)
                star = pygame.Rect(star_x, -star_height, star_width, star_height)
                stars.append(star)

            star_add = max(500, star_add - 60)
            star_count = 0

        #hard difficulty
        if star_count > star_add and difficultyState == "hard":
            for _ in range(random.randint(4,7)):
                star_x = random.randint(0, screen_width - star_width)
                star = pygame.Rect(star_x, -star_height, star_width, star_height)
                stars.append(star)

            star_add = max(400, star_add - 70)
            star_count = 0

        #draw projectiles on screen
        for star in stars:
            pygame.draw.rect(screen, (255,255,255), star)

        #player was hit by projectile and lost
        if hit:
            screen.blit(LostText, (screen_width//2 - 0.4 * LostText.get_width(), 200))
            pygame.display.update()
            pygame.time.delay(2000)
            hit = False
            restart = True
            menuState = "main"

    #in difficulty settings
    elif menuState == "difficulty":
        screen.fill(color)
        screen.blit(DifficultyTxt, (screen_width //2 - 2.45 *DifficultyTxt.get_height() , 350))

        if easy_img.lobbyScreen(screen):
            difficultyState = "easy"
            print("Difficulty set to: Easy")
        elif medium_img.lobbyScreen(screen):
            difficultyState = "medium"
            print("Difficulty set to: Medium")
        elif hard_img.lobbyScreen(screen):
            difficultyState = "hard"
            print("Difficulty set to: Hard")

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
            print("Successful map change to: Winterwonderland")
            player_location = "winter"
            background = winter_game_background
        elif volcano_game.lobbyScreen(screen):
            print("Successful map change: Volcanic Hell")
            player_location = "volcano"
            background = volcano_game_background
        elif grassy_game.lobbyScreen(screen):
            print("Successful map change: Grasslands")
            player_location = "grassy"
            background = grassy_game_background
        elif desert_game.lobbyScreen(screen):
            print("Successful map change: Desert Oasis")
            player_location = "desert"
            background = desert_game_background

    player_color = draw(player_location)

    #draw initial player rectangle at start of game
    while i < 1:
        #create player shape
        player =  pygame.Rect(x, player_start, player_width, player_height)
        i+=1
        
    if menuState == "game":
        pygame.draw.rect(screen, player_color, player)

    #check key pressings and handle accordingly
    for event in pygame.event.get():

        #handle A/D keys pressed to move player accordingly
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - player_velocityX >= 0:
                player.x -= player_velocityX
        if keys[pygame.K_d] and x + player_velocityX + player_width <= screen_width:
                player.x += player_velocityX
        #tab pressed so pause current game
        if event.type == pygame.KEYDOWN and menuState == "game":
            if event.key == pygame.K_TAB:
                menuState = "gamePaused"
                break
            if event.key == pygame.K_SPACE and not isJumping:
                isJumping = True

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

    if isJumping is True:
        player.y -= player_velocityY
        player_velocityY -= 1
        if player_velocityY < -10:
            isJumping = False
            player_velocityY = 10

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


