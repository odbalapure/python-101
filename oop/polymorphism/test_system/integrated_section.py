from test_section import TestSection
from all_sections import *

class IntegratedSection(ReadingSection, ListeningSection):
    def __init__(self, name):
        super().__init__(name)

    def display_info(self):
        super().display_info()
        print("Integrated Section")
