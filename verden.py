from rutenett import Rutenett

class Verden:
    def __init__(self, rader, kolonner):
        self._rutenett = Rutenett(rader,kolonner)
        self._generasjonsnummer = 0
        self._rutenett.fyll_med_tilfeldige_celler()

    def tegn(self):
        self._rutenett.tegn_rutenett()
        print(f'Generasjon: {self._generasjonsnummer} - Antall levende celler: {self._rutenett.antall_levende()}')

    def oppdatering(self):
        self._rutenett.koble_celler()

        #Tell antall naboer
        for rad in self._rutenett.getNostetListe():
            for celle in rad:
                celle.sett_levende_naboer()

        #Oppdater
        for rad in self._rutenett.getNostetListe():
            for celle in rad:
                celle.oppdater_status()


        self._generasjonsnummer += 1
