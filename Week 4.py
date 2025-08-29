

def read_and_modify_file():
    filename = input("Please enter the name of the file to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("\n File read successfully.\n")
    except FileNotFoundError:
        print(" Error: File not found.")
        return
    except IOError:
        print(" Error: Could not read the file.")
        return





    print("Please pick a number to choose how you want to change the text:")
    print("1. Turn to UPPERCASE")
    print("2. Turn to lowercase")
    print("3. Turn to Title Case")
    print("4. Replace the word")
    choice = input("Please put in your choice (1-4): ")

    if choice == '1':
        modified_content = content.upper()
    elif choice == '2':
        modified_content = content.lower()
    elif choice == '3':
        modified_content = content.title()
    elif choice == '4':
        word_to_replace = input("What word would you like to replace: ")
        replacement_word = input("Please enter the new word: ")
        modified_content = content.replace(word_to_replace, replacement_word)
    else:
        print(" That's an invalid choice.")
        return

    
    new_filename = "modified_" + filename

    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
            print(f"\n Modified content written to '{new_filename}'.")
    except IOError:
        print(" Error: Could not write to the new file.")



read_and_modify_file()
