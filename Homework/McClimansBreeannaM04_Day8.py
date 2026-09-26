"""
Use the provided input file 'cleantext.txt' that was output of today's demo to get a count of how many times a particular word occurs in the passage.  
Read the file contents into a string variable and do a split into individual word list based on a blank space delimiter.  
Reference P453 in section 8.3 for explanation of the split string method.
Once you have your string list created.  
You can sort it in preparation to count the words and how many times they have occurred in the passage.  
Reference p375 in section 7.5 for coverage on list methods  including sorting.  
The result of the (ASCII) sort will group all like words together to enable a search and tally for your final analysis 
and display of each word that occurs and how many times it shows up.
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