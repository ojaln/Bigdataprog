# -*- coding: utf-8 -*-
"""
Created on Fri May 17 17:35:25 2019

@author: ADMIN
"""
import random
class Mythology:
    @staticmethod
    def init(self, skills):
        self.skills = skills
        
Aphrodite = Mythology()
Aphrodite.skills= 70
Apollo = Mythology()
Apollo.skills= 98
Ares = Mythology()
Ares.skills= 67
Athena = Mythology()
Athena.skills = 55
Hades = Mythology()
Hades.skills = 92
Hephaestus = Mythology()
Hephaestus.skills = 73
Hermes = Mythology()
Hermes.skills = 84
Zeus = Mythology()
Zeus.skills = 100
Dionysus = Mythology()
Dionysus.skills = 86
Hera = Mythology()
Hera.skills = 97


CardSet1 = [Aphrodite,Apollo,Hermes,Dionysus,Athena]
CardSet2 = [Ares,Hades,Hephaestus,Hera,Zeus]

outdatedList=[]

currentCardSet1 = random.choice([CardSet1,CardSet2])
if(currentCardSet1==CardSet1):
    currentCardSet2=CardSet2
    playerFlag=True
    
else:
    currentCardSet2=CardSet1
    playerFlag=False

gSpellP1used=False
gSpellP2used=False
rSpellP1used=False
rSpellP2used=False

xchangeFlag=False
m = 0
pointsP1=0
pointsP2=0
round = 0
CardSet1=""
CardSet2=""

CardSet1rSpell="No"
CardSet1gSpell="No"
CardSet2gSpell="No"
CardSet2rSpell="No"


def rules(currentCardSet1,currentCardSet2):
    global playerFlag
    global CardSet1
    global CardSet2
    if(playerFlag==True):
        CardSet1="Computer"
        CardSet2="You"
    else:
        CardSet1="You"
        CardSet2="Computer"
   
    while(len(currentCardSet1)>0 and len(currentCardSet2)>0):
        players=playGame(currentCardSet1,currentCardSet2)
        if players is not None:
            if(xchangeFlag==True):
                change=players[1]
                del players[1]
                players.insert(0,change)
            
                if(playerFlag==True):
                    playerFlag=False
                else:
                    playerFlag=True
                Xchange = CardSet1
                CardSet1 = CardSet2
                CardSet2 = Xchange            
        else:
            break
        
    if(pointsP1>pointsP2):
        print("Computer wins")
    else:
        print("You win")

def playGame(currentCardSet1,currentCardSet2):
    global round
    round= round + 1
    global pointsP1
    global pointsP2
    global rSpellP1used
    global m
    if(playerFlag==True):
        if(rSpellP1used==False and m==1):
            global CardSet1rSpell
            CardSet1rSpell=input("Round: "+str(round)+ '\n' + ".Do "+CardSet1 + '\n' + " want to use Recursive spell?" + '\n' + "Yes or No     ")
        global gSpellP1used
        if(gSpellP1used==False):
            global CardSet1gSpell
            CardSet1gSpell=input("Round: "+str(round)+ '\n' +".Do "+CardSet1+"  want to use God's spell?" +'\n' + "Yes or No     ")
        global rSpellP2used
        if(rSpellP2used==False and m==1):
            global CardSet2rSpell
            CardSet2rSpell=input("Round: "+str(round)+ '\n' +".Do "+CardSet2+" want to use recursive spell?" + '\n' + "Yes or No     ")
    else:
        if(rSpellP2used==False and m==1):
            #global CardSet1rSpell
            CardSet1rSpell=input("Round: "+str(round)+ '\n' +".Do "+CardSet1+" want to use Recursive spell?" + '\n' + "Yes or No     ")
        global gSpellP2used
        if(gSpellP2used==False):
            #global CardSet1gSpell
            CardSet1gSpell=input("Round: "+str(round)+ '\n' +".Do "+CardSet1+ "  want to use God's spell?" +'\n' + "Yes or No     ")
        #global rSpellP1used
        if(rSpellP1used==False and m==1):
            #global CardSet2rSpell
            CardSet2rSpell=input("Round: "+str(round)+ '\n' +".Do "+CardSet2+ " want to use recursive spell? Yes or No     ")
#    global CardSet1gSpell    
    if(CardSet1gSpell=="Yes"):
        num = random.randrange(0,len(currentCardSet2),1)
        
        if(CardSet2rSpell=="Yes"):
            recSpell=random.randrange(0,len(outdatedList),1)
            currentCardSet2.insert(0,outdatedList[recSpell])
            CardSet1Choice=input(CardSet2 + " has opted for recursive spell after " + CardSet1 + " cast his God's spell." + '\n' + "Do " + CardSet1 +" want to continue to challenge the new card or want to go back to challenge the previously chosen card using God's spell?" + '\n' + "Hit 1 to continue and hit 0 to change back to previous")
            if(CardSet1Choice==0):
                num=num+1
            else:
                num=num
            if(playerFlag==True):
                rSpellP2used=True
            else:
                rSpellP1used=True
            CardSet2rSpell="No"
        if(playerFlag==True):
            gSpellP1used=True
        else:
            gSpellP2used=True           
        x = currentCardSet2[num]
        currentCardSet2.pop(num)
        currentCardSet2.insert(0,x)
        CardSet1gSpell="No"
        
    if(CardSet2rSpell=="Yes"):
        if(playerFlag==True):
            rSpellP2used=True
        else:
            rSpellP1used=True
        recSpell=random.randrange(0,len(outdatedList),1)
        currentCardSet2.insert(0,outdatedList[recSpell])
        CardSet2rSpell="No"
    if(CardSet1rSpell=="Yes"):
        if(playerFlag==True):
            rSpellP1used=True
        else:
            rSpellP2used=True
        recSpell=random.randrange(0,len(outdatedList),1)
        currentCardSet1.insert(0,outdatedList[recSpell])
        CardSet1rSpell="No"
        
    if(currentCardSet1[0].skills>currentCardSet2[0].skills):
        if(playerFlag==True):
#                global pointsP1
            pointsP1=pointsP1+1
        else:
#                global pointsP2
            pointsP2=pointsP2+1
    else:
        global xchangeFlag
        xchangeFlag = True
        if(playerFlag==True):
#                global pointsP2
            pointsP2=pointsP2+1
        else:
#                global pointsP1
            pointsP1=pointsP1+1
    outdatedList.insert(0,currentCardSet1[0])
    outdatedList.insert(0,currentCardSet2[0])
    del currentCardSet1[0]
    del currentCardSet2[0]
        
    if(playerFlag==True):
        print ("At the end of round "+ str(round) + "," + '\n' + CardSet1 + " score is " + str(pointsP1) + " and "+CardSet2+" score is "+ str(pointsP2)) 
    else:
        print ("At the end of round "+ str(round) + "," + '\n' + CardSet1 + " score is " + str(pointsP2) + " and "+CardSet2+" score is "+ str(pointsP1))
    m=1
    players=[currentCardSet1,currentCardSet2]
        
    return players

rules(currentCardSet1,currentCardSet2)

