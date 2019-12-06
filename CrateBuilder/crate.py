
class Crate:
    # constants
    SLAT_WIDTH = 3.5
    SLAT_THICKNESS = 0.75

    """description of class"""
    def __init__(self, iWidth, iLength, iHeight, sBrace, eBrace):
        self.insideWidth = float(iWidth)
        self.insideLength = float(iLength)
        self.insideHeight = float(iHeight)
        if float(sBrace) == 0:
            self.sideBrace = 0
        elif float(sBrace) == 1:
            self.sideBrace = Crate.SLAT_THICKNESS * 2
        if float(eBrace) == 0:
            self.endBrace = 0
        elif int(eBrace) == 1:
            self.endBrace = Crate.SLAT_THICKNESS * 2

    def outsideWidth(self):
        outsideWidth = self.insideWidth + (Crate.SLAT_THICKNESS * 4) + self.sideBrace
        return outsideWidth

    def outsideLength(self):
        outsideLength = self.insideLength + (Crate.SLAT_THICKNESS * 4) + self.endBrace
        return outsideLength

    def outsideHeight(self):
        outsideHeight = self.insideHeight + (Crate.SLAT_THICKNESS * 4) + Crate.SLAT_WIDTH
        return outsideHeight

