import pygame


class WindowBar:
    def __init__(self, pos, width, height, color):
        self.surf = pygame.Surface((width, height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(topleft=pos)

    def draw(self, draw_surf):
        draw_surf.blit(self.surf, self.rect)


class Window:
    def __init__(self, pos, width, height):
        self.surf = pygame.Surface((width, height))
        self.surf.fill((125, 125, 67))
        self.rect = self.surf.get_rect(center=pos)
        self.dragPos = pos
        self.mousex_in_rect = 0
        self.mousey_in_rect = 0

        self.topBar = WindowBar(self.rect.topleft, width, height/100 * 5, (255, 255, 255))
        self.hold = False

    def draw(self, draw_surf):
        draw_surf.blit(self.surf, self.rect)
        self.topBar.draw(draw_surf)

    def logic(self):
        mouse_pos = pygame.mouse.get_pos()

        if self.topBar.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            self.hold = True
        if not pygame.mouse.get_pressed()[0]:
            self.hold = False
        if self.topBar.rect.collidepoint(pygame.mouse.get_pos()) and not pygame.mouse.get_pressed()[0]:
            self.mousex_in_rect = self.rect.right - self.rect.left - (self.rect.right - mouse_pos[0])
            self.mousey_in_rect = self.rect.bottom - self.rect.top - (self.rect.bottom - mouse_pos[1])
            self.dragPos = pygame.mouse.get_pos()

        if self.hold:
            self.rect.x = self.dragPos[0] + (mouse_pos[0] - self.dragPos[0]) - self.mousex_in_rect
            self.rect.y = self.dragPos[1] + (mouse_pos[1] - self.dragPos[1]) - self.mousey_in_rect

        self.topBar.rect.topleft = self.rect.topleft

    def update(self, draw_surf):
        self.logic()
        self.draw(draw_surf)
