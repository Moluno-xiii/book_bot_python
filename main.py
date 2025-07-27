from stats import get_book_text
import sys


def main():

    if len(sys.argv) < 2:
        print("To start, run `python3 main.py <path_to_txt_file>`")
        return

    get_book_text(sys.argv[1])


main()
