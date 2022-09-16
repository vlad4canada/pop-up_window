# https://www.youtube.com/watch?v=PpLuyOzCKTQ

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup
from kivy.uix.floatlayout import FloatLayout

class Widgets(Widget):
        def btn(self):
            show_popup()

class P(FloatLayout):
    pass

class MyApp(App):
        def build (self):
            return Widgets()

def show_popup():
    show = P()
    popupWindow = Popup(title = "Popup Window", content = show, size_hint = (None,None), size = (400,400))
    popupWindow.open()




if __name__ == "__main__":
    MyApp().run()




