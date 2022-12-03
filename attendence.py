from kivy.uix.screenmanager import Screen, SlideTransition

class Attendence(Screen):
    
    def getAttendence(self): 
         stream = self.manager.get_screen('stream').ids.stream_dropdown.text
         year = self.manager.get_screen('stream').ids.year_dropdown.text
         self.ids.mainlabel.text = f'{year} - {stream}'

        
    def logout(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()
        

    def goback(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'stream'