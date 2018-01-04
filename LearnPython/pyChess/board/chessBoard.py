from pyChess.board.tile import Tile
from pyChess.player.player import Player
from pyChess.pieces.piece import Piece

class Board:

    gameBoardTileList = []
    whitePieces = []
    blackPieces = []

    whitePlayer = None
    blackPlayer = None
    currentPlayer = None

    enPassPawn = None


    def __init__(self, builder):

        self.gameBoardTileList = self.createGameBoardTiles(builder)
        self.whitePieces = self.calculateActivePieces(self.gameBoardTileList, "White")
        self.blackPieces = self.calculateActivePieces(self.gameBoardTileList, "Black")

        self.enPassPawn = builder.EnPassPawn

        whiteMoves = self.calculateLegalMoves(self.whitePieces)
        blackMoves = self.calculateLegalMoves(self.blackPieces)

        pass

    def printBoard(self):
        print('the board is printed')
        pass

    def calculateLegalMoves(self, listOfPieces):
        pass

    def calculateActivePieces(self, gameBoardTiles, alliance):
        activePieces = []
        for tile in gameBoardTiles:
            if tile.isTileOccupied:
                piece = tile.pieceOnTile
                if piece.alliance == alliance:
                    activePieces.append(piece)

        return activePieces

    def getTile(self, tileNumber):
        pass

    def createGameBoardTiles(self, builder):
        tiles = []
        for x in range(64):
            tiles.append(Tile.createTile(x, builder.boardConfig[x]))
        return tiles

    def createStandardBoard(self):
        pass



    class Builder:

        boardConfig = {}
        nextMoveMaker = None
        EnPassPawn = None

        def __init__(self):
            pass

        def setPiece(self, piece):
            pass

        def setMoveMaker(self, alliance):
            pass

        def build(self):
            pass

        def setEnPassPawn(self, pawn):
            pass

