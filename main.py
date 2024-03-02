from repository.clientFileRepository import ClientFileRepository
from repository.clientRepository import ClientRepository
from repository.filmFileRepository import FilmFileRepository
from repository.filmRepository import FilmRepository
from service.clientService import ClientService
from service.client_service_reports import ReportsService
from service.filmService import FilmService
from tests.testAll import testAll
from ui.console import Console


def main():
    #functia apeleaza toate celelalte functii ale aplicatiei
    testAll()
    #filmRepository = FilmRepository()
    filmRepository = FilmFileRepository("filme.txt")
    #clientRepository = ClientRepository()
    clientRepository = ClientFileRepository("clienti.txt")

    filmService = FilmService(filmRepository)
    clientService = ClientService(clientRepository, filmRepository)
    reportsService = ReportsService(clientRepository, filmRepository)
    console = Console(filmService, clientService, reportsService)

    console.Menu()

main()