from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen


class LoginScreen(Screen):
    def clear(self):
        self.ids.welcome_label.text = "WELCOME"
        self.ids.user.text = ""
        self.ids.password.text = ""

    def signin(self):
        username = self.ids.user.text
        password = self.ids.password.text
        if username == "123" and password == "123":
            app = MDApp.get_running_app()
            app.root.current = 'main'
        else:
            self.ids.welcome_label.text = "incorrect please try again"

    def signup(self):
        app2 = MDApp.get_running_app()
        app2.root.current = 'SignUp'


class SignUpScreen(Screen):
    def created(self):
        self.ids.labels.text = "Account created!"
        app3 = MDApp.get_running_app()
        app3.root.current = 'login'


class MainPage(Screen):
    def TextToSpeech(self, text_field, is_enter):
        if is_enter:
            output_label = self.ids.output_label
            output_label.text = text_field.text


class WindowManager(ScreenManager):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='login'))
sm.add_widget(SignUpScreen(name='SignUp'))
sm.add_widget(MainPage(name='main'))


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"
        return Builder.load_file('login.kv')


MainApp().run()
