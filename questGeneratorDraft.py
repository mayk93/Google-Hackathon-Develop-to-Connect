#!/usr/bin/env python3

import soy
from time import sleep
import random
from random import *

client = soy.Client()
room = soy.scenes.Room(10)

room['cam'] = soy.bodies.Camera((0,0,10))
client.window.append(soy.widgets.Projector(room['cam']))

room['light'] = soy.bodies.Light((-2, 3, 5))

room['player'] = soy.bodies.Sphere()
room['player'].position = soy.atoms.Position((5, 1, 0))
room['player'].material = soy.materials.Colored('white')
room['player'].radius = 0.5

x11 = randint(-3, 3)
x12 = randint(-1, 1) 

x21 = randint(-3, 3)
x22 = randint(-1, 1) 

while x11==x21 or x12==x22:
        x21 = randint(-3, 3)
        x22 = randint(-1, 1)
        
target1 = [x11,x12]
target2 = [x21,x22]
targets = [target1,target2]

room['questTarget'] = soy.bodies.Sphere()
room['questTarget'].position = soy.atoms.Position((x11, x12, 0))
room['questTarget'].material = soy.materials.Colored('red')
room['questTarget'].radius = 0.5

room['questTarget2'] = soy.bodies.Sphere()
room['questTarget2'].position = soy.atoms.Position((x21, x22, 0))
room['questTarget2'].material = soy.materials.Colored('blue')
room['questTarget2'].radius = 0.5

qests = []
playerHasSomething = False

def generateSubQuest():
        subQuest = []
        questType = randint(0,1)
        #print('Type: ', questType)
        location = targets[randint(0,1)]
        #print('Location: ', targets[0],targets[1])
        subQuest.append(questType)
        subQuest.append(location)
        return subQuest
        
def generateQuest(numberOfSubquests):
        for i in range(0,numberOfSubquests):
                #print('Quest ',i)
                qests.append(generateSubQuest())

#def isNumber(s):
#   try:
#       float(s)
#       return True
#   except ValueError:
#       return False

#def move():
#       whereX = input('Chose where you go on X axis ')
#       whereY = input('Chose where you go on y axis ')
#       if isNumber(whereX) and isNumber(whereY):
#               room['player'].position = soy.atoms.Position((whereX, whereY, 0))
 
def move():
        room['player'].position = soy.atoms.Position((randint(-5,5), randint(-5,5), 0))
        
def checkIfQuestIsComplete():
        for i in range(0,2):
                questToCheck = qests[i]
                #print('Quest to Check ',questToCheck)
                qType = questToCheck[0]
                location = questToCheck[1]
                x = location[0]
                y = location[1]
                if qType == 0:
                        if room['player'].position ==  soy.atoms.Position((x, y, 0)):
                                playerHasSomething = True
                                print('You just completed a get-something quest')
                elif room['player'].position ==  soy.atoms.Position((x, y, 0)) and playerHasSomething == True:
                                playerHasSomething = False
                                print('You just completed a give-something quest')                                       
        
onlyOnce = True

if __name__ == '__main__' :
        while client.window :
                sleep(.5)
                if onlyOnce:
                        generateQuest(3)
                        onlyOnce = False
                        for i in range(0,2):
                                print('Quest: ', i+1 , qests[i])
                        print('A quest of type 0 means getting something.\n')
                        print('A quest of type 1 means giving something.\n')
                        print('The coordinates where you must go are given next to the quest type.\n')
                        print('Due to time constrains, you will wonder aimlessly.\n')
                        
                move()
                checkIfQuestIsComplete()                                
