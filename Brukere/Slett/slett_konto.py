import os
import sys
sys.path.append(os.getcwd())
import Operasjoner_felles
import Brukere
import Sjekking
import mysqlconnector

def slett_konto (fødselsnummer):
    if Sjekking.count_kontonummere(fødselsnummer) == True: # sjekker først om det finnes kontoer som man kan slette
        print("\nHer er alle kontoene dine:")
        Operasjoner_felles.kontonummere_på_valgt_fødselsnummer(fødselsnummer) # printer ut kontonummere
        print("\nNB! Dersom du sletter en konto, så sletter du også saldoen på kontoen og all relatert historikk!\nDet er umulig å gjenopprette denne informasjonen dersom den slettes.\n")
        konto_som_slettes = input("Skriv hvilken konto du vil slette: ") # valg av hvilken konto du vil slette

        if konto_som_slettes.isdigit() == True and len(konto_som_slettes) == 11 and Sjekking.kontonummer_sjekk_om_finnes_på_fødselsnummer(konto_som_slettes, fødselsnummer) == True:
            mysqlconnector.mycursor.execute(f"SELECT SALDO FROM KONTOER WHERE KONTONUMMER = {konto_som_slettes}")
            myresult = mysqlconnector.mycursor.fetchall()
            svar_bekreft = input(f"Du sletter en konto som har en saldo på {myresult[0][0]} kroner.\nDersom du sletter kontoen, vil ikke saldoen og all historikk bli lagret.\nVi minner på at det er umulig å gjenopprette denne informasjonen dersom den slettes!\n\033[1mSkriv Ja\033[0m dersom du er sikker på at du vil slette kontoen, \033[1meller alt mulig annet\033[0m for å avbryte: ").capitalize()
            # du får vite kort informasjon om kontoen og hva som slettes

            if svar_bekreft == "Ja": # slett kontoen dersom du svarte "Ja"
                Brukere.slett_historikk_og_konto(konto_som_slettes)
                print(f"\nDu har slettet kontoen med kontonummeret {konto_som_slettes}.\nHer er alle kontoene som er igjen på brukeren din:")
                Operasjoner_felles.kontonummere_på_valgt_fødselsnummer(fødselsnummer) # du får printet ut kontoer som du har igjen på brukeren

            else:
                print("\033[1mDu har avbrutt fjerningen av kontoen din.\nVennligst start på nytt eller ta andre valg.\033[0m")
        else:
            Operasjoner_felles.feilmelding()
    else:
        print("Du skrev riktig innloggingsinformasjon, men brukeren din har ingen eksisterende kontoer.\nVennligst opprett en konto og prøv på nytt.")
