class Tile:

    tileCoordinate = None
    emptyTiles = {}
    isTileOccupied = False

    def __init__(self, tileCoordinate):
        self.tileCoordinate = tileCoordinate
        self.createEmptyTiles()

    def createEmptyTiles(self):
        for x in range(64):
            self.emptyTiles[x] = EmptyTile(x)


    def createTile(self, tileCoordinate, piece):
        if piece == None:
            return self.emptyTiles[tileCoordinate]
        else:
            return OccupiedTile(tileCoordinate, piece)



class EmptyTile(Tile):

    isTileOccupied = False

    def __init__(self, coordinate):
        Tile.__init__(coordinate)

    def toString(self):
        return "-"

    def getPiece(self):
        return None


class OccupiedTile(Tile):

    pieceOntile = None
    isTileOccupied = True

    def __init__(self, coordinate, piece):
        Tile.__init__(coordinate)
        self.pieceOntile = piece

    def toString(self):
        return "#"

    def getPiece(self):
        return self.pieceOntile


