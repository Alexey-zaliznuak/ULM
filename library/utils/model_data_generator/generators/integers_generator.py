from .field_generator import FieldGenerator
from random import randint


class IntegerGenerator(FieldGenerator):
    def __init__(self, mn: int = -10**9, mx: int = 10**9):
        self.mn = mn
        self.mx = mx

        assert mn < mx, "Invalid value: min value is greater than max."

    def __call__(self) -> int:
        return randint(self.mn, self.mx)


class PositiveIntegerGenerator(IntegerGenerator):
    def __init__(self, mn: int = 1, mx: int = 10 ** 9):
        assert mn > 0, f'Invalid minimal value for positive int: "{mn}".'

        super().__init__(mn, mx)
