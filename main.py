from stats import word_count, char_count, sort_char_dict


def get_book_text(file_path):
    """Opens a file and returns its full contents as a string."""
    with open(file_path, 'r') as f:
        return f.read()


def print_report(file_path, word_total, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_total} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")
    print("============= END ===============")


def main():
    path = 'books/frankenstein.txt'
    book = get_book_text(path)
    word_total, cleaned_text = word_count(book)
    char_dict = char_count(cleaned_text)
    sorted_chars = sort_char_dict(char_dict)
    print_report(path, word_total, sorted_chars)


if __name__ == "__main__":
    main()

