# Print a user-specified list without duplicates

def add_to_list(string_list: list[str])-> None:
    # Add strings to an empty string list

    string = input("Enter a string (end with \"DONE\"):\n")

    while string != "DONE":
        string_list.append(string)

        print("String has been added to the string list.")

        string = input("Enter another string (end with \"DONE\"):\n")
    
    print("Done adding strings to string list")
    return

def main():
    strings = []
    add_to_list(strings)

    temp = [phrase for phrase in strings if phrase not in temp]

    strings = temp

    print()
    print("Unique list:")

    for words in strings:
        print(words)

if __name__ == "__main__":
    main()
