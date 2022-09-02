import pytest


class FizzBuzzError(Exception):
    def __init__(self, *args: object) -> None:
        pass


def raiseException():
    raise FizzBuzzError("foo")


def test_raise():
    with pytest.raises(FizzBuzzError):
        raiseException()


def test_invalid_error():
    with pytest.raises(FileExistsError):
        raiseException()


def test_without_guard():
    raiseException()
