"""
Convert miles to kilograms
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


CONVERSION = 1.60349


class MilesConverterApp(App):
    """kIVY app for converting miles to kilometres."""
    output_km = StringProperty()

    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, text):
        """Handle calculation(could be button press or other call.)"""
        print("handle calculate")
        miles = self.convert_to_number(text)
        self.update_result(float(miles))

    def handle_increment(self, text, change):
        """Handle up/down button press, update the text input with new value."""
        print("handle increment")
        miles = self.convert_to_number(text) + change
        self.root.ids.input_miles.text = str(miles)

    def update_result(self, miles):
        """Convert mile to kilometer."""
        print("update")
        self.output_km = str(miles * CONVERSION)

    @staticmethod
    def convert_to_number(text):
        """Convert text to float or 0.0 if invalid."""
        try:
            return float(text)
        except ValueError:
            return 0.0


MilesConverterApp().run()