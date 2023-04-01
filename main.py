from sys import exit
from buttonClass import Button
import pygame, math, time

screen = pygame.display.set_mode((0, 0), flags=pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_width(), screen.get_height()
clock = pygame.time.Clock()


demoDict = {
    'font': 'comicsansms',
    'size': 25,
    'bald': True,
    'italic': True,
    'txt': "A demo button",
    'antialias': True,
    'color': (255, 255, 255),
    'pos': (WIDTH / 2, HEIGHT / 2 + 75)
}
demo = Button((WIDTH / 2, HEIGHT / 2), 100, 100, (255, 0, 126), demoDict)


def mainloop():
    FPS = 60
    previousTime = time.time()
    while 1:
        nowTime = time.time()
        speedCallibaration = (nowTime - previousTime) * FPS
        previousTime = nowTime

        screen.fill((0, 0, 0))
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

        demo.update(screen)

        pygame.display.update()


if __name__ == '__main__':
    mainloop()
