#1)
def anagram(s: str, t: str) -> bool:
    return sorted(s.lower()) == sorted(t.lower())
#2)
def valid_sudoku(board: list[list[str]]) -> bool:
    def is_valid_unit(unit):
        unit= [i for i in unit if i != '.']
        return len(unit) == len(set(unit))
    
    def is_valid_row(board):
        for row in board:
            if not is_valid_unit(row):
                return False
        return True
    
    def is_valid_col(board):
        for col in zip(*board):
            if not is_valid_unit(col):
                return False
        return True
    
    def is_valid_square(board):
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                square= [board[x][y] for x in range(i, i +3) for y in range(j, j +3)]
                if not is_valid_unit(square):
                    return False
            return True
    return is_valid_row(board) and is_valid_col(board) and is_valid_square(board)
#3)

#4)
def word_break(s: str, wordDict: list[str]) -> bool:
    word_set = set(wordDict) 
    dp = [False] * (len(s) + 1)
    dp[0] = True  

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  
    return dp[len(s)]

#5)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # Inizializza un nodo dell'albero binario con un valore, un figlio sinistro e un figlio destro
        self.val = val
        self.left = left
        self.right = right

def symmetric(tree: list[int]) -> bool:
    # Controlla se la lista è vuota. Un albero vuoto è considerato simmetrico.
    if not tree:
        return True

    def list_to_tree(nodes):
        # Converte una lista in un albero binario
        if not nodes:
            return None

        def helper(index):
            # Funzione ricorsiva per creare l'albero binario
            if index >= len(nodes) or nodes[index] is None:
                return None
            # Crea un nuovo nodo con il valore corrente
            node = TreeNode(nodes[index])
            # Imposta il figlio sinistro e destro usando la ricorsione
            node.left = helper(2 * index + 1)
            node.right = helper(2 * (index + 1))
            return node

        # Inizia la costruzione dell'albero a partire dalla radice (indice 0)
        return helper(0)

    def is_symmetric(root):
        # Verifica se l'albero è simmetrico
        if not root:
            return True

        def is_mirror(left, right):
            # Controlla se due alberi sono specchi l'uno dell'altro
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and
                    is_mirror(left.left, right.right) and
                    is_mirror(left.right, right.left))

        # Avvia la verifica simmetrica sui figli sinistro e destro della radice
        return is_mirror(root.left, root.right)

    # Converte la lista in un albero binario
    root = list_to_tree(tree)
    # Verifica se l'albero binario è simmetrico
    return is_symmetric(root)

#6)
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def reverse_list(head: ListNode) -> list[int]:
    prev = None
    current = head

    while current is not None:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    result = []
    while prev is not None:
        result.append(prev.val)
        prev = prev.next

    return result

#7)
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
