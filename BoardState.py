class BoardState:
    
    def __init__(self, startColor, boardWidth, boardHeight):
        self.height = boardHeight
        self.width = boardWidth
        self.matrix = [[startColor for y in range(self.height)] for x in range(self.width)]

    def setColor (self, index, newColor):
        xCoor = index[0]
        yCoor = index[1]
        if 0 <= xCoor and xCoor < self.width and 0 <= yCoor and yCoor < self.height:
            self.matrix[xCoor][yCoor] = newColor
        else:
            print "Index out of range"
        

    def __str__(self):
        result = ""
        for y in range(self.height):
            for x in range(self.width):
                result += str(self.matrix[x][y]) + " "
            result += "\n"
        return result
            
        
