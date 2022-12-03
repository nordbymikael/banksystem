def slett_historikk_og_konto (kontonummer):
    mycursor.execute(f"DELETE FROM HISTORIKK_SALDO WHERE KONTONUMMER = {kontonummer}")
    mycursor.execute(f"DELETE FROM HISTORIKK_INNTAK WHERE KONTONUMMER = {kontonummer}")
    mycursor.execute(f"DELETE FROM HISTORIKK_UTTAK WHERE KONTONUMMER = {kontonummer}")
    mycursor.execute(f"DELETE FROM HISTORIKK_TRANSAKSJONER WHERE KONTONUMMER = {kontonummer}")
    mycursor.execute(f"DELETE FROM KONTOER WHERE KONTONUMMER = {kontonummer}")
    mydb.commit()
