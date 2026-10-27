"""Wrap a greeting function with a reusable result-transforming decorator."""

from functools import wraps
from typing import Callable


# PUBLIC_INTERFACE
def uppercase_result(function: Callable[..., str]) -> Callable[..., str]:
    """Decorate a string-returning function to uppercase its result."""
    @wraps(function)
    def wrapper(*args, **kwargs) -> str:
        """Forward arguments and transform the wrapped function's result."""
        return function(*args, **kwargs).upper()

    return wrapper


# PUBLIC_INTERFACE
@uppercase_result
def greet(name: str, punctuation: str = "!") -> str:
    """Return a personalized greeting with optional punctuation."""
    return f"Hello, {name}{punctuation}"


if __name__ == "__main__":
    print(greet("Ada"))                   # HELLO, ADA!
    print(greet("Grace", punctuation="."))  # HELLO, GRACE.
    print(greet.__name__)                 # greet: preserved by wraps.
