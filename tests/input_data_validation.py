from tests.errors import *


class Validation_addFilm():
    def __init__(self, idFilm, titlu, descriere, gen):
        self.idFilm = idFilm
        self.titlu = titlu
        self.descriere = descriere
        self.gen = gen

    def test_idFilm(self):
        if len(self.idFilm) == 0:
            raise IdErrorEmpty(self.idFilm)
        if self.idFilm[0] == "-":
            raise IdError(self.idFilm)
        if self.idFilm.isnumeric() == False:
            raise IdErrorNumeric(self.idFilm)

    def test_TitluFilm(self):
        if len(self.titlu) == 0:
            raise TitleErrorEmpty(self.titlu)

    def test_descriereFilm(self):
        if len(self.descriere) == 0:
            raise DescriptionErrorEmpty(self.descriere)

    def test_genFilm(self):
        if len(self.gen) == 0:
            raise GenErrorEmpty(self.gen)

class Validation_addClient():
    def __init__(self, idClient, nume, cnp):
        self.idClient = idClient
        self.nume = nume
        self.cnp = cnp

    def test_idClient(self):
        if len(self.idClient) == 0:
            raise IdErrorEmpty(self.idClient)
        if self.idClient[0] == "-":
            raise IdError(self.idClient)
        if self.idClient.isnumeric() == False:
            raise IdErrorNumeric(self.idClient)

    def test_nume(self):
        if len(self.nume) == 0:
            raise NameErrorEmpty(self.nume)
        nume_client = self.nume.split()
        for nume in nume_client:
            if nume.isalpha() == False:
                raise NameErrorAlpha(nume)

        if self.nume[0].isupper() == False:
            raise NameErrorUpper(self.nume)

    def test_cnpClient(self):
        if len(self.cnp) == 0:
            raise CnpErrorEmpty(self.cnp)
        if self.cnp[0] == "-":
            raise CnpErrorNegative(self.cnp)
        if self.cnp.isnumeric() == False:
            raise CnpErrorNumeric(self.cnp)
        if not len(self.cnp) == 13:
            raise CnpErrorLength(self.cnp)

        #------S------#
        if not (int(self.cnp[0]) >= 1 and int(self.cnp[0]) <= 8):
            raise CnpErrorS(self.cnp)
        # ------S------#

        # ------LL------#
        LL = self.cnp[3:5]
        LL_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        if LL not in LL_list:
            raise CnpErrorLL(self.cnp)
        # ------LL------#

        # ------ZZ------#
        ZZ = self.cnp[5:7]
        ZZ_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
        if ZZ not in ZZ_list:
            raise CnpErrorZZ(self.cnp)
        # ------ZZ------#

        # ------JJ------#
        JJ = self.cnp[7:9]
        JJ_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
        if JJ not in JJ_list:
            if not(int(JJ) >= 10 and int(JJ) <= 52):
                raise CnpErrorJJ(self.cnp)
        # ------JJ------#

        if self.cnp[11] == "0":
            raise CnpErrorInvalid(self.cnp)

class Validation_updateFilm():
    def __init__(self, idFilm, titluFilm, descriereFilm, genFilm, inchirieri_film):
        self.idFilm = idFilm
        self.titluFilm = titluFilm
        self.descriereFilm = descriereFilm
        self.genFilm = genFilm
        self.inchirieri_film = inchirieri_film

    def test_idFilm(self):
        if len(self.idFilm) == 0:
            raise IdErrorEmpty(self.idFilm)
        if self.idFilm[0] == "-":
            raise IdError(self.idFilm)
        if self.idFilm.isnumeric() == False:
            raise IdErrorNumeric(self.idFilm)

    def test_titluFilm(self):
        if len(self.titluFilm) == 0:
            raise TitleErrorEmpty(self.titluFilm)

    def test_descriereFilm(self):
        if len(self.descriereFilm) == 0:
            raise DescriptionErrorEmpty(self.descriereFilm)

    def test_genFilm(self):
        if len(self.genFilm) == 0:
            raise GenErrorEmpty(self.genFilm)

    def test_inchirieri_film(self):
        if int(self.inchirieri_film) < 0:
            raise InchiriereErrorValue(self.inchirieri_film)

class Validation_updateClient():
    def __init__(self, idClient, numeClient, cnpClient):
        self.idClient = idClient
        self.numeClient = numeClient
        self.cnpClient = cnpClient

    def test_idClient(self):
        if len(self.idClient) == 0:
            raise IdErrorEmpty(self.idClient)
        if self.idClient[0] == "-":
            raise IdError(self.idClient)
        if self.idClient.isnumeric() == False:
            raise IdErrorNumeric(self.idClient)

    def test_numeClient(self):
        if len(self.numeClient) == 0:
            raise NameErrorEmpty(self.numeClient)

        nume_client = self.numeClient.split()
        for nume in nume_client:
            if nume.isalpha() == False:
                raise NameErrorAlpha(nume)

        if self.numeClient[0].isupper() == False:
            raise NameErrorUpper(self.numeClient)

    def test_cnpClient(self):
        if len(self.cnpClient) == 0:
            raise CnpErrorEmpty(self.cnpClient)
        if self.cnpClient[0] == "-":
            raise CnpErrorNegative(self.cnpClient)
        if self.cnpClient.isnumeric() == False:
            raise CnpErrorNumeric(self.cnpClient)
        if not len(self.cnpClient) == 13:
            raise CnpErrorLength(self.cnpClient)

        #------S------#
        if not (int(self.cnpClient[0]) >= 1 and int(self.cnpClient[0]) <= 8):
            raise CnpErrorS(self.cnpClient)
        # ------S------#

        # ------LL------#
        LL = self.cnpClient[3:5]
        LL_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]
        if LL not in LL_list:
            raise CnpErrorLL(self.cnpClient)
        # ------LL------#

        # ------ZZ------#
        ZZ = self.cnpClient[5:7]
        ZZ_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31"]
        if ZZ not in ZZ_list:
            raise CnpErrorZZ(self.cnpClient)
        # ------ZZ------#

        # ------JJ------#
        JJ = self.cnpClient[7:9]
        JJ_list = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
        if JJ not in JJ_list:
            if not(int(JJ) >= 10 and int(JJ) <= 52):
                raise CnpErrorJJ(self.cnpClient)
        # ------JJ------#

        if self.cnpClient[11] == "0":
            raise CnpErrorInvalid(self.cnpClient)