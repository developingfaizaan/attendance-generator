from kivy.uix.screenmanager import Screen, SlideTransition

class Stream(Screen):
    def stream_clicked(self, value):
        self.ids.stream_label.text = f'You Selected: {value}'

    def year_clicked(self, value):
        self.ids.year_label.text = f'You Selected: {value}'

    def getAttendence(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'attendence'