import unittest

from domain.entities import Client
from repository.clientRepository import ClientRepository


class TestClientRepository(unittest.TestCase):
    def setUp(self):
        self.clientRepository = ClientRepository()
        self.client = Client("1","Nume","5030326260056",[1,2])
        self.clientRepository.adaugaClient(self.client)

    def test_getAll(self):
        clienti = self.clientRepository.getAll()

        self.assertEqual(len(clienti),1)
        self.assertEqual(clienti[0].get_id(), "1")

    def test_getById(self):

        client1 = self.clientRepository.getById(self.client.get_id())

        self.assertEqual(client1.get_id(), "1")
        self.assertEqual(client1.get_nume(), "Nume")

    def test_adaugaClient(self):

        clienti = self.clientRepository.getAll()

        self.assertEqual(len(clienti), 1)
        self.assertEqual(clienti[0].get_id(), "1")

    def test_modificaClient(self):

        self.clientRepository.modifica(self.client)
        clienti = self.clientRepository.getAll()
        self.assertEqual(clienti[0].get_nume(),"Nume")

    def test_stergeClient(self):
        self.clientRepository.sterge(self.client.get_id())

        clienti = self.clientRepository.getAll()
        self.assertEqual(len(clienti), 0)
        

if __name__ == '__main__':
    unittest.main()