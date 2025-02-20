from typing import Optional

class Formatter:
    def format(sef, string: str) -> str:
        pass

def format_string(string: str, formatter: Optional[Formatter] = None) -> str:
    class DefaulFormatter(Formatter):
        def format(self, string: str) -> str:
            return str(string).title()
        
    if not formatter:
        formatter = DefaulFormatter()
    return formatter.format(string)

hello_string = "hello world, how are you today?"
print(f"input: {hello_string}")
print(f"output: {format_string(hello_string)}")
