##################################################################################
#  Basic format of minimax algorithm from https://en.wikipedia.org/wiki/Minimax  #
##################################################################################

import math,copy

#battle moves and stats
#{name:[dmg to other, type, dmg to self, defense]}
damage = {'Ember':[15,'Fire',0,0],'Water Gun':[15,'Water',0,0],'Vine Whip':[15,'Grass',0,0],
            'Body Slam':[20,'Normal',0,0],'Taunt':[1,'Normal',0,0],'Scratch':[15,'Normal',0,0],
            'Heal':[0,'Normal',30,0],'Defend':[0,'Normal',5,0.2],'Double Edge':[30,'Normal',-15,0],
            'Explode':[50,'Fire',-50,0],'Aqua Tail':[20,'Water',0,-0.2],'Die':[0,'Normal',-100,0]}

#[hp, [moves], type, defense]
Charmander=[75,['Ember','Body Slam','Explode'],'Fire',1]
Bulbasaur=[75,['Vine Whip','Body Slam','Heal'],'Grass',1]
Mudkip=[75,['Water Gun','Body Slam','Aqua Tail'],'Water',1]
Bidoof=[100,['Scratch','Defend'],'Normal',1]


#ai functions
def battle(poke1,poke2,depth):#poke1=ai poke2=player
    move = battleAi(poke1,poke2,True,depth,-math.inf,math.inf)[1]
    return move

def battleAi(poke1,poke2,player1,depth,alpha,beta): #Minimax, with alpha beta prunning
    if(depth==0 or poke1[0]<=0 or poke2[0]<=0):
        return (poke1[0]-poke2[0],"")        

    if player1:
        bestDiff = -math.inf
        bestMove = ""

        for move in poke1[1]:
            tempPoke1=copy.copy(poke1)
            tempPoke2=copy.copy(poke2)

            tempPoke2[0] -= damage[move][0]*multiplier(damage[move][1],poke2[2],poke2[3])

            if tempPoke1[0] + damage[move][2] <= 100:
                tempPoke1[0] += damage[move][2]
            else:
                tempPoke1[0] = 100
                
            if tempPoke1[3] - damage[move][3] >= 0.6 and tempPoke1[3] - damage[move][3] <= 1.4:
                tempPoke1[3] -= damage[move][3]

            tempDiff = battleAi(tempPoke1,tempPoke2,False,depth,alpha,beta)[0]

            if(tempDiff > bestDiff):
                bestDiff = tempDiff
                bestMove = move

            if bestDiff >= beta:
                break
            alpha = max(alpha,bestDiff)

        return (bestDiff, bestMove)

    else:
        bestDiff = math.inf
        bestMove = ""

        for move in poke2[1]:
            tempPoke1=copy.copy(poke1)
            tempPoke2=copy.copy(poke2)
            
            tempPoke1[0] -= damage[move][0]*multiplier(damage[move][1],poke1[2],poke1[3])

            if tempPoke2[0] + damage[move][2] <= 100:
                tempPoke2[0] += damage[move][2]
            else:
                tempPoke2[0] = 100

            if tempPoke2[3] - damage[move][3] >= 0.6 and tempPoke2[3] - damage[move][3] <= 1.4:
                tempPoke2[3] -= damage[move][3]

            tempDiff = battleAi(tempPoke1,tempPoke2,True,depth-1,alpha,beta)[0]

            if(tempDiff < bestDiff):
                bestDiff = tempDiff
                bestMove = move

            if bestDiff <= alpha:
                break
            beta = min(beta,bestDiff)

        return (bestDiff, bestMove)

def multiplier(a,b,c): #Checks type and returns multiplier (a=move b=opponent c=defense)
    if a=='Normal' or b=='Normal':
        return 1*c
    elif a=='Water':
        if b=='Water':
            return 1*c
        elif b=='Fire':
            return 2*c
        elif b=='Grass':
            return 0.5*c
    elif a=='Fire':
        if b=='Water':
            return 0.5*c
        elif b=='Fire':
            return 1*c
        elif b=='Grass':
            return 2*c
    elif a=='Grass':
        if b=='Water':
            return 2*c
        elif b=='Fire':
            return 0.5*c
        elif b=='Grass':
            return 1*c
