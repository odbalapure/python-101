from test_section import TestSection

class ListeningSection(TestSection):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def display_info(self):
        super().display_info()

    def start_section(self):
        print("Listening section started.")

class ReadingSection(TestSection):
    def __init__(self, name):
        super().__init__(name)

    def display_info(self):
        super().display_info()
        print("Reading Section")

    def start_section(self):
        print("Reading section started.")

class WritingSection(TestSection):
    def __init__(self, name):
        super().__init__(name)

    def display_info(self):
        super().display_info()
        print("Writing Section")

    def start_section(self):
        print("Writing section started.")

class SpeakingSection(TestSection):
    def __init__(self, name):
        super().__init__(name)

    def display_info(self):
        super().display_info()
        print("Speaking Section")

    def start_section(self):
        print("Speaking section started.")
