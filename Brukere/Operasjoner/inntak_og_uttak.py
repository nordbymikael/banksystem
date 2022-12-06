import datetime
dato_idag = datetime.date.today()
import os
import sys
sys.path.append(os.getcwd())
import mysqlconnector
import Brukere
import Sjekking
import Operasjoner_felles

def inntak_og_uttak (startmelding, kontonummer, sluttmelding1, sluttmelding2, svar_logget_inn_start): # inntak og uttak
    Brukere.sjekk_saldo(kontonummer) # sjekke saldo for å vite hvor mye du har
    operasjon_sum = input(f"Hvor mye vil du {startmelding} kontoen din (format: tall med to desimaler etter punktum): ") # variabelet sier om du skal sette inn eller ta ut (hentes fra parameter)
    mysqlconnector.mycursor.execute(f"SELECT SALDO FROM KONTOER WHERE KONTONUMMER = {kontonummer}") # spørring som henter nåværende/forrige saldo
    myresult = mysqlconnector.mycursor.fetchall()
    forrige_saldo = myresult[0][0] # du definerer forrige saldo
    
    if svar_logget_inn_start == "2" and Sjekking.string_er_float(operasjon_sum) == True and float(operasjon_sum) != 0.0: # sjekker at du tar inntak og at summen er float og at du ikke setter inn 0
        nye_saldo = float(forrige_saldo) + float(operasjon_sum) # summerer den gamle saldoen og det du setter inn
        mysqlconnector.mycursor.execute(f"UPDATE KONTOER SET SALDO = {nye_saldo} WHERE KONTONUMMER = {kontonummer}") # oppdatere saldo
        mysqlconnector.mycursor.execute(f"INSERT INTO HISTORIKK_INNTAK (KONTONUMMER, SALDO_FØR, SALDO_ETTER, INNTAK_SUM, TIDSPUNKT) VALUES ({int(kontonummer)}, {float(forrige_saldo)}, {nye_saldo}, {float(operasjon_sum)}, \"{dato_idag}\")") # setter inn i historikk
        mysqlconnector.mydb.commit() # lagre endringer
        print(f"Du har {sluttmelding1} {float(operasjon_sum)} kroner {sluttmelding2} kontoen din (kontonummer {kontonummer}).\nDin nye saldo er {float(nye_saldo)} kroner.") # oppsummering
    
    elif svar_logget_inn_start == "3" and Sjekking.string_er_float(operasjon_sum) == True and forrige_saldo >= float(operasjon_sum) and float(operasjon_sum) != 0.0: #ta ut
        nye_saldo = float(forrige_saldo) - float(operasjon_sum) # subtraherer den gamle saldoen og det du trekker fra kontoen din
        mysqlconnector.mycursor.execute(f"UPDATE KONTOER SET SALDO = {nye_saldo} WHERE KONTONUMMER = {kontonummer}") # oppdatere saldo
        mysqlconnector.mycursor.execute(f"INSERT INTO HISTORIKK_UTTAK (KONTONUMMER, SALDO_FØR, SALDO_ETTER, UTTAK_SUM, TIDSPUNKT) VALUES ({int(kontonummer)}, {float(forrige_saldo)}, {nye_saldo}, {float(operasjon_sum)}, \"{dato_idag}\")") # setter inn i historikk
        mysqlconnector.mydb.commit() # lagre endringer
        print(f"Du har {sluttmelding1} {float(operasjon_sum)} kroner {sluttmelding2} kontoen din (kontonummer {kontonummer}).\nDin nye saldo er {float(nye_saldo)} kroner.") # oppsummering

    else:
        Operasjoner_felles.feilmelding()
