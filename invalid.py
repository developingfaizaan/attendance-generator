from kivy.uix.screenmanager import Screen, SlideTransition

class Invalid(Screen):
    def goBack(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()