class Noleggio:
    def __init__(self, film_list):
        """
        Inizializza la classe Noleggio con una lista di film disponibili in negozio
        e un dizionario per tenere traccia dei film noleggiati da ogni cliente.

        Args:
        - film_list: una lista di oggetti Film disponibili in negozio.
        """
        self.film_list = film_list  
        self.rented_film = {}  

    def isAvaible(self, film):
        """
        Verifica se un film è disponibile in negozio.

        Args:
        - film: l'oggetto Film da verificare.

        Returns:
        - True se il film è disponibile, False altrimenti.
        """
        return film in self.film_list

    def rentAMovie(self, film, clientID):
        """
        Noleggia un film per un cliente.

        Args:
        - film: l'oggetto Film da noleggiare.
        - clientID: l'ID del cliente che noleggia il film.
        """
        if self.isAvaible(film):  
            self.film_list.remove(film)  
            if clientID in self.rented_film:  
                self.rented_film[clientID].append(film)  
            else:
                self.rented_film[clientID] = [film]  
            print(f"Il cliente {clientID} ha noleggiato {film.getTitle()}!")
        else:
            print(f"Non è possibile noleggiare il film {film.getTitle()}!")

    def giveBack(self, film, clientID, days):
        """
        Restituisce un film precedentemente noleggiato.

        Args:
        - film: l'oggetto Film da restituire.
        - clientID: l'ID del cliente che restituisce il film.
        - days: il numero di giorni per cui il cliente ha tenuto il film.
        """
        self.film_list.append(film)  
        self.rented_film[clientID].remove(film)  
        penale = film.calcolaPenaleRitardo(days) 
        print(f"Cliente: {clientID}! La penale da pagare per il film {film.getTitle()} è di {penale} euro!")

    def printMovies(self):
        """
        Stampa l'elenco dei film disponibili in negozio.

        Returns:
        - Una stringa formattata contenente i titoli e i generi dei film disponibili.
        """
        output = "Film disponibili in negozio:\n"
        for film in self.film_list:
            output += f"{film.getTitle()} - {film.getGenere()}\n"
        return output

    def printRentMovies(self, clientID):
        """
        Stampa l'elenco dei film noleggiati da un cliente specifico.

        Args:
        - clientID: l'ID del cliente di cui stampare l'elenco dei film noleggiati.

        Returns:
        - Una stringa formattata contenente i titoli e i generi dei film noleggiati dal cliente.
        """
        if clientID in self.rented_film:  
            output = f"Film noleggiati dal cliente {clientID}:\n"
            for film in self.rented_film[clientID]:
                output += f"{film.getTitle()} - {film.getGenere()}\n"
            return output
        else:
            return f"Nessun film noleggiato dal cliente {clientID}."  