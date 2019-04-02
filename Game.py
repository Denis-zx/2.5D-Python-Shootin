import pygame
pygame.init()
from pygame.locals import *
import Modules.settings
settings = Modules.settings
settings.init()
from Modules.Body import game
from Modules.Body import gameover

def instructionpage():
    Next = 0            # Setting a local variable to control ending the module  
    while not Next:
        settings.screen.fill(0)
        # Display the handle
        settings.screen.blit(settings.controller,[100,150])
        settings.screen.blit(settings.firebutton,[430,250])
        # Firing Key
        keyforfiring = settings.font36.render ("Space",False,(169,169,169))
        firekey = settings.font36.render("Fire Key",False,(169,169,169))
        # Direction/Moving Key
        up = settings.font36.render("UP key",False,(169,169,169))
        down = settings.font36.render("Down key",False,(169,169,169))
        left = settings.font36.render("Left key",False,(169,169,169))
        right = settings.font36.render("Right key",False,(169,169,169))
        # Display instruction
        tocontinue = settings.font36.render ("[Press Space to continue]",False, (255,255,255))
        settings.screen.blit (tocontinue, [330,500])
        loaded = settings.font24.render ("Ready to fire",False, (255,255,255))
        settings.screen.blit (loaded, [150,550])
        # Display elements above on the window
        settings.screen.blit (keyforfiring,[530,255])
        settings.screen.blit (firekey,[530,330])
        settings.screen.blit (up,[170,110])
        settings.screen.blit (down,[150,410])
        settings.screen.blit (left,[30,200])
        settings.screen.blit (right,[270,320])
        settings.screen.blit (settings.loading,[50,500])
        # If Space is pressed, the module will end
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_SPACE:
                    Next = 1
            
        pygame.display.flip()



def mainloop():
    while True:
        settings.screen.fill(0)
        
        Gamestart = settings.font60.render ("Game Start", False, (255,255,255))
        settings.screen.blit (Gamestart, [300,150])

        pressenter = settings.font24.render ("[Press Space]",False, (255,255,255))
        settings.screen.blit (pressenter, [400,240])

        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key==K_SPACE:
         # If Space Key is pressed,display instruction page
                    instructionpage()
         # After intruction page finished diplaying,automatically move to the game
                    game(settings.screen)
         # After the game finished display the ending page
                    gameover()

        pygame.display.flip()






        

mainloop()
