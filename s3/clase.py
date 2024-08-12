class Entitate(object):
    def __init__(self, id, nume):

        self.id = id
        self.nume = nume

    def show(self):
        print("{} {}.".format(self.id, self.nume))


class Tara(Entitate):
    def __init__(self, id, nume, populatie, pib):
        super().__init__(id, nume)
        self.populatie = populatie
        self.pib = pib

    def show(self):
        print("{} {} {} {}.".format(self.id, self.nume,
                                    self.populatie, self.pib))

    def __str__(self):
        return "{} {} {} {}".format(self.id, self.nume,
                                     self.populatie, self.pib)

    def __gt__(self, other):
        return self.pib > other.pib
