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

def main():
    # Open the file and read its contents into a string variable
    try:
        with open('cleantext.txt', 'r') as file:
            text = file.read()
    except FileNotFoundError:
        print("The file 'cleantext.txt' was not found.")
    except IOError:  # noqa: UP024
        print("An error occurred while reading the file.")

    # Split the string into a list of words based on blank space delimiter
    word_list = text.split()

    # Sort the list of words
    word_list.sort()

    # Create a dictionary to count occurrences of each word
    word_count = {}
    for word in word_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    # Display the results
    for word, count in word_count.items():
        print(f"{word}: {count}")

if __name__ == "__main__":
    main()