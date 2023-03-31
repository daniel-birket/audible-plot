from typing import Any

class Pitch(object):

    def __init__(self, value : Any = None) -> None:

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
        # midi = 0

    # Getter and Setter of midi (same as internal _midi)
    @property
    def midi(self) -> float:
        "float MIDI number of pitch."
        return self._midi

    @midi.setter
    def midi(self, m: float) -> None:
        """Sets a MIDI note while at the same time updating frequency and note values.
        Assumes n is a value between 12 and 127."""
        assert isinstance(m, int) or isinstance(m, float)
        assert n > 12 < 127
        self._midi = float(m)

    @midi.deleter
    def midi(self) -> None:
        self._midi = 69.0         # "A4", 440 Hz 'A'


    # Getter and Setter of frequency
    @property
    def freq(self) -> float:
        """Gets the float frequency of pitch in hertz."""
        return self._freq

    @freq.setter
    def freq(self, f: float) -> None:
        assert isinstance(f, int) or isinstance(f, float)
        assert f > 20 < 21900 
        self._midi = f
        self.convert('f', f)

    @freq.deleter
    def freq(self) -> None:
        del self.midi


    # Getter and Setter of note string
    @property
    def note(self) -> str:
        "note string of pitch."
        return self._note

    @note.setter
    def note(self, n) -> None:
        if isinstance(n, tuple):
            note_str, note_bend = n # unpack tuple
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

    def update(type, value):
        """Updates all other class variables depending on the type that is sent to this method.
        For example, if type is 'f', then updates the midi and  note variable.
        Possible types:
            'f': Frequency in HZ
            'm': MIDI note number (float)
            'n': Note str: a string like 'A4'."""

        if type == 'f':
            assert isinstance(value, int) or isinstance(value, float)
        elif type == 'm':
            assert isinstance(value, int) or isinstance(value, float)
        elif type == 'n':
            assert instance (value, str)
        else:
            raise valueError("'type' must be either 'f', 'm', or 'n'.")