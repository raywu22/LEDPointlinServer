
"""
Class to represent an LED board
Individual LEDs have positions denoted by tuples (x,y), with colors denoted by tuples (r,g,b)
"""

class BoardState:
    
    def __init__(self, startColor, boardWidth, boardHeight):
        self.startColor = startColor
        self.height = boardHeight #number of rows in board
        self.width = boardWidth #number of columns in board
        self.matrix = [[self.startColor for y in range(self.height)] for x in range(self.width)]

    def getMatrix(self):
        return self.matrix
    
    def __str__(self):
        result = ""
        for y in range(self.height):
            for x in range(self.width):
                result += str(self.matrix[x][y]) + " "
            result += "\n"
        return result

    #changes startColor and resets board to the new startColor
    def setStartColor(self, newStartColor):
        self.startColor = newStartColor
        self.matrix = [[newStartColor for y in range(self.height)] for x in range(self.width)]

    #changes all of the LEDs that are startColor to a new background color
    def setBackground(self, backgroundColor):
        for x in range(self.width):
            for y in range(self.height):
                if self.matrix[x][y] == self.startColor:
                    self.matrix[x][y] = backgroundColor

    #method to set color at a single index
    def setColorSingleIndex(self, index, newColor):
        (x,y)=index
        if 0 <= x and x < self.width and 0 <= y and y < self.height:
            self.matrix[x][y] = newColor
        else:
            print "Index out of range"

    #method to set color at multiple indices
    def setColorList(self, infoList): #infoList is a list of indices and colors in the format ((x,y), (r,g,b)) 
        for ((x,y), color) in infoList:
            self.matrix[x][y] = color
    
    #reset the color to startColor for the entire board (by default) or for only the desired index
    def reset(self, index = None):
        if index != None:
            (x,y) = index
            self.matrix[x][y] = self.startColor
        else:
            self.matrix = [[self.startColor for y in range(self.height)] for x in range(self.width)]
            

    #scale the brightness of all LEDs on the board by a nonnegative number
    def scaleBrightness(self, scale): #scale is a nonnegative number
        for x in range(self.width):
            for y in range(self.height):
                self.matrix[x][y] = tuple( 255 if scale*e > 255 else int(scale*e) for e in self.matrix[x][y]) #if scale*e is not an integer, use its floor function
        

    #replaces display with a left-to-right gradient of leftColor to rightColor
    def setSideSideGradient(self, leftColor, rightColor):
        for x in range(self.width):
            color = tuple (int(round(rightColor[i] * (float(x)/(self.width-1)) + leftColor[i] * (1.0 - float(x)/(self.width-1)))) for i in range(len(leftColor)))
            for y in range(self.height):
                self.matrix[x][y] = color

    #replaces display with an top-to-bottom gradient of TopColor to BottomColor
    def setTopBottomGradient(self, topColor, bottomColor):
        for y in range(self.height):
            for x in range(self.width):
                color = tuple (int(round(bottomColor[i] * (float(y)/(self.height-1)) + topColor[i] * (1.0 - float(y)/(self.height-1)))) for i in range(len(topColor)))           
                self.matrix[x][y] = color
        
