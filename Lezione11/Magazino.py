#Scrivi un programma in Python che gestisca un magazzino. Il programma deve permettere di aggiungere prodotti al magazzino,
#cercare prodotti per nome e verificare la disponibilità di un prodotto.

#Definisci una classe Prodotto con i seguenti attributi:
#- nome (stringa)
#- quantità (intero)
 
#Definisci una classe Magazzino con i seguenti metodi:
#- aggiungi_prodotto(prodotto: Prodotto): aggiunge un prodotto al magazzino.
#- cerca_prodotto(nome: str) -> Prodotto: cerca un prodotto per nome e lo ritorna se esiste.
#- verifica_disponibilità(nome: str) -> str: verifica se un prodotto è disponibile in magazzino.
...
class Prodotto:
    def init(self, nome: str, quantità: int):
        self.nome = nome
        self.quantità = quantità

class Magazzino:
    def init(self):
        self.prodotti = []

    def aggiungiprodotto(self, prodotto: Prodotto):
        for p in self.prodotti:
            if p.nome == prodotto.nome:
                p.quantità += prodotto.quantità
                return
        self.prodotti.append(prodotto)

    def cercaprodotto(self, nome: str) -> Prodotto:
        for prodotto in self.prodotti:
            if prodotto.nome == nome:
                return prodotto
        return None

    def verificadisponibilità(self, nome: str) -> str:
        prodotto = self.cercaprodotto(nome)
        if prodotto is not None:
            if prodotto.quantità > 0:
                return f"Il prodotto '{nome}' è disponibile con quantità: {prodotto.quantità}."
            else:
                return f"Il prodotto '{nome}' non è disponibile."
        else:
            return f"Il prodotto '{nome}' non esiste nel magazzino."