def get_book_text(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def main():
    book_text = get_book_text('books/frankenstein.txt')
    print(book_text)

if __name__ == '__main__':
    main()
