class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.books = []

    def get_book(self, author, book_name, days_to_return, library):

        for _, user_rented_books in library.rented_books.items():
            for rented_book_name, rented_book_days_to_return in user_rented_books.items():
                if rented_book_name == book_name:
                    return f'The book {book_name} is already rented and' \
                           f' will be available in {rented_book_days_to_return} days!'

        if author not in library.books_available:
            return

        if book_name not in library.books_available[author]:
            return

        library.books_available[author].remove(book_name)

        if self.username not in library.rented_books:
            library.rented_books[self.username] = {}
        library.rented_books[self.username][book_name] = days_to_return
        self.books.append(book_name)
        return f'{book_name} successfully rented for the next {days_to_return} days!'

    def return_book(self, author, book_name, library):
        if book_name not in self.books:
            return f'{self.username} doesn\'t have this book in his/her records!'
        library.books_available[author].append(book_name)
        library.rented_books[self.username].pop(book_name)
        self.books.remove(book_name)

    def info(self):
        return ', '.join(sorted(self.books))

    def __str__(self):
        return f'{self.user_id}, {self.username}, {self.books}'
