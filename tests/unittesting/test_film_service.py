import unittest

from repository.filmRepository import FilmRepository
from service.filmService import FilmService


class TestFilmService(unittest.TestCase):
    def test_getAll(self):
        filmRepository = FilmRepository()
        filmService = FilmService(filmRepository)
        filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)
        filmService.adaugaFilm("2", "Titlu2", "Descriere2", "Gen2", 6)

        filme = filmService.getAll()
        self.assertEqual(len(filme),2)
        self.assertEqual(filme[0].get_id(),"1")
        self.assertEqual(filme[1].get_id(),"2")

    def test_adaugaFilm(self):
        filmRepository = FilmRepository()
        filmService = FilmService(filmRepository)
        filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)

        filme = filmService.getAll()

        self.assertEqual(len(filme),1)
        self.assertEqual(filme[0].get_titlu(),"Titlu")

    def test_modificaFilm(self):
        filmRepository = FilmRepository()
        filmService = FilmService(filmRepository)
        filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)

        filmService.modifica("1", "Titlu1", "Descriere1", "Gen1", 6)

        filme = filmService.getAll()

        self.assertEqual(len(filme),1)
        self.assertEqual(filme[0].get_id(),"1")
        self.assertEqual(filme[0].get_titlu(), "Titlu1")
        self.assertEqual(filme[0].get_descriere(), "Descriere1")
        self.assertEqual(filme[0].get_gen(),"Gen1")

    def test_stergeFilm(self):
        filmRepository = FilmRepository()
        filmService = FilmService(filmRepository)
        filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)

        filmService.sterge("1")

        filme = filmService.getAll()
        self.assertEqual(len(filme),0)

    def test_inchiriere_dupa_id(self):
        filmRepository = FilmRepository()
        filmService = FilmService(filmRepository)
        filmService.adaugaFilm("1", "Titlu", "Descriere", "Gen", 6)

        filmService.inchiriere_film_dupa_id("1")
        filme = filmService.getAll()

        self.assertEqual(filme[0].get_nrf(),7)

    def test_inchiriere_film_sortare(self):
        filmRepository = FilmRepository()
        filmService = FilmService(filmRepository)
        filmService.adaugaFilm("1", "Titlu1", "Descriere1", "Gen1", 1)
        filmService.adaugaFilm("2", "Titlu2", "Descriere2", "Gen2", 10)
        filmService.adaugaFilm("3", "Titlu3", "Descriere3", "Gen3", 7)

        filmService.inchiriere_film_sortare()
        filme = filmService.getAll()

        self.assertEqual(len(filme),3)
        self.assertEqual(filme[0].get_id(),"2")
        self.assertEqual(filme[1].get_id(), "3")
        self.assertEqual(filme[2].get_id(), "1")

        self.assertEqual(filme[0].get_nrf(),10)
        self.assertEqual(filme[1].get_nrf(), 7)
        self.assertEqual(filme[2].get_nrf(), 1)



if __name__ == '__main__':
    unittest.main()