from sys import exit
from buttonClass import Button
from tileClass import Tile
from windowClass import Window
import pygame, math, time


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
            self.gameState = 'tile map maker'
            subWindow = Window((WIDTH/2, HEIGHT/2), 500, 500)



if __name__ == '__main__':
    app = App()

    screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
    WIDTH, HEIGHT = screen.get_width(), screen.get_height()
    clock = pygame.time.Clock()
    FPS = 60
    previousTime = time.time()

    tileMapButton = {
        'font': 'comicsansms',
        'size': 25,
        'bald': True,
        'italic': True,
        'txt': "TileMapMaker",
        'antialias': True,
        'color': (255, 255, 255),
    }
    tileMapButton = Button((100, 75), 100, 100, (255, 0, 126), tileMapButton, True)

    size = 50
    gridColor = (0, 200, 150)
    tileMap = Tile.tile_map(200, 200, 400, 400, size, size, (255, 255, 255))
    subWindow = None
    while 1:
        keys = pygame.key.get_pressed()
        nowTime = time.time()
        speedCallibaration = (nowTime - previousTime) * FPS
        previousTime = nowTime

        app.pygame_event_handler()

        if app.gameState == 'main screen':
            app.button_events_handler()
            for button in Button.buttons:
                button.update(screen)

        elif app.gameState == 'tile map maker':

            Tile.draw_grid(screen, 0, 0, WIDTH, HEIGHT, size, size, gridColor)
            subWindow.update(screen)



        pygame.display.update()
