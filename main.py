def read():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)

def count():
    count_base = []
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        count_base = file_contents.split()
        word_count = len(count_base)
        print(word_count)

def main():
    read()
    count()

main()
