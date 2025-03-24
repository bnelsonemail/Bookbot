



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


