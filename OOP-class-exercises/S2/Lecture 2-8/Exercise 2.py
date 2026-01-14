# 2. Write Python classes to keep track of book reviews for books.
# Each book has author, title and one or more reviews.
# Each book review has rating (1-5 stars) and a text.
# You have to decide on what classes you'll have, what attributes and methods
# and how will the classes communicate with each other.


class Book:
    def __init__(self, author, title):
        self._author = author
        self._title = title
        self._reviews = []

    def add_review(self, rating, text):
        if 5 >= int(rating) >= 1:
            self._reviews.append(Review(int(rating), text))
            return True
        else:
            return False

    def __str__(self):
        return self._author + " - " + self._title + "\n  " + "\n  ".join([str(elem) for elem in self._reviews])


class Review:
    def __init__(self, rating, text):
        self._rating = rating
        self._text = text

    def __str__(self):
        return str(self._rating) + ": " + str(self._text)


b = Book("Martin Amis", "Money")
if b.add_review(1, 0):
    print("Review added.")
else:
    print("Incorrect syntax.")

b.add_review("5", "Great read.")
b.add_review("3", "Not great, not terrible.")
b.add_review("1", "B.A.D.")
print(b)
