"""
Your assignment is to write a program that inputs a sentence from the keyboard, word by word, into a list.  
The program should output the following.
1. The complete sentence, with only the first letter of the first word capitalized (if it wasn't already), 
spaces between each word, and a period at the end.
2. The count of the number of words in the sentence.
Hint: end input on a blank line or on input of the word "done".
For instance, if the input is: 
the
cat
ran 
home
quickly
Your program should output:
The cat ran home quickly.
There are 5 words in the sentence.
"""

def get_words():
    # Create an empty list
    words = []

    # Get words from the user
    while True:
        try:
            word = input(
                "Enter a word (or press Enter to finish, or type 'done'): "
            ).strip()

            # Stop if user presses Enter or types done
            if word == "" or word.lower() == "done":
                break

            # Make sure the input contains only letters
            if not word.isalpha():
                raise ValueError

            # Add valid word to the list
            words.append(word)

        except ValueError:
            print("Invalid input. Please enter a word using letters only.")

    return words


def create_sentence(words):
    # Join the words together with spaces
    sentence = " ".join(words)

    # Capitalize the first letter and add a period
    sentence = sentence.capitalize() + "."

    return sentence


def display_results(words, sentence):
    # Display the sentence and word count
    print(sentence)
    print(f"There are {len(words)} words in the sentence.")


def main():
    # Get the list of words
    words = get_words()

    # Make sure at least one word was entered
    if words:
        sentence = create_sentence(words)
        display_results(words, sentence)
    else:
        print("No words were entered.")


if __name__ == "__main__":
    main()