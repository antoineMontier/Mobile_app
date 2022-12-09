import math
from kivy.graphics.vertex import *
from kivy.properties import ObjectProperty, Clock
from kivy.graphics.vertex_instructions import *
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.app import App
from kivy.config import Config
from math import cos, sin, sqrt
import kivy
import random
import kivy
kivy.require('1.9.0')

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '900')


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


def polygon(x1, y1, x2, y2, x3, y3, x4, y4, empty):
    if(not empty):
        Triangle(points=(x1, y1, x2, y2, x3, y3))
        Triangle(points=(x2, y2, x3, y3, x4, y4))
        Triangle(points=(x3, y3, x4, y4, x1, y1))
        Triangle(points=(x4, y4, x1, y1, x2, y2))
    else:
        Line(points=(x1, y1, x2, y2, x3, y3, x4, y4, x1, y1))

class MyScreen(Widget):
    pass
    # def __init__(self, **kwargs):
    #    super(MyScreen, self).__init__(**kwargs)


class GameCanvas(Widget):

    COLS = 8
    LINES = 20
    INCLINATION = 0.2

    def __init__(self, **kwargs):
        # self declarations of variables
        self.it = 0
        self.fps = 30.0
        self.speed = 0.1
        self.matrix = [[0 for x in range(self.COLS*4)]
                        for y in range(self.LINES)]

        super(GameCanvas, self).__init__(**kwargs)
        self.print_matrix()
        with self.canvas:
            # self declaration of canvas objects
            pass
        Clock.schedule_interval(self.update, 1/self.fps)  # update interval

    def on_size(self, *args):
        print("on_size : " + str(self.width) + ", " + str(self.height))

    # self update of canvas objects and variable every game ticks
    def update(self, dt):  # dt is delta time
        time_factor = self.fps*dt
        with self.canvas:
            Color(0, 0, 0, 1)
            Rectangle(pos=(0, 0), size=(self.width, self.height))
            Color(1, 0, 0, 1)
            #polygon(100, 100, 200, 120, 210, 200, 120, 190, False)
            #Line(points=(0, 0, 0, 400, 200, 200))
            #self.draw_grid()
            #Ellipse(pos=(0, 0), size=(self.width, 100), angle_start=0, angle_end=180)
            Color(0, 1, 0, 1)

            self.draw_rect(self.it)

            Color(0, 0, 1, 1)
            Line(points=(self.width/3, self.height, self.width/3, 0))
            Line(points=(2*self.width/3, self.height, 2*self.width/3, 0))
            Line(points=(self.width, self.height/3, 0, self.height/3))
            Line(points=(self.width, 2*self.height/3, 0, 2*self.height/3))
            print("fps = "+str(1/(dt)))
        self.it = self.it % 1 + self.speed*time_factor


    def draw_grid(self):
        with self.canvas:
            Color(1, 1, 1, 1)
            for i in range(self.LINES + 1):
                Line(points=(0, i*(float(self.height)/self.LINES),
                    self.width, i*(float(self.height)/self.LINES)))
            for i in range(self.COLS + 1):
                Line(points=(i*(float(self.width)/self.COLS), 0,
                    i*(float(self.width)/self.COLS), self.height))

    def print_matrix(self):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end=" ")
            print("|" + str(i))

    def draw_rect(self, animation):
        x = self.width*0.5
        y = self.height*0.3
        w = self.width*0.2
        h = self.height*0.1
        #bottom
        #first the "vertical" lines
        for c in range(self.COLS):
            Line(points=(x - w/2 + c*w/self.COLS, y - h/2, 0 + c*self.width/self.COLS, 0))
        #then the polygons
        for c in range(self.LINES):
            start1 = [x - w/2- (c+animation)  *(x - w/2)/self.LINES, (y  - h/2) - (c+animation)    *(y  - h/2)/self.LINES]
            end1   = [x + w/2+ (c+animation)  *(self.width - x - w/2)/self.LINES, (self.height- y  - h/2) - (c+animation)    *(y  - h/2)/self.LINES]
            start2 = [x - w/2- (c+animation+1)*(x - w/2)/self.LINES, (y  - h/2) - (c+1+animation)*(y  - h/2)/self.LINES]
            end2   = [x + w/2+ (c+animation+1)*(self.width - x - w/2)/self.LINES, (self.height- y  - h/2) - (c+1+animation)*(y  - h/2)/self.LINES]
            for l in range(self.COLS):
                p1 = [start1[0] + l    *(end1[0] - start1[0])/self.COLS, start1[1]]
                p2 = [start2[0] + l    *(end2[0] - start2[0])/self.COLS, start2[1]]
                p3 = [start1[0] + (l+1)*(end1[0] - start1[0])/self.COLS, start1[1]]
                p4 = [start2[0] + (l+1)*(end2[0] - start2[0])/self.COLS, start2[1]]
                if(self.matrix[c][l] == 0):
                    polygon(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1] , p2[0], p2[1], True)
                else:
                    polygon(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1] , p2[0], p2[1], False)

        #up
        #first the "vertical" lines
        for c in range(self.COLS):
            Line(points=(x - w/2 + c*w/self.COLS,  y + h/2, + c*self.width/self.COLS, self.height ))
        #then the polygons
        for c in range(self.LINES):
            start1 = [x - w/2 - (c+animation)    *(x - w/2)/self.LINES, (y  + h/2) + (c+animation)    *(self.height - y  - h/2)/self.LINES]
            end1   = [x + w/2 + (c+animation)    *(self.width - x - w/2)/self.LINES, (y  + h/2) + (c+animation)    *(self.height - y  - h/2)/self.LINES]
            start2 = [x - w/2 - (c+animation+1)*(x - w/2)/self.LINES, (y  + h/2) + (c+animation+1)*(self.height - y  - h/2)/self.LINES]
            end2   = [x + w/2 + (c+animation+1)*(self.width - x - w/2)/self.LINES, (y  + h/2) + (c+animation+1)*(self.height - y  - h/2)/self.LINES]
            for l in range(self.COLS*2, self.COLS*3):
                p1 = [start1[0] + (l - self.COLS*2)    *(end1[0] - start1[0])/self.COLS, start1[1]]
                p2 = [start2[0] + (l - self.COLS*2)    *(end2[0] - start2[0])/self.COLS, start2[1]]
                p3 = [start1[0] + (l - self.COLS*2+1)*(end1[0] - start1[0])/self.COLS, start1[1]]
                p4 = [start2[0] + (l - self.COLS*2+1)*(end2[0] - start2[0])/self.COLS, start2[1]]
                if(self.matrix[c][self.COLS*5-l - 1] == 0):
                    polygon(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1] , p2[0], p2[1], True)
                else:
                    polygon(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1] , p2[0], p2[1], False) 

        #left
        #first the "vertical" lines
        for c in range(self.COLS):
            Line(points=(0, c*self.height/self.COLS, x - w/2, y - h/2 + c*h/self.COLS ))
        #then the polygons
        for c in range(self.LINES):
            start1 = [x - w/2- (c+animation)    *(x - w/2)/self.LINES, (y  - h/2) - (c+animation)    *(y  - h/2)/self.LINES]
            end1   = [x - w/2- (c+animation)    *(self.width - x - w/2)/self.LINES, (y  + h/2) + (c+animation)    *(self.height - y  - h/2)/self.LINES]
            start2 = [x - w/2- (c+animation+1)*(x - w/2)/self.LINES, (y  - h/2) - (c+animation+1)*(y  - h/2)/self.LINES]
            end2   = [x - w/2- (c+animation+1)*(self.width - x - w/2)/self.LINES, (y  + h/2) + (c+animation+1)*(self.height - y  - h/2)/self.LINES]
            for l in range(self.COLS*3, self.COLS*4):
                p1 = [start1[0], start1[1] + (l - self.COLS*3)  *(end1[1]-start1[1])/self.COLS]
                p2 = [start2[0], start2[1] + (l - self.COLS*3)  *(end2[1]-start2[1])/self.COLS]
                p3 = [start1[0], start1[1] + (l - self.COLS*3+1)*(end1[1]-start1[1])/self.COLS]
                p4 = [start2[0], start2[1] + (l - self.COLS*3+1)*(end2[1]-start2[1])/self.COLS]
                if(self.matrix[c][self.COLS*7 - l - 1] == 0):
                    polygon(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1] , p2[0], p2[1], True)
                else:
                    polygon(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1] , p2[0], p2[1], False)

        #right
        #first the "vertical" lines
        for c in range(self.COLS):
            Line(points=(self.width, c*self.height/self.COLS, x + w/2, y - h/2 + c*h/self.COLS ))
        #then the polygons
        for c in range(self.LINES):
            start1 = [x + w/2+ (c+animation)    *(self.width - x - w/2)/self.LINES, (y  - h/2) - (c+animation)    *( y  - h/2)/self.LINES]
            end1   = [x + w/2+ (c+animation)    *(self.width-x - w/2)/self.LINES, (y  + h/2) + (c+animation)    *(self.height - y  - h/2)/self.LINES]
            start2 = [x + w/2+ (c+animation+1)*(self.width - x - w/2)/self.LINES, (y  - h/2) - (c+animation+1)*( y  - h/2)/self.LINES]
            end2   = [x + w/2+ (c+animation+1)*(self.width-x - w/2)/self.LINES, (y  + h/2) + (c+animation+1)*(self.height - y  - h/2)/self.LINES]
            for l in range(self.COLS*1, self.COLS*2):
                p1 = [start1[0], start1[1] + (l - self.COLS*1)  *(end1[1]-start1[1])/self.COLS]
                p2 = [start2[0], start2[1] + (l - self.COLS*1)  *(end2[1]-start2[1])/self.COLS]
                p3 = [start1[0], start1[1] + (l - self.COLS*1+1)*(end1[1]-start1[1])/self.COLS]
                p4 = [start2[0], start2[1] + (l - self.COLS*1+1)*(end2[1]-start2[1])/self.COLS]
                if(self.matrix[c][l] == 0):
                    polygon(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1] , p2[0], p2[1], True)
                else:
                    polygon(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1] , p2[0], p2[1], False)














class MyApp(App):
    """
    button_color = [1, 0, 0, 1]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def build(self):
        #Window.clearcolor = 9/255, 11/255, 10/255, 1#bg color
        #Window.size = (1080*0.3, 2400*0.3)
        return MyScreen()
    """
    pass


if __name__ == '__main__':
    MyApp().run()
