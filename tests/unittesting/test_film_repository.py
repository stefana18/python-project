import unittest

from domain.entities import Film
from repository.filmRepository import FilmRepository


class TestFilmReppository(unittest.TestCase):
    def test_getAll(self):
        filmRepository = FilmRepository()
        film1 = Film("1", "Titlu", "Descriere", "Gen", 6)
        film2 = Film("2", "Titlu2", "Descriere2", "Gen2", 8)
        filmRepository.adaugaFilm(film1)
        filmRepository.adaugaFilm(film2)

        filme = filmRepository.getAll()
        self.assertEqual(len(filme),2)
        self.assertEqual(filme[0].get_id(),"1")
        self.assertEqual(filme[1].get_id(), "2")

    def test_getById(self):
        filmRepository = FilmRepository()
        film1 = Film("1", "Titlu", "Descriere", "Gen", 6)
        filmRepository.adaugaFilm(film1)

        film = filmRepository.getById("1")

        self.assertEqual(film.get_titlu(), "Titlu")


    def test_adaugaFilm(self):
        filmRepository = FilmRepository()
        film1 = Film("1", "Titlu", "Descriere", "Gen", 6)
        filmRepository.adaugaFilm(film1)

        filme = filmRepository.getAll()
        self.assertEqual(len(filme), 1)
        self.assertEqual(filme[0].get_id(),"1")

    def test_modificaFilm(self):
        filmRepository = FilmRepository()
        film1 = Film("1", "Titlu1", "Descriere1", "Gen1", 6)
        film2 = Film("1","Titlu2","Descriere2","gen2",5)
        filmRepository.adaugaFilm(film1)
        filmRepository.modifica(film2)

        filme = filmRepository.getAll()
        self.assertEqual(filme[0].get_titlu(),"Titlu2")

    def test_stergeFilm(self):
        filmRepository = FilmRepository()
        film1 = Film("1", "Titlu1", "Descriere1", "Gen1", 6)
        filmRepository.adaugaFilm(film1)

        filmRepository.sterge(film1.get_id())
        filme = filmRepository.getAll()

        self.assertEqual(len(filme),0)

if __name__ == '__main__':
    unittest.main()
