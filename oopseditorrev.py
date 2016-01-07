import pygame
import cPickle
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

TILE_WIDTH = 50
TILE_HEIGHT = 50


pygame.init()
size = (DISPLAY_WIDTH, DISPLAY_WIDTH)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
game_exit = False


class Entity(pygame.sprite.Sprite):
	"""Base Entity class that provides Sprite class inheritance for subclasses"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)


class Controller(object):
    def __init__(self, name):
        self.name = name
        self.mouse_pos = None
        self.mouse_x = 0
        self.mouse_y = 0

    def __str__(self):
        return unicode(self.name)

    def update_controller(self):
        self.keyboard()
        self.mouse()

    def mouse(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_x = self.mouse_pos[0]
        self.mouse_y = self.mouse_pos[1]

    def shift_mouse(self, shift_x, shift_y):
        "Handles mouse shift"
        self.mouse_x += shift_x
        self.mouse_y += shift_y
        print self.mouse_x, self.mouse_y

    def keyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                prompt = raw_input("Exit? Unsaved chaned will be lost.\ny/n\n").lower()
                if prompt == "y":
                    game_exit = True
                elif prompt == "n":
                    print "resuming"

            if event.type == pygame.KEYDOWN:
                column = self.mouse_x // TILE_HEIGHT
                row = self.mouse_y // TILE_WIDTH
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
                    self.mouse_pos, row,column)
                if event.key == pygame.K_s:
                    graph.grid[row][column] = 2
                    print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                    self.mouse_pos, row,column)
                if event.key == pygame.K_d:
                    graph.grid[row][column] = 3
                    print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                    self.mouse_pos, row,column)
                if event.key == pygame.K_f:
                    graph.grid[row][column] = 4
                    print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                    self.mouse_pos, row,column)
                if event.key == pygame.K_g:
                    graph.grid[row][column] = 5
                    print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                    self.mouse_pos, row,column)
                if event.key == pygame.K_h:
                    graph.grid[row][column] = 6
                    print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                    self.mouse_pos, row,column)



class Graph(object):
    def __init__(self, rows=None, columns=None):
        self.rows = rows
        self.columns = columns
        self.grid = []
        self.graph_shift_x = 0
        self.graph_shift_y = 0

    def graph_update(self):
        for row in range(graph.rows):
            for column in range(graph.columns):
                if self.grid[row][column] == 0:
                    color = WHITE
                    tile = Tile(width=TILE_WIDTH, height=TILE_HEIGHT, color=color)
                elif self.grid[row][column] == 1:
                    color = PURPLE
                    tile = Tile(width=TILE_WIDTH, height=TILE_HEIGHT, color=None, loadedimage="poro.png")
                    # print tile.rect.x, tile.rect.y
                elif self.grid[row][column] == 2:
                    color = BLUE
                    tile = Tile(width=TILE_WIDTH, height=TILE_HEIGHT, color=color)
                elif self.grid[row][column] == 3:
                    color = GREEN
                    tile = Tile(width=TILE_WIDTH, height=TILE_HEIGHT, color=color)
                elif self.grid[row][column] == 4:
                    color = BROWN
                    tile = Tile(width=TILE_WIDTH, height=TILE_HEIGHT, color=color)
                elif self.grid[row][column] == 5:
                    color = YELLOW
                    tile = Tile(width=TILE_WIDTH, height=TILE_HEIGHT, color=color)
                elif self.grid[row][column] == 6:
                    color = BLACK
                    tile = Tile(width=TILE_WIDTH, height=TILE_HEIGHT, color=color)
                screen.blit(tile.image, ((TILE_WIDTH*column)+self.graph_shift_x,(TILE_HEIGHT*row)+self.graph_shift_y))

    def make_graph(self):
        for rows in range(self.rows):
            self.grid.append([])
            for columns in range(self.columns):
                self.grid[rows].append(0)
        return self.grid

    def shift_graph(self, shift_x, shift_y):
        "Shifts graph"
        self.graph_shift_x += shift_x
        self.graph_shift_y += shift_y


class Tile(Entity):
    def __init__(self, width=None, height=None, solid=None, color=None, loadedimage=None):
        Entity.__init__(self)
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

controller = Controller("controller1")
graph = Graph(rows=60, columns=80)
graph.make_graph()
print graph.graph_shift_x

tile_group = pygame.sprite.Group()



def save(arg):
    with open("savegame", "wb") as f:
        cPickle.dump(arg, f)
        print "file saved"

def delete_save():
    answer = raw_input("Are you sure you want to delete the save file? y/n\n").lower()
    if answer == "y":
        os.remove("savegame")
    elif answer == "n":
        print "resuming"
    else:
        print "choose y or n"

try:
	if os.path.exists("savegame"):
		with open("savegame", "rb") as f:
			graph = cPickle.load(f)
except:
    EOFError()

print graph.grid

while not game_exit:
    screen.fill(WHITE)
    graph.graph_update()
    controller.update_controller()

    if controller.mouse_x > 700:
        diff = controller.mouse_x - 700
        #print diff, "mouse_x greater than 700"
        graph.shift_graph(-diff, 0)
        #controller.shift_mouse(diff, 0)
    if controller.mouse_x < 30:
        diff = 30 - controller.mouse_x
        #print diff, "mouse_x less than 30"
        graph.shift_graph(diff, 0)
        # controller.shift_mouse(diff, 0)
    if controller.mouse_y > 700:
        diff = controller.mouse_y - 700
        #print diff, "mouse_y greater than 700"
        graph.shift_graph(0, -diff)
        # controller.shift_mouse(0, diff)
    if controller.mouse_y < 30:
        diff = 30 - controller.mouse_y
        #print diff, "mouse_y less than 30"
        graph.shift_graph(0, diff)
        # controller.shift_mouse(0, -diff)



    # for event in pygame.event.get():
    #     if event.type == pygame.QUIT:
    #         prompt = raw_input("Exit? Unsaved chaned will be lost.\ny/n\n").lower()
    #         if prompt == "y":
    #             game_exit = True
    #         elif prompt == "n":
    #             print "resuming"
    #
    #     if event.type == pygame.KEYDOWN:
    #         pos = pygame.mouse.get_pos()
    #         column = pos[0] // tile.width
    #         row = pos[1] // tile.height
    #         if event.key == pygame.K_p:
    #             pause = True
    #             paused(pause)
    #         if event.key == pygame.K_t:
    #             save(graph)
    #         if event.key == pygame.K_BACKSPACE:
    #             delete_save()
    #
    #         if event.key == pygame.K_a:
    #             graph.grid[row][column] = 1
    #             print "Position: {0}, Grid Coordinates: {1}, {2}".format(
    #             pos, row,column)
    #         if event.key == pygame.K_s:
    #             graph.grid[row][column] = 2
    #             print "Position: {0}, Grid Coordinates: {1}, {2}".format(
    #             pos, row,column)
    #         if event.key == pygame.K_d:
    #             graph.grid[row][column] = 3
    #             print "Position: {0}, Grid Coordinates: {1}, {2}".format(
    #             pos, row,column)
    #         if event.key == pygame.K_f:
    #             graph.grid[row][column] = 4
    #             print "Position: {0}, Grid Coordinates: {1}, {2}".format(
    #             pos, row,column)
    #         if event.key == pygame.K_g:
    #             graph.grid[row][column] = 5
    #             print "Position: {0}, Grid Coordinates: {1}, {2}".format(
    #             pos, row,column)
    #         if event.key == pygame.K_h:
    #             graph.grid[row][column] = 6
    #             print "Position: {0}, Grid Coordinates: {1}, {2}".format(
    #             pos, row,column)
    #
    # for row in range(graph.rows):
    #     for column in range(graph.columns):
    #         if graph.grid[row][column] == 0:
    #             color = WHITE
    #             tile = Tile(width=50, height=50, color=color)
    #         elif graph.grid[row][column] == 1:
    #             color = PURPLE
    #             tile = Tile(width=50, height=50, color=None, loadedimage="poro.png")
    #             # print tile.rect.x, tile.rect.y
    #         elif graph.grid[row][column] == 2:
    #             color = BLUE
    #             tile = Tile(width=50, height=50, color=color)
    #         elif graph.grid[row][column] == 3:
    #             color = GREEN
    #             tile = Tile(width=50, height=50, color=color)
    #         elif graph.grid[row][column] == 4:
    #             color = BROWN
    #             tile = Tile(width=50, height=50, color=color)
    #         elif graph.grid[row][column] == 5:
    #             color = YELLOW
    #             tile = Tile(width=50, height=50, color=color)
    #         elif graph.grid[row][column] == 6:
    #             color = BLACK
    #             tile = Tile(width=50, height=50, color=color)
    #         screen.blit(tile.image, ((tile.width*column),(tile.height*row)))
    #
    # print graph.graph_shift_x, graph.graph_shift_y

    clock.tick(60)
    pygame.display.flip()

pygame.quit()
