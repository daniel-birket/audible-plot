import pitch
import pytest

class TestPitch:

    def test_defaults(self):
        arg_list = [0, 0.0, "0", "0.0", ""]
        for arg in arg_list:
            p = Pitch(arg)
            assert isinstance(p.midi, float)
            assert p.midi == 69.0

    def test_valid_int_midi(self):
        arg_list = range(12, 128)
        for i in arg_list:
            p = Pitch(i)
            assert isinstance(p.midi, float)
            assert p.midi == i

    def test_valid_float_midi(self):
        arg_list = range(12, 128)
        for i in arg_list:
            m = i+0.5
            p = Pitch(m)
            assert isinstance(p.midi, float)
            assert p.midi == m

    def test_low_int(self):
        for i in range(1,12):
            with pytest.raises(ValueError):
                p = Pitch(i)

    def test_low_float(self):
        for i in range(0,12):
            with pytest.raises(ValueError):
                p = Pitch(i+0.5)

    def test_valid_float_freq(self):
        for m in range(47, 128):
            f = 440.0 * 2^((m - 69)/12)
            p = Pitch(f)
            assert abs(p.midi - m) <= 0.01
