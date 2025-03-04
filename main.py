from stats import get_word_count, get_char_count, print_report
import sys

def get_book_text(fp):
    with open(fp) as f:
        text = f.read()
        return text

def main():
    args = sys.argv
    file_path = ""
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return
    else:
        file_path = args[1]

    book_text = get_book_text(file_path)
    word_count = get_word_count(book_text)
    char_dict = get_char_count(book_text)
    print_report(char_dict, word_count, file_path)

main()
