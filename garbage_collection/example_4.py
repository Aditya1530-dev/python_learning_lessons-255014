"""Demonstrate collection of an unreachable self-referencing object."""

import gc
import weakref


# PUBLIC_INTERFACE
class Node:
    """A small object whose self-reference forms a reference cycle."""

    # PUBLIC_INTERFACE
    def __init__(self) -> None:
        """Create a cycle that reference counting alone cannot reclaim."""
        self.link = self


# PUBLIC_INTERFACE
def demonstrate_cycle_collection() -> bool:
    """Return whether explicit collection reclaimed an unreachable cycle."""
    was_enabled = gc.isenabled()
    # Disable automatic collection so only the explicit collect triggers it.
    gc.disable()
    try:
        node = Node()
        reference = weakref.ref(node)  # Does not keep the node alive.
        del node
        print(f"Alive before collection: {reference() is not None}")
        gc.collect()
        collected = reference() is None
        print(f"Collected after gc.collect(): {collected}")
        return collected
    finally:
        # Preserve the caller's original automatic collection setting.
        if was_enabled:
            gc.enable()


if __name__ == "__main__":
    demonstrate_cycle_collection()
