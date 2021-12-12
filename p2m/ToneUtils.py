import math


def calc_tone(amplitude, frequency, sample_rate):
    frequency += 1
    n = int(sample_rate * .05)
    t = int(frequency * .05)
    dt = 1.0 / sample_rate
    #mult = 8.0

    # tone = (amplitude * math.sin(
    #    2 * math.pi * 440 * (2 ** (1 / 12)) ** round((math.log((frequency * mult) / 440)) / (
    #        math.log((2 ** (1 / 12))))) * n * dt)
    #        for n in range(n))

    tone = (amplitude * math.sin(
        2 * math.pi * 440 * (2 ** (1 / 12)) ** round((frequency-128)/5.33) * n * dt)
            for n in range(n))
    print(frequency)
    print(round((frequency-128)/5.33))
    # for samp in tone:
    #    print(samp)

    return tone
