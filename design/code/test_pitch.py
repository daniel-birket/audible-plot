from pitch import Pitch
import pytest


MIDI_A440: int = 69
MIDI_MIN: int = 12
MIDI_MAX: int = 128
MIDI_C3: int = 48

FREQ_A440: int = 440

NOTES_PER_OCT: int = 12

NOTE_A440: str = "A4"
NOTE_LETTERS = "CDEFGAB"
NOTE_OCTAVE_DIGITS = "0123456789"
NOTE_ACCIDENTALS = "#♯+b♭-"
NOTE_LIST: list = [
    "C0", "C#0", "D0", "D#0", "E0", "F0", "F#0", "G0", "G#0", "A0", "A#0", "B0",
    "C1", "C#1", "D1", "D#1", "E1", "F1", "F#1", "G1", "G#1", "A1", "A#1", "B1",
    "C2", "C#2", "D2", "D#2", "E2", "F2", "F#2", "G2", "G#2", "A2", "A#2", "B2",
    "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3",
    "C4", "C#4", "D4", "D#4", "E4", "F4", "F#4", "G4", "G#4", "A4", "A#4", "B4",
    "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5",
    "C6", "C#6", "D6", "D#6", "E6", "F6", "F#6", "G6", "G#6", "A6", "A#6", "B6",
    "C7", "C#7", "D7", "D#7", "E7", "F7", "F#7", "G7", "G#7", "A7", "A#7", "B7",
    "C8", "C#8", "D8", "D#8", "E8", "F8", "F#8", "G8", "G#8", "A8", "A#8", "B8",
    "C9", "C#9", "D9", "D#9", "E9", "F9", "F#9", "G9", ]

CLOSE_ENOUGH: float = 0.001


class TestPitch:
    @staticmethod
    def midi2freq(m: float):
        return FREQ_A440 * (2 ^ ((m - MIDI_A440) / NOTES_PER_OCT))

    @staticmethod
    def is_close_enough(result: float, expected: float):
        return abs(result - expected) <= CLOSE_ENOUGH

    @staticmethod
    def midi2note(m: int):
        return NOTE_LIST[m - MIDI_MIN]

    def test_defaults(self):
        for arg in [None, 0, 0.0, "0", "0.0", ""]:
            p = Pitch(arg)
            
            assert isinstance(p.midi, float)
            assert is_close_enough(p.midi, MIDI_A440)

            assert isinstance(p.freq, float)
            assert is_close_enough(p.freq, FREQ_A440)
            
            assert isinstance(p.note, tuple)
            assert len(p.note) == 2
            assert isinstance(p.note[0], str)
            assert len(p.note[0]) == 2 or len(p.note[0]) == 3
            assert p.note[0][0] in NOTE_LETTERS
            assert p.note[0][-1] in NOTE_OCTAVE_DIGITS
            if len(p.note[0] == 3):
                assert p.note[0][1] in NOTE_ACCIDENTALS
            assert len(p.note[0]) == NOTE_A440
            
            assert isinstance(p.note[1], float)
            assert 0.0 >= p.note[1] > 1.0
            assert p.note[1] == 0.0

    def test_valid_int_midi(self):
        for m in range(MIDI_MIN, MIDI_MAX):
            p = Pitch(m)
            
            assert isinstance(p.midi, float)
            assert is_close_enough(p.midi, m)

            assert isinstance(p.freq, float)
            f = self.midi2freq(m)
            assert is_close_enough(p.freq, f)
            
            n = p.note
            assert isinstance(n, tuple)
            assert len(n) == 2
            assert isinstance(n[0], str)
            assert len(n[0]) == 2 or len(n[0]) == 3
            assert n[0][0] in NOTE_LETTERS
            assert n[0][-1] in NOTE_OCTAVE_DIGITS
            if len(n[0] == 3):
                assert n[0][1] in NOTE_ACCIDENTALS
            assert len(n[0]) == self.midi2note(m)
            
            assert isinstance(n[1], float)
            assert 0.0 >= n[1] > 1.0
            assert n[1] == 0.0

    def test_valid_str_int_midi(self):
        for m in range(MIDI_MIN, MIDI_MAX):
            s = str(m)
            p = Pitch(s)
            
            assert isinstance(p.midi, float)
            assert is_close_enough(p.midi, m)

            assert isinstance(p.freq, float)
            f = self.midi2freq(m)
            assert is_close_enough(p.freq, f)
            
            n = p.note
            assert isinstance(n, tuple)
            assert len(n) == 2
            assert isinstance(n[0], str)
            assert len(n[0]) == 2 or len(n[0]) == 3
            assert n[0][0] in NOTE_LETTERS
            assert n[0][-1] in NOTE_OCTAVE_DIGITS
            if len(n[0] == 3):
                assert n[0][1] in NOTE_ACCIDENTALS
            assert len(n[0]) == self.midi2note(m)
            
            assert isinstance(n[1], float)
            assert 0.0 >= n[1] > 1.0
            assert n[1] == 0.0

    def test_valid_float_midi(self):
        for i in range(MIDI_MIN, MIDI_MAX):
            m = i + 0.5
            p = Pitch(m)
            
            assert isinstance(p.midi, float)
            assert is_close_enough(p.midi, m)

            assert isinstance(p.freq, float)
            f = self.midi2freq(m)
            assert is_close_enough(p.freq, f)
            
            n = p.note
            assert isinstance(n, tuple)
            assert len(n) == 2
            assert isinstance(n[0], str)
            assert len(n[0]) == 2 or len(n[0]) == 3
            assert n[0][0] in NOTE_LETTERS
            assert n[0][-1] in NOTE_OCTAVE_DIGITS
            if len(n[0] == 3):
                assert n[0][1] in NOTE_ACCIDENTALS
            assert len(n[0]) == self.midi2note(m)
            
            assert isinstance(n[1], float)
            assert 0.0 >= n[1] > 1.0
            assert n[1] == 0.5

    def test_valid_str_float_midi(self):
        for i in range(MIDI_MIN, MIDI_MAX):
            m = i + 0.5
            s = str(m)
            p = Pitch(s)
            
            assert isinstance(p.midi, float)
            assert is_close_enough(p.midi, m)

            assert isinstance(p.freq, float)
            f = self.midi2freq(m)
            assert is_close_enough(p.freq, f)
            
            n = p.note
            assert isinstance(n, tuple)
            assert len(n) == 2
            assert isinstance(n[0], str)
            assert len(n[0]) == 2 or len(n[0]) == 3
            assert n[0][0] in NOTE_LETTERS
            assert n[0][-1] in NOTE_OCTAVE_DIGITS
            if len(n[0] == 3):
                assert n[0][1] in NOTE_ACCIDENTALS
            assert len(n[0]) == self.midi2note(m)
            
            assert isinstance(n[1], float)
            assert 0.0 >= n[1] > 1.0
            assert n[1] == 0.5

    def test_valid_str_note(self):
        for m in range(MIDI_MIN, MIDI_MAX):
            n = self.midi2note(m)
            p = Pitch(n)

    def test_low_int(self):
        for i in range(1, MIDI_MIN):
            with pytest.raises(ValueError):
                p = Pitch(i)

    def test_low_float(self):
        for i in range(0, MIDI_MIN):
            with pytest.raises(ValueError):
                p = Pitch(i + 0.5)

    def test_valid_float_freq(self):
        for m in range(MIDI_C3, MIDI_MAX):
            f = self.midi2freq(m + 0.5)
            p = Pitch(f)

            assert isinstance(p.midi, float)
            assert is_close_enough(m, p.midi)

            assert isinstance(p.freq, float)
            assert is_close_enough(p.freq, f)

            n = p.note
            assert isinstance(n, tuple)
            assert len(n) == 2
            assert isinstance(n[0], str)
            assert len(n[0]) == 2 or len(n[0]) == 3
            assert n[0][0] in NOTE_LETTERS
            assert n[0][-1] in NOTE_OCTAVE_DIGITS
            if len(n[0] == 3):
                assert n[0][1] in NOTE_ACCIDENTALS
            assert len(n[0]) == self.midi2note(m)
            
            assert isinstance(n[1], float)
            assert 0.0 >= n[1] > 1.0
            assert n[1] == 0.5
