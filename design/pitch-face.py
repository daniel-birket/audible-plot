"""Temporary module to document the Pitch class"""
from typing import Any


class Pitch(object):

    # Getter and Setter of midi (same as internal _midi)
    @property
    def midi(self) -> float:
        "float MIDI number of pitch."
        return self._midi

    @midi.setter
    def midi(self, m: float) -> None:
        assert isinstance(m, int) or isinstance(m, float)
        # assert valid 12 to 127 midi number here
        self._midi = float(m)

    @midi.deleter
    def midi(self) -> None:
        self._midi = 69.0  # "A4", 440 Hz 'A'

    # Getter and Setter of frequency
    @property
    def freq(self) -> float:
        "float frequence of pitch in hertz."
        return 0.0

    @freq.setter
    def freq(self, f: float) -> None:
        assert isinstance(f, int) or isinstance(f, float)
        # assert audible frequency range here
        self._midi = 0.0

    @freq.deleter
    def freq(self) -> None:
        del self.midi

    # Getter and Setter of note string
    @property
    def note(self) -> tuple:
        "pitch as tuple of note string and fractional note."
        return ("A4", 0.0)

    @note.setter
    def note(self, n) -> None:
        if isinstance(n, tuple):
            note_str, note_bend = n  # unpack tuple
        elif isinstance(n, str):
            note_str = n
            note_bend = 0.0
        assert isinstance(note_str, str), "Note string must be a string like 'A4'."
        assert isinstance(note_bend, float), "Note bend must be a float like 0.0."
        assert 0.0 <= note_bend < 1.0, "Note bend must 0.0 or between 0.0 and 1.0."

        self._midi = 0.0

    @note.deleter
    def note(self) -> None:
        del self.midi
    
    def __init__(self, value: Any = None) -> None:
        pass
        if isinstance(value, tuple) or isinstance(value, str):
            self.note = value
        elif isinstance(value, float) or isinstance(value, int):
            if value < 128.0:
                self.midi = value
            else:
                self.freq = value
        else:
            raise TypeError("value must be tuple, string, float or int.")

        # if isinstance(value, int) or isinstance(value, float)
        midi = 0

    def __str__(self) -> str:
        """Return string of note and bend."""
        n = self.note
        return n[0] + "+" + str(n[1])

    def __repl__(self) -> str:
        """Return represenation of Pitch."""
        return type(self).__name__ + "(" + self.midi + ")"
