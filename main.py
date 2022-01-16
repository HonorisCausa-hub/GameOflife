import pygame
from cell import CellGrid
import sys


LIFECOLOR = (31, 97, 189)
LINECOLOR = (52, 53, 46)
LINE_WIDTH = 3
EDGE_WIDTH = 20
START_POSX = 20
START_POSY = 20
BG = (20, 20, 20)


class Game:

    screen = None

    def __init__(self, width, height, cx, cy):
        self.width = width
        self.height = height
        self.cx_rate = int((width - 2*EDGE_WIDTH) / cx)
        self.cy_rate = int((height - 2*EDGE_WIDTH) / cy)
        self.screen = pygame.display.set_mode([width, height])
        self.cells = CellGrid(cx, cy)

    def show_life(self):

        for i in range(self.cells.cx + 1):
            pygame.draw.line(self.screen, LINECOLOR, (START_POSX, START_POSY + i * self.cy_rate),
                             (START_POSX + self.cells.cx * self.cx_rate, START_POSY + i * self.cy_rate), LINE_WIDTH)
            pygame.draw.line(self.screen, LINECOLOR, (START_POSX + i * self.cx_rate, START_POSY),
                             (START_POSX + i * self.cx_rate, START_POSY + self.cells.cx * self.cy_rate), LINE_WIDTH)

        for cell_list in self.cells.cells:
            for item in cell_list:
                x = item.ix
                y = item.iy
                if item.is_live:
                    pygame.draw.rect(self.screen, LIFECOLOR,
                                     [START_POSX+x * self.cx_rate+ (LINE_WIDTH - 1),
                                      START_POSY+y * self.cy_rate+ (LINE_WIDTH - 1),
                                      self.cx_rate- LINE_WIDTH, self.cy_rate- LINE_WIDTH])

def main():
    pygame.init()
    pygame.display.set_caption("Game of Life")
    game = Game(440, 440, 50, 50)
    clock = pygame.time.Clock()
    while True:
        game.screen.fill(BG)
        clock.tick(3)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        game.cells.circulate_nbcount()
        game.cells.circulate_rule()

        game.show_life()
        pygame.display.flip()

        for i in game.cells.cells:
            txt = ""
            for j in i:
                txt += str(j)
            print(txt)


if __name__ == "__main__":
    main()

