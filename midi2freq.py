"""
MIDI to Frequency converter

A class which converts MIDI note numbers to frequency numbers.

When using this class as a function parameter as demonstrated, the function will see only the final frequency conversion,
making it easier to create and use lists of objects.

"""

# AI Disclamer:
# This code has been written with assistence from GPT-4o Mini.
# To the best of my ability, I have reviewed and tested the code before publishing,
# and made modifications whenever necessary.

from time import sleep

class GetFrequency:
    """Gets, or converts MIDI note to frequency number.

    Args:
        midi_number: The MIDI number that'll be converted to frequency."""
    
    A440 = 440.0  # Frequency of A4 in Hz
    A4_MIDI_NUMBER = 69  # MIDI number for A4

    def __init__(self, midi_number):
        self.midi_number = midi_number
        self.frequency = self.calculate_frequency()

    def calculate_frequency(self):
        # Calculate frequency using the formula
        return self.A440 * (2 ** ((self.midi_number - self.A4_MIDI_NUMBER) / 12))

    def __float__(self):
        return self.frequency

# Example usage:
def print_frequency(midi_converter):
    print(f"The frequency of MIDI note {midi_converter.midi_number} is {float(midi_converter)} Hz.")

# Create an instance of the converter
# Modified to run in a for loop to test multiple cases.

for i in range(128):
    midi_note = GetFrequency(i)
    print_frequency(midi_note)  # Output: The frequency of MIDI note 69 is 440.0 Hz.
    sleep(0.5)