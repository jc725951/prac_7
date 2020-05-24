from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    text = StringProperty()

    def __init__(self, **kwargs):


        super().__init__(**kwargs)
        self.names = ["ok","anil","aaish"]

    def build(self):


        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_labels()
        return self.root

    def create_labels(self):


        for name in self.names:
            label_widget = Label(text=name)
            self.root.ids.labels.add_widget(label_widget)


DynamicLabelsApp().run()