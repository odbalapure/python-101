class TestSection:
    def __init__(self, name: str) -> None:
        self.name = name
    
    def display_info(self) -> None:
        print(f"Test section: {self.name}")

    def start_section(self) -> None:
        ...
