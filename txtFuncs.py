import pygame

pygame.font.init()


def create_txt(font: str = None, size: int = 0, bald: bool = False, italic: bool = False, txt: str = '',
               antialias: bool = False, color: tuple[int, int, int] = (0, 0, 0), pos: tuple[int, int] = (0, 0)):

    font = pygame.font.SysFont(font, size, bald, italic)

    txt_surf = font.render(txt, antialias, color)
    txt_rect = txt_surf.get_rect(center=pos)

    return txt_surf, txt_rect
