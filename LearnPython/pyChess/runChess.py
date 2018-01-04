import pygame

from pyChess.board import chessBoard

pygame.init()
gameDisplay = pygame.display.set_mode((600, 600))
pygame.display.set_caption("PyChess")
clock = pygame.time.Clock()




board = chessBoard.Board()




quitChess = False
while not quitChess:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.display.update()
    clock.tick(60)


