import pygame


class Tile:

    def __init__(self, pos, color, index, sizex=25, sizey=25):
        self.surf = pygame.Surface((sizex, sizey))
        self.surf.fill(color)
        self.rect = self.surf.get_rect(topleft=pos)
        self.index = index

    def draw(self, draw_surf):
        draw_surf.blit(self.surf, self.rect)

    @staticmethod
    def draw_tiles(draw_surf, topleft, bottomright, tilemap):
        new_tile_map = Tile.slice_tile_map(topleft, bottomright, tilemap)
        for row in new_tile_map:
            for tile in row:
                tile.draw(draw_surf)

    @staticmethod
    def tile_map(sx, sy, ex, ey, sizex, sizey, color):
        return [[Tile((x, y), color, (y // sizey, x // sizex), sizex, sizey) for y in range(sy, ey, sizey)] for x in
                range(sx, ex, sizex)]

    @staticmethod
    def slice_tile_map(topleft, bottomright, tilemap):
        return [[tile for tile in row[topleft[1]:bottomright[1] + 1]] for row in tilemap[topleft[0]:bottomright[0] + 1]]

    @staticmethod
    def draw_grid(draw_surf, sx, sy, ex, ey, sizex, sizey, color):
        for x in range(sx, ex, sizex):
            pygame.draw.line(draw_surf, color, (x, 0), (x, ey))
        for y in range(sy, ey, sizey):
            pygame.draw.line(draw_surf, color, (0, y), (ex, y))
