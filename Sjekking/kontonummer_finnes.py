import os
import sys
sys.path.append(os.getcwd())
import Operasjoner_felles
import mysqlconnector

def kontonummer_sjekk_om_finnes (kontonummer):
    mysqlconnector.mycursor.execute(f"SELECT KONTONUMMER FROM KONTOER") # spørring som henter alle kontonummere fra KONTOER tabellen
    myresult = mysqlconnector.mycursor.fetchall() # setter sammen alle resultater som jeg fikk fra spørringen og returnerer en liste med tuples
    return kontonummer_sjekk_om_finnes_loop(myresult, kontonummer) # denne har jeg på en egen funksjon for å forkorte koden. mer om det er sagt på forrige funksjon

def kontonummer_sjekk_om_finnes_loop (myresult, kontonummer):
    for x in myresult:
        adjustedX = Operasjoner_felles.legge_til_nuller(x[0], 1) # legger til nuller for hvert kontonummer som hentes fra spørringen (legger til nuller for å få 11 sifre)
        if adjustedX == kontonummer:
            return True # returnere True dersom kontonummeret som vi skrev ble funnet
