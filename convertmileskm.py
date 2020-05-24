from kivy.app import App
from kivy.lang import Builder
from kivy.app import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    result = StringProperty()

    def build(self):

        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.take_validate_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):

        value = self.take_validate_miles() + change
        self.root.ids.input_miles.text = str(value)
        self.handle_calculate()

    def take_validate_miles(self):

        try:
            value = (self.root.ids.input_miles.text)
            return value
        except ValueError:
            return 0


MilesConverterApp().run()