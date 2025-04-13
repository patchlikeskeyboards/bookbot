import sys
def main(book):
    book_path = sys.argv[1]
    file_contents = get_book_text(book_path)
    word_count = get_num_words(file_contents)
    file_con_low = lowercase(file_contents)
    character_count = get_char_count(file_con_low)
    print(f"--- Commencing report of {book_path} ---")
    print(f"–.-.-.-")
    print(f"{word_count} words located within in the document.")
    print("–.-.-.-")
    for character in character_count:
        counter = character_count[character]
        print(f"The letter '{character}' appears {counter} times.")
# I believe you're meant to have main up at the top
# Here, main starts everything and makes the next few lines simpler
def get_num_words(file_contents):
    count_base = file_contents.split()
    return len(count_base)
# gnw takes the file contents and splits it into a list, before returning the list len
def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()
# gbt acts as our "with open" section quite nicely
# This way we don't have to write it every time
def lowercase(file_contents):
    file_con_low = file_contents.lower()
    return file_con_low
# Just a short section to convert to lowercase for the char count later
def get_char_count(file_con_low):
    characters = {}
    split_up = list(file_con_low)
    for split in split_up:
        if split.isalpha():
            if split not in characters:
                characters.update({split:1})
            else:
                characters[split] += 1

    return characters
# This was very finicky but basically adds a character if it doesn't appear yet
# and just adds one value if the character alread exists'
# remember to call main at the end.

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    book = sys.argv[1]
    main(book)
# Currently trying to add the capability to put in any book and get
# a word count etc from it.
# Basically if you follow the right syntax of entry, you'll be able to
# scan any book out there (in txt form)
