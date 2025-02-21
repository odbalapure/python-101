from test_section import TestSection
from all_sections import *
from integrated_section import IntegratedSection

def main_section(section):
    section.display_info()
    section.start_section()

listening = ListeningSection("Listening Test")
reading = ReadingSection("Reading Test")
writing = WritingSection("Writing Test")
speaking = SpeakingSection("Speaking Test")
integrated = IntegratedSection("Integrated Test")

sections: list[TestSection] = [listening, reading, writing, speaking, integrated]

print("*" * 98)
print("\t\t\t\t\t Testing System")
print("*" * 98)

for section in sections:
    main_section(section)
