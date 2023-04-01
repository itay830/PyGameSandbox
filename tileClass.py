import pygame


class Tile:
    tileCounter = 0

    def __init__(self, pos, color, sizex=25, sizey=25):
        self.surf = pygame.Surface((sizex, sizey))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(topleft=pos)
        self.tileNum = Tile.tileCounter
        Tile.tileCounter += 1

    def draw(self, draw_surf):
        draw_surf.blit(self.surf, self.rect)

    def update(self, draw_surf):
        self.draw(draw_surf)

    @staticmethod
    def tile_map(sx, sy, ex, ey, sizex, sizey, color):
        return [[Tile((x, y), color, sizex, sizey) for x in range(sx, ex, sizex)] for y in
                range(sy, ey, sizey)]

    @staticmethod
    def draw_grid(draw_surf, sx, sy, ex, ey, sizex, sizey, color):
        for x in range(sx, ex, sizex):
            pygame.draw.line(draw_surf, color, (x, 0), (x, ey))
        for y in range(sy, ey, sizey):
            pygame.draw.line(draw_surf, color, (0, y), (ex, y))
