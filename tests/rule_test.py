from example.rule import fizz_rule, buzz_rule
from example.value import to_value, Value


def test_fizz_rule_on_3():
    value = fizz_rule(to_value(3))
    assert value == Value(3, "Fizz")




def test_fizz_rule_on_5():
    value = fizz_rule(to_value(5))
    assert value == to_value(5)


def test_fizz_rul_on_pre():
    value = fizz_rule(Value(9, "foo"))
    expected = Value(9, "fooFizz")
    assert value == expected


class TestIntegBuzzRule:
    def test_buzz_rule(self):
        assert False
