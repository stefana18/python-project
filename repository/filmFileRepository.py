from domain.entities import Film
from repository.filmRepository import FilmRepository
from tests.errors import *
from tests.input_data_validation import Validation_addFilm


class FilmFileRepository(FilmRepository):
    def __init__(self, file_name):
        super().__init__()
        self.__file_name = file_name
        self.__load_data()

    def __load_data(self):
        with open(self.__file_name) as f:
            for line in f:
                lista_filme = line.split(",")
                if lista_filme[3][len(lista_filme[3])-1] == '\n':
                    lista_filme[3] = lista_filme[3][:-1]
                film = Film(lista_filme[0],lista_filme[1],lista_filme[2],lista_filme[3],0)
                try:
                    validation_addFilm = Validation_addFilm(lista_filme[0], lista_filme[1], lista_filme[2], lista_filme[3])
                    validation_addFilm.test_idFilm()
                    validation_addFilm.test_TitluFilm()
                    validation_addFilm.test_descriereFilm()
                    validation_addFilm.test_genFilm()
                    super().adaugaFilm(film)
                except KeyError as e:
                    print(e)
                except IdError as ie:
                    print(ie)
                except IdErrorEmpty as iee:
                    print(iee)
                except IdErrorNumeric as ien:
                    print(ien)
                except TitleErrorEmpty as tee:
                    print(tee)
                except DescriptionErrorEmpty as dee:
                    print(dee)
                except NameErrorEmpty as aee:
                    print(aee)
                except NameErrorAlpha as aea:
                    print(aea)
                except NameErrorUpper as aeu:
                    print(aeu)
        f.close()

    def adaugaFilm(self, film):
        #with open(self.__file_name, "a") as f:
            #f.write("\n" + film.get_id() + "," + film.get_title() + "," + film.get_description() + "," + book.get_author() + "," + str(book.get_brn()))
        super().adaugaFilm(film)
        self.write_in_file()

    def modifica(self, filmNou):
        super().modifica(filmNou)
        self.write_in_file()

    def sterge(self, idFilm):
        super().sterge(idFilm)
        self.write_in_file()

    def write_in_file(self):
        try:
            f = open(self.__file_name, "w")
            lista_filme = super().getAll()
            for film in lista_filme:
                id = film.get_id()
                titlu = film.get_titlu()
                descriere = film.get_descriere()
                gen = film.get_gen()
                nrf = film.get_nrf()
                line = id + "," + titlu + "," + descriere + "," + gen + "," + str(nrf) + "\n"
                f.write(line)
            f.close()
        except IOError as IOE:
            print(IOE)