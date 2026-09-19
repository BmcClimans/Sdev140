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

def main():
    # Initialize an empty list to store the words
    words = []

    # Prompt the user for input until they enter a blank line or "done"
    while True:
        try:
            word = input("Enter a word (or press Enter to finish, or type 'done'): ")
            if word == "" or word.lower() == "done":
                break
            #check thta input contains only letters
            if not word.isalpha():
                raise ValueError
            #add words to the list
            words.append(word)
        except ValueError:
            print("Invalid input. Please enter a word using letters only.")

    # Create the complete sentence
    if words:
        sentence = " ".join(words)
        sentence = sentence.capitalize() + "."
        print(sentence)
        print(f"There are {len(words)} words in the sentence.")
    else:
        print("No words were entered.")

if __name__ == "__main__":
    main() 