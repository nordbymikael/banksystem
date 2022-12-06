import os
import sys
sys.path.append(os.getcwd())
import Operasjoner_felles
import Brukere
import mysqlconnector

def slett_bruker (fødselsnummer):
    svar_bekreft = input("Du er på vei til å slette din bruker.\nDersom du sletter brukeren din, vil alle kontoer og deres relatert informasjon (saldo og historikk) slettes.\nAll personlig informasjon som du skrev inn når du lagde brukeren blir også slettet!\nDet er umulig å gjenopprette denne informasjonen dersom den slettes!\n\033[1mSkriv Ja\033[0m dersom du er sikker på at du vil slette brukeren, \033[1meller alt mulig annet\033[0m for å avbryte: ").capitalize()

    if svar_bekreft == "Ja": # dersom du svarer "Ja", så vil brukeren din bli slettet
        mysqlconnector.mycursor.execute(f"SELECT KONTONUMMER FROM KONTOER WHERE FØDSELSNUMMER = \"{fødselsnummer}\"") # spørring som henter kontonummere på valgt fødselsnummer
        myresult = mysqlconnector.mycursor.fetchall()
        
        for x in myresult:
            Brukere.slett_historikk_og_konto(Operasjoner_felles.legge_til_nuller(x[0], 1)) # kaller funksjonen som sletter kontoen som for loopen går gjennom nå. legge til nuller funksjonen legger til nuller til kontonummeret som ble funnet
            print(f"All historikk og saldoen til kontoen {Operasjoner_felles.legge_til_nuller(x[0], 1)} ble slettet.") # sier at kontoen er slettet. legge til nuller funksjonen legger til nuller
        mysqlconnector.mycursor.execute(f"DELETE FROM KUNDEINFO WHERE FØDSELSNUMMER = {fødselsnummer}") # sletter informasjon fra KUNDEINFO som var relatert til alle kontonene som ble slettet
        mysqlconnector.mydb.commit() # lagre endringer
        print(f"Alle kontoene dine ble slettet.\nBrukeren din med fødselsnummeret {fødselsnummer} ble slettet.\nVi minner på om at denne informasjonen ikke er lagret hos oss nå.")
    else:
        print("\033[1mDu har avbrutt fjerningen av brukeren din.\nVennligst start på nytt eller ta andre valg.\033[0m") # burker ikke feilmelding pga. passer ikke inn
