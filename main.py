import kivy
kivy.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

# Import your game center functions here

class GameCenterApp(App):
    def build(self):
        root = BoxLayout(orientation='vertical')
        title_label = Label(text="Game Center", size_hint=(1, 0.2))
        menu_button = Button(text="Open Game Center", on_press=self.open_game_center, size_hint=(1, 0.8))

        root.add_widget(title_label)
        root.add_widget(menu_button)

        return root

    def open_game_center(self, instance):
        # Add code to open your game center here

if __name__ == '__main__':
    GameCenterApp().run()
