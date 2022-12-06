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
from kivy.metrics import *
from kivy.properties import ObjectProperty
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

