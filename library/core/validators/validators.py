import validators
from typing import Any
from library.core.exceptions import ValidationError


class LengthValidator():
    def __init__(self, *, mn: int = None, mx: int = None) -> None:
        if not (mn or mx):
            raise AttributeError('mn or mx must be set.')
        if mx and mn and mx < mn:
            raise ValueError('mx nust be greater than mn')

        self.mx = mx
        self.mn = mn

    def __call__(self, value):
        errors = []
        if self.mx and value > self.mx:
            errors.append(
                f'Value of this field mustn`t be greater then {self.mx}'
            )

        if self.mn and value < self.mn:
            errors.append(f'Value of this field must be low then {self.mn}')

        return errors


class URLValidator():
    def __call__(self, value) -> Any:
        try:
            validators.url(value)
        except validators.ValidationError:
            raise ValidationError('Invalid URL')
