import random
import time

NORTH = 1
WEST = 2
EAST = 3
SOUTH = 4

terrainList = ['P', 'M', 'W', 'S', 'H', 'D', 'F'] 
#Must take in a list
def initializeMap(gameMap):
    for i in range(len(gameMap)):
        for j in range(3):
            gameMap[i].append('X')

            
#Takes in a 2d list and prints it
def printMap(gameMap, playerX, playerY):
    for i in range(len(gameMap)):
        for j in range(len(gameMap[i])):
            if i == playerX and j == playerY:
                print('-', end='')
            else:
                print(gameMap[i][j], end='')
        print()



def travelWait():
    time.sleep(2)
    print("You begin to travel, taking time to note the landmarks and update your map.")
    time.sleep(2)



def newTile(gameMap, direction, playerX, playerY):
    nearby = []
    if direction == NORTH:
        nearby = [gameMap[playerX - 1][playerY],
                  gameMap[playerX - 1][playerY - 1],
                  gameMap[playerX - 1][playerY + 1]]
    elif direction == SOUTH:
        nearby = [gameMap[playerX + 1][playerY],
                  gameMap[playerX + 1][playerY - 1],
                  gameMap[playerX + 1][playerY + 1]]
    elif direction == WEST:
        nearby = [gameMap[playerX][playerY - 1],
                  gameMap[playerX + 1][playerY - 1],
                  gameMap[playerX - 1][playerY - 1]]
    elif direction == EAST:
        nearby = [gameMap[playerX][playerY + 1],
                  gameMap[playerX + 1][playerY + 1],
                  gameMap[playerX - 1][playerY + 1]]
    print(nearby)

    while 'X' in nearby:
        nearby.remove('X')
        
    nearby = nearby * 3
    print(nearby)
    
    
    weightedTerrain = nearby + terrainList
    tileIndex = random.randint(0, len(weightedTerrain) - 1)

    return weightedTerrain[tileIndex]


## Initialize the map
newMap = []
newMap.append([])
newMap.append([])
newMap.append([])
initializeMap(newMap)


playerIn = ''
#Init player position in middle of the map
position = [1,1]

rowSize = 0
columnSize = 0

while playerIn != '0':

    rowSize = len(newMap[position[0]])
    columnSize = len(newMap)
    
    printMap(newMap, position[0], position[1])
    print('''To navigate the map,
        1. To move north       3. To move east
        2. To move west        4. To move south

        9. For map information
        0. to quit (you will lose your map)''')

    playerIn = input()

    #---------------------NORTH-------------------------
    if playerIn == '1':
        if newMap[position[0] - 1][position[1]] == 'X':
            newMap[position[0] - 1][position[1]] = newTile(newMap, NORTH, position[0], position[1])

        #update position, move it one unit up
        position[0] = position[0] - 1
        #update map, add generation here later

        #newMap[position[0]][position[1]] = '-'


        #Adds more "fog" to the map if the player
        #approaches the known map boundary
        if (position[0]) == 0:
            newMap.insert(0, [])
            for i in range(rowSize):
                newMap[0].append('X')

            position[0] = position[0] + 1

        
            
    #---------------------WEST------------------------                
    elif playerIn == '2':
        if newMap[position[0]][position[1] - 1] == 'X':
            newMap[position[0]][position[1] - 1] = newTile(newMap, WEST, position[0], position[1])
        #update position, move it one unit left
        position[1] = position[1] - 1

        #newMap[position[0]][position[1]] = '-'
        
        #Adds more "fog" to the map if the player
        #approaches the known map boundary
        if (position[1]) == 0:
            
            for i in range(columnSize):
                newMap[i].insert(0,'X')

            position[1] = position[1] + 1

            
    #---------------------EAST-------------------------
    elif playerIn == '3':
        if newMap[position[0]][position[1] + 1] == 'X':
            newMap[position[0]][position[1] + 1] = newTile(newMap, EAST, position[0], position[1])
        #update position, move it one unit right
        position[1] = position[1] + 1

        #newMap[position[0]][position[1]] = '-'

        #Adds more "fog" to the map if the player
        #approaches the known map boundary
        if (position[1]) == (rowSize - 1):
            
            for i in range(columnSize):
                newMap[i].append('X')

            
    #---------------------SOUTH-------------------------
    elif playerIn == '4':
        if newMap[position[0] + 1][position[1]] == 'X':
            newMap[position[0] + 1][position[1]] = newTile(newMap, SOUTH, position[0], position[1])
        #update position, move it one unit down
        position[0] = position[0] + 1

        #newMap[position[0]][position[1]] = '-'

        #Adds more "fog" to the map if the player
        #approaches the known map boundary
        if (position[0]) == (columnSize - 1):
            newMap.append([])
            for i in range(rowSize):
                newMap[columnSize].append('X')
    elif playerIn == '9':
        print('''P = plains
M = mountains              H = hills
W = water                  D = desert
S = swamp                  F = forest

''')
        
    #travelWait()

    #print(position[0])
    #print(position[1])


    
    
