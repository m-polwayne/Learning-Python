from tkinter import Canvas
from turtle import color


class Circle(object):
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius

    def draw(self, Canvas):
        rad = self.radius
        x1 = self.center[0]-rad
        y1 = self.center[1]-rad
        x2 = self.center[0]+rad
        y2 = self.center[1]+rad
        Canvas._create(x1, y1, x2, y2)


circle = Circle([10, 30], 20)
circle.draw(Canvas)
