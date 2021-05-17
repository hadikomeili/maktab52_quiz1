import dill, pickle


class Book:

    def __init__(self, ISBN, name, author, publisher, publish_date):
        self.ISBN = ISBN
        self.name = name
        self.author = author
        self.publisher = publisher
        self.publish_date = publish_date

with open('books.pkl', 'rb') as f:
    data = pickle.load(f)

    ans1 = sorted(data, key=data.ISBN)
    