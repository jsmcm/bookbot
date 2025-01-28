

def main():

    title =  "books/frankenstein.txt"
    contents = read_book(title)

    word_count = count_words(contents)
    character_count = count_characters(contents)

    print_report(title, word_count, character_count)

def read_book(file_name):
    with open(file_name) as f:
        return f.read()


def print_report(title, word_count, character_count):
    print(f"--- Begin report of {title} ---")
    print(f"{word_count} words found in the document")
    print("")
    
    for data in character_count:
        if data.isalpha():
            print(f"The '{data}' character was found {character_count[data]} times")

def count_words(book_text):
    words = book_text.split()
    return len(words)
    
    
def lower_case_words(book_text):
    return book_text.lower()
    

def count_characters(book_text):

    characters = {}

    for character in lower_case_words(book_text):
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    
    return characters

main()