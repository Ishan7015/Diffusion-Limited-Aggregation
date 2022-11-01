import random
from tkinter.tix import Tree
import numpy as np
import pygame


class Application:

    def __init__(self):
        self.size = self.width, self.height = 1000, 1000
        self.startX, self.startY = round(self.width/2), round(self.height/2)
        self.X, self.Y = self.startX, self.startY
        self.displaySurface = None
        self.pixelArray = None
        self.pixelColor = None

    def on_init(self):
        pygame.init()
        pygame.display.set_caption("Diffuion-limited Aggregation")
        self.displaySurface = pygame.display.set_mode(self.size)
        self.pixelArray = pygame.PixelArray(self.displaySurface)
        self.pixelColor = (255, 0, 0)
        self.isRunning = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.isRunning = False

    def on_loop(self):
        newDirection = random.choice(((0, 1), (0, -1), (1, 0), (-1, 0)))
        dX, dY = newDirection
        self.X += dX
        self.Y += dY

        if (self.X < 0):
            self.X = 0
        if (self.X > self.width-1):
            self.X = self.width-1
        if (self.Y < 0):
            self.Y = 0
        if (self.Y > self.height-1):
            self.Y = self.height-1

        if (self.pixelArray[self.X, self.Y] == 0xFF0000):
            self.pixelColor = (255, 255, 0)
            print(True)
        else:
            self.pixelColor = (255, 0, 0)

    def on_render(self):
        self.pixelArray[self.X, self.Y] = self.pixelColor

        pygame.display.update()

    def on_execute(self):
        if self.on_init() == False:
            self.isRunning = False

        while self.isRunning:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            self.on_render()

        pygame.quit()


if __name__ == "__main__":
    t = Application()
    t.on_execute()
