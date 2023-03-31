from typing import Any, Union


# Module Constants
MIDI_A440: int = 69
MIDI_MIN: int = 12
MIDI_MAX: int = 128
FREQ_A440: int = 440
NOTES_PER_OCT: int = 12
NOTE_A440: str = "A4"
NOTE_LETTERS = "CDEFGAB"
NOTE_OCTAVE_DIGITS = "0123456789"
NOTE_ACCIDENTALS = "#b+-♯♭"


class Pitch(object):
    def __init__(self, value: Union[tuple, str, int, float, None] = None) -> None:

        if isinstance(value, tuple) or isinstance(value, str):
            self.note = value
        elif isinstance(value, float) or isinstance(value, int):
            if value < MIDI_MAX:  # TODO: avoid magic numbers. Use all-cap constants.
                self.midi = value
            else:
                self.freq = value
        else:                   # TODO: must handle string first
            raise TypeError("value must be tuple, string, float or int.")

        # if isinstance(value, int) or isinstance(value, float)
        # midi = 0


    # Getter and Setter of midi (same as internal _midi)
    @property
    def midi(self) -> float:
        "Return float MIDI number of pitch."
        return self._midi

    @midi.setter
    def midi(self, m: Union[int, float]) -> None:
        """Sets a MIDI note while at the same time updating frequency and note values.
        Assumes n is a value between 12 and 127.""" # TODO: no, please just set _midi
        assert isinstance(m, int) or isinstance(m, float)
        assert MIDI_MIN <= m < MIDI_MAX  # TODO: must put n between compares. use constants.
        self._midi = float(m)

    @midi.deleter
    def midi(self) -> None:
        self._midi = 69.0  # "A4", 440 Hz 'A'
        # TODO: magic number above.
        # NOTE: contants are just variables. If in class scope, must reference with self or class name. Can define at module level to avoid saying self or Pitch.


    # Getter and Setter of frequency
    @property
    def freq(self) -> float:
        """Gets the float frequency of pitch in hertz."""
        return self._freq  # TODO: Please compute from _midi here

    @freq.setter
    def freq(self, f: Union[int, float]) -> None:
        assert isinstance(f, int) or isinstance(f, float)
        assert f > 20 < 21900  # TODO: must put f between compares
        self._midi = f
        self.convert("f", f)  # TODO: convert f to m once here and store _midi.

    @freq.deleter
    def freq(self) -> None:
        del self.midi


    # Getter and Setter of note string
    @property
    def note(self) -> tuple:
        "pitch as tuple of note string and bend float."
        return self._note  # TODO: convert _midi to note once here

    # TODO: must return a tuple with a string and a float (I updated interface.)

    @note.setter
    def note(self, n: Union[tuple, str]) -> None:
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

    def update(type, value):  # TODO: Please do conversions in getters and setters.
        """Updates all other class variables depending on the type that is sent to this method.
        For example, if type is 'f', then updates the midi and  note variable.
        Possible types:
            'f': Frequency in HZ
            'm': MIDI note number (float)
            'n': Note str: a string like 'A4'."""

        if type == "f":
            assert isinstance(value, int) or isinstance(value, float)
        elif type == "m":
            assert isinstance(value, int) or isinstance(value, float)
        elif type == "n":
            assert instance(value, str)
        else:
            raise valueError("'type' must be either 'f', 'm', or 'n'.")
