
'''Sistema Avanzato di Gestione Biblioteca

Si desidera sviluppare un sistema per la gestione di una biblioteca in Python. Il sistema deve permettere di gestire un 
inventario di libri e le operazioni di prestito e restituzione degli stessi. Gli utenti del sistema devono essere in grado
 di aggiungere libri al catalogo, prestarli, restituirli e visualizzare quali libri sono disponibili in un dato momento.

Classi:
- Libro: Rappresenta un libro con titolo, autore, stato del prestito. Il libro deve essere inizialmente disponibile (non prestato).

- Biblioteca: Gestice tutte le operazioni legate alla gestione di una biblioteca.

    Metodi:
    - aggiungi_libro(libro): Aggiunge un nuovo libro al catalogo della biblioteca. Restituisce un messaggio di conferma.

    - presta_libro(titolo): Cerca un libro per titolo e, se disponibile e non già prestato, lo segna come disponibile.
     Restituisce un messaggio di stato.

    - restituisci_libro(titolo): Cerca un libro per titolo e, se trovato e prestato, lo segna come disponibile. 
    Restituisce un messaggio di stato.

    - mostra_libri_disponibili(): Restituisce una lista dei titoli dei libri attualmente disponibili. Se non ci sono libri 
    disponibili, restituisce un messaggio di errore.

Test Cases:
- Un amministratore della biblioteca aggiunge alcuni libri all'inventario.

- Un utente prende in prestito un libro, che viene quindi marcato come non disponibile.

- L'utente restituisce il libro, che viene marcato di nuovo come disponibile.

- In qualsiasi momento, un utente può visualizzare quali libri sono disponibili per il prestito.
'''

class Book:

    def __init__(self, title, author):

        self.title: str = title
        self.autor: str = author


class Library:

    def __init__(self):
        self.catalog: list =[]
    
    def add_books(self, book):
        self.catalog.append(book)
        return f"The book '{book.title}' is successfully added to the catolog"

    def borrow_book(self, title):
        for book in self.catalog:
            if book.title == title:
                if book.available:
                    book.available = False
                    return f"The book '{title}' is alredy borrowed."
                else:
                    
                    return f"The book'{title}' is borrowed with success."
        return f"The book'{title}' is not in the catalog." 
    
    def return_book(self, title):
        for book in self.catalog:
            if book.title == title:
                if not book.available:
                    book.available = True
                    if book.borrow:
                        return f"The book '{title}' is ok."
                else:
                    return f"The book {title} is not available"
                
    
    def show_books_available(self):
    
        book_available = [book.title for book in self.catalog if book.available]
        if book_available:
            return "Book available: " + ", ".join(book_available)
        else:
            return "No book available."




biblioteca = Library()

# Aggiunta dei libri
libro1 = Book("Il signore degli anelli", "J.R.R. Tolkien")
libro2 = Book("1984", "George Orwell")
libro3 = Book("Harry Potter e la pietra filosofale", "J.K. Rowling")



# Prestito di un libro
print(biblioteca.borrow_book("1984"))
print(biblioteca.borrow_book("1984"))  # Tentativo di prendere in prestito lo stesso libro di nuovo

# Restituzione di un libro
print(biblioteca.return_book("1984"))

# Mostra libri disponibili
print(biblioteca.show_books_available())






























