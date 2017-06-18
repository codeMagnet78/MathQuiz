from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from arithmetic import Arithmetic

import webbrowser

class MathQuizRoot(BoxLayout):

    math_screen = ObjectProperty(None)
    
    def __init__(self, **kwargs):
        super(MathQuizRoot, self).__init__(**kwargs)
        # list of previous screens
        self.screen_list = []

    def changeScreen(self, next_screen):
        print('I am here')
        operations = "addition substraction mulitplication division".split()
        question = None

        # if screen is not already in the list of prvious screens
        if self.ids.screen_manager.current not in self.screen_list:
            self.screen_list.append(self.ids.screen_manager.current)
            
        if next_screen == "about this app":
            self.ids.screen_manager.current = 'about_screen'
        else:
            self.math_screen.question_text = next_screen
            self.ids.screen_manager.current = 'math_screen'

    def onBackBtn(self):
        # Check if there is any screen to go back to
        if self.screen_list:
            self.ids.screen_manager.current = self.screen_list.pop()
            # we do not want to close
            return True
        # No more screen to go
        return False

class MathScreen(Screen, Arithmetic):

    def __init__(self, *args, **kwargs):
        super(MathScreen, self).__init__(*args, **kwargs)

class MathQuizApp(App):
    def __init__(self, **kwargs):
        super(MathQuizApp, self).__init__(**kwargs)
        Window.bind(on_keyboard=self.onBackBtn)

    def onBackBtn(self, window, key, *args):
        # user press back button
        if key == 27:
            return self.root.onBackBtn()

    def build(self):
        return MathQuizRoot()

    def getText(self):
        return ("Hey There!\nThis App was built using"
                "[b][ref=kivy]Kivy[/ref][/b]\n"
                "Feel free to look at the source code ")
    def on_ref_press(self, instance, ref):
        _dict = {"kivy": "http://kivy.org"}

        webbrowser.open(_dict[ref])
        
if __name__ == '__main__':
    MathQuizApp().run()
