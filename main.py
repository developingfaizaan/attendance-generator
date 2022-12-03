from kivy.app import App
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition

# Importing Screen Files
from stream import Stream
from attendence import Attendence
from invalid import Invalid

class Login(Screen):
    def do_login(self, loginText, passwordText):
        app = App.get_running_app()

        app.username = loginText
        app.password = passwordText

        if (app.username == "admin" and app.password == "maaz"):
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'stream'
        else:
            self.manager.transition = SlideTransition(direction="right")
            self.manager.current = 'invalid'

    def resetForm(self):
        self.ids['login'].text = ""
        self.ids['password'].text = ""

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    def build(self):
        manager = ScreenManager()

        manager.add_widget(Login(name='login'))
        manager.add_widget(Stream(name='stream'))
        manager.add_widget(Invalid(name='invalid'))
        manager.add_widget(Attendence(name='attendence'))

        return manager


if __name__ == '__main__':
    LoginApp().run()