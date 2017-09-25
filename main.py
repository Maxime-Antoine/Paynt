from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line


class PayntApp(App):
   
    def build(self):
        parent = Widget()
        self.painter = PayntWidget()
        clear_btn = Button(text='Clear')
        clear_btn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clear_btn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


class PayntWidget(Widget):
    def on_touch_down(self, touch):
        with self.canvas:
            color = (random(), 1, 1)
            Color(*color, mode='hsv')
            d = 15
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y]


if __name__ == "__main__":
    PayntApp().run()
