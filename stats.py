def get_num_words(text: str):
    return len(text.split())

def get_num_chars(text: str):
    char_counts = {}
    for char in text.lower():
        if char.isalpha() or char.isspace():
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def sort_char_counts(char_counts: dict):
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    return [{"char": char, "num": count} for char, count in sorted_chars]
