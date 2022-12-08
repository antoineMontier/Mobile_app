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
    LINES = 10
    INCLINATION = 0.2

    def __init__(self, **kwargs):
        # self declarations of variables
        self.it = 0
        self.fps = 10.0
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
            Color(1, 0, 0, 1)
            #polygon(100, 100, 200, 120, 210, 200, 120, 190, False)
            #Line(points=(0, 0, 0, 400, 200, 200))
            #self.draw_grid()
            #Ellipse(pos=(0, 0), size=(self.width, 100), angle_start=0, angle_end=180)
            self.draw_rect()

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

    def draw_rect(self):
        center_x = self.width/2
        center_y = self.height/2
        center_width = self.width/3
        center_height = self.height/3
        #display down border :
        sx = 0
        count = 0 
        while count <= self.LINES :
            count += 1
            y = sx*(center_y - center_height/2)/(center_x - center_width/2)
            x = sx
            Line(points=(x, y, self.width - x, y))
            sx += (center_x - center_width/2)/self.LINES
        
        #display left border :
        sy = 0
        count = 0 
        while count <= self.LINES :
            count += 1
            x = sy*(center_x - center_width/2)/(center_y - center_height/2)
            y = sy
            Line(points=(x, y, x, self.height - y))
            sy += (center_y - center_height/2)/self.LINES
        
        #display right border :
        sx = self.width
        count = 0 
        while count <= self.LINES :
            count += 1
            y = sx*(center_y - center_height/2)/(center_x + center_width/2 - self.width) + self.height
            x = sx
            Line(points=(x, y, x, self.height - y))
            sx -= (self.width - (center_x + center_width/2))/self.LINES

        #display top border :
        sy = self.height
        count = 0
        while count <= self.LINES :
            count += 1
            x = sy*(center_x - center_width/2)/(center_y - center_height/2)
            y = sy
            Line(points=(x, y, self.width - x, y))
            sy -= (self.height - (center_y + center_height/2))/self.LINES

















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
