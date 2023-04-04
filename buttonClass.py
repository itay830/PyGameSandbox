import pygame
from txtFuncs import create_txt

pygame.init()


class Button:
    buttons = []
    selectorsButtonGapX = 150
    selectorsButtonGapY = 150

    def __init__(self, pos, width, height, color, txt_properties: dict = None, selector_button: bool = False,
                 selectors_name: str = 'PROJECT NAME'):
        self.surf = pygame.Surface((width, height))
        self.surf.fill(color)
        if selector_button:
            self.rect = self.surf.get_rect(center=(Button.selectorsButtonGapX, Button.selectorsButtonGapY))
        else:
            self.rect = self.surf.get_rect(center=pos)
        self.clickStage = None

        self.held = False

        if txt_properties is not None:
            self.txtProperties = txt_properties
            if selector_button:
                self.txtProperties['txt'] = selectors_name
                self.txtProperties['pos'] = (Button.selectorsButtonGapX, self.rect.centery + 75)
            self.txtSurf, self.txtRect = create_txt(self.txtProperties.get('font'), self.txtProperties.get('size', 0),
                                                    self.txtProperties.get('bald', False),
                                                    self.txtProperties.get('italic', False),
                                                    self.txtProperties.get('txt', ''),
                                                    self.txtProperties.get('antialias', False),
                                                    self.txtProperties.get('color', (0, 0, 0)),
                                                    self.txtProperties.get('pos', (0, 0)))

        Button.buttons.append(self)
        Button.selectorsButtonGapX += 150
        if Button.selectorsButtonGapX > pygame.display.get_window_size()[0]:
            Button.selectorsButtonGapX = 150
            Button.selectorsButtonGapY += 150

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
                self.held = True
                self.surf.fill((0, 255, 0))
            if self.held and not pygame.mouse.get_pressed()[0]:
                self.clickStage = 1

        else:
            self.clickStage = False
            self.held = False
            self.surf.fill((0, 0, 255))

    def update(self, draw_surf):
        self.logic()
        self.draw(draw_surf)
