import pygame
import sys
import random


class seeker(object):
    def __init__(self, posX, posY):
        self.position = [posX*GRIDSIZE, posY*GRIDSIZE]
        self.color = (17, 24, 47)

    def setPosition(self, newX, newY):
        self.position[0] = newX*GRIDSIZE
        self.position[1] = newY*GRIDSIZE

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


class hider(object):
    def __init__(self, posX, posY):
        self.position = [posX*GRIDSIZE, posY*GRIDSIZE]
        self.color = (223, 163, 49)

    def setPosition(self, newX, newY):
        self.position[0] = newX*GRIDSIZE
        self.position[1] = newY*GRIDSIZE

    def draw(self, surface):
        r = pygame.Rect(
            (self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)

class block(object):
    def __init__(self, posX, posY):
        self.position = [posX*GRIDSIZE, posY*GRIDSIZE]
        self.color = (0,225, 0)

    def setPosition(self, newX, newY):
        self.position[0] = newX*GRIDSIZE
        self.position[1] = newY*GRIDSIZE

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)


def DrawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x+y) % 2 == 0:
                r = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (93, 216, 228), r)
            else:
                rr = pygame.Rect((x*GRIDSIZE, y*GRIDSIZE),
                                 (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (84, 198, 205), rr)

def GameOver():
    while True:
        a = 0

def DFSRandom(board, curX, curY, directX, directY, count, surface, screen, clock, seeker, hider, check, block):
    # seeker.setPosition(curX, curY)
    # updateGameState(surface, screen, clock, seeker, hider, block)
    check = checkVision(directX, directY, curX, curY, board)
    if check[0] != -1:
        while curX < check[0]:
            curX+=1
            seeker.setPosition(curX, curY)
            updateGameState(surface, screen, clock, seeker, hider, block)
        while curX > check[0]:
            curX-=1
            seeker.setPosition(curX, curY)
            updateGameState(surface, screen, clock, seeker, hider, block)
        while curY < check[1]:
            curY+=1
            seeker.setPosition(curX, curY)
            updateGameState(surface, screen, clock, seeker, hider, block)
        while curY > check[1]:
            curY-=1
            seeker.setPosition(curX, curY)
            updateGameState(surface, screen, clock, seeker, hider, block)
        GameOver()

    if count[0] <= 5:
        for i in range(8):
            newY = curY+directY[i]
            newX = curX+directX[i]
            if newX < SCREEN_WIDTH/GRIDSIZE and newY < SCREEN_HEIGHT/GRIDSIZE and newX >= 0 and newY >= 0:
                if board[newY][newX] == -1:
                    board[newY][newX] = 1
                    count[0]+=1
                    DFSRandom(board, newX, newY, directX, directY, count, surface, screen, clock, seeker, hider, check, block)
                    if check[0] == True:
                        return
                    count[0]-=1
                    board[newY][newX] = -1
                    seeker.setPosition(curX, curY)
                    updateGameState(surface, screen, clock, seeker, hider, block)
                    
                elif board[newY][newX] == 2:
                    seeker.setPosition(newX, newY)
                    updateGameState(surface, screen, clock, seeker, hider, block)
                    GameOver()
    else: 
        count[0] = 0
        randDirectX = []
        randDirectY = []
        for i in range(8):
            randDirectX.insert(random.randint(0, 7), directX[i])
            randDirectY.insert(random.randint(0, 7), directY[i])
        for i in range(8):
            newY = curY+randDirectY[i]
            newX = curX+randDirectX[i]
            if newX < SCREEN_WIDTH/GRIDSIZE and newY < SCREEN_HEIGHT/GRIDSIZE and newX >= 0 and newY >= 0:
                if board[newY][newX] == -1:
                    board[newY][newX] = 1
                    count[0]+=1
                    DFSRandom(board, newX, newY, randDirectX, randDirectY, count, surface, screen, clock, seeker, hider, check, block)
                    if check[0] == True:
                        return
                    count[0]-=1
                    board[newY][newX] = -1
                    seeker.setPosition(curX, curY)
                    updateGameState(surface, screen, clock, seeker, hider, block)
                elif board[newY][newX] == 2:
                    seeker.setPosition(newX, newY)
                    updateGameState(surface, screen, clock, seeker, hider, block)
                    GameOver()

def checkVision(directX, directY, curX, curY, board):
    for i in range(3):
        for j in range(8):
            newX = curX + directX[j]
            newY = curY + directY[j]
            if directX[j] < 0:
                newX-=i
            else:
                newX+=i
            if directY[j] < 0:
                newY-=i
            else:
                newY+=i
            if newX < SCREEN_WIDTH/GRIDSIZE and newY < SCREEN_HEIGHT/GRIDSIZE and newX >= 0 and newY >= 0:
                if board[newY][newX] == 2: 
                    return [newX, newY]
                elif 
    return [-1, -1]

def updateGameState(surface, screen, clock, seeker, hider, block):
    clock.tick(10)
    DrawGrid(surface)
    seeker.draw(surface)
    hider.draw(surface)
    for i in range(len(block)):
        block[i].draw(surface)
    # handle events
    screen.blit(surface, (0, 0))
    pygame.display.update()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

GRIDSIZE = 20
GRID_WIDTH = SCREEN_HEIGHT / GRIDSIZE
GRID_HEIGHT = SCREEN_WIDTH / GRIDSIZE

def main():
    board = []
    for i in range(int(SCREEN_HEIGHT/GRIDSIZE)):
        tmp = []
        for j in range(int(SCREEN_WIDTH/GRIDSIZE)):
            tmp.insert(0, -1)
        board.insert(0, tmp)
    print(len(board))
    print(len(board[0]))

    posXSeeker = int(input("Seeker X: "))
    posYSeeker = int(input("Seeker Y: "))
    posXHider = int(input("Hider X: "))
    posYHider = int(input("Hider Y: "))
    numBlock = int(input("How many blocks you want: "))
    blocks = []
    for i in range(numBlock):
        posXBlock = int(input("Block X: "))
        posYBlock = int(input("Block y: "))
        blocks.insert(0, block(posXBlock, posYBlock))
        board[posYBlock][posXBlock] = 1

    print(blocks)
    
    board[posYHider][posXHider] = 2
    board[posYSeeker][posXSeeker] = 3

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()
    DrawGrid(surface)

    directX = [-4, 0, 4, 0, -4, 4, 4, -4]
    directY = [0, -4, 0, 4, -4, -4, 4, 4]

    newHider = hider(posXHider, posYHider)
    newSeeker = seeker(posXSeeker, posYSeeker)

    # newHider = hider(0, 0)
    # newSeeker = seeker(10, 10)
    # while True:
    #     updateGameState(surface, screen, clock, newSeeker, newHider)

    count = [0]
    check = [False]
    point = [100]

    myFont = pygame.font.SysFont("monospace", 16)

    while (True):
        DFSRandom(board, posXSeeker, posYSeeker, directX, directY, count, surface, screen, clock, newSeeker, newHider, check, blocks)

main()
