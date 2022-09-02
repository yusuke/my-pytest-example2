from example.value import Value, to_value


def mkValue(v: int) -> Value:
    return Value(v, None)


def test_mkValue():
    value = mkValue(20)
    v = to_value(20)
    assert value == v


def test_mkValue2():
    mv = mkValue(200)
    tv = to_value(100)
    assert mv == tv


class TestValue:
    def test_something(self):
        value = to_value(10)
        assert value.text is None
        assert value.original == 10

    def test_complete(self):
        value = Value(10, "foo")
        assert value.original == 10
        assert value.text == "foo"

    def test_str_original(self):
        value = to_value(2)
        assert f"{value}" == "2"
        assert value.fizz_buzz_value() == "2"

    def test_str_text(self):
        value = Value(5, "bar")
        assert f"{value}" == "bar"
        assert value.fizz_buzz_value() == "bar"
