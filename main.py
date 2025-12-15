import sys
from stats import get_num_words, get_num_chars, sort_char_counts

def get_book_text(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    if (len(sys.argv) < 2):
        print('Usage: python3 main.py <path_to_book>')
        sys.exit(1)

    book_filepath = sys.argv[1]

    print('============ BOOKBOT ============')
    print(f'Analyzing book found at {book_filepath}...')

    book_text = get_book_text(book_filepath)
    num_words = get_num_words(book_text)
    print('----------- Word Count ----------')
    print(f'Found {num_words} total words')

    char_counts = get_num_chars(book_text)
    sorted_chars = sort_char_counts(char_counts)
    print('--------- Character Count -------')
    for char_info in sorted_chars:
        if char_info['char'].isalpha():
            print(f'{char_info["char"]}: {char_info["num"]}')

if __name__ == '__main__':
    main()
