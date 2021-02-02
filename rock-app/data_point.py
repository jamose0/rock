# JM 

class DataPoint:
    def __init__(self, x, y, unit):
        self.x_val = x
        self.y_val = y
        self.unit = unit

    def to_tuple(self):
        return (self.x_val, self.y_val)

    def get_x(self):
        return self.x_val

    def get_y(self):
        return self.y_val
