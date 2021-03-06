import pygame
from game.resourses.Const import *

class Main():
    def __init__(self, screen):
        self.screen = screen
        self.background = pygame.image.load('1.jpg')
        self.running = True
        self.main_loop()

    def render(self):
        self.screen.blit(self.background, (0,0))
        pygame.display.flip()
        pass

    def main_loop(self):
        while self.running == True:
            self.render()

    def handle_events(self):
        pass


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
game = Main(screen)