import os
import sys
sys.path.append(os.getcwd())
import mysqlconnector

def poststed_sjekk_om_finnes (postnummer):
    mysqlconnector.mycursor.execute(f"SELECT POSTSTED FROM POSTSTED WHERE POSTNUMMER = \"{postnummer}\"") # jeg henter postnummeret som jeg definerte i parameter og kjører en spørring som sjekker om postnummeret er definert i POSTSTED tabellen
    myresult = mysqlconnector.mycursor.fetchall() # setter sammen alle resultater som jeg fikk fra spørringen og returnerer en liste med tuples

    if myresult == []:
        return False # returnerer False dersom det ikke finnes noe poststed for postnummeret som vi hentet fra parameter. denne brukes for å sjekke om poststedet til brukeren finnes i POSTSTED tabellen. dersom poststedet ikke finnes, kan brukeren fylle opp tabellen med poststed for oss.
    else:
        return True # returnerer True dersom postnummeret som vi hetet fra parameter har et definert poststed i en egen tabell
