"""Generate Fibonacci numbers lazily instead of building a list."""

from typing import Iterator


# PUBLIC_INTERFACE
def fibonacci(count: int) -> Iterator[int]:
    """Yield count Fibonacci numbers, starting at zero.

    Raise ValueError when iteration begins if count is negative.
    """
    if count < 0:
        raise ValueError("count must be non-negative")

    current, following = 0, 1
    for _ in range(count):
        yield current
        current, following = following, current + following


if __name__ == "__main__":
    numbers = fibonacci(7)
    print(next(numbers))   # 0: execution pauses at the first yield.
    print(list(numbers))   # [1, 1, 2, 3, 5, 8]: resume the same generator.
    print(list(numbers))   # []: generators are exhausted after one pass.
