import kivy, random
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.graphics import *
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.metrics import dp
from kivy.graphics.vertex_instructions import  *
from kivy.properties import ObjectProperty, Clock
from kivy.graphics.vertex import *

kivy.require('1.9.0')




class MyScreen(Widget):
    pass
    #def __init__(self, **kwargs):
    #    super(MyScreen, self).__init__(**kwargs)



class Canvas1(Widget):
    pass
    
class Canvas2(Widget):
    def __init__(self, **kwargs):
        super(Canvas2, self).__init__(**kwargs)
        with self.canvas:
            Line(points=(100, 100, 400, 500), width=5)
            Color(0, 0.6, 0.4, 1)
            self.rect = Rectangle(pos=(300, 400), size=(50, 50))

    def redraw(self):
        x, y = self.rect.pos
        x += dp(50)
        if(x > self.width):
            x = dp(0)
        self.rect.pos = (x, y)

class Canvas3(Widget):
    def __init__(self, **kwargs):
        self.fps = 60
        self.vx = dp(5)
        self.vy = dp(5)
        self.ball_size = dp(50)
        self.ball_x = self.width/2
        self.ball_y = self.height/2
        super(Canvas3, self).__init__(**kwargs)
        with self.canvas:
            self.ball = Ellipse(pos=(self.ball_x, self.ball_y), size=(self.ball_size, self.ball_size))

        Clock.schedule_interval(self.update, 1/self.fps)#update every one second


    def on_size(self, *args):
        print("on_size : " + str(self.width) + ", "+ str(self.height))
        self.ball.pos = self.width/2-self.ball_size/2, self.height/2-self.ball_size/2

    def update(self, dt):#dt is delta time
        x, y = self.ball.pos
        if(x + self.ball.size[0] > self.width or x < 0):
            self.vx *= -1
        if(y+ self.ball.size[1] > self.height or y < 0):
            self.vy *= -1
        self.ball.pos = (x+self.vx, y+self.vy)














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

