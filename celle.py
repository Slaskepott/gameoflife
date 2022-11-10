class Celle:
    # Konstruktør
    def __init__(self):
        self._status = 'doed'
        self._naboer = []
        self._ant_levende_naboer = 0

    def sett_doed(self):
        self._status = 'doed'

    def sett_levende(self):
        self._status = 'levende'

    def er_levende(self):
        if self._status == 'levende':
            return True
        return False

    def hent_status_tegn(self):
        if self._status == 'levende':
            return 'O'
        return ' '

    def legg_til_nabo(self, nabo):
        self._naboer.append(nabo)

    def sett_levende_naboer(self):
        ant = 0
        for nabo in self._naboer:
            if nabo.er_levende():
                ant += 1
        self._ant_levende_naboer = ant
        return ant

    def get_levende_naboer(self):
        return self._ant_levende_naboer

    def get_status(self):
        return self._status

    def oppdater_status(self):
        levende = self.er_levende()
        ant_Levende_Naboer = self._ant_levende_naboer
        if (levende and ant_Levende_Naboer < 2) or (levende and ant_Levende_Naboer > 3):
            self.sett_doed()
        if (not levende) and ant_Levende_Naboer == 3:
            self.sett_levende()

    def __str__(self):
        return f'Cellen er {self._status} og har {self._ant_levende_naboer} naboer.'
