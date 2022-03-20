from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import NoTransition
import requests


from kivy.app import App
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, ObjectProperty


class MainPage(Screen):
    pass


class ExercisePage(Screen):

    def test(self):
        self.manager.current = "mainpage"


class MyApp(App):
    pass


if __name__ == '__main__':
    MyApp().run()