
class Crate:
    # constants
    SLAT_WIDTH = 3.5
    SLAT_THICKNESS = 0.75
    RUNNER_THICKNESS = 1.5

    """description of class"""
    def __init__(self, iWidth, iLength, iHeight, sBrace, eBrace, runners):
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
        self.numRunners = float(runners)

    def outsideWidth(self):
        outsideWidth = self.insideWidth + (Crate.SLAT_THICKNESS * 4) + self.sideBrace
        return outsideWidth

    def outsideLength(self):
        outsideLength = self.insideLength + (Crate.SLAT_THICKNESS * 4) + self.endBrace
        return outsideLength

    def outsideHeight(self):
        outsideHeight = self.insideHeight + (Crate.SLAT_THICKNESS * 4) + Crate.SLAT_WIDTH
        return outsideHeight

    # This function calculates the spacing of slats for a pallet with a max of 2" between each slat.
    def palletSlatSpacing(self):
        numSlats = 1 #Value to start with (at first calculation numSlats is 2.
        palletSlatSpacing = 3 # Value greater than 2 to start with
        while palletSlatSpacing > 2:
            numSlats += 1
            palletSlatSpacing = (self.insideWidth - (numSlats * Crate.SLAT_WIDTH)) / (numSlats - 1)
        return palletSlatSpacing

    # same as slatSpacing function but it returns number of slats instead of slat spacing
    def numSlats(self):
        numSlats = 1 #Value to start with (at first calculation numSlats is 2.
        palletSlatSpacing = 3 # Value greater than 2 to start with
        while palletSlatSpacing > 2:
            numSlats += 1
            palletSlatSpacing = (self.insideWidth - (numSlats * Crate.SLAT_WIDTH)) / (numSlats - 1)
        return numSlats

    def palletRunnerSpacing(self):
        palletRunnerSpacing = (self.insideWidth - (self.numRunners * Crate.RUNNER_THICKNESS)) / (self.numRunners - 1)
        return palletRunnerSpacing

    def sideTopRailLength(self):
        sideTopRailLength = self.insideLength + (2 * Crate.SLAT_THICKNESS)
        return sideTopRailLength

    def sideVertRailLength(self):
        outsideHeight=self.outsideHeight()
        sideVertRailLength = outsideHeight - Crate.SLAT_THICKNESS
        return sideVertRailLength

    def endTopRailLength(self):
        endTopRailLength = self.insideWidth + (4 * Crate.SLAT_THICKNESS)
        return endTopRailLength

    def endVertRailLength(self):
        outsideHeight=self.outsideHeight()
        endVertRailLength = outsideHeight - (2 * Crate.SLAT_THICKNESS)
        return endVertRailLength
