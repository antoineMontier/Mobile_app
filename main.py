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
from kivy.properties import ObjectProperty

kivy.require('1.9.0')




class MyScreen(Widget):
    def __init__(self, **kwargs):
        super(MyScreen, self).__init__(**kwargs)



class Canvas1(Widget):
    pass
    


class MyApp(App):

    button_color = [1, 0, 0, 1]

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        

    def build(self):
        #Window.clearcolor = 9/255, 11/255, 10/255, 1#bg color
        #Window.size = (1080*0.3, 2400*0.3)
        return MyScreen()
    

if __name__ == '__main__':
    MyApp().run()

