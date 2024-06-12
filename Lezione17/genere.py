from film import Film

class Genre(Film):
    def __init__(self, id, title, genre, penale):
       
        super().__init__(id, title)
        self.__genre = genre  
        self.__penale = penale  
    
    def getGenere(self):
        
        return self.__genre

    def getPenale(self):
        
        return self.__penale

    def calcolaPenaleRitardo(self, days):
        
        return self.__penale * days

class Azione(Genre):
    def __init__(self, id, title):
        
        super().__init__(id, title, "Azione", 3.0)

class Commedia(Genre):
    def __init__(self, id, title):
        
        super().__init__(id, title, "Commedia", 2.5)

class Drama(Genre):
    def __init__(self, id, title):
        
        super().__init__(id, title, "Dramma", 2.0)