import pygame
import pickle

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
LEAST_DISPLAY_WIDTH = 0
MAX_DISPLAY_WIDTH = 800
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PURPLE = (255, 0, 255)
DIRT = (0, 0, 16, 16)
GREEN = (34,139,34)
YELLOW = (255,255,51)
BROWN = (210,180,140)
BLUE = (0, 255, 255)

pygame.init()
size = (DISPLAY_WIDTH, DISPLAY_WIDTH)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game_exit = False

class Graph(object):
    def __init__(self, rows=None, columns=None):
        self.rows = rows
        self.columns = columns
        self.grid = []

    def make_graph(self):
        for rows in range(self.rows):
            self.grid.append([])
            for columns in range(self.columns):
                self.grid[rows].append(0)
        return self.grid

class Tile(object):
    def __init__(self, width=None, height=None, color=None, loadedimage=None):
        self.width = width
        self.height = height
        self.color = color
        self.image = pygame.Surface((self.width, self.height))
        if self.color != None:
            self.image.fill(self.color)
        self.loadedimage = loadedimage
        if self.loadedimage != None:
            self.image = pygame.image.load(str(loadedimage))
            self.rect = self.image.get_rect()
            self.width = self.rect.x
            self.height = self.rect.y
        self.image.convert()
        self.rect = self.image.get_rect()


graph = Graph(rows=60, columns=80)
graph.make_graph()


# with open("savegame", "rb") as f:
#     graph = pickle.load(f)


while not game_exit:
    for row in range(graph.rows):
        for column in range(graph.columns):
            if graph.grid[row][column] == 0:
                color = WHITE
                tile = Tile(width=20, height=20, color=color)
            elif graph.grid[row][column] == 1:
                color = None
                tile = Tile(width=20, height=20, color=None, loadedimage="poro.png")
                # print tile.rect.x, tile.rect.y
            elif graph.grid[row][column] == 2:
                color = BLUE
                tile = Tile(width=20, height=20, color=color)
            elif graph.grid[row][column] == 3:
                color = GREEN
                tile = Tile(width=20, height=20, color=color)
            elif graph.grid[row][column] == 4:
                color = BROWN
                tile = Tile(width=20, height=20, color=color)
            elif graph.grid[row][column] == 5:
                color = YELLOW
                tile = Tile(width=20, height=20, color=color)
            elif graph.grid[row][column] == 6:
                color = BLACK
                tile = Tile(width=20, height=20, color=color)
            screen.blit(tile.image, ((tile.width*column),(tile.height*row)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_exit = True

        if event.type == pygame.KEYDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // tile.width
            row = pos[1] // tile.height
            if event.key == pygame.K_a:
                graph.grid[row][column] = 1
                print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                pos, row,column)
            if event.key == pygame.K_s:
                graph.grid[row][column] = 2
                print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                pos, row,column)
            if event.key == pygame.K_d:
                graph.grid[row][column] = 3
                print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                pos, row,column)
            if event.key == pygame.K_f:
                graph.grid[row][column] = 4
                print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                pos, row,column)
            if event.key == pygame.K_g:
                graph.grid[row][column] = 5
                print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                pos, row,column)
            if event.key == pygame.K_h:
                graph.grid[row][column] = 6
                print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                pos, row,column)

    clock.tick(60)
    pygame.display.flip()

# with open("savegame", "wb") as f:
#     pickle.dump(graph, f)

print graph.grid
pygame.quit()
