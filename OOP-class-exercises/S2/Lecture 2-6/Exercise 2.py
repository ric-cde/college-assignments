# Write a class Book –each book has a title (string) and one or more authors.
# Write a class to represent an author –each author has a name (string) and an email address (string


class Book:
    def __init__(self, title):
        self._title = title
        self._authors = []

    def add_author(self, a):
        self._authors.append(a)

    # def _author_list(self, l):
    #     result = ""
    #     for a in l:
    #         result = result + a._name + " " + a._email + ", "
    #     return result

    def print_book(self):
        print(self._title)
        for a in self._authors:
            print(a)

    def __str__(self):
        return self._title + ' - ' + ' - '.join(map(str, self._authors))
        # return self._title + self._author_list(self._authors)


class Author:
    def __init__(self, name, email):
        self._name = name
        self._email = email

    def __str__(self):
        return self._name + " " + self._email


a1 = Author("Roald Dahl", "roald@books.com")
a2 = Author("Richard Herlihy", "richardherlihy@gmail.com")
print(a1)

my_book = Book("Fantastic Mr. Fox")
my_book.add_author(a1)
my_book.add_author(a2)

my_book.print_book()

print(my_book)