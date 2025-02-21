from pathlib import Path

class AudioFile:
    ext: str

    def __init__(self, filepath: Path) -> None:
        # Can check the file type without actually knowing which subclass it is referring to.
        if not filepath.suffix == self.ext:
            raise ValueError("Invalid file format")
        self.filepath = filepath

class MP3File(AudioFile):
    ext = ".mp3"
    def play(self) -> None:
        print(f"playing {self.filepath} as mp3")

class WavFile(AudioFile):
    ext = ".wav"
    def play(self) -> None:
        print(f"playing {self.filepath} as wav")

class OggFile(AudioFile):
    ext = ".ogg"
    def play(self) -> None:
        print(f"playing {self.filepath} as ogg")

# Following example does not extend AudioFile, but it can be interacted with in Python using the exact same interface
# This is possible due to "Duck Typing"
class FlacFile:
    def __init__(self, filepath: Path) -> None:
        if not filepath.suffix == ".flac":
            raise ValueError("Not a .flac file")
        self.filepath = filepath
    def play(self) -> None:
        print(f"playing {self.filepath} as flac")

mp3_file = MP3File(Path("song.mp3"))
wav_file = WavFile(Path("sound.wav"))
ogg_file = OggFile(Path("track.ogg"))
flac_file = FlacFile(Path("album.flac"))

audio_files: list[AudioFile] = \
    [mp3_file, wav_file, ogg_file, flac_file]

for audio in audio_files:
    audio.play()
