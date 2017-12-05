import math


class Position(object):
    #constructor
    def __init__(self, x=0, y=0):
        self._x=x
        self._y=y

    def x(self):
        return self._x

    def y(self):
        return self._y

    def distance_to(self, other):
        delta_x = self.x() - other.x()
        delta_y = self.y() - other.y()
        return math.sqrt(delta_x**2 + delta_y**2)


class Velocity(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def magnitude(self):
        return self.end.distance_to(self.start)

    def angle(self):

