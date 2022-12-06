import os
import sys
sys.path.append(os.getcwd())
import Operasjoner_felles
import mysqlconnector

def kontonummere_på_valgt_fødselsnummer (fødselsnummer): # printer ut alle kontonummere på valgt fødselsnummer (oppgitt i parameter)
    mysqlconnector.mycursor.execute(f"SELECT KONTONUMMER FROM KONTOER WHERE FØDSELSNUMMER = \"{fødselsnummer}\"")
    myresult = mysqlconnector.mycursor.fetchall()

    for x in myresult: # kaller legg til nuller funksjonen for hvert funnet kontonummer og printer ut hvert kontonummer som ble funnet
        Operasjoner_felles.legge_til_nuller(x[0], 2)
