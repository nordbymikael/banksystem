import datetime
dato_idag = datetime.date.today()

def sjekk_saldo (kontonummer):
    mycursor.execute(f"SELECT SALDO FROM KONTOER WHERE KONTONUMMER = {kontonummer}") # spørring som henter saldoen din på valgt kontonummer
    myresult = mycursor.fetchall()
    print(f"Din nåværende saldo på kontoen er {myresult[0][0]} kroner.") # printer ut din saldo

    mycursor.execute(f"INSERT INTO HISTORIKK_SALDO (KONTONUMMER, SALDO, TIDSPUNKT) VALUES ({int(kontonummer)}, {myresult[0][0]}, \"{dato_idag}\")") # sette inn sjekket saldo i historikk
    mydb.commit()
