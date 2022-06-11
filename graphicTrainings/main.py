from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Ellipse, Line
import random
import math

class MyPaintWidget(Widget):
    def __init__(self, **kwargs):
        super(MyPaintWidget, self).__init__(**kwargs)
        self.add_widget(Widget)
        n1, n2 = 0, 1
        count = 0
        nth=1
        nterms= 360
        with self.canvas:
            while count < nterms:
                x= math.sin(math.radians(count))*count
                y= math.cos(math.radians(count))*count
                Color(count, count , count)
                Ellipse(pos=(touch.x + x, touch.y + y), size=(count/3, count/3))
                nth = n1 + n2
                # update values
                n1 = n2
                n2 = nth
                count += 1

class MyApp(App):

    def build(self):
        return MyPaintWidget()
if __name__ == '__main__':
    MyApp().run()