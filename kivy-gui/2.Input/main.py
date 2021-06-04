import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2

        self.add_widget(Label(text="Name: "))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Age: "))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)

        self.add_widget(Label(text="Gender: "))
        self.gender = TextInput(multiline=False)
        self.add_widget(self.gender)

        self.submit = Button(text="Submit", font_size=32)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)


    def press(self, instance):
        name = self.name.text
        age = self.age.text
        gender = self.gender.text

        self.add_widget(Label(text=f"Your name is {name} and {age} years old, and you are a {gender}"))

        self.name.text = ''
        self.age.text = ''
        self.gender.text = ''


class MyApp(App):
    def build(self):
        return MyGridLayout()

if __name__ == '__main__':
    MyApp().run()