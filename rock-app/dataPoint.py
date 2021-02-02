# JM 

class DataPoint:
    def __init__(self, x, y, unit):
        self.x_val = x
        self.y_val = y
        self.unit = unit

    def toTuple(self):
        return (self.x_val, self.y_val)

    def getX(self):
        return self.x_val

    def getY(self):
        return self.y_val
