from kivy.app import App
from kivy.base import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image

Builder.load_string("""
<rootwi>:
    orientation:'vertical'

        """)

class StartScreen(GridLayout):

    def __init__(self, **kwargs):
        super(StartScreen, self).__init__(**kwargs)
        self.cols = 1
        #self.image = Image(source="FantasyImage.jpg")
        self.createButton = Button(text="Create Character")
        self.loadButton = Button(text="Load Character")
        self.startButton = Button(text="Start playing")
        #self.add_widget(self.image)
        self.add_widget(self.createButton)
        self.add_widget(self.loadButton)
        self.add_widget(self.startButton)

class ChampionsOfITK(App):

    def build(self):
        return StartScreen()

ChampionsOfITK().run()
