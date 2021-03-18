from kivymd.app import App
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import  Builder

Window.size = (300, 500)



class VolAutoBus(BoxLayout):
    def __init__(self, **kwargs):
        super(VolAutoBus, self).__init__(**kwargs)

    def changeScreen(self,next_screen):
         if next_screen =='second':
             self.ids.kivy_screen_manager.current = 'SecondScreen'



class VolAutoBusApp(MDApp):

    def __init__(self, **kwargs):
        super(VolAutoBusApp, self).__init__(**kwargs)

    def build(self):
        return VolAutoBus()

    def getText(self):
        return ('ddddddddddddd')

    def on_ref_press(self,instance, ref):
        _dict = {1:'eeee',
                 2:'ttttt'}

        return 'tttttt'


if __name__ == '__main__':
    VolAutoBusApp().run()
