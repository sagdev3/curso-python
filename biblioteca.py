class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f'El libro {self.author} ha sido prestado')
        else:
            print(f'El libro {self.title} no esta disponible')

    def return_book(self):
        self.available = True
        print(f'El libro {self.title} ha sido devuelto')


class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
        else:
            print(f'El libro {book.title} no esta disponible')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
        else:
            print(f'El libro {book.title} no esta en la lista de prestados')


class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_books(self, book):
        self.books.append(book)
        print(f'El libro {book.title} ha sido agregado')

    def register_user(self, user):
        self.users.append(user)
        print(f'El usuario {user.name} ha sido agregado')

    def show_books(self):
        print("Los Libros disponibles: ")
        for book in self.books:
            if book.available:
                print(f'{book.title} por {book.author}')


book1 = Book("El principito", "Atoine de Saint-Exupery")
book2 = Book('1984', "George Orwell")

user1 = User('Santiago', '1')
user2 = User("Dayana", '2')

library = Library()
library.add_books(book1)
library.add_books(book2)
library.register_user(user1)
library.register_user(user2)

library.show_books()

user1.borrow_book(book1)

library.show_books()

user2.borrow_book(book2)
user1.return_book(book1)

library.show_books()
