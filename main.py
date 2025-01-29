def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        letter_count = {}
        for letter in file_contents.lower():
            if letter.isalpha():
                if letter in letter_count:
                    letter_count[letter] += 1
                else:
                    letter_count[letter] = 1
        sorted_letter_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")
        for letter, count in sorted_letter_count:
            print(f"The '{letter}' character was found {count} times")
        print("--- End report ---")
if __name__ == "__main__":
    main()