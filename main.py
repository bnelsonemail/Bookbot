from stats import word_count


def get_book_text(file_path):
    """Opens a file and returns its full contents as a string."""
    with open(file_path, 'r') as f:
        return f.read()


def main():
    """Reads book content from a file and prints word count."""
    file_content = get_book_text('books/frankenstein.txt')
    word_count(file_content)
    return file_content


if __name__ == "__main__":
    main()
