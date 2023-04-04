from sys import exit
from buttonClass import Button
from tileClass import Tile
from windowClass import Window
from shapes import Picture
import pygame
import time
import math


class App:
    def __init__(self):
        self.gameState = 'main screen'

    def pygame_event_handler(self):
        screen.fill((0, 0, 0))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        if self.gameState != 'main screen':
            if keys[pygame.K_LCTRL] and keys[pygame.K_r]:
                self.gameState = 'main screen'

    def button_events_handler(self):
        global subWindow
        if tileMapButton.clickStage:
            tileMapButton.clickStage = None
            tileMapButton.held = False
            self.gameState = 'tile map maker'

        if butterFlyEffectButton.clickStage:
            butterFlyEffectButton.clickStage = None
            butterFlyEffectButton.held = False
            self.gameState = 'butterfly physics'


if __name__ == '__main__':
    app = App()
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
    WIDTH, HEIGHT = screen.get_width(), screen.get_height()
    clock = pygame.time.Clock()
    FPS = 60
    previousTime = time.time()

    selectorsTxtProperties = {
        'font': 'comicsansms',
        'size': 15,
        'bald': True,
        'italic': True,
        'txt': "PROJECT NAME",
        'antialias': True,
        'color': (255, 255, 255),
    }
    tileMapButton = Button((100, 75), 100, 100, (255, 0, 126), selectorsTxtProperties, True, 'TileMapMaker')
    butterFlyEffectButton = Button((250, 75), 100, 100, (255, 0, 126), selectorsTxtProperties, True, 'ButterFlyPhysics')
    [Button((250, 75), 100, 100, (255, 0, 126), selectorsTxtProperties, True, 'ButterFlyPhysics') for _ in range(0, 40)]

    # For tile map
    size = 50
    gridColor = (0, 200, 150)
    tileMap = Tile.tile_map(0, 0, WIDTH, HEIGHT, size, size, (255, 255, 255))
    subWindow = Window((0, HEIGHT), 500, 500)

    # For butterfly effect
    circlePic = Picture((WIDTH/2, HEIGHT/2), 'resources/circle.png')
    circles = []



    # For mouse
    mouseSurf = pygame.Surface((10, 10))
    mouseSurf.fill((255, 255, 255))
    mouseMask = pygame.mask.from_surface(mouseSurf)

    while 1:
        keys = pygame.key.get_pressed()
        nowTime = time.time()
        speedCallibaration = (nowTime - previousTime) * FPS
        previousTime = nowTime
        mousePos = pygame.mouse.get_pos()
        app.pygame_event_handler()


        if app.gameState == 'main screen':
            app.button_events_handler()
            for button in Button.buttons:
                button.update(screen)

        elif app.gameState == 'tile map maker':
            Tile.draw_grid(screen, 0, 0, WIDTH, HEIGHT, size, size, gridColor)
            subWindow.update(screen)

        elif app.gameState == 'butterfly physics':
            if circlePic.mask.overlap(mouseMask, (mousePos[0] - circlePic.rect.x, mousePos[1] - circlePic.rect.y)):
                mouseSurf.fill((255, 0, 0))
            else:
                mouseSurf.fill((0, 0, 255))
            circlePic.draw(screen)

        screen.blit(mouseSurf, mousePos)
        pygame.display.update()
