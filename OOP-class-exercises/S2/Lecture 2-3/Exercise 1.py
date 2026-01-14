# Write a class Book –every book has a ISBN, title and author

class Book:
    def __init__(self, ISBN, title, author):
        self.ISBN = ISBN
        self.title = title
        self.author = author
    def __str__(self):
        return("Title: {}\nAuthor: {}\nISBN: {}".format(self.title, self.author, self.ISBN))

p = Book(234234, '1984', 'George Orwell')

print(p)