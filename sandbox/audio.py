try:
    import numpy as np
    import sounddevice as sd
except:
    print("I couldn't find either numpy or sounddevice on your system. Please make sure you have them installed. Use\npip install numpy\npip install sounddevice")
from time import sleep

def slprint(string = ''):
    sleep(1)
    print(string)
    sleep(1)

class Synth:
    def __init__(self, frequency, duration = 500, volume = 0.2):
        """Initializes a synth object if given a frequency, a duration (default 500  milliseconds, and a volume of 0.2."""

        # I would like to thank ChatGPT/GPT3 for contributing most of the code in this function.
        # It was slitely modified to be used within a class object.
        self.frequency = frequency # inHz
        self.duration = duration / 1000 # in milliseconds
        self.volume = volume
        self.samples = int(self.duration * 44100) # 44100 samples per second
        self.t = np.linspace(0, self.duration, self.samples, False)
        self.sign = self.volume * np.sin(self.frequency * self.t * 2 * np.pi)
        self.square = self.volume * np.sign(np.sin(self.frequency * self.t * 2 * np.pi))
        self.sawtooth = self.volume * (2 * (self.frequency * self.t - np.floor(self.frequency * self.t + 0.5)))

    def play(self, sound):
        """Plays the given wave, e.g. self.square, using sounddevice as sd."""
        sd.play(sound, 44100)
        sd.wait()


freqs = [220, 110, 330, 165] * 3 + [220, 110]
durs = [500] * 13 + [1500]
objs = [Synth(freqs[i], durs[i]) for i in range(14)]

slprint("Sign waves")

for i in objs:
    i.play(i.sign)

slprint("Square waves")

for i in objs:
    i.play(i.square)

slprint("Sawtooth waves")

for i in objs:
    i.play(i.sawtooth)


slprint("Done!")
