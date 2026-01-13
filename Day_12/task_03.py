class Book:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __str__(self):
        return f"Readable Title for Users: {self.title}"

    def __repr__(self):
        return f"Book(id={self.id}, title='{self.title}')"

book = Book(101, "Code")
print(book)

books = [book]
print(books)

