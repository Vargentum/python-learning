from .time import Time


class TestTime:

    def test_should_be_creatable(self):
        time = Time(24, 12, 12)
        assert time.hours == 24
        assert time.minutes == 12
        assert time.seconds == 12

    def test_should_be_comparable(self):
        a = Time(12, 0, 0)
        b = Time(12, 1, 0)
        assert a < b
        assert not a > b
        assert a != b

        c = Time(12, 0, 0)
        assert a == c

    def test_should_be_convertible_to_seconds(self):
        a = Time(0, 0, 60)
        b = Time(1, 1, 1)
        assert a.convert_to_seconds() == 60
        assert b.convert_to_seconds() == 1 + 1*60 + 1*3600
