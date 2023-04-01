import pygame
from txtFuncs import create_txt

pygame.init()


class Button:
    buttons = []

    def __init__(self, pos, width, height, color, txt_properties: dict = None, selector_button: bool = False):
        self.surf = pygame.Surface((width, height))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=pos)
        self.clickStage = None

        if txt_properties is not None:
            self.txtProperties = txt_properties
            if selector_button:
                txt_properties['pos'] = (self.rect.centerx, self.rect.centery + 75)
            self.txtSurf, self.txtRect = create_txt(txt_properties.get('font'), txt_properties.get('size', 0),
                                                    txt_properties.get('bald', False),
                                                    txt_properties.get('italic', False), txt_properties.get('txt', ''),
                                                    txt_properties.get('antialias', False),
                                                    txt_properties.get('color', (0, 0, 0)),
                                                    txt_properties.get('pos', (0, 0)))

        Button.buttons.append(self)

    def add_txt(self, txt_properties: dict):
        self.txtSurf, self.txtRect = create_txt(txt_properties.get('font'), txt_properties.get('size', 0),
                                                txt_properties.get('bald', False),
                                                txt_properties.get('italic', False), txt_properties.get('txt', ''),
                                                txt_properties.get('antialias', False),
                                                txt_properties.get('color', (0, 0, 0)),
                                                txt_properties.get('pos', (0, 0)))

    def draw(self, draw_surf):
        draw_surf.blit(self.surf, self.rect)
        if 'txtSurf' in self.__dict__:
            draw_surf.blit(self.txtSurf, self.txtRect)

    def logic(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.clickStage = 0
            self.surf.fill((255, 0, 0))
            if pygame.mouse.get_pressed()[0]:
                self.clickStage = 1
                self.surf.fill((0, 255, 0))

        else:
            self.clickStage = None
            self.surf.fill((0, 0, 255))

    def update(self, draw_surf):
        self.logic()
        self.draw(draw_surf)
