import unittest
from film import Film
from genere import Azione, Commedia, Drama
from noleggio import Noleggio

class TestBlockbuster(unittest.TestCase):
    def setUp(self):
        
        self.azione1 = Azione(1, "Film d'azione 1")
        self.azione2 = Azione(2, "Film d'azione 2")
        self.azione3 = Azione(3, "Film d'azione 3")
        self.commedia1 = Commedia(4, "Film commedia 1")
        self.commedia2 = Commedia(5, "Film commedia 2")
        self.dramma1 = Drama(6, "Film dramma 1")
        self.film_list = [self.azione1, self.azione2, self.azione3,
                          self.commedia1, self.commedia2, self.dramma1]
        self.noleggio = Noleggio(self.film_list)  

    def test_isAvaible(self):
        
        self.assertTrue(self.noleggio.isAvaible(self.azione1))
        self.assertFalse(self.noleggio.isAvaible(Film(7, "Film sconosciuto")))

    def test_rentAMovie(self):
        
        self.noleggio.rentAMovie(self.azione1, 1)
        self.assertNotIn(self.azione1, self.noleggio.film_list)
        self.assertIn(self.azione1, self.noleggio.rented_film[1])

        
        self.noleggio.rentAMovie(Film(7, "Film sconosciuto"), 2)
        self.assertNotIn(2, self.noleggio.rented_film)

    def test_giveBack(self):
        
        self.noleggio.rentAMovie(self.azione1, 1)
        self.noleggio.giveBack(self.azione1, 1, 3)
        self.assertIn(self.azione1, self.noleggio.film_list)
        self.assertNotIn(self.azione1, self.noleggio.rented_film[1])

    def test_calcolaPenaleRitardo(self):
        
        self.assertEqual(self.azione1.calcolaPenaleRitardo(2), 6.0)
        self.assertEqual(self.commedia1.calcolaPenaleRitardo(3), 7.5)
        self.assertEqual(self.dramma1.calcolaPenaleRitardo(4), 8.0)

    def test_printMovies(self):
        
        expected_output = "Film disponibili in negozio:\n"
        for film in self.film_list:
            expected_output += f"{film.getTitle()} - {film.getGenere()}\n"
        self.assertEqual(expected_output, self.noleggio.printMovies())

    def test_printRentMovies(self):
        
        self.noleggio.rentAMovie(self.azione1, 1)
        self.noleggio.rentAMovie(self.commedia1, 1)
        self.noleggio.rentAMovie(self.dramma1, 2)
        expected_output_client1 = "Film noleggiati dal cliente 1:\n"
        expected_output_client1 += f"{self.azione1.getTitle()} - {self.azione1.getGenere()}\n"
        expected_output_client1 += f"{self.commedia1.getTitle()} - {self.commedia1.getGenere()}\n"
        expected_output_client2 = "Film noleggiati dal cliente 2:\n"
        expected_output_client2 += f"{self.dramma1.getTitle()} - {self.dramma1.getGenere()}\n"
        self.assertEqual(expected_output_client1, self.noleggio.printRentMovies(1))
        self.assertEqual(expected_output_client2, self.noleggio.printRentMovies(2))

if __name__ == '__main__':
    unittest.main()