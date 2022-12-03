import datetime
dato_idag = datetime.date.today()
import sys
sys.path.append("Prosjekt_jul")
import hovedprogram
sys.path.append("Prosjekt_jul/Operasjoner_felles")
import feilmelding
sys.path.append("")
sys.path.append("")
sys.path.append("")

def overføring (kontonummer_sender): # 
    sjekk_saldo(hovedprogram.svar_logg_inn_kontonummer) # sjekker saldo slik at du får vite hvor mye du kan overføre
    hovedprogram.mycursor.execute(f"SELECT SALDO FROM KONTOER WHERE KONTONUMMER = {kontonummer_sender}")
    myresult = hovedprogram.mycursor.fetchall()
    forrige_saldo_sender = myresult[0][0] # definerer forrige saldo på senderen
    operasjon_sum = input(f"Hvor mye vil du overføre fra kontoen din (format: tall med to desimaler etter punktum): ") # hvor mye du vil overføre

    if string_er_float(operasjon_sum) and forrige_saldo_sender >= float(operasjon_sum) and float(operasjon_sum) != 0.0: # sjekker at du ikke overfører mer enn du har og at du ikke overfører 0 + sjekk at operasjon_sum er float
        kontonummer_mottaker = input(f"Hvilket kontonummer vil du overføre pengene til (format: 11 sifre, for eksempel 00000000001): ") # kontonummer du vil overføre til

        if kontonummer_mottaker.isdigit() and len(kontonummer_mottaker) == 11 and kontonummer_sjekk_om_finnes(kontonummer_mottaker) == True and kontonummer_mottaker != kontonummer_sender: # sjekk at kontonummer er riktig skrevet, at det finnes og at du ikke sender til deg selv
            ny_saldo_sender = float(forrige_saldo_sender) - float(operasjon_sum) # din nye saldo
            hovedprogram.mycursor.execute(f"UPDATE KONTOER SET SALDO = {ny_saldo_sender} WHERE KONTONUMMER = {kontonummer_sender}") # oppdatere din saldo
            hovedprogram.mycursor.execute(f"SELECT SALDO FROM KONTOER WHERE KONTONUMMER = {kontonummer_mottaker}") # spørring som henter forrige saldo mottaker
            myresult = hovedprogram.mycursor.fetchall()
            forrige_saldo_mottaker = myresult[0][0] # definere forrige saldo mottaker
            ny_saldo_mottaker = float(forrige_saldo_mottaker) + float(operasjon_sum) # ny saldo mottaker
            hovedprogram.mycursor.execute(f"UPDATE KONTOER SET SALDO = {ny_saldo_mottaker} WHERE KONTONUMMER = {kontonummer_mottaker}") # oppdatere saldo mottaker
            hovedprogram.mycursor.execute(f"INSERT INTO HISTORIKK_TRANSAKSJONER (KONTONUMMER, SENDT_TIL_KONTONUMMER, SALDO_FØR, SALDO_ETTER, TRANSAKSJON_SUM, TIDSPUNKT) VALUES ({kontonummer_sender}, {kontonummer_mottaker}, {float(forrige_saldo_sender)}, {ny_saldo_sender}, {float(operasjon_sum)}, \"{dato_idag}\")") # sette inn i historikk
            hovedprogram.mydb.commit() # lagre endringer
            hovedprogram.mycursor.execute(f"SELECT SALDO FROM KONTOER WHERE KONTONUMMER = {kontonummer_sender}") # henter din saldo
            myresult = hovedprogram.mycursor.fetchall()
            print(f"Du har overført {float(operasjon_sum)} kroner til kontoen med kontonummeret {kontonummer_mottaker}.\nDin nye saldo er {myresult[0][0]} kroner.") # printer en oppsummering som skriver hvor mye du overførte, til hvem og hva din saldo er nå
        else:
            feilmelding.feilmelding()
    else:
        feilmelding.feilmelding()
