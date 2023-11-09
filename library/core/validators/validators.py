import validators
from typing import Any
from library.core.exceptions import ValidationError


class ValueValidator:
    def __init__(self, mn: int = None, mx: int = None) -> None:
        if not (mn or mx):
            raise AttributeError('mn or mx must be set.')
        if mx and mn and mx < mn:
            raise ValueError('mx nust be greater than mn')

        self.mx = mx
        self.mn = mn

    def __call__(self, value):
        errors = []
        if self.mx and value > self.mx:
            raise ValidationError(
                f'Value of this field mustn`t be greater then {self.mx}'
            )

        if self.mn and value < self.mn:
            raise ValidationError(
                f'Value of this field must be low then {self.mn}'
            )

        return errors


class LengthValidator(ValueValidator):
    def __call__(self, value):
        errors = []
        value = len(value)

        if self.mx and value > self.mx:
            raise ValidationError(
                f'Value len of this field mustn`t be greater then {self.mx}'
            )

        if self.mn and value < self.mn:
            raise ValidationError(
                f'Value len of this field must be low then {self.mn}'
            )

        return errors


class URLValidator():
    def __call__(self, value) -> Any:
        try:
            validators.url(value)
        except validators.ValidationError:
            raise ValidationError('Invalid URL')


class PhoneValidator():
    NUMBERS_IN_PHONE_COUNT = 10

    def __call__(self, value: str) -> Any:
        c = 0
        for s in value:
            if s.isdigit():
                c += 1

        if c != self.NUMBERS_IN_PHONE_COUNT:
            raise ValidationError(f'Inalid telephone number length - {c+1}')
