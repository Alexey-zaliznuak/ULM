from typing import Any, Union


class empty:
    """
    This class is used to represent no data being provided for a given input
    or output value.

    It is required because `None` may be a valid input or output value.
    """
    pass


class AllPossibleValues:
    """
    class for filters, use instead when:
    queryset.where(value.in_(all_possible_values)) == queryset
    """
    pass


InitValue = Union[empty, Any]
