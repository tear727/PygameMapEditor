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
PORO = "poro.png"


TILE_WIDTH = 50
TILE_HEIGHT = 50


pygame.init()
size = (DISPLAY_WIDTH, DISPLAY_WIDTH)
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
background = pygame.Surface((200, 150))
pygame.draw.rect(background,(0,255,255),(0,0,200,200))

FONT = pygame.font.Font(None, 32)

class Entity(pygame.sprite.Sprite):
	"""Base Entity class that provides Sprite class inheritance for subclasses"""
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)


class Controller(object):
    def __init__(self, name):
        self.name = name
        #these will keep track of how far the graph has moved overall
        self.x_offset, self.y_offset = 0, 0
        #these will hold the current mouse position relative to the graph
        self.graph_x, self.graph_y = 0, 0
        self.terrain_keys = {
                pygame.K_a: 1,
                pygame.K_s: 2,
                pygame.K_d: 3,
                pygame.K_f: 4,
                pygame.K_g: 5,
                pygame.K_h: 6,
                pygame.K_j: 7}
        self.game_exit = False

    def __str__(self):
        return unicode(self.name)

    def update_controller(self):
        self.keyboard()
        self.mouse()

    def mouse(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        offset = [0, 0]
        if mouse_x > 770:
            offset[0] = -75 #700 - mouse_x
        elif mouse_x < 30:
            offset[0] = 75 #30 - mouse_x
        if mouse_y > 770:
            offset[1] = -75 #700 - mouse_y
        elif mouse_y < 30:
            offset[1] = 75 #30 - mouse_y
        graph.shift_graph(*offset)
        self.x_offset -= offset[0]
        self.y_offset -= offset[1]
        self.graph_x = mouse_x + self.x_offset
        self.graph_y = mouse_y + self.y_offset

    def keyboard(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                prompt = "Exit? Unsaved chaned will be lost. y/n"
                ok = confirmation_prompt(prompt)
                if ok:
                    self.game_exit = True
                else:
                    print "resuming"

            if event.type == pygame.KEYDOWN:
                column = self.graph_x // TILE_HEIGHT
                row = self.graph_y // TILE_WIDTH
                if event.key == pygame.K_p:
                    pause = True
                    paused(pause)
                if event.key == pygame.K_t:
                    save(graph)
                if event.key == pygame.K_BACKSPACE:
                    delete_save()
                #check if current cell is in grid first (careful of negative indices, they're valid but incorrect)
                bad_column = not (0 <= column <= graph.columns - 1)
                bad_row = not (0 <= row <= graph.rows - 1)
                if bad_column or bad_row:
                    return
                try:
                    terrain_num = self.terrain_keys[event.key]
                    graph.grid[column][row] = terrain_num
                    print "Position: {0}, Grid Coordinates: {1}, {2}".format(
                            pygame.mouse.get_pos(), column, row)
                except KeyError:
                    pass


class Graph(object):
    def __init__(self, rows=None, columns=None, scale_factor=None, grid=None):
        self.rows = rows
        self.columns = columns
        if grid != None:
            self.grid = grid
        else:
            self.grid = []
        self.graph_shift_x = 0
        self.graph_shift_y = 0
        self.terrain_colors = {
                0: WHITE,
                1: PURPLE,
                2: BLUE,
                3: GREEN,
                4: BROWN,
                5: YELLOW,
                6: BLACK,
                7: PORO 
        }
        self.scale_factor = scale_factor    

    def set_scale_factor(self, scale_factor=None):
        self.scale_factor = scale_factor

    def graph_update(self, minimap=None):
        for column in range(self.columns):
            for row in range(self.rows):
                color = self.terrain_colors[self.grid[column][row]]
                if type(color) == str:
                    tile = Tile(width=(TILE_WIDTH), height=(TILE_HEIGHT), loadedimage=color)
                else:
                    tile = Tile(width=(TILE_WIDTH), height=(TILE_HEIGHT), color=color)
                screen.blit(tile.image, (((TILE_WIDTH)*column)+self.graph_shift_x,((TILE_HEIGHT)*row)+self.graph_shift_y))


    def make_graph(self):
        for x in range(self.columns):
            self.grid.append([0] * self.rows)
        return self.grid

    def shift_graph(self, shift_x, shift_y):
        "Shifts graph"
        self.graph_shift_x += shift_x
        self.graph_shift_y += shift_y

    def copy(self):
        return self.grid


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
            self.image = pygame.image.load(loadedimage)
            self.rect = self.image.get_rect()
            self.width = self.rect.width
            self.height = self.rect.height
        self.image.convert()
        self.rect = self.image.get_rect()
        self.solid = solid


class MiniMap(object):
    def __init__(self, width=None, height=None, graph=None):
        self.width = width
        self.height = height
        self.graph = graph
        self.grid = graph.copy()
        self.pos = (200, 150)
        self.terrain_colors = {
                0: WHITE,
                1: PURPLE,
                2: BLUE,
                3: GREEN,
                4: BROWN,
                5: YELLOW,
                6: BLACK,
                7: PORO 
        }

    def scale_graph(self, scale_factor=None):
        if graph != None:
            self.graph.set_scale_factor(scale_factor)

    def minimap_update(self, graph=None):
        self.grid = graph.copy()
        print self.grid
        # for column in range(80):
        #     for row in range(60):
        #         color = self.terrain_colors[self.grid[column][row]]
        #         print "color: ", color
        #         pygame.draw.rect(background, color, (row,column,row,column))
        screen.blit(background, (0,0))

def paused(pause):
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    pause = False
        clock.tick(60)

def confirmation_prompt(prompt_text):
    msg = FONT.render(prompt_text, True, pygame.Color("gray80"), pygame.Color("gray20"))
    msg_rect = msg.get_rect(center=(DISPLAY_WIDTH//2, DISPLAY_HEIGHT//2))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                else:
                    return False
        screen.blit(msg, msg_rect)
        pygame.display.update()

def save(arg):
    with open("savegame", "wb") as f:
        cPickle.dump(arg, f)
        print "file saved"

def delete_save():
    prompt = "Are you sure you want to delete the save file? y/n\n"
    ok = confirmation_prompt(prompt)
    if ok:
        os.remove("savegame")
    else:
        print "resuming"

try:
	if os.path.exists("savegame"):
		with open("savegame", "rb") as f:
			graph = cPickle.load(f)
except:
    EOFError()

"""Instantiations"""

controller = Controller("controller1")
graph = Graph(rows=60, columns=80, scale_factor=4)
graph.make_graph()
print graph.graph_shift_x
print graph.grid
mini_map = MiniMap(graph=graph)

while not controller.game_exit:
    screen.fill(WHITE)
    graph.graph_update(minimap=background)
    mini_map.minimap_update(graph)
    controller.update_controller()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
