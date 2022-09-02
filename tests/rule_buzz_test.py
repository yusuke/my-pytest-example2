from example.rule import buzz_rule
from example.value import to_value, Value


class TestBuzzRule:
    def test_on_5(self):
        value = buzz_rule(to_value(5))
        assert value == Value(5, "Buzz")

    def test_on_3(self):
        value = buzz_rule(to_value(3))
        assert value == to_value(3)

    def test_on_pre(self):
        value = buzz_rule(Value(30, "Fizz"))
        assert value == Value(30, "FizzBuzz")
