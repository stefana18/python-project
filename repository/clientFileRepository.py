#clasa va adauga dintr-un fisier clienti in ClientRepository
from domain.entities import Client
from repository.clientRepository import ClientRepository
from tests.errors import IdErrorEmpty, IdError, IdErrorNumeric, CnpErrorEmpty, CnpErrorNegative, CnpErrorLength, \
    CnpErrorS, CnpErrorNumeric, CnpErrorLL, CnpErrorZZ, CnpErrorJJ, CnpErrorInvalid
from tests.input_data_validation import Validation_addClient


class ClientFileRepository(ClientRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                lista_clienti = line.split(",")
                if lista_clienti[2][len(lista_clienti[2])-1] == '\n':
                    lista_clienti[2] = lista_clienti[2][:-1]
                client = Client(lista_clienti[0], lista_clienti[1], lista_clienti[2], [])
                try:
                    validation_addClient = Validation_addClient(lista_clienti[0], lista_clienti[1], lista_clienti[2])
                    validation_addClient.test_idClient()
                    validation_addClient.test_nume()
                    validation_addClient.test_cnpClient()
                    super().adaugaClient(client)
                except KeyError as e:
                    print(e)
                except IdErrorEmpty as iee:
                    print(iee)
                except IdError as ie:
                    print(ie)
                except IdErrorNumeric as ien:
                    print(ien)
                except CnpErrorEmpty as cee:
                    print(cee)
                except CnpErrorNegative as cen:
                    print(cen)
                except CnpErrorLength as cel:
                    print(cel)
                except CnpErrorS as ces:
                    print(ces)
                except CnpErrorNumeric as cenu:
                    print(cenu)
                except CnpErrorLL as cell:
                    print(cell)
                except CnpErrorZZ as cezz:
                    print(cezz)
                except CnpErrorJJ as cejj:
                    print(cejj)
                except CnpErrorInvalid as cei:
                    print(cei)
        f.close()

    def adaugaClient(self, client):
        #with open(self.__file_name, "a") as f:
            #f.write("\n" + client.get_id() + "," + client.get_name() + "," + client.get_cnp() + "," + str(client.get_list_rent()))
        super().adaugaClient(client)
        self.write_in_file()

    def modifica(self, clientNou):
        super().modifica(clientNou)
        self.write_in_file()

    def sterge(self, idClient):
        super().sterge(idClient)
        self.write_in_file()

    def write_in_file(self):
        try:
            f = open(self.__file_name, "w")
            lista_clienti = super().getAll()
            for client in lista_clienti:
                id = client.get_id()
                nume = client.get_nume()
                cnp = client.get_cnp()
                lista_inchirieri = client.get_lista_inchirieri()
                line = id + "," + nume + "," + cnp + "," + str(lista_inchirieri) + "\n"
                f.write(line)
            f.close()
        except IOError as IOE:
            print(IOE)