import pygame
def init():
    global world,screen,camera_pos,playerpos,enermypos
    global HealthValue,Health,Survivetime,running,exitcode
    global enermyfreeze,floor, level,enermyspeed, levelup,enermybase,enermyup, enermydown,enermyleft,enermyright,Newenermytime,enermytime,enermylimit,gate
    global gunfire1,gunfire2,gunfire3,gunfire4,gunfires,gun, loading,Reload,Cooldown,gunpos,point
    global Menu,Next,font24,font36,font60, width, height
    global horiwall, vertiwall,playerup,playerdown,playerleft,playerright,enermy,healthbar, health, controller, firebutton

    font24 = pygame.font.SysFont('Comic Sans MS', 24) # set the size to 24 (Normal)
    font36 = pygame.font.SysFont('Comic Sans MS', 36) # set the size to 36 (Subtitle)
    font60 = pygame.font.SysFont('Comic Sans MS', 60) # set the size to 60 (title)

    width, height = 800,600 # define screen size
    screen=pygame.display.set_mode((width, height)) # initialize a window
    playerpos=[512,384] # original place (middle of the screen)
    enermypos = []  # it is an array storing all the enermy postition (X,Y)
    space = 10  # put spacing between enermy so they wouldn't squash togeter
    camera_pos = (100,100)
    world = pygame.Surface((1600,1400))

    
    Newenermytime = 20     # Time before the next enermy appear
    enermytime = 0         # set a timer for refreshing enermy, when enermytime count down to 0, a new enermy refresh.
                           # At the start, it will auto refresh 1 enermy in the beginning
    enermylimit = 1        # set the amount of maximum number of enermy
    gate = 0               # there are four for enermy refreshing, thus 
    level = 0
    levelup = 0
    enermyspeed = 5
    enermyfreeze = 10
    
    Reload = 5              # Time for gun to cooldown and reload the bullet, that is, the character can't fire constantly
    gun = False             # Whether the fire key is pressed 
    Cooldown = 0
    gunpos = 0
    point = 0
    gunfires = [[0,0,0,3]]
    
    
    HealthValue = 100
    Health = HealthValue
    survivetime = [0,0]
    running = 1
    exitcode = 0

    Menu = 0
    Next = 0


    # 3 - Load images
    floor = pygame.image.load("resources/images/floor.jpg")
    horiwall = pygame.image.load("resources/images/wall.png")
    vertiwall = pygame.transform.rotate(horiwall,90)
    playerup = pygame.image.load ("resources/images/PlayerUP.png")
    playerdown = pygame.transform.rotate(playerup,180)
    playerleft = pygame.transform.rotate(playerup,90)
    playerright = pygame.transform.rotate(playerup,-90)
    enermybase = pygame.image.load("resources/images/enermybase.png")
    enermydown  = pygame.image.load ("resources/images/Zombi.png")
    enermyup = pygame.transform.rotate(enermydown,180)
    enermyleft = pygame.transform.rotate(enermydown,-90)
    enermyright = pygame.transform.rotate(enermydown,90)
    gun = pygame.image.load("resources/images/Gun.png")
    loading = pygame.image.load("resources/images/loading.png")
    health = pygame.image.load ("resources/images/health.png")
    controller = pygame.image.load ("resources/images/Controller.png")
    firebutton = pygame.image.load ("resources/images/Space.png")
