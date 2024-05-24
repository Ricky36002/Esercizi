
#Sistema di Prenotazione Cinema

#Sviluppa un sistema in Python che gestisca le prenotazioni per un cinema. Il cinema ha diverse sale, ognuna con un diverso film
#in programmazione. Gli utenti possono vedere quali film sono disponibili e prenotare posti per un determinato spettacolo.

#Classi:
#- Film: Rappresenta un film con titolo e durata.
#- Sala: Rappresenta una sala con numero identificativo, film attualmente in programmazione, posti totali, posti prenotati.

#    Metodi:
#    - prenota_posti(num_posti): Prenota un certo numero di posti nella sala, se disponibili. Restituisce un messaggio di 
#      conferma o di errore.
#    - posti_disponibili(): Restituisce il numero di posti ancora disponibili nella sala.
#- Cinema: Gestisce le operazioni legate alla gestione delle sale.

#    Metodi:
#    - aggiungi_sala(sala): Aggiunge una nuova sala al cinema.
#    - prenota_film(titolo_film, num_posti): Trova il film desiderato e tenta di prenotare posti. Restituisce un messaggio di stato.

#Test case:
#- Un gestore del cinema configura le sale aggiungendo i film e i dettagli dei posti.

#- Un cliente sceglie un film e prenota un certo numero di posti.

#- Il sistema verifica la disponibilità e conferma o rifiuta la prenotazione.

class Film:

    def __init__(self, title: str, duration: str):

        self.title: str = title 
        self.duration: str = duration

class Room:
    def __init__(self, room_number:int, film_ongoing: str, total_seats: int):

        self.room_number: int = room_number
        self.film_ongoing :str = film_ongoing
        self.total_seats: int = total_seats
        self.preno_seat: int = 0

    def pre_seat (self, number_seats):
        
        open_seats = self.total_seats - self.preno_seat
        if number_seats <= open_seats:
            self.preno_seat += number_seats
            return(f"Prenotazione confermata per{number_seats} posti per il film {self.film_ongoing.title}")
        else:
            return(f"Spiacenti, non ci sono abbastanza posti disponibili")
        
    def posti_disponibili(self):
        
        return self.total_seats - self.preno_seat

class Cinema:

    def __init__(self):
        
        self.rooms: list = []


    def aggiungi_sala(self, room):

        self.rooms.append(room)

    def prenota_film(self, film_title: str, num_posti):

        for room in self.rooms:
            
            if room.film_ongoing.title == film_title:
                
                return room.pre_seat(num_posti)
        return (f"Spiacent, il film selezionato non è in programmazione")

cinema = Cinema()

room1= Room(1, Film("Pinocchio", 110), 80)
room2= Room(2, Film("Biancaneve", 120),90)
cinema.aggiungi_sala(room1)
cinema.aggiungi_sala(room2)

print(cinema.prenota_film("Pinocchio", 3))
print(cinema.prenota_film("Biancaneve", 99))
print(cinema.prenota_film("Bambi",5))




            
    

































































































