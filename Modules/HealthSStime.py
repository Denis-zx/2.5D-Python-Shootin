import Modules.settings
settings = Modules.settings
def HandT ():
        for Health in range(settings.Health*2):
            settings.screen.blit(settings.health, (Health+8,8))
        # Suvive Time Display
        clock = settings.font24.render(str(settings.survivetime[0])+":"+str(settings.survivetime[1]), False, (0,0,0))
        settings.screen.blit (clock,(700,50))
