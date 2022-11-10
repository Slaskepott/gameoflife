from random import randint
from celle import Celle

class Rutenett:
    def __init__(self, rader, kolonner):
        self._ant_rader = rader
        self._ant_kolonner = kolonner
        self._rutenett = self._lag_tomt_rutenett()

    def getNostetListe(self):
        return self._rutenett

    def _lag_tomt_rutenett(self):
        nostet_liste = []
        for i in range(self._ant_rader):
            nostet_liste.append(self._lag_tom_rad())
        return nostet_liste

    def _lag_tom_rad(self):
        liste = []
        for i in range(self._ant_kolonner):
            liste.append(None)
        return liste

    def fyll_med_tilfeldige_celler(self):
        i = 0
        j = 0
        for rad in self._rutenett:
            for kolonne in rad:
                self.lag_celle(i,j)
                j += 1
            j = 0
            i += 1

    def lag_celle(self, rad, kol):
        nyCelle = Celle()
        if randint(0,2) == 0:
            nyCelle.sett_levende()
        self._rutenett[rad][kol] = nyCelle

    #Henter celleobjekt på index x,y
    def hent_celle(self, rad, kol):
        if (0 <= rad < len(self._rutenett)): #sjekk om rad er i intervallet (0,lengden på rad-lista)
            if 0 <= kol < len(self._rutenett[rad]): #sjekk om kol er i intervallet (0, lengden på kol-lista)
                return self._rutenett[rad][kol] #returner objektet
        return None

    def tegn_rutenett(self):
        i = 0 #rad
        j = 0 #kolonne
        for rad in self._rutenett:
            nyRad = ''
            for kolonne in self._rutenett[i]:
                nyRad += f'{kolonne.hent_status_tegn()}'
                j += 1
            print(nyRad)
            j = 0
            i += 1

    #Oppdater cellens naboer-variabel
    def _sett_naboer(self, rad, kol):
        celle = self.hent_celle(rad,kol)
        celle._naboer = []
        for i in range(rad-1,rad+2): #Sjekk raden over, samme rad, og raden under
            for j in range(kol-1,kol+2): #Sjekk kolonnen til venstre, samme kolonne, og til høyre
                tempNabo = self.hent_celle(i,j) #Hent ut objektet
                if tempNabo != None and not (tempNabo is celle): #Sjekk om det er None (utenfor brettet) eller er "seg selv"
                    celle._naboer.append(tempNabo) #Oppdater nabolista

    def koble_celler(self):
        i = 0
        j = 0
        for rad in self._rutenett:
            for kolonne in rad:
                self._sett_naboer(i,j)
                j += 1
            j = 0
            i += 1

    def hent_alle_celler(self):
        liste = []
        for rad in self._rutenett:
            for kolonne in rad:
                liste.append(kolonne)
        return liste

    def antall_levende(self):
        antall = 0
        for celle in self.hent_alle_celler():
            if celle.er_levende():
                antall += 1
        return antall
