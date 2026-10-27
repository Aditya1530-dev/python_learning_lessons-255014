"""Demonstrate keyword-only arguments and their default values."""


# PUBLIC_INTERFACE
def greet(name, *, greeting="Hello"):
    """Return a greeting for name; greeting must be supplied by keyword."""
    # Parameters after the bare * cannot be passed positionally.
    return f"{greeting}, {name}!"


if __name__ == "__main__":
    print(greet("Aditya"))
    print(greet("Aditya", greeting="Welcome"))
    print(greet(name="Aditya", greeting="Good morning"))
