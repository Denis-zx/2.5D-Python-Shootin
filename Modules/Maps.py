import Modules.settings
settings =Modules.settings

# 5.2 - draw boundary
def maps():
    for x in range(0,2):
        for y in range (0,2):
            settings.world.blit(settings.floor,(x*800,y*750))
    
    for x in range (0,31):
        for y in range (0,1):
            settings.world.blit(settings.horiwall,(x*50,y*50))
    for x in range (0,31):
        for y in range (27,28):
            settings.world.blit(settings.horiwall,(x*50,y*50))

    for x in range (0,2):
        for y in range (5,6):
            settings.world.blit(settings.horiwall,(x*50,y*50)) # wall 1
    for x in range (4,5):
        for y in range (5,20):
            settings.world.blit(settings.vertiwall,(x*50,y*50)) # wall 2
    for x in range (0,2):
        for y in range (23,24):
            settings.world.blit(settings.horiwall,(x*50,y*50)) # wall 3
                
    for x in range (27,30):
        for y in range (5,6):
            settings.world.blit (settings.horiwall,(x*50,y*50))
    for x in range (27,28):
        for y in range (5,20):
            settings.world.blit (settings.vertiwall,(x*50,y*50))
    for x in range (27,31):
        for y in range (23,24):
            settings.world.blit (settings.horiwall,(x*50,y*50))


    settings.world.blit(settings.enermybase,(80,70)) 
    settings.world.blit(settings.enermybase,(1400,70))
    settings.world.blit(settings.enermybase,(80,1200))
    settings.world.blit(settings.enermybase,(1400,1200))

def boundaryverify(x,y,pos_x,camera_posx,pos_y,camera_posy):
    if x<250 and 150<y<1200:
        return (250,y,150,pos_y)
    if x>1200 and 150<y<1200:
        return (1200,y,-900,pos_y)
    else:
        return (x,y,pos_x,pos_y)
    
    
