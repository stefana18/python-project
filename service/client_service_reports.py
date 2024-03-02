from repository.clientRepository import ClientRepository
from repository.filmRepository import FilmRepository
from domain.entities_dto import *


class ReportsService:
    def __init__(self, clientRepository: ClientRepository, filmRepository: FilmRepository):
        self.__clientRepository = clientRepository
        self.__filmRepository = filmRepository

    def sortare_dupa_nume_si_numar(self):
        clienti_dto = self.__create_client_dto()
        clienti_dto = sorted(clienti_dto, key = lambda x: x.nume)
        clienti_dto = sorted(clienti_dto, key = lambda x: x.lista_nr)
        return clienti_dto

    def thirty_percent(self):
        clienti_dto = self.__create_client_dto()
        clienti_dto = sorted(clienti_dto, key = lambda x: x.lista_nr, reverse = True)
        rez = (30 * len(clienti_dto)) // 100
        rez += 1
        return clienti_dto[:rez]

    def __create_client_dto(self):
        clients_dto = []
        for client in self.__clientRepository.getAll():
            dto = ClientDTOAssembler.create_client_dto(client)
            clients_dto.append(dto)
        return clients_dto