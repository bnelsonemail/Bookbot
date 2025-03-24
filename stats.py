



def word_count(book):
    """Counts the words in the book (case-insensitive)."""
    book = book.lower()  # Convert to lowercase early on
    words = book.split()
    count = len(words)
    return count, " ".join(words)  # Join to send back a clean string


def char_count(text):
    """Counts the characters in a book and returns a dictionary of counts."""
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on(item):
    return item["count"]


def sort_char_dict(char_dict):
    """Convert to list of dicts, filter for a-z, sort descending."""
    sorted_chars = []

    for char, count in char_dict.items():
        if char.isalpha():  # Only include alphabetic characters
            sorted_chars.append({"char": char, "count": count})

    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars
