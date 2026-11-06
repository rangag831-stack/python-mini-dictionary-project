# 1. To create an empty dictionary
dictionary = {}

# 2. To repeat the program until the user exits
while True:

    # 3. To display the project title
    print("\n   Dictionary management system  ")

    # 4. To display menu options
    print("1. Add a word")
    print("2.Search for meaning")
    print("3.Display all words")
    print("4.update meaning")
    print("5.Delete word")
    print("6.exit")

    # 5. To get the user's choice
    choice = input("enter your choice")

    # 6. To check Add a word option
    if choice == "1":

        # 7. To get the word and convert it into lowercase
        word = input("enter the word : ").lower()

        # 8. To get the meaning
        meaning = input("enter the meaning : ")

        # 9. To store word and meaning
        dictionary[word] = meaning

        print("word added successfully .....")

    # 10. To check Search option
    elif choice == "2":

        # 11. To get the word to search
        word = input("enter the word to search :").lower()

        # 12. To check whether word exists
        if word in dictionary:
            print("meaning :", dictionary[word])
        else:
            print("word not found in the dictionary....")

    # 13. To check Display all words option
    elif choice == "3":

        # 14. To check whether dictionary is empty
        if dictionary:
            print("words and their meaning : ")

            # 15. To access all words and meanings
            for word, meaning in dictionary.items():
                print(f"{word}:{meaning}")

        else:
            print("dictionary is empty......")

    # 16. To check Update meaning option
    elif choice == "4":

        # 17. To get the word to update
        word = input("Enter word: ").lower()

        if word in dictionary:

            # 18. To get the new meaning
            meaning = input("Enter new meaning: ")

            # 19. To update the old meaning
            dictionary[word] = meaning

            print("Meaning updated successfully.")
            print("New meaning:", dictionary[word])

        else:
            print("Word not found.")

    # 20. To check Delete word option
    elif choice == "5":

        # 21. To get the word to delete
        word = input("enter the word to delete").lower()

        if word in dictionary:

            # 22. To delete the word
            del dictionary[word]

            print("word deleted successfully,,,")
        else:
            print("word not found in the dictionary......")

    # 23. To check Exit option
    elif choice == "6":
        print("exiting program.......")

        # 24. To stop the loop
        break

    # 25. To handle invalid choices
    else:
        print("invalid choice please try again give valid....")   
