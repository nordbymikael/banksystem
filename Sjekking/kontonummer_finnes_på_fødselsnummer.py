import os
import sys
sys.path.append(os.getcwd())
import Sjekking
import mysqlconnector

def kontonummer_sjekk_om_finnes_på_fødselsnummer (kontonummer, fødselsnummer): # gjør det samme som den forrige funksjonen, men spørringen gjelder bare for kontonummere på fødselsnummeret som vi har valgt
    mysqlconnector.mycursor.execute(f"SELECT KONTONUMMER FROM KONTOER WHERE FØDSELSNUMMER = \"{fødselsnummer}\"")
    myresult = mysqlconnector.mycursor.fetchall() 
    return Sjekking.kontonummer_sjekk_om_finnes_loop(myresult, kontonummer) # denne har jeg på en egen funksjon for å forkorte koden. mer om det er sagt på forrige funksjon
