"""Use a closure to retain a counter without a global variable."""

from typing import Callable


# PUBLIC_INTERFACE
def make_counter(start: int = 0) -> Callable[[], int]:
    """Return a counter that increments its own captured value on each call."""
    count = start

    def increment() -> int:
        """Update the enclosing counter rather than creating a local value."""
        nonlocal count
        count += 1
        return count

    return increment


if __name__ == "__main__":
    counter = make_counter(10)
    other_counter = make_counter()
    print(counter())        # 11
    print(counter())        # 12
    print(other_counter())  # 1: each closure has independent state.
