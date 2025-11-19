# program1_sort.py
# -*- coding: utf-8 -*-

"""
Program 1: Custom sorting of Ukrainian and English text strings.

Rules:
- Ukrainian words (any case) go before Latin words (any case).
- Comparison is case-insensitive.
- For Ukrainian words we use Ukrainian alphabet order (including Ґ, Є, І, Ї).
"""

UKR_ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
UKR_INDEX = {ch: idx for idx, ch in enumerate(UKR_ALPHABET)}


def is_ukrainian_letter(ch: str) -> bool:
    """Return True if character is a Ukrainian letter (case-insensitive)."""
    return ch.lower() in UKR_INDEX


def ukrainian_word_key(word: str):
    """
    Build a comparable key for a Ukrainian word using Ukrainian alphabet order.
    Non-Ukrainian characters are placed after Ukrainian letters but remain deterministic.
    """
    normalized = word.lower()
    key = []
    for ch in normalized:
        if ch in UKR_INDEX:
            key.append(UKR_INDEX[ch])
        else:
            key.append(len(UKR_ALPHABET) + ord(ch))
    return key


def sort_key(word: str):
    """
    Custom sort key:
    1) Detect first alphabetic character.
    2) If it is Ukrainian -> category 0, else -> category 1.
    3) Inside category:
       - Ukrainian: use ukrainian_word_key()
       - Latin/other: use word.lower()
    """
    first_alpha = None
    for ch in word:
        if ch.isalpha():
            first_alpha = ch
            break

    if first_alpha is None:
        first_alpha = word[0] if word else ""

    if is_ukrainian_letter(first_alpha):
        category = 0  # Ukrainian first
        secondary = ukrainian_word_key(word)
    else:
        category = 1  # Latin later
        secondary = word.lower()

    return (category, secondary)


def main():
    # List must contain: EN/UA, lower/upper, starting with і/ї/є/І/Ї/Є
    words = [
        "English",
        "інформація",   # ua, lower 'і'
        "android",
        "Windows",
        "Добрий день",  # ua, upper
        "матриця",
        "актова зала",
        "біоресурси",
        "єдиний",       # ua, lower 'є'
        "кава",
        "Інститут",     # ua, upper 'І'
        "Їжа",          # ua, upper 'Ї'
        "Єдність",      # ua, upper 'Є'
        "їжачок",       # ua, lower 'ї'
    ]

    print("Заданий список:")
    print(words)

    sorted_words = sorted(words, key=sort_key)

    print("\nВідсортований список:")
    print(sorted_words)


if __name__ == "__main__":
    main()
