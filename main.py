from stats import get_word_count, get_char_count

def get_book_text(fp):
    with open(fp, mode='r', encoding="utf-8-sig") as f:
        text = f.read()
        return text

def main():
    file_path = "books/frankenstein.txt"
    book_text = get_book_text(file_path)
    word_count = get_word_count(book_text)
    print(f"{word_count} words found in the document")
    char_dict = get_char_count(book_text)
    print(char_dict)


main()
