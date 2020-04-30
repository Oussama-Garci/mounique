import random
import numpy as np
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from bidi.algorithm import get_display
from kivy.core.audio import SoundLoader

class Mouna(FloatLayout):
    vd = ObjectProperty("welcome")
    vc = ObjectProperty("hungry.jpg")
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def afficheur (self):
        A = np.array(["كسكسي بالخضرة", "طبيخة", "كسكسي ازعر بالفول", "مقرونة فل بالتن", "مقرونة بالدجاج", "مقرونة بالسكالوب",
             "تسطيرة", "مصلي بالدجاج", "عجة مرقاز", "ملوخية", "مرقة بالكعابر", "حوت و بطاطا فريت", "حلالم", "نواصر", "روز احمر", "قلايا كبدة",
             "جلبانة بالسيبيا", "شربة و بريك", "رشتة", "مرقة لوبيا", "مرقة بطاطا", "امك حورية", "روز بالخضرة النية", "مقرونة بالشوفرات", "عين صبنيورية",
             "كسكسي بالمناني", "مقرونة بالموزاريلا", "شربة شعير", "شربة لسان عصفور", "كفتة", "لبلابي", "لازانيا", "دويدة", "سردينة مشوية"])
        B = np.array(["c1.jpg", "c2.jpg", "c3.jpg", "c4.jpg", "c5.jpg", "c5.jpg", "c6.jpg", "c7.jpg", "c8.jpg", "c9.jpg",
             "c10.jpg", "c11.jpg", "c12.jpg", "c13.jpg", "c14.jpg", "c15.jpg", "c16.jpg", "c17.jpg", "c18.jpg",
             "c19.jpg", "c20.jpg", "c21.jpg", "c22.jpg", "c23.jpg", "c24.jpg", "c25.jpg", "c26.png", "c27.jpg", "c28.jpg",
             "c29.jpg", "c30.png", "c31.jpg", "c32.jpg", "c33.jpg"])
        i = random.randrange(0, len(A))
        self.vd = A[i]
        self.vc = B[i]
class MyApp(App):
    def build(self):
        self.sound = SoundLoader.load("sound.wav")
        self.sound.play()
        return Mouna()
if __name__ == '__main__':
    MyApp().run()