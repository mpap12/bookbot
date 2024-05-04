def main():
    book_path = "books/frankenstein.txt"
    print(f"--- Begin report of {book_path} ---")
    book_text = get_book_text(book_path)
    book_num_words = word_count(book_text)
    print(f"{book_num_words} words found in the document")
    book_letters = convert_to_list(letter_count(book_text))
    book_letters.sort(reverse=True, key=sort_on)
    for entry in book_letters:
        print (f"The {entry["letter"]} character was found {entry["num"]} times.")
    print ("--- End report ---")


def letter_count(text):
    lowered_text = text.lower()
    letter_dict = {}
    counter = 1
    for letter in lowered_text:
        if letter.isalpha():
            if letter not in letter_dict:
             letter_dict[letter] = 1
            else:
                letter_dict[letter] = letter_dict[letter] + 1
    return letter_dict

def sort_on(dict):
    return dict["num"]

def convert_to_list(dict):
    letter_list = []
    letter_keys = dict.keys()
    for key in letter_keys:
        mini_dict = {}
        mini_dict.update({"letter" : key})
        mini_dict.update({"num" : dict[key]})
        letter_list.append(mini_dict)
    return letter_list

def word_count(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()