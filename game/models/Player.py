import pygame
from game.resourses.Const import *

class Player():

    def __init__(self):
        self.direction = RIGHT
        self.state = ALIVE
        self.position = [START_X, START_Y, RIGHT]
        self.name = 'Egor'
        self.image_pack = ['../../data/archerr', '../../data/archerd', '../../data/archerl', '../../data/archeru']
        self.images = []
        for image in self.image_pack:
            temp = pygame.image.load(image).covert_alpha()