"""
CP1404/CP5632 Practical
Kivy GUI program to concert miles to km
Lee Crawford, IT@JCU
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.app import StringProperty

__author__ = 'Lee Crawford'
CONVERSION_RATE = 1.60934


class MilesConversionKmApp(App):
    """MilesConversionKmApp is a Kivy App for converting miles to kms"""
    message = StringProperty()

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, increment):
        try:
            if increment == -1:
                result = int(self.root.ids.input_number.text) - 1
            else:
                result = int(self.root.ids.input_number.text) + 1
            self.root.ids.input_number.text = str(result)
        except ValueError:
            self.root.ids.input_number.text = str(0 + increment)

    def convert_miles_to_km(self, mile):
        try:
            conversion = mile * CONVERSION_RATE
            self.message = str(conversion)
        except ValueError:
            self.message = str(0.0)


MilesConversionKmApp().run()
