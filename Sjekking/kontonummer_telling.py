import os
import sys
sys.path.append(os.getcwd())
import mysqlconnector

def count_kontonummere (fødselsnummer): # teller alle kontonummere på valgt fødselsnummer
    mysqlconnector.mycursor.execute(F"SELECT COUNT(*) FROM KONTOER WHERE FØDSELSNUMMER = {fødselsnummer}")
    myresult = mysqlconnector.mycursor.fetchall()

    if myresult[0][0] == 0:
        return False # returnerer False dersom spørringen ga 0 som svar (at ingen kontoer ble funnet)
    else:
        return True # returnerer True dersom spørringen fant kontonummere
