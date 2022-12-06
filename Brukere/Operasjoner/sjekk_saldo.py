import datetime
dato_idag = datetime.date.today()

import os
import sys
sys.path.append(os.getcwd())
import mysqlconnector

def sjekk_saldo (kontonummer):
    mysqlconnector.mycursor.execute(f"SELECT SALDO FROM KONTOER WHERE KONTONUMMER = {kontonummer}") # spørring som henter saldoen din på valgt kontonummer
    myresult = mysqlconnector.mycursor.fetchall()
    print(f"Din nåværende saldo på kontoen er {myresult[0][0]} kroner.") # printer ut din saldo

    mysqlconnector.mycursor.execute(f"INSERT INTO HISTORIKK_SALDO (KONTONUMMER, SALDO, TIDSPUNKT) VALUES ({int(kontonummer)}, {myresult[0][0]}, \"{dato_idag}\")") # sette inn sjekket saldo i historikk
    mysqlconnector.mydb.commit()
