from stats import get_num_words, get_each_char, sort_dict
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)
    else:
        book_path = sys.argv[1]
    #book_path = "books/frankenstein.txt"
    book_text = (get_book_text(book_path))
    word_num = get_num_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_num} total words")
    print("--------- Character Count -------")
    char_count = get_each_char(book_text)
    new_sorted_dict = sort_dict(char_count)
    for row in new_sorted_dict:
        print(f"{row['char']}: {row['num']}")
    print("============= END ===============")
    
    
def get_book_text (path_to_file):
    with open(path_to_file) as f:
        return f.read()
    

    
main()