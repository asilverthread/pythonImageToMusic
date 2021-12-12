import math


def calc_tone(amplitude, frequency, sample_rate):
    n = int(sample_rate * .05)
    t = int(frequency * .05)  # repeat for T cycles
    dt = 1.0 / sample_rate

    tone = (amplitude * math.sin(
        2 * math.pi * 440 * (2 ** (1 / 12)) ** round((math.log(frequency / 440)) / (
            math.log((2 ** (1 / 12))))) * n * dt)
            for n in range(n))
    return tone
