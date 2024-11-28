class Book:
    def __init__(self, title, author):
        # Initialize the book with a title, author, and status (default: available)
        self.title = title
        self.author = author
        self.status = "available"

    # String representation of the book, showing its title, author, and status
    def __str__(self):
        return f"'{self.title}' by {self.author} ({self.status})"

# making the member of the library
class Member:
    def __init__(self, name, member_id):
        # we are initializing the name id and books borrowed in a list
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    #show who borrowed the book and their iD
    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) - Borrowed Books: {len(self.borrowed_books)}"

# show the library itself
class Library:
    def __init__(self):
        # library empty with no books or members
        self.catalog = []
        self.members = []

    # now add a book
    def add_book(self, book):
        self.catalog.append(book)  # Add the book object to the empty catalog list
        print(f"Added {book} to the library.")  # Confirmation message

    # Remove a book from catalog
    def remove_book(self, book_title):
        # Look for the book in the catalog by its title
        for book in self.catalog:
            if book.title == book_title:
                self.catalog.remove(book)  # Remove the book if found
                print(f"Removed '{book_title}' from the library.")
                return
        # If the book is not found
        print(f"Book '{book_title}' not found in the library.")

    # Add someone to library
    def add_member(self, member):
        self.members.append(member)  # Add the member to the members list
        print(f"Added member: {member}")  # Confirmation message

    # Remove a member from the library
    def remove_member(self, member_id):
        # Look for the member in the members list by their ID
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)  # Remove the member if found
                print(f"Removed member with ID {member_id}.")
                return
        # If the member is not found, display a message
        print(f"Member with ID {member_id} not found in the library.")

    # Borrow a book
    def borrow_book(self, member_id, book_title):
        # make sure they are members first
        for member in self.members:
            if member.member_id == member_id:
                # Find the book by its title
                for book in self.catalog:
                    if book.title == book_title and book.status == "available":
                        # Mark the book as borrowed and add it to the member's borrowed books
                        book.status = "borrowed"
                        member.borrowed_books.append(book)
                        print(f"'{book_title}' has been borrowed by {member.name}.")
                        return
                # If the book is not available
                print(f"'{book_title}' is not available.")
                return
        # If the individual is not a member
        print(f"Member with ID {member_id} not found.")

    # Return a borrowed book to the library
    def return_book(self, member_id, book_title):
        # Find the member by their ID
        for member in self.members:
            if member.member_id == member_id:
                # Look for the book in the member's borrowed books
                for book in member.borrowed_books:
                    if book.title == book_title:
                        # say the book is there and then remove it
                        book.status = "available"
                        member.borrowed_books.remove(book)
                        print(f"'{book_title}' has been returned by {member.name}.")
                        return
                # if its not there than say its not borrowed
                print(f"'{book_title}' is not borrowed by {member.name}.")
                return
        # if the individual isnt a member then print a messeage for that
        print(f"Member with ID {member_id} not found.")

    # Display all books in the library
    def display_books(self):
        print("\nBooks in the Library:")
        if not self.catalog:
            print("No books available.")
        for book in self.catalog:
            print(f"  - {book}")  # Print each book in the catalog

    # Display all members of the library
    def display_members(self):
        print("\nLibrary Members:")
        if not self.members:
            print("No members found.")
        for member in self.members:
            print(f"  - {member}")  # Print each member


# running the code
if __name__ == "__main__":
    # Creating the library object
    library = Library()

    # Add some books
    book1 = Book("To Kill a Mockingbird", "Harper Lee")
    book2 = Book("1984", "George Orwell")
    book3 = Book("Moby Dick", "Herman Melville")
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)

    # Add some members
    member1 = Member("Alice", 1)
    member2 = Member("Bob", 2)
    library.add_member(member1)
    library.add_member(member2)

    # Display all books
    library.display_books()

    # Display all members
    library.display_members()

    # Borrowing a book
    library.borrow_book(1, "1984")

    # borrowing the same book
    library.borrow_book(2, "1984")

    # Return the book
    library.return_book(1, "1984")

    # Display books again to see the updated status
    library.display_books()

    # Remove a book from the library
    library.remove_book("Moby Dick")

    # Remove a member from the library
    library.remove_member(2)

    # Display updated lists of books and members
    library.display_books()
    library.display_members()
               