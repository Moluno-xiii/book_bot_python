def get_book_text(path_to_file):
    with open(path_to_file) as f:
        book_content = f.read()
        characters = count_characters(book_content)

        number_of_words = count_words(book_content)
        sorted_items = dict(sorted(characters.items(), key=sort_on, reverse=True))

        print(f"Found a total of {number_of_words} in your file ({path_to_file}).")
        print(sorted_items)


def count_words(string):
    return f"{len(string.split())} words"


def sort_on(items):
    return items[1]


def count_characters(string):
    character_set = {}

    for character in string:
        character = character.lower()
        if character in character_set:
            character_set[character] += 1
        else:
            character_set[character] = 1

    return character_set
