# Write a class Book –every book has a ISBN, title and author

class Book:
    def __init__(self, ISBN, title, author):
        self.__ISBN = ISBN
        self.__title = title
        self.__author = author
    def __str__(self):
        #return("Title: {}\nAuthor: {}\nISBN: {}".format(self.__title, self.__author, self.__ISBN))
        return(f"'{self.__title}' by {self.__author} ({self.__ISBN})")


# Extend the program from last week about the class Book and modify it
# so that it will create 5 books at run-time and add them to a list.
# Print the contents of the list

p = []
for i in range(2):
    isbn = input("Enter ISBN: ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    new_book = Book(isbn, title, author)
    p.append(new_book)

for b in p:
    print(b)

# print(p[0]._Book__title)

# p = Book(234234, '1984', 'George Orwell')
# print(p)
# print(p._Book__title)