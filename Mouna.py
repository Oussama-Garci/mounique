import random
import numpy as np
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from bidi.algorithm import get_display


class Mouna(FloatLayout):
    vd = ObjectProperty("welcome")
    vc = ObjectProperty("hungry.jpg")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def afficheur (self):
        A = np.array(["كسكسي بالخضرة", "طبيخة", "كسكسي ازعر بالفول", "مقرونة فل بالتن", "سردينة مشوية"])
        B = np.array(["c1.jpg", "c2.jpg", "c3.jpg", "c4.jpg", "c5.jpg"])
        i = random.randrange(0, len(A))
        y = B[i]
        zx = A[i]
        self.vd = get_display(zx)
        self.vc = y
class MyApp(App):
    def build(self):
        return Mouna()
if __name__ == '__main__':
    MyApp().run()