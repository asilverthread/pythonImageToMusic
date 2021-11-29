from __future__ import division
from pyaudio import PyAudio
import pyaudio
import math
import struct
import numpy
import scipy
import scipy.misc
import imageio
from math import log

# at normal tempo a half note lasts for half a second

AMPLITUDE = 1
# Following method takes in params individually and PLAYS a note (old way of doing it for ex1 and ex2)
def play_tone_2(frequency, amplitude, duration, fs, stream):
        N = int(fs / frequency)
        T = int(frequency * duration)  # repeat for T cycles
        dt = 1.0 / fs

        tone = (amplitude * math.sin(2 * math.pi * frequency * n * dt)
                for n in range(N))

        data = ''.join(struct.pack('f', samp) for samp in tone)
        for n in range(T):
            stream.write(data)
# Following method takes in params as list for F,A,D, and PLAYS a note (new way of doing it for ex3)
def play_tone_1(FADlist, fs, stream):
    #if you do a fancy try catch or if else structure here you can make it so
    #that the older examples with just one argument work as well, IE setting defaults for 
    #each of the values frequency, amplitude, and duration
    frequency = FADlist[0]
    # I'm gonna try and tune this real quick
    # going with 213 as our input

    amplitude = FADlist [1]
    duration = FADlist[2]

    N = int(fs / frequency)
    T = int(frequency * duration)  # repeat for T cycles
    dt = 1.0 / fs

    tone = (amplitude * math.sin(2 * math.pi * frequency * n * dt)
            for n in range(N))

    data = b''.join(struct.pack('f', samp) for samp in tone)
    for n in range(T):
        stream.write(data)

# This is take two, a rewrite trying to understand the specifics of how pyaudio goes and makes a soundwave
def play_tone(FADlist, fs, stream):
    # if you do a fancy try catch or if else structure here you can make it so
    # that the older examples with just one argument work as well, IE setting defaults for
    # each of the values frequency, amplitude, and duration
    frequency = FADlist[0]
    # I'm gonna try and tune this real quick
    # going with 213 as our input

    amplitude = 3
    duration = FADlist[2]

    N = int(fs * .05)
    T = int(frequency * .05)  # repeat for T cycles
    dt = 1.0 / fs

    tone = (amplitude * math.sin(
        2 * math.pi * 440 * (2 ** (1 / 12)) ** round((log(frequency / 440)) / (log((2 ** (1 / 12))))) * n * dt)
            for n in range(N))

    data = b''.join(struct.pack('f', samp) for samp in tone)
    for n in range(T):
        stream.write(data)


fs = 48000
p = pyaudio.PyAudio()
stream = p.open(
    format=pyaudio.paFloat32,
    channels=1,
    rate=fs,
    output=True)


# Simple addition for IDIOTS
def RGBToHertzExOne(RedVal, GreenVal, BlueVal):
    hertz = RedVal + GreenVal + BlueVal;
    return hertz


# Some kinda fancier crap where other stuff does other stuff (still not cool)
def RGBToHertzExTwo(RedVal, GreenVal, BlueVal):
    hertz = ((RedVal + 1) * math.ceil(((GreenVal + 1) / 128)) * math.ceil(((BlueVal + 1) / 64)))
    return hertz


# we're starting to do some cool stuff thats what we are starting to do
def RGBToHertzExThree(R, G, B):
    hertz = 440 * (2 ** (1 / 12)) ** round((log(R / 440)) / (log((2 ** (1 / 12)))))
    duration = .5  # something about G
    # we need to map duration to actual note values
    amplitude = AMPLITUDE  # some nonsense about B
    coolShit = [hertz, amplitude, duration]
    # start thinking about some cool shenanigans we could do with the alpha channel for when we are working with digital art
    return coolShit


# play_tone(RGBToHertzExTwo(227,173,235),AMPLITUDE,.75,fs,stream) <- That doodoo was for the second example, we are moving on now boys

# play_tone(RGBToHertzExThree(440, 1, 1),fs,stream)

arr = imageio.imread('SampleImages/oneCoolGuy.jpg')

a = 0

for x in arr:
    # break #uncomment to unskip
    for n in x:
        print(n)
        play_tone(n, fs, stream)
    print(a)
    break


