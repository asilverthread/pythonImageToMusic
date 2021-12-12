import math
import struct
from abc import ABC

import pyaudio

from p2m import ToneUtils
from p2m.TonePlayers.TonePlayer import TonePlayer


class DefaultTonePlayer(TonePlayer, ABC):

    def __init__(self):
        pass

    def play_tone(self, arr):
        stream, sample_rate = TonePlayer.configure_output_stream(48000, 1)
        frequency = arr[0]
        amplitude = 3
        duration = arr[2]
        tone = ToneUtils.calc_tone(amplitude, frequency, sample_rate)

        data = b''.join(struct.pack('f', samp) for samp in tone)
        #print(data)
        for n in range(int(frequency * .05)):
            stream.write(data)
            #print(data)
            pass
