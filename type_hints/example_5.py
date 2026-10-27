"""Demonstrate typed dictionary fields and an optional lookup result."""

from typing import Optional, TypedDict


# PUBLIC_INTERFACE
class Student(TypedDict):
    """Describe the expected keys and value types of a student dictionary."""

    name: str
    score: int


# PUBLIC_INTERFACE
def find_student(students: list[Student], name: str) -> Optional[Student]:
    """Return the first student with the given name, or None if not found."""
    for student in students:
        if student["name"] == name:
            return student
    return None


if __name__ == "__main__":
    # TypedDict describes an ordinary dictionary; it does not validate at runtime.
    students: list[Student] = [
        {"name": "Ada", "score": 95},
        {"name": "Grace", "score": 98},
    ]

    for name in ("Ada", "Linus"):
        match = find_student(students, name)
        # Checking for None narrows Optional[Student] to Student.
        if match is not None:
            print(f"{match['name']} scored {match['score']}")
        else:
            print(f"No student named {name}")
