from Tkinter import *
import pygame
import random
import os
global playing
playing=False
def playpause():
    global playing
    if playing==True:
        playing=False
    else:
        playing=True
root = Tk()
embed = Frame(root, width=640, height=480)
embed.grid(row=0,column=2)
playpausebutton=Button(root, command=playpause, text="Play/Pause")
playpausebutton.grid(row=1,column=2)
root.update()
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
# os.environ['SDL_VIDEODRIVER'] = 'windib'
pygame.display.init()
screen = pygame.display.set_mode((640,480))
pygame.display.flip()
while True:
    #your code here
    if playing:
            screen.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    pygame.display.flip()
    root.update()
