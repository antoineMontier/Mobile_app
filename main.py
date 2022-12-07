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

    COLS = 10
    LINES = 20
    MEMORY_ROWS = 20
    INCLINATION = 0.2

    def __init__(self, **kwargs):
        # self declarations of variables
        self.fps = 60.0
        self.matrix = [[0 for x in range(self.COLS)]
                        for y in range(self.LINES + self.MEMORY_ROWS)]
        self.matrix[5][0] = 1
        self.matrix[6][1] = 1
        self.matrix[7][2] = 1

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
        self.draw_cylinder()


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

    def draw_cylinder(self):
        with self.canvas:
            precision_draw = 0.001
            # lets find the radius of the bigger circle (englobing the full screen):
            tile_size = 0.0
            radius = distance(self.width/2, self.height/2, 0, 0)
            end_opening = radius*0.01
            Color(1, 1, 0, 1)
            for i in range(self.COLS):#colss display
                alpha = i/(float(self.COLS))*3.1415*2
                Line(points=(self.width/2 + cos(alpha)*(end_opening+2),self.height/2 + sin(alpha)*(end_opening+2), self.width/2 + cos(alpha)*radius,self.height/2 + sin(alpha)*radius))
            for i in range(self.LINES + self.MEMORY_ROWS):#line display
                long = end_opening + i*i*(radius - end_opening)/(self.LINES*self.LINES)
                Line(circle=(self.width/2, self.height/2, long*2))
            #now let's color the inside of the cells:
            Color(1, 0, 0, 1)
            for i in range(self.LINES + self.MEMORY_ROWS):
                for j in range(self.COLS):
                    if(self.matrix[i][j] != 0):
                        alpha1 = (j-1)/(float(self.COLS))*3.1415*2
                        alpha2 = j/(float(self.COLS))*3.1415*2
                        
                        angle = min(alpha1, alpha2)
                        
                        while(angle < max(alpha1, alpha2)):
                            leng1 = end_opening + i*i*((radius - end_opening)/(self.LINES*self.LINES) *(1 + self.INCLINATION))
                            leng2 = end_opening + (i+1)*(i+1)*((radius - end_opening)/(self.LINES*self.LINES)*(1 + self.INCLINATION))
                            print(angle)
                            Line(points=(self.width/2 + leng1*cos(angle), self.height/2 + leng1*sin(angle), self.width/2 + leng2*cos(angle), self.height/2 + leng2*sin(angle)))
                            angle+=precision_draw*3.1415*2
                    






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
