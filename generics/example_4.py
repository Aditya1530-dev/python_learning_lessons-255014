"""Use a type variable to preserve an iterable's element type."""

from typing import Iterable, TypeVar

T = TypeVar("T")


# PUBLIC_INTERFACE
def first(items: Iterable[T]) -> T:
    """Return the first item, or raise ValueError for an empty iterable.

    The shared type variable tells type checkers that the return type matches
    the input element type; annotations do not enforce types at runtime.
    """
    for item in items:
        return item
    raise ValueError("items must contain at least one element")


if __name__ == "__main__":
    number: int = first([10, 20, 30])
    name: str = first(["Ada", "Grace"])
    print(number)  # 10
    print(name)    # Ada

    try:
        first([])
    except ValueError as error:
        print(error)  # items must contain at least one element
