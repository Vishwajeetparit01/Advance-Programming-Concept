

def add_book():
    with open("books.txt", "a") as f:
        id = input("Enter Book ID: ")
        title = input("Enter Book Name: ")
        author = input("Enter Author: ")
        f.write(id + "," + title + "," + author + ",Available\n")


def search_book():
    title = input("Enter Book Name: ")

    with open("books.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[1].lower() == title.lower():
                print("Book Found:", line.strip())
                return

    print("Book not found")


def issue_book():
    title = input("Enter Book Name: ")

    with open("books.txt", "r") as f:
        books = f.readlines()

    with open("books.txt", "w") as f:
        for line in books:
            data = line.strip().split(",")

            if data[1].lower() == title.lower():
                data[3] = "Issued"

            f.write(",".join(data) + "\n")


def return_book():
    title = input("Enter Book Name: ")

    with open("books.txt", "r") as f:
        books = f.readlines()

    with open("books.txt", "w") as f:
        for line in books:
            data = line.strip().split(",")

            if data[1].lower() == title.lower():
                data[3] = "Available"

            f.write(",".join(data) + "\n")


def display_available():
    with open("books.txt", "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[3] == "Available":
                print(line.strip())


while True:
    print("\n1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Available Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_book()
    elif choice == "2":
        search_book()
    elif choice == "3":
        issue_book()
    elif choice == "4":
        return_book()
    elif choice == "5":
        display_available()
    elif choice == "6":
        break