books = {}

def add_book(name):
    books[name] = "Available"

def issue_book(name):
    if name in books and books[name] == "Available":
        books[name] = "Issued"
    else:
        print("Book not available")

def return_book(name):
    if name in books:
        books[name] = "Available"

def search_book(name):
    print(books.get(name, "Book not found"))

def display_books():
    for name, status in books.items():
        if status == "Available":
            print(name)

n = int(input("Enter number of books: "))

for i in range(n):
    add_book(input("Enter book name: "))

issue_book(input("Enter book to issue: "))
print("Available books:")
display_books()