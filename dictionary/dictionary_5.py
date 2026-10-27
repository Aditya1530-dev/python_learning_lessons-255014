"""Count whitespace-separated words using a dictionary."""


# PUBLIC_INTERFACE
def count_words(text: str) -> dict[str, int]:
    """Return case-insensitive word counts; punctuation is left unchanged."""
    counts: dict[str, int] = {}
    for word in text.casefold().split():
        # A missing key starts at zero; existing keys keep their running count.
        counts[word] = counts.get(word, 0) + 1
    return counts


if __name__ == "__main__":
    frequencies = count_words("Python makes learning fun Python makes sense")
    for word, count in sorted(frequencies.items()):
        print(f"{word}: {count}")
    # fun: 1, learning: 1, makes: 2, python: 2, sense: 1 (one per line).
