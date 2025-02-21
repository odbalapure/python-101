from typing import Protocol

class Playable(Protocol):
    def play(self) -> None:
        ...

class MP3File:
    def play(self) -> None:
        print("Playing MP3 file")

class OggFile:
    def play(self) -> None:
        print("Playing OGG file")

class NotPlayable:
    pass

def play_audio(audio: Playable) -> None:
    audio.play()

# Running the code
mp3 = MP3File()
ogg = OggFile()
# not_audio = NotPlayable()
# play_audio(not_audio)  # This will work at runtime but will fail during type checking if using Mypy

all_files: list[Playable] = [mp3,  ogg]
for file in all_files:
    file.play()
