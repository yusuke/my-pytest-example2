from typing import Callable

from example.value import Value

Rule = Callable[[Value], Value]


def fizz_rule(value: Value) -> Value:
    if value.original % 3 != 0:
        return value
    else:
        if value.text is None:
            return Value(value.original, "Fizz")
        else:
            return Value(value.original, f"{value.text}Fizz")


def buzz_rule(value: Value) -> Value:
    if value.original % 5 != 0:
        return value
    else:
        if value.text is None:
            return Value(value.original, "Buzz")
        else:
            return Value(value.original, f"{value.text}Buzz")
