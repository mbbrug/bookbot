def word_count(book):
    words = book.split()
    return len(words)

def letter_count(book):
    chars={}
    symbols = 'abcdefghijklmnopqrstuvwxyz'

    for c in symbols:
       chars[c] = book.lower().count(c)

    return chars

with open("books/frankenstein.txt") as f:
    file_contents = f.read()

    w_count = word_count(file_contents)
    l_count = letter_count(file_contents)
    
    print(f"{w_count} words found in the document")
    
    for l in l_count:
        print(f"The '{l}' character was found {l_count[l]} times")

