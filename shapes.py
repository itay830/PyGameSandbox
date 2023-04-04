import pygame


class Circle:
    def __init__(self, pos, width, height, radius, color):
        self.surf = pygame.Surface((width, height))
        self.rect = self.surf.get_rect(center=pos)
        pygame.draw.circle(self.surf, color, (self.rect.w/2, self.rect.height/2), radius)
        self.mask = pygame.mask.from_surface(self.surf)

    def draw(self, draw_surf):
        draw_surf.blit(self.surf, self.rect)


class Picture:
    def __init__(self, pos, path):
        self.surf = pygame.image.load(path).convert_alpha()
        self.rect = self.surf.get_rect(center=pos)
        self.mask = pygame.mask.from_surface(self.surf)

    def draw(self, draw_surf):
        draw_surf.blit(self.surf, self.rect)

