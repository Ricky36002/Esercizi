##############  EDOARDO DI LISIO  ##############
##############      24-05-00      ##############
'''
Sistema di Prenotazione Cinema
Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film in 
programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.
Classi:
- Film: Rappresenta un film con titolo e durata.
- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.
    Metodi:
    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di conferma o di errore.
    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
- Cinema: Gestisce le operazioni legate alla gestione delle sale.
    Metodi:
    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.
Test case:
- Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.
- Un cliente sceglie un film e prenota un certo numero di posti.
- Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.
'''

class Film:
    def __init__(self, titolo, durata):
        self.titolo = titolo  # Titolo del film
        self.durata = durata  # Durata del film in minuti

class Sala:
    def __init__(self, numero, film, posti_totali):
        self.numero = numero  # Numero identificativo della sala
        self.film = film  # Film attualmente in programmazione nella sala
        self.posti_totali = posti_totali  # Numero totale di posti nella sala
        self.posti_prenotati = 0  # Numero di posti già prenotati in sala

    def prenota_posti(self, num_posti):
        # Calcola il numero di posti disponibili
        posti_disponibili = self.posti_totali - self.posti_prenotati
        # Controlla se ci sono abbastanza posti disponibili per la prenotazione richiesta
        if num_posti <= posti_disponibili:
            # Se ci sono abbastanza posti disponibili, aggiorna il numero di posti prenotati e restituisce un messaggio di conferma
            self.posti_prenotati += num_posti
            return f"Prenotazione confermata per {num_posti} posti per il film {self.film.titolo}."
        else:
            # Se non ci sono abbastanza posti disponibili, restituisce un messaggio di errore
            return "Spiacenti, non ci sono abbastanza posti disponibili."

    def posti_disponibili(self):
        # Restituisce il numero di posti ancora disponibili nella sala
        return self.posti_totali - self.posti_prenotati

class Cinema:
    def __init__(self):
        self.sale = []  # Lista delle sale nel cinema

    def aggiungi_sala(self, sala):
        # Aggiunge una nuova sala al cinema
        self.sale.append(sala)

    def prenota_film(self, titolo_film, num_posti):
        # Cerca il film desiderato tra le sale del cinema
        for sala in self.sale:
            if sala.film.titolo == titolo_film:
                # Se il film è trovato, tenta di prenotare posti nella sala e restituisce un messaggio di stato
                return sala.prenota_posti(num_posti)
        # Se il film non è trovato, restituisce un messaggio di errore
        return "Spiacenti, il film selezionato non è in programmazione."

# Test case
cinema = Cinema()

# Aggiungi sale con film
sala1 = Sala(1, Film("Interstellar", 180), 100)
sala2 = Sala(2, Film("Inception", 150), 80)
cinema.aggiungi_sala(sala1)
cinema.aggiungi_sala(sala2)

# Prenotazione di posti
print(cinema.prenota_film("Inception", 2))  # Output: Prenotazione confermata per 2 posti per il film Inception.
print(cinema.prenota_film("Interstellar", 120))  # Output: Spiacenti, non ci sono abbastanza posti disponibili.
print(cinema.prenota_film("The Dark Knight", 2))  # Output: Spiacenti, il film selezionato non è in programmazione.