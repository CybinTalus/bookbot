from stats import word_counter, letter_counter, sorter
import sys

# filepath = "books/frankenstein.txt"

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
        print(file_contents)


    
def main():
    # get_book_text(filepath)
    # word_counter(filepath)
    # letter_counter(filepath)
    # sorter(filepath)
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    sorter(sys.argv[1])
        
main()