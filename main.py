import kivy

class HelloWorld(kivy.app.App):
    def build(self):
        return kivy.uix.Label(text='Hello world')

if __name__ == '__main__':
    HelloWorld().run()
