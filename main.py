from library_manager import LibraryManager

lib = LibraryManager()

while True:
    print("\n---- Library Menu ----")
    print("1. Add Book")
    print("2. Display All Books")
    print("3. Search Book")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        book_id = input("Enter Book ID: ")
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        lib.add_book(book_id, title, author)

    elif choice == "2":
        lib.display_books()

    elif choice == "3":
        title = input("Enter title to search: ")
        lib.search_book(title)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")