def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    print(f"{num_words} words found in the document")
    print(num_characters)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_num_characters(text):
    #Convert words to lowercase
    lowercase = text.lower()
    character_count = {}
    #Loop through the text and add the character count to list
    for char in lowercase:
        if char in character_count:
            character_count[char]+=1
        else:
            character_count[char]=1
    return character_count



def get_book_text(path):
    with open(path) as f:
        return f.read()


main()