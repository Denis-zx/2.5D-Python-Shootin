import pygame
pygame.init()
import Modules.settings
from Modules.Maps import maps
from Modules.Maps import boundaryverify
from Modules.Enemy import enermy
from Modules.Gunsmodule import gunsystem
from Modules.Gunsmodule import Gundisplay
from Modules.HealthSStime import HandT
from Modules.Enemy import levelgearup
from Modules.Enemy import leveldisplay
settings = Modules.settings

class Player:
    def __init__(self):
        self.image = settings.playerup # Create Player Image
        self.rect = pygame.Rect((250,170),(10,10))
        
    def move(self,camera_pos):
        pos_x,pos_y = camera_pos # Split camara_pos
        key = pygame.key.get_pressed()

        if key[pygame.K_UP]:                    # Checkinng which key has been push
            self.rect.y -= 8                    # Moving character's position
            pos_y += 8                          # Moving camara's coordinate
            self.image = settings.playerup      # Make the character on the screen face the correct direction
            settings.gunpos = 1                 # Setting up the gun direction for later use
        elif key[pygame.K_DOWN]:
            self.rect.y += 8
            pos_y -= 8
            self.image = settings.playerdown
            settings.gunpos = 2
        elif key[pygame.K_LEFT]:
            self.rect.x -= 8
            pos_x += 8
            settings.gunpos = 3
            self.image = settings.playerleft
        elif key[pygame.K_RIGHT]:
            self.rect.x += 8
            pos_x -= 8
            self.image = settings.playerright
            settings.gunpos = 4

        # basic boundary verification
        if self.rect.x < 50: 
            self.rect.x = 50  
            pos_x = camera_pos[0] 
        elif self.rect.x > 1400:
            self.rect.x = 1400
            pos_x = camera_pos[0]
        if self.rect.y < 50:
            self.rect.y = 50
            pos_y = camera_pos[1]
             
        elif self.rect.y > 1300:
            self.rect.y = 1300
            pos_y = camera_pos[1]

        # wall collision checking
        self.rect.x,self.rect.y,pos_x,pos_y = boundaryverify (self.rect.x,self.rect.y,pos_x,camera_pos[0],pos_y,camera_pos[1])

        # activate the gun system
        if key[pygame.K_SPACE]:
            gunsystem()

        #setting the global playerpos for enemy function
        settings.playerpos[0] = self.rect.x
        settings.playerpos[1] = self.rect.y

        #Updating the survived time here
        settings.survivetime[0] = (pygame.time.get_ticks())//60000
        settings.survivetime[1] = (pygame.time.get_ticks())//1000%60
        
        # Return New Camera Pos
        return (pos_x,pos_y) 
        
    def render(self,display):       # Display the player in the game
        display.blit(self.image,(self.rect.x,self.rect.y))



def game(display):
    #initializing some variables
    clock=pygame.time.Clock()
    settings.survivetime = [0,0]
    player = Player()
    camera_pos = settings.camera_pos
    world = settings.world
    while settings.running:
        # Quitting function
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                return

        #Update camera and player's position
        camera_pos=player.move(camera_pos)
        settings.screen.fill(255)
        world.fill((255,255,255))
        maps()              # Drawing maps on the windows
        enermy()            # Updating zombies' position
        levelgearup()       # Increasing the difficulties
        leveldisplay()      # Display the level when difficulies increase
        player.render(world)# Calling the module to display the player
        display.blit(world,camera_pos)
        HandT()             # Display health bar and survived time
        Gundisplay()        # Display loading icon
        clock.tick(60)      # Set up the time for each frame
        pygame.display.flip() # Once the health value drop to 0
        if settings.Health <= 0: # The game stop
            settings.running = 0


def gameover():
    while True:
        settings.screen.fill(0)
        GameEnd = settings.font36.render ("Game End",False, (255,255,255))
        settings.screen.blit (GameEnd, (230,250))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                return


        


