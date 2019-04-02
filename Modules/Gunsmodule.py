import Modules.settings
settings =Modules.settings

def gunsystem():
        if settings.Cooldown == 0:
            for i in range (len(settings.enermypos)):
                if settings.gunpos == 1: #up
                    if  settings.playerpos[0]-200<settings.enermypos[i][0]<settings.playerpos[0]+200 and  settings.playerpos[1]-200<settings.enermypos[i][1]<settings.playerpos[1]:
                        settings.enermypos.pop(i) 
                        settings.point += 1
                        break
                elif settings.gunpos == 2: #down
                    if  (settings.playerpos[0]-200<settings.enermypos[i][0]<settings.playerpos[0]+200 and  settings.playerpos[1]<settings.enermypos[i][1]<settings.playerpos[1]+400):
                        settings.enermypos.pop(i)        
                        settings.point += 1
                        break
                elif settings.gunpos == 3: #left
                    if  settings.playerpos[0]-200<settings.enermypos[i][0]<settings.playerpos[0] and  settings.playerpos[1]-200<settings.enermypos[i][1]<settings.playerpos[1]+200:
                        settings.enermypos.pop(i)
                        settings.point += 1
                        break
                elif settings.gunpos == 4: #right
                    if  settings.playerpos[0]<settings.enermypos[i][0]<settings.playerpos[0]+400 and  settings.playerpos[1]-200<settings.enermypos[i][1]<settings.playerpos[1]+200:
                        settings.enermypos.pop(i)
                        settings.point +=1
                        break
            settings.Cooldown = settings.Reload

def Gundisplay():
        if settings.Cooldown == 0:
            settings.screen.blit(settings.gun,(50,450))
        else:
            settings.Cooldown -= 1


