from sys import exit
from buttonClass import Button
import pygame, math, time


class App:
    @staticmethod
    def event_handler():
        screen.fill((0, 0, 0))
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()




if __name__ == '__main__':
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
    demo = Button((100, 75), 100, 100, (255, 0, 126), tileMapButton, True)

    while 1:
        nowTime = time.time()
        speedCallibaration = (nowTime - previousTime) * FPS
        previousTime = nowTime
        App.event_handler()

        for button in Button.buttons:
            button.update(screen)

        pygame.display.update()
