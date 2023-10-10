from typing import Generic, TypeVar


Attribute = TypeVar('Attribute')


class LazyAttribute(Generic[Attribute]):
    def __init__(self, obj, attr_name: str):
        self.obj = obj
        self.attr_name = attr_name

    def __call__(self, *args, **kwargs) -> Attribute:
        return getattr(self.obj, self.attr_name)
