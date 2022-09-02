from typing import NewType, Optional

FizzBuzzValue = NewType('FizzBuzzValue', str)


class Value:
    def __init__(self, original: int, text: Optional[str]):
        self.original = original
        self.text = text

    def __str__(self) -> str:
        if self.text is None:
            return f"{self.original}"
        else:
            return self.text

    def __eq__(self, other):
        if other is None or (not isinstance(other, Value)):
            return False
        if self.original != other.original:
            return False
        if self.text is None and other.text is None:
            return True
        return self.text == other.text

    def fizz_buzz_value(self) -> FizzBuzzValue:
        return FizzBuzzValue(self.__str__())


# noinspection PyTypeChecker
def to_value(original: int) -> Value:
    return Value(original, None)
