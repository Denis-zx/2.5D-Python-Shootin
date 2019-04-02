import Modules.settings
import random
from Modules.Maps import boundaryverify
settings = Modules.settings


def enermy():
        if len(settings.enermypos) <= settings.enermylimit:
            if settings.enermytime >= settings.Newenermytime:
                gate = random.randint(1,4)
                if gate == 1:
                    settings.enermypos.append([100,100,0])
                elif gate == 2:
                    settings.enermypos.append([1350,100,0])
                elif gate == 3:
                    settings.enermypos.append([100,1200,0])
                elif gate == 4:
                    settings.enermypos.append([1350,1200,0])
                settings.enermytime = 0
            else:
                settings.enermytime += 1
        
        enermyspeed = settings.enermyspeed
        for i in range (len(settings.enermypos)):
            x = settings.enermypos[i][0]
            y = settings.enermypos[i][1]
            if abs(x-settings.playerpos[0])<20 or abs (y-settings.playerpos[1])<20:
                    if abs (y-settings.playerpos[1])<5:
                            if (settings.playerpos[0] - x >10):
                                settings.enermypos[i][0],settings.enermypos[i][1],a,b = boundaryverify(x+enermyspeed,y,0,0,0,0)
                                settings.world.blit(settings.enermyright,(settings.enermypos[i][0],settings.enermypos[i][1]))
                            elif (settings.playerpos[0] - x < -10):
                                settings.enermypos[i][0],settings.enermypos[i][1],a,b = boundaryverify(x-enermyspeed,y,0,0,0,0)
                                settings.world.blit(settings.enermyleft,(settings.enermypos[i][0],settings.enermypos[i][1]))
                    else:
                            if (settings.playerpos[1] - y >5):
                                settings.enermypos[i][0],settings.enermypos[i][1],a,b = boundaryverify(x,y+enermyspeed,0,0,0,0)
                                settings.world.blit(settings.enermydown,(settings.enermypos[i][0],settings.enermypos[i][1]))
                            elif (settings.playerpos[1] - y < -5):
                                settings.enermypos[i][0],settings.enermypos[i][1],a,b = boundaryverify(x,y-enermyspeed,0,0,0,0)
                                settings.world.blit(settings.enermyup,(settings.enermypos[i][0],settings.enermypos[i][1]))
            else:
                    xyselection = random.randint(1,2)
                    if xyselection == 1:
                            if (settings.playerpos[0] - x >10):
                                settings.enermypos[i][0],settings.enermypos[i][1],a,b = boundaryverify(x+5,y,0,0,0,0)
                                settings.world.blit(settings.enermyright,(settings.enermypos[i][0],settings.enermypos[i][1]))
                            elif (settings.playerpos[0] - x < -10):
                                settings.enermypos[i][0],settings.enermypos[i][1],a,b = boundaryverify(x-5,y,0,0,0,0)
                                settings.world.blit(settings.enermyleft,(settings.enermypos[i][0],settings.enermypos[i][1]))
                    else:
                            if (settings.playerpos[1] - y >10):
                                settings.enermypos[i][0],settings.enermypos[i][1],a,b = boundaryverify(x,y+5,0,0,0,0)
                                settings.world.blit(settings.enermydown,(settings.enermypos[i][0],settings.enermypos[i][1]))
                            elif (settings.playerpos[1] - y < -10):
                                settings.enermypos[i][0],settings.enermypos[i][1],a,b = boundaryverify(x,y-5,0,0,0,0)
                                settings.world.blit(settings.enermyup,(settings.enermypos[i][0],settings.enermypos[i][1]))
            if settings.enermypos[i][2] == 0:
                    if settings.enermypos[i][0]-50<settings.playerpos[0]<settings.enermypos[i][0]+50 and settings.enermypos[i][1]-50<settings.playerpos[1]<settings.enermypos[i][1]+50:
                            settings.Health -= 20
                            settings.enermypos[i][2] = settings.enermyfreeze
            else:
                    settings.enermypos[i][2]-=1

def levelgearup ():
        if settings.survivetime[1] == 20 or settings.survivetime[1] == 40 or settings.survivetime[1] == 0:
            if settings.levelup == 0:
                settings.level += 1    
                settings.enermylimit = 2**(settings.level)
                settings.Newenermytime = 20-settings.level
                settings.enermyspeed += 0.2
                settings.levelup = 1
        if settings.survivetime[1] == 21 or settings.survivetime[1] == 41 or settings.survivetime[1] == 1:
                settings.levelup = 0
        

def leveldisplay ():
        if settings.survivetime[1] == 21 or settings.survivetime[1] == 41 or settings.survivetime[1] == 1 or settings.survivetime[1] == 22 or settings.survivetime[1] == 42 or settings.survivetime[1] == 2:
            level = settings.font36.render("Level" + str(settings.level), False, (255,255,255))
            settings.world.blit(level,(settings.playerpos[0]-200,settings.playerpos[1]-150))    


