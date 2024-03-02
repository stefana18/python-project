from dataclasses import dataclass

@dataclass

class ClientDTO:
    nume: str
    lista_nr: int
    lista_inchirieri: list

class ClientDTOAssembler:
    @staticmethod
    def create_client_dto(client):
        nume = client.get_nume()
        lista_nr = len(client.get_lista_inchirieri())
        lista_inchirieri = client.get_lista_inchirieri()

        return ClientDTO(nume, lista_nr, lista_inchirieri)




