#!/usr/bin/python3
# coding:utf-8


class MyFirstClass:
    """

    """
    pass


class Point:
    def reset(self):
        self.x = 0
        self.y = 0

    def reset2(this):
        this.x = 0
        this.y = 0

    def reset3(marcha):
        marcha.x = 0
        marcha.y = 0

    pass


# p1 = Point()

# p2 = Point()

# p1.x = 5
# p1.y = 4

# p2.x = 3
# p2.y = 6


# print(p1.x, p1.y)
# print(p2.x, p2.y)

# p = Point()

# p.reset3()

# print(p.x, p.y)

# p = Point()

# Point.reset(p)

# print(p.x, p.y)

import math


class Point:
    'Represnets a point in two-dimentionals geometric coordinates'

    def __init__(self, x=None, y=None):
        '''
        Initialize the position of a new point.
        the x and y coordiantes can be specified
        if not the point defaults to origin.
        '''
        self.move(x, y)

    def move(self, x, y):
        'move the point to a new place of a 2d point'
        self.x = x
        self.y = y

    def reset(self):
        'reset the point back to the geometric origin:0,0'
        self.move(0, 0)

    def calculate_distance(self, other_point):
        'caculate thr distance from this point to a second point passed as a parameter ,the distance returns a float'
        data = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return '%6.3f' % data


# point1 = Point()
# point2 = Point()

# point1.reset()
# point2.move(5, 0)

# assert (point2.calculate_distance(point1) == point1.calculate_distance(point2))
# point1.move(3, 4)

# print(point1.calculate_distance(point2))
# print(point1.calculate_distance(point1))

# point = Point(3, 5)
# print(point.x)
# print(point.y)
