

class DigitalBook():
    def __init__(self, name):
        self._name = name
        self._borrowed_by = []

    def borrowed_by(self, user):
        self._borrowed_by.append(user)

    def __str__(self):
        s = self._name + " borrowed by:"
        # for u in self._borrowed_by:
        #     s = s + str(u) + " "
        return s


class User():
    def __init__(self, name):
        self._name = name
        self._books_borrowed = []

    def borrow_book(self, book):
        self._books_borrowed.append(book)

    def __str__(self):
        s = self._name + " has borrowed:"
        for b in self._books_borrowed:
            s = s + str(b) + " "
        return s


class DigitalLibrary():
    def __init__(self):
        self._users = []
        self._books = []

    def add_user(self, name):
        self._users.append(User(name))

    def find_user(self, name):
        for u in self._users:
            if u._name == name:
                return u

    def find_book(self, name):
        for b in self._books:
            if b._name == name:
                return b

    def add_book(self, name):
        self._books.append(DigitalBook(name))

    def borrow_book(self):
        user_name = input("Enter a name: ")
        book_name = input("Enter book name: ")

        user = self.find_user(user_name)
        book = self.find_book(book_name)

        book.borrowed_by(user)
        user.borrow_book(book)

    def print_all(self):
        for u in self._users:
            print(u)

        for b in self._books:
            print(b)

lib = DigitalLibrary()
lib.add_book("1948")
lib.add_book("Fantastic Mr. Fox")
lib.add_book("The Stand")

lib.add_user("John")
lib.add_user("Mary")
lib.add_user("Ann")

lib.borrow_book()

lib.print_all()

