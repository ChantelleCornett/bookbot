from stats import count_words, count_characters, sorted_dict
import sys
def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        
    return(file_contents)

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(count_words(get_book_text(sys.argv[1])))
    print("-------- Character Count -------")
    for i in sorted_dict(count_characters(get_book_text(sys.argv[1]))):
        print(f"{str(i)}: {count_characters(get_book_text(sys.argv[1]))[i]}")

main()