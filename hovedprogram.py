from verden import Verden
from celle import Celle

def hovedprogram():
    run = True
    storrelse_rader = input('Hvor mange rader ønsker du?')
    storrelse_kolonner = input('Hvor mange kolonner ønsker du?')
    verden = Verden(int(storrelse_rader),int(storrelse_kolonner))
    verden.tegn()
    while run:
        verden.oppdatering()
        verden.tegn()
        svar = input('Trykk enter for å fortsette. Skriv q og trykk enter for å avslutte.')
        if svar == 'q':
            run = False

# starte hovedprogrammet
hovedprogram()
