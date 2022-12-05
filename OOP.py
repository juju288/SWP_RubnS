from enum import Enum


class Geschlecht(Enum):
    Männlich = 0
    Weiblich = 1


class Person:
    def __init__(self, first_name, last_name, geschlecht):
        self.first_name = first_name
        self.last_name = last_name
        self.geschlecht = geschlecht

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.geschlecht}"




class Abteilung(Enum):
    Drehen = 0
    IT = 1
    Verwaltung = 2
    Montage = 3
    Buchhaltung = 4


class Mitarbeiter(Person):
    def __init__(self, first_name, last_name, geschlecht, abteilung, vollzeit: bool):
        super().__init__(first_name, last_name, geschlecht)
        self.abteilung = Abteilung.UNDEFINED if Abteilung is None else abteilung
      #  self.gehalt = gehalt
        self.vollzeit = vollzeit

    def __repr__(self) -> str:
        return super().__str__() + f"{self.abteilung} {self.vollzeit}"




class Gruppenleiter(Mitarbeiter):
    def __init__(self, first_name, last_name, geschlecht, abteilung, anzMitarbeiter):
        super().__init__(first_name, last_name, geschlecht, abteilung, True)
        self.anzMitarbeiter = anzMitarbeiter

    def __repr__(self) -> str:
        return super().__str__() + f"{self.anzMitarbeiter}"




class Firma:

    def __init__(self, mitarbeiter: list = None):
        self.mitarbeiter = [] if mitarbeiter is None else mitarbeiter

    def add_mitarbeiter(self, mitarbeiter):
        self.mitarbeiter.append(mitarbeiter)


    def init_mitarbeiter(self):
        self.mitarbeiter.append(Mitarbeiter("Tim", "Mair", Geschlecht.Männlich, Abteilung.IT, True))
       # self.mitarbeiter.append(Mitarbeiter())
        self.mitarbeiter.append(Gruppenleiter("Tom", "Mayer", Geschlecht.Männlich, Abteilung.IT, 10))


    def count_mitarbeiter(self):
        # return len([ m for m in self.mitarbeiter if type(m) == Mitarbeiter])
        c = 0
        for m in self.mitarbeiter:
            if type(m) == Mitarbeiter:
                c += 1
        return c

    def count_gruppenleiter(self):
        c = 0
        for g in self.mitarbeiter:
            if type(g) == Gruppenleiter:
                c += 1
        return c


    def count_abteilungen(self):
        temp = {}
        for m in self.mitarbeiter:
            temp[m.abteilung] = 0
        return len(temp)


    def groeßte_abteilung(self):
        temp = {}
        for m in self.mitarbeiter:
            if m.abteilung in temp.keys():      #ist es in der Liste
                temp[m.abteilung] += 1
            else:
                temp[m.abteilung] = 1
        abteilung = temp.keys()[0]
        for a in temp.keys():
            if temp[abteilung] < temp[a]:
                abteilung = a
        return abteilung


    def prozentanteil_frauen(self):
        temp = {
            Geschlecht.MALE: 0,
            Geschlecht.FEMALE: 0
        }
        for m in self.mitarbeiter:
            if m.Geschlecht in temp.keys():
                temp[m.Geschlecht] += 1/len(self.mitarbeiter)
            else:
                temp[m.Geschlecht] = 1/len(self.mitarbeiter)
        for key in temp.keys():
            temp[key] = round(temp[key] *100, 1)
        return temp


if __name__ == '__main__':
    f = Firma()
    f.init_mitarbeiter()
