from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.screenmanager import NoTransition
import requests


from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import NoTransition
import requests


class MainPage(Screen):
    pass


class ExercisePage(Screen):
    link = ObjectProperty(None)

    def test(self):
        # link = self.manager.get_screen('mainpage')
        print(self.link)
        # a = requests.get(f'{link.ids.http.text}/gpio12On')

    def testt(self):
        # link = self.manager.get_screen('mainpage')
        print(self.link)
        # a = requests.get(f'{link.ids.http.text}/gpio12Off')


class MyApp(App):
    pass


if __name__ == '__main__':
    MyApp().run()


if __name__ == '__main__':
    MyApp().run()