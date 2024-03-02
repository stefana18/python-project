import unittest


from domain.entities import Client, Film


class TestClient(unittest.TestCase):
    def setUp(self):
        self.client = Client("1", "Nume", "5030326260056", [1,2])

    def test_get_id(self):
        self.assertEqual(self.client.get_id(), "1")

    def test_get_nume(self):
        self.assertEqual(self.client.get_nume(),"Nume")

    def test_get_cnp(self):
        self.assertEqual(self.client.get_cnp(), "5030326260056")

    def test_set_id(self):
        self.client.set_id("2")
        self.assertEqual(self.client.get_id(),"2")

    def test_set_nume(self):
        self.client.set_nume("Nume2")
        self.assertEqual(self.client.get_nume(),"Nume2")

    def test_set_cnp(self):
        self.client.set_cnp("6030326260056")
        self.assertEqual(self.client.get_cnp(),"6030326260056")

    def tearDown(self) -> None:
        pass

class TestFilm(unittest.TestCase):
    def setUp(self):
        self.film = Film("1", "Titlu", "Descriere", "Gen", 6)

    def test_get_id(self):
        self.assertEqual(self.film.get_id(),"1")

    def test_get_titlu(self):
        self.assertEqual(self.film.get_titlu(),"Titlu")

    def test_get_descriere(self):
        self.assertEqual(self.film.get_descriere(),"Descriere")

    def test_get_gen(self):
        self.assertEqual(self.film.get_gen(), "Gen")

    def test_get_nrf(self):
        self.assertEqual(self.film.get_nrf(),6)

    def test_set_id(self):
        self.film.set_id("2")
        self.assertEqual(self.film.get_id(),"2")

    def test_set_titlu(self):
        self.film.set_titlu("Titlu1")
        self.assertEqual(self.film.get_titlu(),"Titlu1")

    def test_set_descriere(self):
        self.film.set_descriere("Descriere1")
        self.assertEqual(self.film.get_descriere(),"Descriere1")

    def test_set_gen(self):
        self.film.set_gen("Gen1")
        self.assertEqual(self.film.get_gen(),"Gen1")

    def test_set_nrf(self):
        self.film.set_nrf(2)
        self.assertEqual(self.film.get_nrf(),2)

    def tearDown(self) -> None:
        pass

def testAllEntities():
    test_get_id()

if __name__ == '__main__':
    unittest.main()