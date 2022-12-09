import math, random
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
    LINES = 5
    INCLINATION = 0.2

    def __init__(self, **kwargs):
        # self declarations of variables
        self.it = 0
        self.fps = 60.0
        self.speed = 0.05
        self.matrix = [[1 for x in range(self.COLS*4)]
                        for y in range(self.LINES)]
        self.new_row = [0 for x in range(self.COLS*4)]
        self.last_path = self.COLS*1 + 2
        self.matrix[0][3] = 1
        for i in range(len(self.matrix[0])):
            self.matrix[0][i] = 1
        self.new_row[self.last_path] = 1

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
        if(self.it >= 1):
            self.it = 0
            i = len(self.matrix) - 1
            while i > 0:
                self.matrix[i] = self.matrix[i-1]
                i -= 1
            # i = 0
            self.matrix[0] = self.new_row
            self.new_row = [0 for i in range(len(self.new_row))]
            a = random.random()
            if(a < 0.3):#new path to the left
                if(self.last_path == 0):
                    self.new_row[len(self.new_row)-1] = 1
                    self.new_row[self.last_path] = 1
                    self.last_path = len(self.new_row)-1
                else:
                    self.new_row[self.last_path] = 1
                    self.new_row[self.last_path-1] = 1
                    self.last_path -= 1
            elif(a < 0.6):#new path to the right
                if(self.last_path == len(self.new_row)-1):
                    self.new_row[0] = 1
                    self.new_row[self.last_path] = 1
                    self.last_path = 0
                else:
                    self.new_row[self.last_path] = 1
                    self.new_row[self.last_path+1] = 1
                    self.last_path += 1
            else:#new path forward
                self.new_row[self.last_path] = 1
            self.print_matrix()




        self.it += self.speed*time_factor


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

    def draw_rect(self, a):
        x = self.width*0.5
        y = self.height*0.6
        w = self.width*0.2
        h = self.height*0.1
        #bottom
        for c in range(self.COLS):
            #first the "vertical" lines
            Line(points=(x - w/2 + c*w/self.COLS, y - h/2, 0 + c*self.width/self.COLS, 0))
            #first the "vertical" lines
            Line(points=(x - w/2 + c*w/self.COLS,  y + h/2, + c*self.width/self.COLS, self.height))
            #first the "vertical" lines
            Line(points=(0, c*self.height/self.COLS, x - w/2, y - h/2 + c*h/self.COLS ))
            #first the "vertical" lines
            Line(points=(self.width, c*self.height/self.COLS, x + w/2, y - h/2 + c*h/self.COLS))
        #then the polygons
        for c in range(self.LINES):#
            for l in range(self.COLS):
                if(self.matrix[c][l] != 0):
                    p1 = [(x - w/2)*(1- (c+a)/self.LINES) + l*(c+a)*(self.width - w)/(self.LINES*self.COLS) + l*w/self.COLS,
                    (y  - h/2)*(1 - (c + a)/self.LINES)]
                    p2 = [(x - w/2)*(1- (c+a+1)/self.LINES) + l*(c+a+1)*(self.width - w)/(self.LINES*self.COLS) + l*w/self.COLS,
                    (y  - h/2)*(1 - (c + a + 1)/self.LINES)]
                    p3 = [(x - w/2)*(1- (c+a)/self.LINES) + (l+1)*(c+a)*(self.width - w)/(self.LINES*self.COLS) + (l+1)*w/self.COLS,
                    (y  - h/2)*(1 - (c + a)/self.LINES)]
                    p4 = [(x - w/2)*(1- (c+a+1)/self.LINES) + (l+1)*(c+a+1)*(self.width - w)/(self.LINES*self.COLS) + (l+1)*w/self.COLS,
                    (y  - h/2)*(1 - (c + a + 1)/self.LINES)]
                    polygon(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1] , p2[0], p2[1], False)

        #up
        #then the polygons
        for c in range(self.LINES):
            for l in range(self.COLS*2, self.COLS*3):
                if(self.matrix[c][self.COLS*5-l - 1] != 0):
                    p1 = [((x - w/2)*(1- (c+a)/self.LINES))   + (l/self.COLS - 2)    *(w + (c+a)  *(self.width - w)/self.LINES),
                    (y  + h/2) + (c+a)    *(self.height - y  - h/2)/self.LINES]
                    p2 = [((x - w/2)*(1- (c+1+a)/self.LINES)) + (l/self.COLS - 2)    *(w + (c+a+1)*(self.width - w)/self.LINES),
                    (y  + h/2) + (c+a+1)*(self.height - y  - h/2)/self.LINES]
                    p3 = [((x - w/2)*(1- (c+a)/self.LINES))   + ((l+1)/self.COLS - 2)*(w + (c+a)  *(self.width - w)/self.LINES),
                    (y  + h/2) + (c+a)    *(self.height - y  - h/2)/self.LINES]
                    p4 = [((x - w/2)*(1- (c+1+a)/self.LINES)) + ((l+1)/self.COLS - 2)*(w + (c+a+1)*(self.width - w)/self.LINES),
                    (y  + h/2) + (c+a+1)*(self.height - y  - h/2)/self.LINES]
                    polygon(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1] , p2[0], p2[1], False)
                

        #left
        #then the polygons
        for c in range(self.LINES):
            for l in range(self.COLS*3, self.COLS*4):
                if(self.matrix[c][self.COLS*7 - l - 1] != 0):
                    p1 = [(x - w/2)*(1-(c+a)/self.LINES),
                    (y  - h/2)*(1 - (c+a)/self.LINES)   + (l/self.COLS - 3)     *(h + (self.height - h)*(c+a)/self.LINES)]
                    p2 = [(x - w/2)*(1-(c+a+1)/self.LINES),
                    (y  - h/2)*(1 - (c+a+1)/self.LINES) + (l/self.COLS - 3)     *(h + (self.height - h)*(c+a+1)/self.LINES)]
                    p3 = [(x - w/2)*(1-(c+a)/self.LINES),
                    (y  - h/2)*(1 - (c+a)/self.LINES)   + ((l+1)/self.COLS - 3) *((h + (self.height - h)*(c+a)/self.LINES))]
                    p4 = [(x - w/2)*(1-(c+a+1)/self.LINES),
                    (y  - h/2)*(1 - (c+a+1)/self.LINES) + ((l+1)/self.COLS - 3) *(h + (self.height - h)*(c+a+1)/self.LINES)]
                    polygon(p1[0], p1[1], p3[0], p3[1], p4[0], p4[1] , p2[0], p2[1], False)

        #right
        #then the polygons
        for c in range(self.LINES):
            for l in range(self.COLS*1, self.COLS*2):
                if(self.matrix[c][l] != 0):
                    p1 = [x + w/2+ (c+a)*(self.width - x - w/2)/self.LINES,
                    ((y  - h/2)*(1- (c+a)/self.LINES))   + (l/self.COLS - 1)    *(h + (c+a)/self.LINES   *(self.height - h))]
                    p2 = [x + w/2+ (c+a+1)*(self.width - x - w/2)/self.LINES,
                    ((y  - h/2)*(1- (c+a+1)/self.LINES)) + (l/self.COLS-1)      *(h + (c+a+1)/self.LINES *(self.height - h))]
                    p3 = [x + w/2+ (c+a)*(self.width - x - w/2)/self.LINES,
                    ((y  - h/2)*(1- (c+a)/self.LINES))   + ((l+1)/self.COLS -1) *(h + (c+a)/self.LINES   *(self.height - h))]
                    p4 = [x + w/2+ (c+a+1)*(self.width - x - w/2)/self.LINES,
                    ((y  - h/2)*(1- (c+a+1)/self.LINES)) + ((l+1)/self.COLS -1) *(h + (c+a+1)/self.LINES *(self.height - h))]
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
