from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class MathQuizRoot(BoxLayout):
    def __init__(self, **kwargs):
        super(MathQuizRoot, self).__init__(**kwargs)


class MathQuizApp(App):
    def __init__(self, **kwargs):
        super(MathQuizApp, self).__init__(**kwargs)

    def build(self):
        return MathQuizRoot()

if __name__ == '__main__':
    MathQuizApp().run()
