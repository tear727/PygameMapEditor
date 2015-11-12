import pygame
import pickle
import os

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
    def __init__(self, width=None, height=None, solid=None, color=None, loadedimage=None):
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
            self.width = self.rect.width
            self.height = self.rect.height
        self.image.convert()
        self.rect = self.image.get_rect()
        self.solid = solid

def paused(pause):
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    pause = False
        clock.tick(60)

graph = Graph(rows=60, columns=80)
graph.make_graph()

def save(arg):
    with open("savegame", "wb") as f:
        pickle.dump(arg, f)
        print "file saved"

def delete_save():
    answer = raw_input("Are you sure you want to delete the save file? y/n\n").lower()
    if answer == "y":
        os.remove("savegame")
    elif answer == "n":
        print "resuming"
    else:
        print "choose y or n"

if os.path.exists("savegame"):
    with open("savegame", "rb") as f:
        graph = pickle.load(f)
screen.fill(WHITE)

while not game_exit:
    for row in range(graph.rows):
        for column in range(graph.columns):
            if graph.grid[row][column] == 0:
                color = WHITE
                tile = Tile(width=50, height=50, color=color)
            elif graph.grid[row][column] == 1:
                color = PURPLE
                tile = Tile(width=50, height=50, color=None, loadedimage="poro.png")
                # print tile.rect.x, tile.rect.y
            elif graph.grid[row][column] == 2:
                color = BLUE
                tile = Tile(width=50, height=50, color=color)
            elif graph.grid[row][column] == 3:
                color = GREEN
                tile = Tile(width=50, height=50, color=color)
            elif graph.grid[row][column] == 4:
                color = BROWN
                tile = Tile(width=50, height=50, color=color)
            elif graph.grid[row][column] == 5:
                color = YELLOW
                tile = Tile(width=50, height=50, color=color)
            elif graph.grid[row][column] == 6:
                color = BLACK
                tile = Tile(width=50, height=50, color=color)
            screen.blit(tile.image, ((tile.width*column),(tile.height*row)))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            prompt = raw_input("Exit? Unsaved chaned will be lost.\ny/n\n").lower()
            if prompt == "y":
                game_exit = True
            elif prompt == "n":
                print "resuming"

        if event.type == pygame.KEYDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // tile.width
            row = pos[1] // tile.height
            if event.key == pygame.K_p:
                pause = True
                paused(pause)
            if event.key == pygame.K_t:
                save(graph)
            if event.key == pygame.K_BACKSPACE:
                delete_save()

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

pygame.quit()
