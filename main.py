def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_characters = get_characters_sorted(num_characters)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{num_words} words found in the document")
    
    for char in sorted_characters:
        if char.isalpha():
            print(f"The '{char}' character was found {sorted_characters[char]} times")
    print("--- End report ---")
   


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

def get_characters_sorted(num_characters):
    #Sort characters using sorted
    sorted_characters = sorted(num_characters.items(), key = lambda x:x[1], reverse=True)
    sorted_dict = dict(sorted_characters)
    return sorted_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()