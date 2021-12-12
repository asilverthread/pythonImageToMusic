from abc import abstractmethod

import pyaudio


class TonePlayer:
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def play_tone(self):
        pass

    @abstractmethod
    def play_tone(self, arr):
        pass

    @classmethod
    def configure_output_stream(cls, sample_rate, bool_output):
        stream = pyaudio.PyAudio().open(
            format=pyaudio.paFloat32,
            channels=1,
            rate=sample_rate,
            output=bool_output)
        return stream, sample_rate

        return stream
