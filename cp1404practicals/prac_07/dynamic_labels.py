"""
CP1404/CP5632 Practical
Kivy GUI program to concert miles to km
Lee Crawford, IT@JCU
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label


class MilesConversionKmApp(App):
    """MilesConversionKmApp is a Kivy App for converting miles to kms"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]
        
    def build(self):
        Window.size = (400, 200)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('dynamic_widgets.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):

        """Create labels from a list and add them to the GUI."""
        for name in self.names:
            temp_label = Label(text=name)
            temp_label.bind(on_release=self)
            self.root.ids.entries_box.add_widget(temp_label)
