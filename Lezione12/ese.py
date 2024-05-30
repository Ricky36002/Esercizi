class Book:
    def __init__(self, book_id, title, author):
        # Inizializzazione degli attributi di un libro
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = False  # All'inizio il libro non è preso in prestito

    def borrow(self):
        # Metodo per contrassegnare il libro come preso in prestito
        if not self.is_borrowed:
            self.is_borrowed = True  # Se il libro non è già preso in prestito, lo contrassegna come preso
        else:
            raise ValueError("Book is already borrowed")  # Solleva un'eccezione se il libro è già in prestito

    def return_book(self):
        # Metodo per contrassegnare il libro come restituito
        if self.is_borrowed:
            self.is_borrowed = False  # Se il libro è in prestito, lo contrassegna come restituito
        else:
            raise ValueError("Book is not borrowed")  # Solleva un'eccezione se il libro non è in prestito


class Member:
    def __init__(self, member_id, name):
        # Inizializzazione degli attributi di un membro
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []  # All'inizio il membro non ha libri in prestito

    def borrow_book(self, book):
        # Metodo per aggiungere un libro nella lista dei libri presi in prestito dal membro
        if book not in self.borrowed_books:
            book.borrow()  # Contrassegna il libro come preso in prestito
            self.borrowed_books.append(book)  # Aggiunge il libro alla lista dei libri presi in prestito
        else:
            raise ValueError("Book is already borrowed by the member.")  # Solleva un'eccezione se il libro è già preso in prestito dal membro

    def return_book(self, book):
        # Metodo per rimuovere un libro dalla lista dei libri presi in prestito dal membro
        if book in self.borrowed_books:
            book.return_book()  # Contrassegna il libro come restituito
            self.borrowed_books.remove(book)  # Rimuove il libro dalla lista dei libri presi in prestito
        else:
            raise ValueError("Book not borrowed by this member")  # Solleva un'eccezione se il libro non è preso in prestito dal membro


class Library:
    def __init__(self):
        # Inizializzazione dei dizionari per memorizzare i libri e i membri della biblioteca
        self.books = {}
        self.members = {}

    def add_book(self, book_id, title, author):
        # Metodo per aggiungere un nuovo libro nella biblioteca
        if book_id not in self.books:
            self.books[book_id] = Book(book_id, title, author)  # Crea un nuovo oggetto Book e lo aggiunge al dizionario dei libri
        else:
            raise ValueError("Book ID already exists")  # Solleva un'eccezione se l'ID del libro già esiste

    def register_member(self, member_id, name):
        # Metodo per iscrivere un nuovo membro nella biblioteca
        if member_id not in self.members:
            self.members[member_id] = Member(member_id, name)  # Crea un nuovo oggetto Member e lo aggiunge al dizionario dei membri
        else:
            raise ValueError("Member ID already exists")  # Solleva un'eccezione se l'ID del membro già esiste

    def borrow_book(self, member_id, book_id):
        # Metodo per permettere a un membro di prendere in prestito un libro
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.borrow_book(book)  # Chiama il metodo borrow_book del membro per prendere in prestito il libro
        elif member_id not in self.members:
            raise ValueError("Member not found")  # Solleva un'eccezione se il membro non esiste
        else:
            raise ValueError("Book not found")  # Solleva un'eccezione se il libro non esiste

    def return_book(self, member_id, book_id):
        # Metodo per permettere a un membro di restituire un libro
        if member_id in self.members and book_id in self.books:
            member = self.members[member_id]
            book = self.books[book_id]
            member.return_book(book)  # Chiama il metodo return_book del membro per restituire il libro
        else:
            raise ValueError("Member or book does not exist")  # Solleva un'eccezione se il membro o il libro non esistono

    def get_borrowed_books(self, member_id):
        # Metodo per restituire la lista dei libri presi in prestito da un membro
        if member_id in self.members:
            member = self.members[member_id]
            return [book.title for book in member.borrowed_books]  # Restituisce una lista dei titoli dei libri presi in prestito dal membro
        else:
            raise ValueError("Member does not exist")  # Solleva un'eccezione se il membro non esiste
