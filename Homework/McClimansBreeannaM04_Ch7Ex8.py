"""
8. Name Search                                                      
If you have downloaded the source code you will find a file in the Chapter 07 folder named popular_names.txt. 
This file contains a list of the 400 most popular names given to children born in the United States from the year 2000 through 2009.
Write a program that reads the contents of file into a list. 
The user should be able to enter a name and the program will display a message indicating whether the name was among the most popular.
You'll need to use the girlnames.txt  and boynames.txt files from the Companion Site
"""

def read_names_from_file(filename: str) -> list:
    #Read names from the file and return them as a list of strings
    try:
        with open(filename, 'r') as file:
            names = [line.strip() for line in file]
        return names
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except IOError:  # noqa: UP024
        print(f"Error: An error occurred while reading the file {filename}.")
        return []

def get_name() -> str:
    #Prompt the user to enter a name and return it, title to return names regardless of case
    try:
        name = input("Enter a name to search for: ").strip().title()
        if name == "":
            raise ValueError    
        if not name.isalpha():
            raise ValueError 
        return name
    except ValueError:
        print("Invalid input. Please enter a valid name.")

def search_name(name: str, girl_names: list, boy_names: list) -> None:
    #Search for the name in the girl and boy names lists and display a message
    if name in girl_names and name in boy_names:
        print(f"{name} is among the most popular names for both girls and boys.")
    elif name in girl_names:
        print(f"{name} is among the most popular names for girls.")
    elif name in boy_names:
        print(f"{name} is among the most popular names for boys.")
    else:
        print(f"{name} is not among the most popular names.")

def search_again() -> bool:
    #Ask the user if they want to search for another name and return True or False
    while True:
        response = input("Would you like to search for another name? (yes/no): ").lower()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main() -> None:
    #Read names from the files
    girl_names = read_names_from_file("girlnames.txt")
    boy_names = read_names_from_file("boynames.txt")

    #Main loop to search for names
    while True:
        name = get_name()
        if name:
            search_name(name, girl_names, boy_names)
        if not search_again():
            print("Thank you for using the name search program.")
            break

if __name__ == "__main__":
    main()
