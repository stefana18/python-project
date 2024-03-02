import unittest

from domain.entities import Film
from repository.clientRepository import ClientRepository
from repository.filmRepository import FilmRepository
from service.clientService import ClientService


class TestClientService(unittest.TestCase):
    def test_getAll(self):
        clientRepository = ClientRepository()
        filmRepository = FilmRepository()
        clientService = ClientService(clientRepository,filmRepository)
        clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])

        clienti = clientService.getAll()

        self.assertEqual(len(clienti),1)
        self.assertEqual(clienti[0].get_id(),"1")

    def test_adaugaClient(self):
        clientRepository = ClientRepository()
        filmRepository = FilmRepository()
        clientService = ClientService(clientRepository, filmRepository)
        clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])

        clienti = clientService.getAll()

        self.assertEqual(len(clienti), 1)
        self.assertEqual(clienti[0].get_id(), "1")

    def test_modificaClient(self):
        clientRepository = ClientRepository()
        filmRepository = FilmRepository()
        clientService = ClientService(clientRepository, filmRepository)
        clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])

        clientService.modifica("1", "Nume1", "5030326260056", [1, 2])
        clienti = clientService.getAll()

        self.assertEqual(clienti[0].get_nume(),"Nume1")
        self.assertEqual(len(clienti), 1)

    def test_stergeClient(self):
        clientRepository = ClientRepository()
        filmRepository = FilmRepository()
        clientService = ClientService(clientRepository, filmRepository)
        clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])

        clientService.sterge("1")

        clienti = clientService.getAll()
        self.assertEqual(len(clienti),0)


    def test_inchiriereFilm(self):
        clientRepository = ClientRepository()
        filmRepository = FilmRepository()
        clientService = ClientService(clientRepository, filmRepository)
        clientService.adaugaClient("1", "Nume", "5030326260056", [1, 2])
        film = Film("15", "Titlu", "Descriere", "Gen", 6)
        filmRepository.adaugaFilm(film)

        clientService.inchiriere_film("15", "1")

        clienti = clientService.getAll()

        self.assertEqual(clienti[0].get_lista_inchirieri(), [1,2,'15'])

    def test_sortareDupaNumeSiNumar(self):
        clientRepository = ClientRepository()
        filmRepository = FilmRepository()
        clientService = ClientService(clientRepository, filmRepository)
        clientService.adaugaClient("1", "Bogdan", "5030326260051", [1, 2, 3])
        clientService.adaugaClient("2", "Alin", "5030326260052", [5, 6, 7, 8, 9, 10])
        clientService.adaugaClient("3", "Teodora", "5030326260053", [2, 5, 99, 100])
        clientService.adaugaClient("4", "Nume4", "5030326260054", [])

        sorted_list = clientService.sortare_dupa_nume_si_numar()

        self.assertEqual(len(sorted_list),3)
        self.assertEqual(sorted_list[0].get_id(),"1")
        self.assertEqual(sorted_list[1].get_id(),"3")
        self.assertEqual(sorted_list[2].get_id(),"2")

    def test_thirtyPercent(self):
        clientRepository = ClientRepository()
        filmRepository = FilmRepository()
        clientService = ClientService(clientRepository, filmRepository)
        clientService.adaugaClient("1", "Bogdan", "5030326260051", [1, 2, 3])
        clientService.adaugaClient("2", "Alin", "5030326260052", [5, 6, 7, 8, 9, 10])
        clientService.adaugaClient("3", "Teodora", "5030326260053", [2, 5, 99, 100])
        clientService.adaugaClient("4", "Nume4", "5030326260054", [])

        sorted_list = clientService.thirty_percent()

        self.assertEqual(len(sorted_list),1)
        self.assertEqual(sorted_list[0].get_id(),"2")
        self.assertEqual(sorted_list[0].get_lista_inchirieri(),[5,6,7,8,9,10])

if __name__ == '__main__':
    unittest.main()
