import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen


class ProfileWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


class volAutoBusApp(App):
    def build(self):
        return Builder.load_file('volAutoBus.kv')

if __name__ == "__main__":
    volAutoBusApp().run()
