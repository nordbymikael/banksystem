import os
import sys
sys.path.append(os.getcwd())
import mysqlconnector

def slett_historikk_og_konto (kontonummer):
    mysqlconnector.mycursor.execute(f"DELETE FROM HISTORIKK_SALDO WHERE KONTONUMMER = {kontonummer}")
    mysqlconnector.mycursor.execute(f"DELETE FROM HISTORIKK_INNTAK WHERE KONTONUMMER = {kontonummer}")
    mysqlconnector.mycursor.execute(f"DELETE FROM HISTORIKK_UTTAK WHERE KONTONUMMER = {kontonummer}")
    mysqlconnector.mycursor.execute(f"DELETE FROM HISTORIKK_TRANSAKSJONER WHERE KONTONUMMER = {kontonummer}")
    mysqlconnector.mycursor.execute(f"DELETE FROM KONTOER WHERE KONTONUMMER = {kontonummer}")
    mysqlconnector.mydb.commit()
