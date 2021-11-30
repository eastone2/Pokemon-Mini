from graphics import *
from AI import*
from BFS import*
import random, copy

###################################################################
#  Special Thanks to Callum Bagnall who gave me the png files     #
#  https://www.youtube.com/watch?v=G3VwuCR2C7g                    #
#  All code is original                                           #
###################################################################

#Variables
def appStarted(app): #Images and Variables
    #Images
    app.up0=app.loadImage('images' + os.sep + 'm_still_-1_0.png').convert()
    app.up=ImageTk.PhotoImage(app.up0)
    app.down0=app.loadImage('images' + os.sep + 'm_still_1_0.png').convert()
    app.down=ImageTk.PhotoImage(app.down0)
    app.left0=app.loadImage('images' + os.sep + 'm_still_0_-1.png').convert()
    app.left=ImageTk.PhotoImage(app.left0)
    app.right0=app.loadImage('images' + os.sep + 'm_still_0_1.png').convert()
    app.right=ImageTk.PhotoImage(app.right0)                                            #player

    app.tree0=app.loadImage('images' + os.sep + 'tree.png').convert()
    app.tree=ImageTk.PhotoImage(app.tree0)                                              #tree
    app.center=app.loadImage('images' + os.sep + 'center.png').convert()                #center
    app.gym=app.loadImage('images' + os.sep + 'gym.png').convert()                      #gym
    app.sign=app.loadImage('images' + os.sep + 'sign.png').convert()                    #sign
    app.road10=app.loadImage('images' + os.sep + 'road1.png').convert()                 #top road
    app.road1=ImageTk.PhotoImage(app.road10)
    app.road20=app.loadImage('images' + os.sep + 'road2.png').convert()                 #bottom road
    app.road2=ImageTk.PhotoImage(app.road20)
    app.road3=app.loadImage('images' + os.sep + 'road3.png').convert()
    app.road4=app.loadImage('images' + os.sep + 'road4.png').convert()                  #edge roads
    app.grass0=app.loadImage('images' + os.sep + 'grass.png').convert()
    app.grass=ImageTk.PhotoImage(app.grass0)                                            #grass
    app.tgrass0=app.loadImage('images' + os.sep + 'tallgrass.png').convert()
    app.tgrass=ImageTk.PhotoImage(app.tgrass0)                                          #tallgrass
    app.flower0=app.loadImage('images' + os.sep + 'flower.png').convert()
    app.flower=ImageTk.PhotoImage(app.flower0)                                          #flower
    app.floor=app.loadImage('images' + os.sep + 'floor.png').convert()                  #center floor
    app.desk=app.loadImage('images' + os.sep + 'desk.png').convert()                    #desk
    app.pc=app.loadImage('images' + os.sep + 'pc.png').convert()                        #pc
    app.plant=app.loadImage('images' + os.sep + 'plant.png').convert()                  #plant
    app.carpet=app.loadImage('images' + os.sep + 'carpet.png').convert()                #carpet
    app.ware0=app.loadImage('images' + os.sep + 'warehouse.png').convert()
    app.ware=ImageTk.PhotoImage(app.ware0)                                              #warehouse
    app.poke0=app.loadImage('images' + os.sep + 'pokeball.png').convert()
    app.poke=ImageTk.PhotoImage(app.poke0)                                              #pokeball                                                        
    app.rock0=app.loadImage('images' + os.sep + 'rock.png').convert()
    app.rock=ImageTk.PhotoImage(app.rock0)                                              #rock
    app.block=app.loadImage('images' + os.sep + 'block.png').convert()                  #block
    app.girl=app.loadImage('images' + os.sep + 'girl.png').convert()                    #girl
    app.mud=app.loadImage('images' + os.sep + 'mudgrass.png').convert()                 #mudgrass
    app.gymFloor0=app.loadImage('images' + os.sep + 'gym_floor.png').convert()
    app.gymFloor=ImageTk.PhotoImage(app.gymFloor0)                                      #floor
    app.brightFloor0=app.loadImage('images' + os.sep + 'bright_floor.png').convert()
    app.brightFloor=ImageTk.PhotoImage(app.brightFloor0)                                #bright floor
    app.x=app.loadImage('images' + os.sep + 'x.png').convert()                          #dead
    app.Charmander=app.loadImage('images' + os.sep + '020.png').convert()               #charmander
    app.bigCharmander=app.scaleImage(app.Charmander,4)
    app.Charmanderb=app.loadImage('images' + os.sep + '020b.png').convert()
    app.bigCharmanderb=app.scaleImage(app.Charmanderb,4)
    app.Bulbasaur=app.loadImage('images' + os.sep + '026.png').convert()                #bulbasaur
    app.bigBulbasaur=app.scaleImage(app.Bulbasaur,4)
    app.Bulbasaurb=app.loadImage('images' + os.sep + '026b.png').convert()
    app.bigBulbasaurb=app.scaleImage(app.Bulbasaurb,4)
    app.Mudkip=app.loadImage('images' + os.sep + '023.png').convert()                   #mudkip
    app.bigMudkip=app.scaleImage(app.Mudkip,4)
    app.Mudkipb=app.loadImage('images' + os.sep + '023b.png').convert()
    app.bigMudkipb=app.scaleImage(app.Mudkipb,4)
    app.Bidoof=app.loadImage('images' + os.sep + '048.png').convert()                   #Bidoof
    app.bigBidoof=app.scaleImage(app.Bidoof,4)
    app.Bidoofb=app.loadImage('images' + os.sep + '048b.png').convert()
    app.Mike=app.loadImage('images' + os.sep + 'Mike.png').convert()                    #Mike
    app.wall0=app.loadImage('images' + os.sep + 'wall.png').convert()
    app.wall=ImageTk.PhotoImage(app.wall0)                                              #Wall
    app.bigPoke0=app.scaleImage(app.poke0,6)
    app.bigPoke=ImageTk.PhotoImage(app.bigPoke0)                                        #bigPokeball
    app.smallPoke0=app.scaleImage(app.poke0,0.8)
    app.smallPoke=ImageTk.PhotoImage(app.smallPoke0)                                    #smallPokeball
    app.lamp0=app.loadImage('images' + os.sep + 'lamp.png').convert()                    
    app.lamp=app.scaleImage(app.lamp0,0.5)                                              #lamp
    app.barrel0=app.loadImage('images' + os.sep + 'barrel.png').convert()
    app.barrel=ImageTk.PhotoImage(app.barrel0)                                          #barrel
 
    #Varibles
    app.cx=0
    app.cy=0
    app.m=16
    app.timer=0                                                                 #timer
    app.player=app.down
    app.dir='down'                                                              #direction
    app.move=True                                                               #can move
    app.moving=False                                                            #moving

    app.rx,app.ry=random.randint(0,22),random.randint(0,2)                      
    app.a,app.b=96+app.rx*64,480+app.ry*64                                      #random location
    app.random=True                                                             #running random  

    app.mikeX=128                                                               #Mike location
    app.battleX=-1392                                                           #Batte animation
    app.battleY=0
    app.endY=0                                                                  #End scroll

    app.inCenter=False                                                          #inCenter
    app.inGym=False                                                             #inGym
    app.battle=False                                                            #startBattle
    app.inBattle=False                                                          #inBattle
    app.openPc=False                                                            #openPc
    app.endGame=False                                                           #end game
    app.lights=False                                                            #gym vision
    app.showPath=False                                                          #show path in gym
    app.path=getPath(map,board)                                                 #path
    app.ghost=False                                                             #ghost mode

    app.cantRun=False                                                           #cant run message
    app.cantCycle=False                                                         #cant cycle

    app.turn=True                                                               #player's turn
    app.mikeAlive=True                                                          #Mike alive
    app.battleTimer=0                                                           #battle timer
    app.currMove=0                                                              #current move
    app.opponent=False                                                          #opponents turn
    app.endTimer=0
    app.queue=False                                                             #end timer
    app.fainted=False
    app.faintedTimer=0                                                          #fainted message
    app.loadMessage=False
    app.saveMessage=False
    app.messageTimer=0
    
    #'Mudkip': Mudkip,'Charmander': Charmander,'Bulbasaur': Bulbasaur
    app.bag={}                                                                  #bag
    app.MikeBag={'Bidoof': [100,['Scratch','Defend'],'Normal',1]}               #Mike bag


    #Saved state
    app.cx1=0
    app.cy1=0
    app.m1=16
    app.timer1=0                                                                 #timer
    app.player1=app.down
    app.dir1='down'                                                              #direction
    app.move1=True                                                               #can move
    app.moving1=False                                                            #moving
    app.rx1,app.ry1=random.randint(0,22),random.randint(0,2)                      
    app.a1,app.b1=96+app.rx*64,480+app.ry*64                                      #random location
    app.random1=True                                                             #running random  
    app.mikeX1=128                                                               #Mike location
    app.battleX1=-1392                                                           #Batte animation
    app.battleY1=0
    app.endY1=0                                                                  #End scroll
    app.inCenter1=False                                                          #inCenter
    app.inGym1=False                                                             #inGym
    app.battle1=False                                                            #startBattle
    app.inBattle1=False                                                          #inBattle
    app.openPc1=False                                                            #openPc
    app.endGame1=False                                                           #end game
    app.lights1=False                                                            #gym vision
    app.showPath1=False                                                          #show path in gym
    app.path1=getPath(map,board)                                                 #path
    app.ghost1=False                                                             #ghost mode
    app.cantRun1=False                                                           #cant run message
    app.cantCycle1=False                                                         #cant cycle
    app.turn1=True                                                               #player's turn
    app.mikeAlive1=True                                                          #Mike alive
    app.battleTimer1=0                                                           #battle timer
    app.currMove1=0                                                              #current move
    app.opponent1=False                                                          #opponents turn
    app.endTimer1=0
    app.queue1=False                                                             #end timer
    app.fainted1=False
    app.faintedTimer1=0                                                          #fainted message
    app.bag1={}                                                                  #bag
    app.MikeBag1={'Bidoof': [100,['Scratch','Defend'],'Normal',1]}               #Mike bag


#Input
def keyPressed(app,event): #Keybinds
    if app.endGame==False:
        if event.key=='[':                                        #save game
            saveGame(app)
            app.saveMessage=True
        elif event.key==']':                                      #load game
            loadGame(app)
            app.loadMessage=True
        if app.inBattle==False:
            if app.inCenter==False and app.inGym==False:          #Moving Outside
                if event.key == 'w' and app.move==True:
                    app.moving=True
                    app.dir='up'
                    if checkBound(app.cx,app.cy-app.m):
                        app.cy -= app.m
                elif event.key=='s' and app.move==True:
                    app.moving=True
                    app.dir='down'
                    if checkBound(app.cx,app.cy+app.m):
                        app.cy += app.m
                elif event.key=='a' and app.move==True:
                    app.moving=True
                    app.dir='left'
                    if checkBound(app.cx-app.m,app.cy):
                        app.cx -= app.m
                elif event.key=='d' and app.move==True:
                    app.moving=True
                    app.dir='right'
                    if checkBound(app.cx+app.m,app.cy):
                        app.cx += app.m
            elif app.inCenter==True:                              #Moving in Center
                if event.key == 'w' and app.move==True:
                    app.moving=True
                    app.dir='up'
                    if checkCenter(app.cx,app.cy-app.m):
                        app.cy -= app.m
                elif event.key=='s' and app.move==True:
                    app.moving=True
                    app.dir='down'
                    if app.cy>=160 and app.cx in [-16,0,16]:
                        app.inCenter=False
                        app.cx,app.cy=-288,-32
                        app.dir='down'
                    if checkCenter(app.cx,app.cy+app.m):
                        app.cy += app.m
                elif event.key=='a' and app.move==True:
                    app.moving=True
                    app.dir='left'
                    if checkCenter(app.cx-app.m,app.cy):
                        app.cx -= app.m
                elif event.key=='d' and app.move==True:
                    app.moving=True
                    app.dir='right'
                    if checkCenter(app.cx+app.m,app.cy):
                        app.cx += app.m
            elif app.inGym == True:                               #Moving in Gym
                if event.key == 'w' and app.move==True:
                    app.moving=True
                    app.dir='up'
                    if gymBound(app,app.cx,app.cy-app.m):
                        app.cy -= app.m
                elif event.key=='s' and app.move==True:
                    app.moving=True
                    app.dir='down'
                    if gymBound(app,app.cx,app.cy+app.m):
                        app.cy += app.m
                elif event.key=='a' and app.move==True:
                    app.moving=True
                    app.dir='left'
                    if gymBound(app,app.cx-app.m,app.cy):
                        app.cx -= app.m
                elif event.key=='d' and app.move==True:
                    app.moving=True
                    app.dir='right'
                    if gymBound(app,app.cx+app.m,app.cy):
                        app.cx += app.m
                elif event.key=='u':
                    app.ghost=not(app.ghost)
            if event.key == 'f':                                                        #Interact
                if app.inCenter==False and app.cx in [-304,-288,-272] and app.cy==-32 and app.dir=='up':                    #Go in Center
                    app.inCenter=True
                    app.cx,app.cy=0,0
                elif app.inCenter==True and app.cx==160 and app.cy==-400 and app.dir=='up':                                 #Open Pc
                    app.openPc=True
                    app.move=False
                elif app.inCenter==True and app.cx==0 and app.cy==-400 and app.dir=='up':                                   #Heal pokemon
                    if allHealed(app)==False:
                        for poke in app.bag:
                            app.bag[poke][0]=100
                            app.bag[poke][3]=1
                elif app.inCenter==False and app.cy==-192 and app.cx==992 and app.dir=='up' and 'Bulbasaur' not in app.bag: #Catch bulbasaur
                    app.bag['Bulbasaur'] = [75,['Vine Whip','Body Slam','Heal'],'Grass',1]
                elif app.inCenter==False and app.cy==-192 and app.cx==928 and app.dir=='up' and 'Charmander' not in app.bag:#Catch Charmander
                    app.bag['Charmander'] = [75,['Ember','Body Slam','Explode'],'Fire',1]
                elif app.inCenter==False and onPlayer(app.a-app.cx,app.b-app.cy) and 'Mudkip' not in app.bag:               #Catch Mudkip
                    app.bag['Mudkip'] = [75,['Water Gun','Body Slam','Aqua Tail'],'Water',1]
                    app.random=False
                elif app.inCenter==False and app.cx in [48,64,80] and app.cy==-32 and app.dir=='up':                        #Go in gym
                    if len(app.bag) == 0 or isZero(app,1):
                        app.cx=64
                        app.cy=-32
                        app.dir='down'
                    else:
                        updatePoke(app)
                        app.inGym=True
                        app.cx=0
                        app.cy=0
                        app.dir='up'
                        app.fainted=False
                elif app.inGym==True and app.cx in [-16,0,16] and app.cy in [-1232,-1216,-1200,-1184,]:                      #Finish game
                    app.endGame=True
                elif app.inGym==True and app.cx==208 and app.cy in [-144,-128,-112,-96] and app.dir=='right':
                    app.lights=not(app.lights)
            elif event.key=='m' and app.inGym==True and app.cx<=-368 and app.cy>=-16:
                app.showPath=True                                                                                           #show path in gym
            elif event.key == 'g' and app.openPc==True:                                                                      #Close Pc
                app.openPc=False
                app.move=True
            elif event.key == 'Space' and app.move==False and app.inCenter==False and app.inGym==False:                      #Leave Conversation
                app.move=True
                app.cx+=32
                app.dir='right'
        else:                                                                                                                #battle binds
            if app.turn:
                if event.key == '1':
                    app.cantRun=False
                    app.cantCycle=False
                    app.turn=False
                    app.opponent=True
                    app.currMove=1
                    if app.mikeAlive:
                        battleMove(app,1)                                       #does move 1
                elif event.key == '2':
                    app.cantRun=False
                    app.cantCycle=False
                    app.turn=False
                    app.opponent=True
                    app.currMove=2
                    if app.mikeAlive:
                        battleMove(app,2)                                       #does move 2
                elif event.key == '3':
                    app.cantRun=False
                    app.cantCycle=False
                    app.turn=False
                    app.opponent=True
                    app.currMove=3
                    if app.mikeAlive:
                        battleMove(app,3)                                       #does move 3
                elif event.key == '4':
                    app.cantCycle=False
                    app.cantRun=True                                            #cant run
                elif event.key == '5':                                          #cycles poke
                    app.cantRun=False
                    cyclePoke(app)
    else:
        if app.endY>448:
            appStarted(app)                                                     #start over game

def keyReleased(app,event): #Checks if running
    if event.key == 'w':
        app.moving=False
    elif event.key == 's':
        app.moving=False
    elif event.key == 'a':
        app.moving=False
    elif event.key == 'd':
        app.moving=False


#Timer functions
def timerFired(app): #Timer
    changeDir(app)                                                              #change direction
    if app.saveMessage==True or app.loadMessage==True:
        app.messageTimer+=1
        if app.messageTimer>=10:
            app.saveMessage=False
            app.loadMessage=False
            app.messageTimer=0
    if app.inGym==False and app.inCenter==False:
        forceMove(app)                                                          #talk with girl
        app.timer+=1
        if app.timer%15==0 and app.random==True:
            app.rx,app.ry=random.randint(0,22),random.randint(0,2)
            app.a,app.b=96+app.rx*64,480+app.ry*64                              #Mudkip spawn
    elif app.inGym==True:
        forceBattle(app)                                                        #force battle
        if app.battle==True:
            if app.battleX<0:
                app.battleX+=48
            else:
                app.inBattle=True
                if app.battleY<=384:
                    app.battleY+=32
                else:
                    app.battle=False                                            #battle animatin
        if app.inBattle:
            if isZero(app,1):
                if app.endTimer<20:
                    app.endTimer+=1
                else:
                    app.endTimer=0
                    lost(app)                                                   #lost battle
            if isZero(app,2):
                if app.endTimer<20:
                    app.endTimer+=1
                else:
                    app.endTimer=0
                    app.inBattle=False
                    app.move=True
                    app.cx=-256
                    app.cy=-48
                    app.dir='up'
                    app.battleX=-1392
                    app.battleY=0
                    app.mikeAlive=False                                         #won battle with mike
            if app.bag[app.curr][0]<=0:
                app.fainted=True
                if app.faintedTimer<15:
                    app.faintedTimer+=1
                else:
                    app.fainted=False
                    updatePoke(app)                                             #fainted
            if app.opponent and app.mikeAlive:
                app.battleTimer+=1
                if app.battleTimer==10:
                    app.currMove=battle(app.MikeBag['Bidoof'],app.bag[app.curr],3)
                    if isZero(app,2)==False and app.fainted==False:
                        opponentMove(app,app.currMove)                          #does apponent move
                elif app.battleTimer==25:
                    app.turn=True
                    app.opponent=False
                    app.battleTimer=0                                           #opponent does battle
        if app.endGame and app.endY<=448:
            app.endY+=8                                                         #game end screen

def changeDir(app): #Update player direction
    if app.dir=='up':
        app.player=app.up
    elif app.dir=='down':
        app.player=app.down
    elif app.dir=='left':
        app.player=app.left
    elif app.dir=='right':
        app.player=app.right

def forceMove(app): #Forces Conversation with girl
    if app.cx==-432 and app.cy in [-32,-16,0,16]:
        app.cy=-32
        app.dir='up'
        app.move=False

def forceBattle(app): #Force battles
    if app.cx<=-240 and app.cy>-32 and app.mikeAlive:
        app.move=False
        app.mikeX=192
        app.cx,app.cy=-272,32
        app.dir='left'
        app.battle=True

def updatePoke(app): #Updates current pokemon
    if 'Mudkip' in app.bag and app.bag['Mudkip'][0] > 0:
        app.curr='Mudkip'
    elif 'Charmander' in app.bag and app.bag['Charmander'][0] > 0:
        app.curr='Charmander'
    elif 'Bulbasaur' in app.bag and app.bag['Bulbasaur'][0] > 0:
        app.curr='Bulbasaur'

def cyclePoke(app): #Cycles pokemon
    if app.curr=='Mudkip':
        if 'Charmander' in app.bag and app.bag['Charmander'][0] > 0:
            app.curr='Charmander'
        elif 'Bulbasaur' in app.bag and app.bag['Bulbasaur'][0] > 0:
            app.curr='Bulbasaur'
        else:
            app.cantCycle=True
    elif app.curr=='Charmander':
        if 'Bulbasaur' in app.bag and app.bag['Bulbasaur'][0] > 0:
            app.curr='Bulbasaur'
        elif 'Mudkip' in app.bag and app.bag['Mudkip'][0] > 0:
            app.curr='Mudkip'
        else:
            app.cantCycle=True
    elif app.curr=='Bulbasaur':
        if 'Mudkip' in app.bag and app.bag['Mudkip'][0] > 0:
            app.curr='Mudkip'
        elif 'Charmander' in app.bag and app.bag['Charmander'][0] > 0:
            app.curr='Charmander'
        else:
            app.cantCycle=True


#Collision
def checkBound(x,y): #Checks bounds outside
    if x-16<-448 or y+16<-320 or x+16>1024 or y+32>256:  #board
        return False
    elif x-16<896 and y+16<-16:                           #center and warehouse
        return False
    elif y+16<-176:                                       #pokeballs
        return False
    return True

def gymBound(app,x,y): #Check bounds in gym
    if x-16<-426 or y+16<-1216 or x+16>416 or y+32>64:            #board
        return False
    elif app.ghost:                                                 #ghost mode
        return True
    elif x-16<-160 and x+16>-224 and y+32>-192:                  #Walls
        return False
    elif x-16<352 and x+16>-352 and y+32>-192 and y+16<-128:
        return False
    elif x-16<-288 and x+16>-416 and y+32>-64 and y+16<0:
        return False
    elif x-16<352 and x+16>-96 and y+32>-64 and y+16<0:
        return False
    elif x-16<352 and x+16>288 and y+32>-128 and y+16<-64:
        return False
    elif x-16<416 and x+16>-352 and y+32>-320 and y+16<-256:
        return False
    elif x-16<288 and x+16>224 and y+32>-128 and y+16<-64:           #lamp
        return False                                           
    elif x-16<-160 and y+32>-448 and y+16<-384:                      #barrels
        return False
    elif x-16<-96 and x+16>-352 and y+32>-576 and y+16<-512:
        return False
    elif x-16<-96 and y+32>-704 and y+16<-640:
        return False
    elif x-16<-224 and y+32>-832 and y+16<-768:
        return False
    elif x-16<-32 and x+16>-96 and y+32>-768 and y+16<-448:
        return False
    elif x-16<-32 and x+16>-96 and y+32>-384 and y+16<-320:
        return False
    elif x-16<224 and x+16>160 and y+32>-384 and y+16<-320:
        return False
    elif x-16<96 and x+16>32 and y+32>-448 and y+16<-384:
        return False
    elif x-16<352 and x+16>288 and y+32>-448 and y+16<-384:
        return False
    elif x-16<352 and x+16>-32 and y+32>-512 and y+16<-448:
        return False
    elif x+16>32 and y+32>-640 and y+16<-576:
        return False
    elif x-16<352 and x+16>160 and y+32>-768 and y+16<-704:
        return False
    elif x+16>224 and y+32>-896 and y+16<-832:
        return False
    elif x-16<160 and x+16>-32 and y+32>-896 and y+16<-832:
        return False
    elif x-16<32 and x+16>-32 and y+32>-896 and y+16<-704:
        return False
    elif x-16<160 and x+16>96 and y+32>-896 and y+16<-704:
        return False
    elif x+16>32 and y+32>-1024 and y+16<-960:
        return False
    elif x-16<352 and x+16>-96 and y+32>-1152 and y+16<-1088:
        return False
    elif x-16<96 and x+16>32 and y+32>-1216 and y+16<-1152:
        return False
    elif x-16<-32 and x+16>-96 and y+32>-1088 and y+16<-960:
        return False
    elif x-16<-96 and x+16>-160 and y+32>-1024 and y+16<-832:
        return False
    elif x-16<-288 and x+16>-352 and y+32>-1152 and y+16<-896:
        return False
    elif x-16<-160 and x+16>-224 and y+16<-1088:
        return False
    elif x-16<-160 and x+16>-288 and y+32>-1024 and y+16<-960:
        return False
    return True

def checkCenter(x,y): #Check bounds in center
    if y+32>=208 or y-32<=-448 or x+32>=224 or x-32<=-224:
        return False
    return True


#Draw outside and center
def drawBoard(app,canvas): #Draw outside
    if app.inCenter==False:
        for x in range(32,1024,64):
            for y in range(32,768,64):
                canvas.create_image(x,y,image=app.grass)                                     #grass
        for x in range(32,1570,64):
            if onScreen(x-app.cx,32-app.cy):
                canvas.create_image(x-app.cx,32-app.cy,image=app.tree)                       #top border
            if onScreen(x-app.cx,672-app.cy):
                canvas.create_image(x-app.cx,672-app.cy,image=app.tree)                      #bottom border
        for y in range(96,672,64):
            if onScreen(32-app.cx,y-app.cy):
                canvas.create_image(32-app.cx,y-app.cy,image=app.tree)                       #left border
            if onScreen(1570-app.cx,y-app.cy):
                canvas.create_image(1570-app.cx,y-app.cy,image=app.tree)                     #right border
        if onScreen(1440-app.cx,96-app.cy):
            canvas.create_image(1440-app.cx,96-app.cy,image=app.tree)
            canvas.create_image(1504-app.cx,96-app.cy,image=app.tree)                        #tree
        for x in range(160,2018,64):
            if onScreen(x-app.cx,416-app.cy):
                canvas.create_image(x-app.cx,352-app.cy,image=app.road1) #road
                canvas.create_image(x-app.cx,416-app.cy,image=app.road2)
        if onScreen(96-app.cx,416-app.cy):
            canvas.create_image(96-app.cx,352-app.cy,image=ImageTk.PhotoImage(app.road3))
            canvas.create_image(96-app.cx,416-app.cy,image=ImageTk.PhotoImage(app.road4))    #road edge
        if onScreen2(224-app.cx,352-app.cy):
            canvas.create_image(224-app.cx,192-app.cy,image=ImageTk.PhotoImage(app.center))  #center
        if onScreen2(576-app.cx,192-app.cy):
            canvas.create_image(576-app.cx,192-app.cy,image=ImageTk.PhotoImage(app.gym))     #gym
        if onScreen2(1248-app.cx,176-app.cy):
            canvas.create_image(1248-app.cx,176-app.cy,image=app.ware)
        if onScreen2(928-app.cx,176-app.cy):
            canvas.create_image(928-app.cx,176-app.cy,image=app.ware)                        #warehouse
        if onScreen(384-app.cx,352-app.cy):
            canvas.create_image(304-app.cx,320-app.cy,image=ImageTk.PhotoImage(app.sign))    #sign
            canvas.create_image(80-app.cx,320-app.cy,image=ImageTk.PhotoImage(app.girl))     #girl
        for x in range(96,1568,64):
            for y in range(480,672,64):
                if onScreen(x-app.cx,y-app.cy) and onPlayer(x-app.cx,y-app.cy)==False:
                    canvas.create_image(x-app.cx,y-app.cy,image=app.tgrass)                  #tallgrass
                elif onScreen(x-app.cx,y-app.cy) and onPlayer(x-app.cx,y-app.cy)==True:
                    canvas.create_image(x-app.cx,y-app.cy,image=app.flower)                  #flower
        if onScreen(app.a-app.cx,app.b-app.cy) and app.random==True:
            canvas.create_image(app.a-app.cx,app.b-app.cy,image=ImageTk.PhotoImage(app.mud)) #hidden poke
        if onScreen(1440-app.cx,176-app.cy) and 'Charmander' not in app.bag:
            canvas.create_image(1440-app.cx,176-app.cy,image=app.poke)                        #pokeball1
        if onScreen(1504-app.cx,176-app.cy) and 'Bulbasaur' not in app.bag:
            canvas.create_image(1504-app.cx,176-app.cy,image=app.poke)                        #pokeball2
        if onScreen(1440-app.cx,176-app.cy) and 'Charmander' in app.bag:
            canvas.create_image(1440-app.cx,176-app.cy,image=app.rock)                        #rock1
        if onScreen(1504-app.cx,176-app.cy) and 'Bulbasaur' in app.bag:
            canvas.create_image(1504-app.cx,176-app.cy,image=app.rock)                        #rock2
        if onScreen(1570-app.cx,352-app.cy):
            canvas.create_image(1570-app.cx,352-app.cy,image=ImageTk.PhotoImage(app.block))
            canvas.create_image(1570-app.cx,416-app.cy,image=ImageTk.PhotoImage(app.block))    #blocks
        if onScreen(1954-app.cx,352-app.cy):
            canvas.create_image(1954-app.cx,352-app.cy,image=app.poke)                         #pokeballs
            canvas.create_image(1954-app.cx,416-app.cy,image=app.poke)
            canvas.create_image(2018-app.cx,352-app.cy,image=app.poke)  
            canvas.create_image(2018-app.cx,416-app.cy,image=app.poke)

def drawCenter(app,canvas): #Draw center
    canvas.create_rectangle(0,0,1024,768,fill='black')
    canvas.create_image(512-app.cx,384-app.cy,image=ImageTk.PhotoImage(app.floor))              #floor1
    canvas.create_image(512-app.cx,0-app.cy,image=ImageTk.PhotoImage(app.floor))                #floor2
    canvas.create_image(512-app.cx,16-app.cy,image=ImageTk.PhotoImage(app.carpet))              #carpet
    canvas.create_image(512-app.cx,-96-app.cy,image=ImageTk.PhotoImage(app.desk))               #desk
    canvas.create_image(672-app.cx,-64-app.cy,image=ImageTk.PhotoImage(app.pc))                 #pc
    canvas.create_image(352-app.cx,-64-app.cy,image=ImageTk.PhotoImage(app.plant))              #plant

def drawPc(app,canvas): #Draw pc when open
    if app.openPc == True:
        canvas.create_rectangle(640,0,1024,248,fill='lightblue')
        canvas.create_text(832,32,text='Press g to close pc',font='Arial 20 bold',fill='gray')                   #pc
        if len(app.bag) == 0:
            canvas.create_text(832,64,text='You dont have any pokemons',fill='blue',font='Arial 15 bold')
        else:
            if 'Bulbasaur' in app.bag:
                canvas.create_text(960,96,text='Bulbasaur',fill='blue',font='Arial 15 bold')
                canvas.create_image(960,160,image=ImageTk.PhotoImage(app.Bulbasaur))
                canvas.create_rectangle(928,212,992,224,fill='lightgray',width=2)
                hp1 = app.bag['Bulbasaur'][0]
                if hp1<0:
                    hp1=0
                canvas.create_rectangle(928,212,928+64*(hp1/100),224,fill='green',width=1.5)
                if hp1==0:
                    canvas.create_image(960,160,image=ImageTk.PhotoImage(app.x))
            if 'Charmander' in app.bag:
                canvas.create_text(824,96,text='Charmander',fill='blue',font='Arial 15 bold')
                canvas.create_image(824,160,image=ImageTk.PhotoImage(app.Charmander))
                canvas.create_rectangle(798,212,856,224,fill='lightgray',width=2)
                hp2 = app.bag['Charmander'][0]
                if hp2<0:
                    hp2=0
                canvas.create_rectangle(798,212,798+64*(hp2/100),224,fill='green',width=1.5)
                if hp2==0:
                    canvas.create_image(824,160,image=ImageTk.PhotoImage(app.x))
            if 'Mudkip' in app.bag:
                canvas.create_text(696,96,text='Mudkip',fill='blue',font='Arial 15 bold')
                canvas.create_image(696,160,image=ImageTk.PhotoImage(app.Mudkip))
                canvas.create_rectangle(664,212,728,224,fill='lightgray',width=2)
                hp3 = app.bag['Mudkip'][0]
                if hp3<0:
                    hp3=0
                canvas.create_rectangle(664,212,664+64*(hp3/100),224,fill='green',width=1.5)
                if hp3==0:
                    canvas.create_image(696,160,image=ImageTk.PhotoImage(app.x))

def drawDialogue(app,canvas): #Draw diaogues
    if app.inCenter==False and (app.cx>=-224 and app.cx<=-192) and (app.cy==-32):                 
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='Come heal your pokemon',font='Arial 20 bold')                                 #sign center
    elif app.inCenter==False and app.cx in [-304,-288,-272] and app.cy==-32 and app.dir=='up':
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='Press f to enter',font='Arial 25 bold')                                       #door center
    elif app.inCenter==False and app.cx in [48,64,80] and app.cy==-32 and app.dir=='up':
        canvas.create_rectangle(0,640,1024,704,fill='white')                              
        canvas.create_text(512,672,text='Press f to enter',font='Arial 25 bold')                                       #door gym
    elif app.inCenter==False and app.cx==1008 and app.cy in [-48,-32,-16,0,16,32] and app.dir=='right':
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='Construction ahead',font='Arial 25 bold')                                     #construction
    elif app.inCenter==False and app.cy==-192 and app.cx==992 and app.dir=='up' and 'Bulbasaur' not in app.bag:
        canvas.create_rectangle(0,640,1024,704,fill='white')    
        canvas.create_text(512,672,text='Press f to get Bulbasaur',font='Arial 25 bold')                               #Bulbasaur
    elif app.inCenter==False and app.cy==-192 and app.cx==928 and app.dir=='up' and 'Charmander' not in app.bag:         
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='Press f to get Charmander',font='Arial 25 bold')                              #Charmander
    elif app.inCenter==False and onPlayer(app.a-app.cx,app.b-app.cy) and app.random==True:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='Press f to get Mudkip',font='Arial 25 bold')                                  #Mudkip
    elif app.inCenter==False and app.cx==-432 and app.cy in [-32,-16,0,16]:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        if 'Mudkip' not in app.bag:
            canvas.create_text(512,672,text='You can catch Mudkip in the bushes if you are fast enough!',font='Arial 25 bold')
        else:
            canvas.create_text(512,672,text='Wild pokemons come at 75 health!',font='Arial 25 bold')
        canvas.create_text(512,736,text='Press Space to leave',font='Arial 25 bold',fill='white')                      #conversation girl
    elif app.inCenter==False and app.cy>=64 and app.cx>=-432 and app.cx<=1008 and app.cy<=224 and app.moving==True:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='*grass noises*',font='Arial 15')                                              #grass noise
    elif app.inCenter==True and app.cx==160 and app.cy==-400 and app.dir=='up' and app.openPc == False:
            canvas.create_rectangle(0,640,1024,704,fill='white')
            canvas.create_text(512,672,text='Press f to open pc',font='Arial 25 bold')                                 #pc
    elif app.inCenter==False and (len(app.bag)==0 or isZero(app,1)) and app.cx==64 and app.cy==-32 and app.dir=='down':
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='You have no avilable pokemons for battle',font='Arial 25 bold')               #kicked
    elif app.inCenter==True and app.cx==0 and app.cy==-400 and app.dir=='up':
        if allHealed(app):
            canvas.create_rectangle(0,640,1024,704,fill='white')
            canvas.create_text(512,672,text='You have no healable pokemons',font='Arial 25 bold')                      #Can't heal
        else:
            canvas.create_rectangle(0,640,1024,704,fill='white')
            canvas.create_text(512,672,text='Press f to heal',font='Arial 25 bold')                                    #Heal

def drawPlayer(app,canvas): #Draw player
    canvas.create_image(512,384,image=app.player)


#Draw in gym
def drawGym(app,canvas): #Draw gym
    canvas.create_rectangle(0,0,1024,768,fill='black')
    for x in range(128,960,64):
        for y in range(-800,480,64):
            if onScreen3(x-app.cx,y-app.cy) or (app.lights==True and onScreen4(x-app.cx,y-app.cy)):
                canvas.create_image(x-app.cx,y-app.cy,image=app.gymFloor)                                       #floor
            if (onScreen3(x-app.cx,y-app.cy) or (app.lights==True and onScreen4(x-app.cx,y-app.cy))) and app.showPath==True:
                if (x,y) in app.path:
                    canvas.create_image(x-app.cx,y-app.cy,image=app.brightFloor)                                #path
    if onScreen3(512-app.cx,416-app.cy) or (app.lights==True and onScreen4(512-app.cx,416-app.cy)):
        canvas.create_image(512-app.cx,416-app.cy,image=app.brightFloor)                                        #entrance
    if onScreen3(512-app.cx,-800-app.cy) or (app.lights==True and onScreen4(512-app.cx,-800-app.cy)):
        canvas.create_image(512-app.cx,-800-app.cy,image=app.brightFloor)                                       #exit
    if (onScreen3(app.mikeX-app.cx,416-app.cy) or (app.lights==True and onScreen4(app.mikeX-app.cx,416-app.cy))):
        canvas.create_image(128-app.cx,416-app.cy,image=app.brightFloor)
        if app.mikeAlive:
            canvas.create_image(app.mikeX-app.cx,416-app.cy,image=ImageTk.PhotoImage(app.Mike))                     #Mike
    for x in range(128,256,64):
        if onScreen3(x-app.cx,352-app.cy) or (app.lights==True and onScreen4(x-app.cx,352-app.cy)):
            canvas.create_image(x-app.cx,352-app.cy,image=app.wall)                                             #Walls
    for x in range(192,320,64):
        if onScreen3(x-app.cx,224-app.cy) or (app.lights==True and onScreen4(x-app.cx,224-app.cy)):
            canvas.create_image(x-app.cx,224-app.cy,image=app.wall)
    for y in range(224,480,64):
        if onScreen3(320-app.cx,y-app.cy) or (app.lights==True and onScreen4(320-app.cx,y-app.cy)):
            canvas.create_image(320-app.cx,y-app.cy,image=app.wall)
    for x in range(192,960,64):
        if onScreen3(x-app.cx,96-app.cy) or (app.lights==True and onScreen4(x-app.cx,96-app.cy)):
            canvas.create_image(x-app.cx,96-app.cy,image=app.wall)
    for x in range(448,896,64):
        if onScreen3(x-app.cx,352-app.cy) or (app.lights==True and onScreen4(x-app.cx,352-app.cy)):
            canvas.create_image(x-app.cx,352-app.cy,image=app.wall)
    for x in range(384,896,64):
        if onScreen3(x-app.cx,224-app.cy) or (app.lights==True and onScreen4(x-app.cx,224-app.cy)):
            canvas.create_image(x-app.cx,224-app.cy,image=app.wall)
    if onScreen3(832-app.cx,288-app.cy) or (app.lights==True and onScreen4(832-app.cx,288-app.cy)):
        canvas.create_image(832-app.cx,288-app.cy,image=app.wall)
    if onScreen3(768-app.cx,288-app.cy) or (app.lights==True and onScreen4(768-app.cx,288-app.cy)):
        if app.lights:
            canvas.create_oval(768-32-app.cx,256-8-app.cy,768+32-app.cx,288+8-app.cy,fill='yellow',width=0)    #light
        canvas.create_image(768-app.cx,288-app.cy,image=ImageTk.PhotoImage(app.lamp))                          #lamp
    for x in [128,192,256,320]:                                                                                    #barrels
        if onScreen3(x-app.cx,-32-app.cy) or (app.lights==True and onScreen4(x-app.cx,-32-app.cy)):
            canvas.create_image(x-app.cx,-32-app.cy,image=app.barrel)   
    for x in [448,512,576,640,704,768,832]:
        if onScreen3(x-app.cx,-96-app.cy) or (app.lights==True and onScreen4(x-app.cx,-96-app.cy)):
            canvas.create_image(x-app.cx,-96-app.cy,image=app.barrel)
    for x in [192,256,320,384,448]:
        if onScreen3(x-app.cx,-160-app.cy) or (app.lights==True and onScreen4(x-app.cx,-160-app.cy)):
            canvas.create_image(x-app.cx,-160-app.cy,image=app.barrel)
    if onScreen3(448-app.cx,32-app.cy) or (app.lights==True and onScreen4(448-app.cx,32-app.cy)):
        canvas.create_image(448-app.cx,32-app.cy,image=app.barrel)
    if onScreen3(576-app.cx,-32-app.cy) or (app.lights==True and onScreen4(576-app.cx,-32-app.cy)):
        canvas.create_image(576-app.cx,-32-app.cy,image=app.barrel)
    if onScreen3(704-app.cx,32-app.cy) or (app.lights==True and onScreen4(704-app.cx,32-app.cy)):
        canvas.create_image(704-app.cx,32-app.cy,image=app.barrel)
    if onScreen3(832-app.cx,-32-app.cy) or (app.lights==True and onScreen4(832-app.cx,-32-app.cy)):
        canvas.create_image(832-app.cx,-32-app.cy,image=app.barrel)
    for x in [576,640,704,768,832,896]:
        if onScreen3(x-app.cx,-224-app.cy) or (app.lights==True and onScreen4(x-app.cx,-224-app.cy)):
            canvas.create_image(x-app.cx,-224-app.cy,image=app.barrel)
    if onScreen3(448-app.cx,-224-app.cy) or (app.lights==True and onScreen4(448-app.cx,-224-app.cy)):
            canvas.create_image(448-app.cx,-224-app.cy,image=app.barrel)
    for x in [128,192,256,320,384,448]:
        if onScreen3(x-app.cx,-288-app.cy) or (app.lights==True and onScreen4(x-app.cx,-288-app.cy)):
            canvas.create_image(x-app.cx,-288-app.cy,image=app.barrel)
    for x in [448,512,640,704,768,832]:
        if onScreen3(x-app.cx,-352-app.cy) or (app.lights==True and onScreen4(x-app.cx,-352-app.cy)):
            canvas.create_image(x-app.cx,-352-app.cy,image=app.barrel)
    for x in [128,192,256,512,640]:
        if onScreen3(x-app.cx,-416-app.cy) or (app.lights==True and onScreen4(x-app.cx,-416-app.cy)):
            canvas.create_image(x-app.cx,-416-app.cy,image=app.barrel)
    for x in [384,512,576,640,768,832,896]:
        if onScreen3(x-app.cx,-480-app.cy) or (app.lights==True and onScreen4(x-app.cx,-480-app.cy)):
            canvas.create_image(x-app.cx,-480-app.cy,image=app.barrel)
    for x in [192,384]:
        if onScreen3(x-app.cx,-544-app.cy) or (app.lights==True and onScreen4(x-app.cx,-544-app.cy)):
            canvas.create_image(x-app.cx,-544-app.cy,image=app.barrel)
    for x in [192,256,320,384,448,576,640,704,768,832,896]:
        if onScreen3(x-app.cx,-608-app.cy) or (app.lights==True and onScreen4(x-app.cx,-608-app.cy)):
            canvas.create_image(x-app.cx,-608-app.cy,image=app.barrel)
    for x in [192,448]:
        if onScreen3(x-app.cx,-672-app.cy) or (app.lights==True and onScreen4(x-app.cx,-672-app.cy)):
            canvas.create_image(x-app.cx,-672-app.cy,image=app.barrel)
    for x in [192,320,448,512,576,640,704,768,832]:
        if onScreen3(x-app.cx,-736-app.cy) or (app.lights==True and onScreen4(x-app.cx,-736-app.cy)):
            canvas.create_image(x-app.cx,-736-app.cy,image=app.barrel)
    for x in [320,576]:
        if onScreen3(x-app.cx,-800-app.cy) or (app.lights==True and onScreen4(x-app.cx,-800-app.cy)):
            canvas.create_image(x-app.cx,-800-app.cy,image=app.barrel)

def drawBag(app,canvas): #Draws bag
    canvas.create_rectangle(640,0,1024,184,fill='lightblue')
    if 'Bulbasaur' in app.bag:
        canvas.create_text(960,32,text='Bulbasaur',fill='blue',font='Arial 15 bold')
        canvas.create_image(960,96,image=ImageTk.PhotoImage(app.Bulbasaur))
        canvas.create_rectangle(928,148,992,160,fill='lightgray',width=2)
        hp1 = app.bag['Bulbasaur'][0]
        if hp1<0:
            hp1=0
        canvas.create_rectangle(928,148,928+64*(hp1/100),160,fill='green',width=1.5)
        if hp1==0:
            canvas.create_image(960,96,image=ImageTk.PhotoImage(app.x))
    if 'Charmander' in app.bag:
        canvas.create_text(824,32,text='Charmander',fill='blue',font='Arial 15 bold')
        canvas.create_image(824,96,image=ImageTk.PhotoImage(app.Charmander))
        canvas.create_rectangle(792,148,856,160,fill='lightgray',width=2)
        hp2 = app.bag['Charmander'][0]
        if hp2<0:
            hp2=0
        canvas.create_rectangle(792,148,792+64*(hp2/100),160,fill='green',width=1.5)
        if hp2==0:
            canvas.create_image(824,96,image=ImageTk.PhotoImage(app.x))
    if 'Mudkip' in app.bag:
        canvas.create_text(696,32,text='Mudkip',fill='blue',font='Arial 15 bold')
        canvas.create_image(696,96,image=ImageTk.PhotoImage(app.Mudkip))
        canvas.create_rectangle(664,148,728,160,fill='lightgray',width=2)
        hp3 = app.bag['Mudkip'][0]
        if hp3<0:
            hp3=0
        canvas.create_rectangle(664,148,664+64*(hp3/100),160,fill='green',width=1.5)
        if hp3==0:
            canvas.create_image(696,96,image=ImageTk.PhotoImage(app.x))

def drawDialogue2(app,canvas): #Draw dialogues
    if app.cx in [-32,-16,0,16,32] and app.cy in [-16,0,16,32]:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='Welcome to the Mellon Institute',font='Arial 20 bold')     #welcome
    elif app.cx<=-368 and app.cy>=-16:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='Press m to show path',font='Arial 20 bold')   #show path
    elif app.cx==-272 and app.cy==32 and app.mikeAlive:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='Hey! My name is Mike Oxmaul',font='Arial 20 bold')
    elif app.cx in [-16,0,16] and app.cy in [-1232,-1216,-1200,-1184,]:                      #Finish game
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='Press f to finish game',font='Arial 20 bold')
    elif app.cx==208 and app.cy in [-144,-128,-112,-96] and app.dir=='right':                #Lights
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='Press f to toggle lights',font='Arial 20 bold')


#Draw animation to battle
def drawAnimation(app,canvas): #Draw battle animation
    canvas.create_rectangle(0-app.battleX,0-app.battleY,1024-app.battleX,384-app.battleY,fill='red',width=0)
    canvas.create_rectangle(0-app.battleX,384+app.battleY,1024-app.battleX,768+app.battleY,fill='white',width=0)
    if app.inBattle==False:
        canvas.create_image(512-app.battleX,384,image=app.bigPoke) #,angle=math.pi/16*app.battleX


#Draw in battle
def drawBattle1(app,canvas): #Draws battle with Mike
    canvas.create_rectangle(0,0,1024,192,fill='lightblue')
    canvas.create_rectangle(0,192,1024,768,fill='green')
    canvas.create_oval(432,216,976,360,fill='tan')
    canvas.create_oval(448,224,960,352,fill='lightgreen')
    canvas.create_oval(112,536,656,680,fill='tan')
    canvas.create_oval(128,544,640,672,fill='lightgreen')                                #background
    
    if isZero(app,2)==False:                                                             #draw Bidoof
        canvas.create_image(704,256,image=ImageTk.PhotoImage(app.bigBidoof))
        canvas.create_polygon(124,124,414,124,448,228,124,228,fill='black')
        canvas.create_polygon(128,128,410,128,442,224,128,224,fill='lightgray')
        canvas.create_text(176,152,text='Bidoof',font='Arial 15 bold')
        canvas.create_image(160,192,image=app.smallPoke)
        canvas.create_rectangle(192,172,384,196,fill='lightgray',width=2)
        hp1 = app.MikeBag['Bidoof'][0]//1
        if hp1<0:
            hp1=0
        canvas.create_rectangle(192,172,192+192*(hp1/100),196,fill='green',width=1.5)
        canvas.create_text(348,208,text=f'{hp1} / 100',font='Arial 13 bold')

    if app.curr=='Mudkip':                                                           #draw mudkip
        canvas.create_image(384,576,image=ImageTk.PhotoImage(app.bigMudkipb))
        canvas.create_polygon(668,508,958,508,958,612,634,612,fill='black')
        canvas.create_polygon(672,512,954,512,954,608,640,608,fill='lightgray')
        canvas.create_text(724,536,text='Mudkip',font='Arial 15 bold')
        canvas.create_image(700,576,image=app.smallPoke)
        canvas.create_rectangle(732,556,924,580,fill='lightgray',width=2)
        hp = app.bag['Mudkip'][0]//1
        if hp<0:
            hp=0
        canvas.create_rectangle(732,556,732+192*(hp/100),580,fill='green',width=1.5)
        canvas.create_text(888,592,text=f'{hp} / 100',font='Arial 13 bold')
    elif app.curr=='Charmander':                                                       #draw charmander
        canvas.create_image(384,576,image=ImageTk.PhotoImage(app.bigCharmanderb))
        canvas.create_polygon(668,508,958,508,958,612,634,612,fill='black')
        canvas.create_polygon(672,512,954,512,954,608,640,608,fill='lightgray')
        canvas.create_text(724,536,text='Charmander',font='Arial 15 bold')
        canvas.create_image(700,576,image=app.smallPoke)
        canvas.create_rectangle(732,556,924,580,fill='lightgray',width=2)
        hp = app.bag['Charmander'][0]//1
        if hp<0:
            hp=0
        canvas.create_rectangle(732,556,732+192*(hp/100),580,fill='green',width=1.5)
        canvas.create_text(888,592,text=f'{hp} / 100',font='Arial 13 bold')
    elif app.curr=='Bulbasaur':                                                                    #draw bulbasaur
        canvas.create_image(384,576,image=ImageTk.PhotoImage(app.bigBulbasaurb))
        canvas.create_polygon(668,508,958,508,958,612,634,612,fill='black')
        canvas.create_polygon(672,512,954,512,954,608,640,608,fill='lightgray')
        canvas.create_text(724,536,text='Bulbasaur',font='Arial 15 bold')
        canvas.create_image(700,576,image=app.smallPoke)
        canvas.create_rectangle(732,556,924,580,fill='lightgray',width=2)
        hp = app.bag['Bulbasaur'][0]//1
        if hp<0:
            hp=0
        canvas.create_rectangle(732,556,732+192*(hp/100),580,fill='green',width=1.5)
        canvas.create_text(888,592,text=f'{hp} / 100',font='Arial 13 bold')

    if app.turn and isZero(app,1)==False:
        canvas.create_rectangle(0,258,224,359,fill='lightgrey')                     #1
        canvas.create_text(112,308.5,text=f'(1) {app.bag[app.curr][1][0]}',font='Arial 21 bold')
        canvas.create_rectangle(224,258,448,359,fill='lightgrey')                   #2
        canvas.create_text(336,308.5,text=f'(2) {app.bag[app.curr][1][1]}',font='Arial 21 bold')
        canvas.create_rectangle(0,359,224,460,fill='lightgrey')                     #3
        canvas.create_text(112,409.5,text=f'(3) {app.bag[app.curr][1][2]}',font='Arial 21 bold')
        canvas.create_rectangle(224,359,448,460,fill='lightgrey')                   #4
        canvas.create_text(336,409.5,text='(4) Run',font='Arial 21 bold')

def drawDialogue3(app,canvas): #Draw dialogues in battle
    if app.turn:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text=f'What would you like {app.curr} to do?',font='Arial 20 bold')           #ask user
        canvas.create_text(512,736,text='Press 5 to cycle pokemon',font='Arial 20 bold',fill='white')
    if app.cantRun:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='You cant run from a player battle!',font='Arial 20 bold')    #cant run
    if app.cantCycle:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='You dont have pokemons to switch to!',font='Arial 20 bold')    #cant switch
    if app.battleTimer!=0 and app.battleTimer<10:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text=f'{app.curr} used {app.bag[app.curr][1][app.currMove-1]}',font='Arial 20 bold')  #Your move
    elif app.battleTimer>=10 and app.battleTimer<25 and app.fainted==False and app.turn==False:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text=f'Bidoof used {app.currMove}',font='Arial 20 bold')   #Opponent Move
    if app.fainted==True:
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text=f'{app.curr} fainted!',font='Arial 20 bold')           #fainted message
    if isZero(app,1):
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='All of your pokemon fainted :(, try again next time',font='Arial 20 bold')     #lost battle
    elif isZero(app,2):
        canvas.create_rectangle(0,640,1024,704,fill='white')
        canvas.create_text(512,672,text='Congratulations! You beat Mike!\nCheck under Mike for a surprise ;)',font='Arial 20 bold')     #won battle

def drawBag2(app,canvas): #Draws bag
    if app.curr=='Mudkip':
        canvas.create_rectangle(640,3,748,168,fill='lightblue')
    elif app.curr=='Charmander':
        canvas.create_rectangle(748,3,896,168,fill='lightblue')
    elif app.curr=='Bulbasaur':
        canvas.create_rectangle(896,3,1021,168,fill='lightblue')
    if 'Bulbasaur' in app.bag:
        canvas.create_text(960,32,text='Bulbasaur',fill='blue',font='Arial 15 bold')
        canvas.create_image(960,96,image=ImageTk.PhotoImage(app.Bulbasaur))
        canvas.create_rectangle(928,148,992,160,fill='lightgray',width=2)
        hp1 = app.bag['Bulbasaur'][0]
        if hp1<0:
            hp1=0
        canvas.create_rectangle(928,148,928+64*(hp1/100),160,fill='green',width=1.5)
        if hp1==0:
            canvas.create_image(960,96,image=ImageTk.PhotoImage(app.x))
    if 'Charmander' in app.bag:
        canvas.create_text(824,32,text='Charmander',fill='blue',font='Arial 15 bold')
        canvas.create_image(824,96,image=ImageTk.PhotoImage(app.Charmander))
        canvas.create_rectangle(792,148,856,160,fill='lightgray',width=2)
        hp2 = app.bag['Charmander'][0]
        if hp2<0:
            hp2=0
        canvas.create_rectangle(792,148,792+64*(hp2/100),160,fill='green',width=1.5)
        if hp2==0:
            canvas.create_image(824,96,image=ImageTk.PhotoImage(app.x))
    if 'Mudkip' in app.bag:
        canvas.create_text(696,32,text='Mudkip',fill='blue',font='Arial 15 bold')
        canvas.create_image(696,96,image=ImageTk.PhotoImage(app.Mudkip))
        canvas.create_rectangle(664,148,728,160,fill='lightgray',width=2)
        hp3 = app.bag['Mudkip'][0]
        if hp3<0:
            hp3=0
        canvas.create_rectangle(664,148,664+64*(hp3/100),160,fill='green',width=1.5)
        if hp3==0:
            canvas.create_image(696,96,image=ImageTk.PhotoImage(app.x))


#Draw end screen
def drawEnd(app,canvas): #Draw end screen
    canvas.create_rectangle(0,0,1024,768,fill='black')
    canvas.create_text(512,768-app.endY,text='Thank you for playing Pokemon Mini!!!',font='Arial 30 bold',fill='white')
    canvas.create_text(512,832-app.endY,text='Hope you enjoyed the ride!',font='Arial 20 bold',fill='white')
    canvas.create_text(512,896-app.endY,text='By: Lucas Yi',font='Arial 20 bold',fill='white')
    canvas.create_text(512,1152-app.endY,text='Press any key to restart!',font='Arial 20 bold',fill='white')


#Draw load/save message
def drawMessage(app,canvas):
    if app.loadMessage:
        canvas.create_rectangle(768,0,1024,128,fill='white')
        canvas.create_text(896,64,text='Loaded State!',font='Arial 20 bold',fill='black')
    if app.saveMessage:
        canvas.create_rectangle(768,0,1024,128,fill='white')
        canvas.create_text(896,64,text='Saved State!',font='Arial 20 bold',fill='black')


#Helpers
def onScreen(x,y): #On screen for normal objects
    if x+32>=0 and x-32<=1024 and y+32>=0 and y-32<=768:
        return True
    return False

def onScreen2(x,y): #On screen for buidings
    if x+192>=0 and x-128<=1024 and y+192>=0 and y-128<=768:
        return True
    return False

def onScreen3(x,y): #On screen limited vision with lights off
    if x+32>=320 and x-32<=704 and y+32>=256 and y-32<=512:
        return True
    return False

def onScreen4(x,y): #On screen limited vision with lights on
    if x+32>=192 and x-32<=832 and y+32>=192 and y-32<=576:
        return True
    return False

def onPlayer(x,y): #Checks if object is on person
    if x+16>480 and x-16<544 and y-16<416 and y+16>352:
        return True
    return False

def allHealed(app): #Checks if all pokemon are healed
    for poke in app.bag:
        if app.bag[poke][0] != 100:
            return False
    return True

def isZero(app,num): #Checks if all pokemon are dead
    if num==1:
        for poke in app.bag:
            if app.bag[poke][0] > 0:
                return False
        return True
    elif num==2:
        for poke in app.MikeBag:
            if app.MikeBag[poke][0] > 0:
                return False
        return True

def battleMove(app,battleNum): #Does the move
    move=app.bag[app.curr][1][battleNum-1]

    app.MikeBag['Bidoof'][0] -= (damage[move][0]
        *multiplier(damage[move][1],app.MikeBag['Bidoof'][2],app.MikeBag['Bidoof'][3])) #damage to other

    if app.bag[app.curr][0] + damage[move][2] <= 100:        #heal/damage to self
        app.bag[app.curr][0] += damage[move][2]
    else:
        app.bag[app.curr][0] = 100
        
    if app.bag[app.curr][3] - damage[move][3] >= 0.6 and app.bag[app.curr][3] - damage[move][3] <= 1.4:        #defense
        app.bag[app.curr][3] -= damage[move][3]

def opponentMove(app,move): #Does opponents move
    app.bag[app.curr][0] -= (damage[move][0]
        *multiplier(damage[move][1],app.bag[app.curr][2],app.bag[app.curr][3])) #damage to other

    if app.MikeBag['Bidoof'][0] + damage[move][2] <= 100:        #heal/damage to self
        app.MikeBag['Bidoof'][0] += damage[move][2]
    else:
        app.MikeBag['Bidoof'][0] = 100
        
    if app.MikeBag['Bidoof'][3] - damage[move][3] >= 0.6 and app.MikeBag['Bidoof'][3] - damage[move][3] <= 1.4:        #defense
        app.MikeBag['Bidoof'][3] -= damage[move][3]

def lost(app): #Reset settings when you lose
    app.cx=0
    app.cy=-336
    app.m=16
    app.timer=0                                                                 #timer
    app.dir='up'                                                                #direction
    app.move=True                                                               #can move
    app.moving=False                                                            #moving

    app.mikeX=128                                                               #Mike location
    app.battleX=-1392                                                           #Batte animation
    app.battleY=0
    app.endY=0                                                                  #End scroll

    app.inCenter=True                                                           #inCenter
    app.inGym=False                                                             #inGym
    app.battle=False                                                            #startBattle
    app.inBattle=False                                                          #inBattle
    app.openPc=False                                                            #openPc
    app.endGame=False                                                           #end game
    app.lights=False                                                            #gym vision
    app.showPath=False                                                          #show path

    app.cantRun=False                                                           #cant run message

    app.turn=True                                                               #player's turn
    app.mikeAlive=True                                                          #Mike alive
    app.battleTimer=0                                                           #battle timer
    app.currMove=0                                                              #current move
    app.opponent=False                                                          #opponents turn
    app.endTimer=0
    app.queue=False                                                             #end timer
    app.fainted=False
    app.faintedTimer=0                                                          #fainted message

    app.MikeBag={'Bidoof': [100,['Scratch','Defend'],'Normal',1]}

def saveGame(app): #save game
    app.cx1=app.cx
    app.cy1=app.cy
    app.m1=app.m
    app.timer1=app.timer
    app.player1=app.player
    app.dir1=app.dir
    app.move1=app.move
    app.moving1=app.moving
    app.rx1,app.ry1=app.rx,app.ry             
    app.a1,app.b1=app.a,app.b
    app.random1=app.random
    app.mikeX1=app.mikeX
    app.battleX1=app.battleX
    app.battleY1=app.battleY
    app.endY1=app.endY
    app.inCenter1=app.inCenter
    app.inGym1=app.inGym
    app.battle1=app.battle
    app.inBattle1=app.inBattle
    app.openPc1=app.openPc
    app.endGame1=app.endGame
    app.lights1=app.lights
    app.showPath1=app.showPath
    app.path1=app.path
    app.ghost1=app.ghost
    app.cantRun1=app.cantRun
    app.cantCycle1=app.cantCycle
    app.turn1=app.turn
    app.mikeAlive1=app.mikeAlive
    app.battleTimer1=app.battleTimer
    app.currMove1=app.currMove
    app.opponent1=app.opponent
    app.endTimer1=app.endTimer
    app.queue1=app.queue
    app.fainted1=app.fainted
    app.faintedTimer1=app.faintedTimer
    app.bag1=copy.deepcopy(app.bag)
    app.MikeBag1=copy.deepcopy(app.MikeBag)
    app.curr1=app.curr

def loadGame(app): #load game
    app.cx=app.cx1
    app.cy=app.cy1
    app.m=app.m1
    app.timer=app.timer1
    app.player=app.player1
    app.dir=app.dir1
    app.move=app.move1
    app.moving=app.moving1
    app.rx,app.ry=app.rx1,app.ry1             
    app.a,app.b=app.a1,app.b1
    app.random=app.random1
    app.mikeX=app.mikeX1
    app.battleX=app.battleX1
    app.battleY=app.battleY1
    app.endY=app.endY1
    app.inCenter=app.inCenter1
    app.inGym=app.inGym1
    app.battle=app.battle1
    app.inBattle=app.inBattle1
    app.openPc=app.openPc1
    app.endGame=app.endGame1
    app.lights=app.lights1
    app.showPath=app.showPath1
    app.path=app.path1
    app.ghost=app.ghost1
    app.cantRun=app.cantRun1
    app.cantCycle=app.cantCycle1
    app.turn=app.turn1
    app.mikeAlive=app.mikeAlive1
    app.battleTimer=app.battleTimer1
    app.currMove=app.currMove1
    app.opponent=app.opponent1
    app.endTimer=app.endTimer1
    app.queue=app.queue1
    app.fainted=app.fainted1
    app.faintedTimer=app.faintedTimer1
    app.bag=copy.deepcopy(app.bag1)
    app.MikeBag=copy.deepcopy(app.MikeBag1)
    app.curr=app.curr1


#Draw
def redrawAll(app, canvas): #Draw all
    if app.inGym == False:
        drawBoard(app,canvas)
        if app.inCenter == True:
            drawCenter(app,canvas)
            drawPc(app,canvas)
        drawDialogue(app,canvas)
    elif app.inGym == True:
        if app.inBattle == False:
            drawGym(app,canvas)
            drawBag(app,canvas)
            drawDialogue2(app,canvas)
        else:
            drawBattle1(app,canvas)
            drawDialogue3(app,canvas)
            drawBag2(app,canvas)
    if app.inBattle == False:
        drawPlayer(app,canvas)
    if app.battle == True:
        drawAnimation(app,canvas)
    if app.endGame == True:
        drawEnd(app,canvas)
    drawMessage(app,canvas)


runApp(width=1024, height=768) #Run app