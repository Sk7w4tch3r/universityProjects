import pygame


class GUI:
    pixelWidth, pixelHeight, page, cubeSize, colors = 0, 0, 0, 0, []

    def __init__(self, cubeSize, delay, state):
        self.delay=delay
        w   = len(state.map_array[0])
        h   = len(state.map_array)
        rock    = (90, 90, 90)      # gray
        hole    = (0, 0, 0)         # black
        empty   = (255, 255, 255)   # white
        box     = (255, 255, 0)     # yellow
        agent   = (255, 0, 0)     # red
        self.colors=[rock, hole, empty, box, agent]
        self.cubeSize = cubeSize
        self.pixelWidth, self.pixelHeight = w * self.cubeSize+w-1, h * self.cubeSize+h-1
        self.page = pygame.display.set_mode((self.pixelWidth, self.pixelHeight+2*self.cubeSize))
        self.redrawPage(state)

    def redrawPage(self, game):
        mapArr=game.map_array[:-1]
        self.page.fill((0,0,0))
        self.drawTile(mapArr)
        self.drawScores(game)
        pygame.display.update()
        pygame.time.delay(self.delay)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

    def drawTile(self, array):
        for i, a in enumerate(array):
            for j, tile in enumerate(a):
                self.colorCube(j, i, self.colors[tile+2])

    def drawScores(self, state):
        panelColor  = (255,255,255)
        pygame.draw.rect(self.page, panelColor, (0,self.pixelHeight , self.pixelWidth, 2*self.cubeSize))
        pygame.font.init()
        font        = pygame.font.SysFont('arial', self.cubeSize)

        textColor       = (0,0,0)
        text            = "score: " + str(state.cost)
        text_surface    = font.render(text, True, textColor)

        self.page.blit(text_surface, (self.cubeSize//3, self.pixelHeight+self.cubeSize//3))

        pygame.display.update()

    def colorCube(self, i, j, color):
        pygame.draw.rect(self.page, color, (self.pixelPos(i), self.pixelPos(j), self.cubeSize, self.cubeSize))

    def pixelPos(self, i):
        return i * self.cubeSize + i
