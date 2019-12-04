from kivy.app import App
from kivy.base import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image

Builder.load_file('ChampionsOfITK.kv')

class MainScreen(FloatLayout):
    pass
    #def __init__(self, **kwargs):

    #def do_start(self):
        #self.remove_widget(StartScreen)
        #self.add_widget(GameScreen)

class StartScreen(FloatLayout):
    pass

class ChampionsOfITK(App):

    def build(self):
        return MainScreen()

ChampionsOfITK().run()
