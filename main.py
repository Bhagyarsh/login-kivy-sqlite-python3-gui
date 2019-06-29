
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.properties import StringProperty, ObjectProperty,AliasProperty,NumericProperty
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.app import App
from kivy.uix.popup import Popup
from dbcall import get_password,insertintologin,return_16_digit_password,set_password
from kivy.config import Config
Config.set('graphics','resizable', False)

def update_window_size(width, height):
    Window.size = (width, height)

class AccinfoPopup(Popup):
    manager = ObjectProperty()
    title = StringProperty()
    label = StringProperty()
    def __init__(self, title, label,manager, **kwargs):
        super(AccinfoPopup, self).__init__(**kwargs)
        self.manager = manager
        self.set_description(title, label)
    def set_description(self, title, label):
        self.title = title
        self.label = label



class CreateUserScreen(Screen):
    
    def __init__(self,name):
        self.name = name
        super(CreateUserScreen, self).__init__()


    def on_call_popup(self,label):
        self.pops=AccinfoPopup('USER', label,self.manager)
        self.pops.open()

    def on_pre_enter(self):
        update_window_size(300, 600) 

    def makeInputTextNull(self):
        self.ids.usernameForNewUser.text = ''
        self.ids.Newpassword.text = ''
        self.ids.confirmdNewpassword.text = ''
        self.ids.digit_key.text = ''

    def createNewUser(self):
        userNameForNewUser = self.ids.usernameForNewUser.text.lstrip()
        Newpassword = self.ids.Newpassword.text.lstrip()
        confirmdNewpassword = self.ids.confirmdNewpassword.text.lstrip()
        digit_key = self.ids.digit_key.text.lstrip()
        print(userNameForNewUser)
        print(Newpassword)
        print(confirmdNewpassword)
        print(digit_key)
        if digit_key == return_16_digit_password():
            if userNameForNewUser and Newpassword:
                if Newpassword == confirmdNewpassword:
                    user,LabelText = insertintologin(userNameForNewUser,Newpassword)
                    if user:
                        self.makeInputTextNull()
                        self.on_call_popup(LabelText)
        if user:
            self.manager.current = 'Login'
class ForgotpaswordScreen(Screen):
    def __init__(self,name):
        self.name = name
        super(ForgotpaswordScreen, self).__init__()
        # update_window_size(250, 500)
    def on_call_popup(self,label):
        self.pops=AccinfoPopup('USER', label,self.manager)
        self.pops.open()
    def createNewUser(self):
        userNameForNewUser = self.ids.usernameForNewUser.text.lstrip()
        Newpassword = self.ids.Newpassword.text.lstrip()
        confirmdNewpassword = self.ids.confirmdNewpassword.text.lstrip()
        digit_key = self.ids.digit_key.text.lstrip()
        print(userNameForNewUser)
        print(Newpassword)
        print(confirmdNewpassword)
        print(digit_key)
        if digit_key == return_16_digit_password():
            if userNameForNewUser and Newpassword:
                if Newpassword == confirmdNewpassword:
                    user,LabelText = insertintologin(userNameForNewUser,Newpassword)
                    if user:
                        self.makeInputTextNull()
                        self.on_call_popup(LabelText)
        if user:
            self.manager.current = 'Login'
    def makeInputTextNull(self):
        self.ids.usernameForgetpassword.text = ''
        self.ids.NewpasswordFornew.text = ''
        self.ids.confirmdNewpasswordForNew.text = ''
        self.ids.digit_key_for_new_password.text = ''
    
    def on_pre_enter(self):
        update_window_size(300, 600)

  
    def change_password(self,username=None):
        usernameForgetpassword = self.ids.usernameForgetpassword.text.lstrip()
        NewpasswordFornew = self.ids.NewpasswordFornew.text.lstrip()
        digit_key_for_new_password = self.ids.digit_key_for_new_password.text.lstrip()
        confirmdNewpasswordForNew = self.ids.confirmdNewpasswordForNew.text.lstrip()
        print(usernameForgetpassword)
        print(NewpasswordFornew)
        print(digit_key_for_new_password)
        print(confirmdNewpasswordForNew)
        if digit_key_for_new_password == return_16_digit_password():
            if NewpasswordFornew and confirmdNewpasswordForNew:
                if NewpasswordFornew == confirmdNewpasswordForNew:
                    user,password_changed = set_password(usernameForgetpassword,NewpasswordFornew)
                    print(user,password_changed)
        if user:
            self.on_call_popup(password_changed)
    # Config.set('graphics', 'resizable', False)
class Manager(ScreenManager):
    screen_one = ObjectProperty(None)
    screen_two = ObjectProperty(None)
class LoginScreen(Screen):

    def __init__(self,name):
        super(LoginScreen, self).__init__()
        self.name = name
        # Change login screen size in it's __init__
        
    def on_pre_enter(self):
        update_window_size(275, 500)
    def makeInputTextNull(self):
        self.ids.username.text = ''
        self.ids.password.text = ''

    def login(self):
        usernameInput = self.ids.username.text.lstrip()
        passwordInput = self.ids.password.text.lstrip()
        user,password = get_password(usernameInput)
        if user:
            if password == passwordInput:
                print("login")
                self.ids.loginError.text = ""
            else:
                self.ids.loginError.text = "password incorrect !"
        else:
            self.ids.loginError.text = "User not found"
        
class MainScreenWidgetApp(App):
    def build(self):
        self.title = 'Login'
        sm = Manager()
        sm.add_widget(LoginScreen(name="Login"))
        sm.add_widget(ForgotpaswordScreen(name="Forgotpassword"))
        sm.add_widget(CreateUserScreen(name="CreateUser"))
        return sm

MainScreenWidgetApp().run()