from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.label import Label


class DynamicLabelsApp(App):

    text = StringProperty()

    def __init__(self, **kwargs):


        super().__init__(**kwargs)
        self.names = ["asmi","jay","aaish"]

    def build(self):


        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamiclabel.kv')
        self.create_labels()
        return self.root

    def create_labels(self):


        for name in self.names:
            widget_of_label = Label(text=name)
            self.root.ids.labels.add_widget(widget_of_label)


DynamicLabelsApp().run()