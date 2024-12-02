def main():
    word_count = 0
    # Read Frankenstein
    with open("books/frankenstein.txt") as f:
        file_contents = f.read() 
    # Loop through the sentence 
    for words in file_contents.split():
        word_count+=1
    print(word_count)


main()