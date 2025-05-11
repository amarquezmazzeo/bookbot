from stats import get_text_wc
from stats import get_chars_dict
from stats import format_char_dict
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    filepath = sys.argv[1]

    book_text = get_book_text(filepath)
    book_wc = get_text_wc(book_text)
    chars_dict = get_chars_dict(book_text)
    print(f"{book_wc} words found in the document")
    print(chars_dict)
    dict_list = format_char_dict(chars_dict)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {book_wc} total words")
    for i in dict_list:
        if i['char'].isalpha():
            print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
main()