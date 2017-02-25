import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button

class UI(FloatLayout):
    def __init__(self, **kwargs):
        super(UI, self).__init__(**kwargs)
        button = Button(text='Do magic', size_hint=(.6, .6), pos_hint={'x':.2, 'y':.2})
        self.add_widget(button)

class Launcher(App):
    def build(self):
        return UI()

if __name__ == '__main__':
    Launcher().run()
