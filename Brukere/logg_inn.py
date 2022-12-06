import os
import sys
sys.path.append(os.getcwd())
import Operasjoner_felles
import Brukere
import Sjekking

def logg_inn (svar_start): # logger inn og velger svaralternativer fra starten (på slutten av denne funksjonen) for å kalle nødvendige funksjoner
    global svar_logg_inn_fødselsnummer
    svar_logg_inn_fødselsnummer = input("Vennligst skriv inn ditt fødselsnummer: ")

    if svar_logg_inn_fødselsnummer.isdigit() == True and len(svar_logg_inn_fødselsnummer) == 11 and Sjekking.fødselsnummer_sjekk_om_finnes(svar_logg_inn_fødselsnummer) == True: # sjekker om fødselsnummer er 11 sifre, er tall og finnes
        global svar_logg_inn_pinkode
        svar_logg_inn_pinkode = input("Vennligst skriv inn din pinkode: ")

        if svar_logg_inn_pinkode.isdigit() == True and len(svar_logg_inn_pinkode) in range(4, 8, 2) and Sjekking.pinkode_sjekk_om_riktig(svar_logg_inn_fødselsnummer, svar_logg_inn_pinkode) == True: # sjekker om pinkoden er riktig skrevet og stemmer med pinkoden til brukeren
            
            if svar_start == "2" and Sjekking.count_kontonummere(svar_logg_inn_fødselsnummer) == True: # velge kontonummer og kontrollere at du skrev en av de som du fikk opp
                global svar_logg_inn_kontonummer
                print(f"Du har logget inn på brukeren din.\nDu kan nå velge en av disse kontoene:")
                Operasjoner_felles.kontonummere_på_valgt_fødselsnummer(svar_logg_inn_fødselsnummer)
                svar_logg_inn_kontonummer = input("Vennligst skriv inn kontonummeret som du vil bruke: ")
                
                if svar_logg_inn_kontonummer.isdigit() == True and len(svar_logg_inn_kontonummer) == 11 and Sjekking.kontonummer_sjekk_om_finnes_på_fødselsnummer(svar_logg_inn_kontonummer, svar_logg_inn_fødselsnummer) == True:
                    Brukere.logget_inn_på_brukeren(svar_logg_inn_kontonummer, svar_logg_inn_fødselsnummer)

                else:
                    Operasjoner_felles.feilmelding()

            elif svar_start == "2" and Sjekking.count_kontonummere(svar_logg_inn_fødselsnummer) == False: # du kan ikke logge deg inn dresom du ikke har kontonummere på brukeren
                print("Du skrev riktig innloggingsinformasjon, men brukeren din har ingen eksisterende kontoer.\nVennligst opprett en konto og prøv på nytt.")

            elif svar_start == "3": # kalle legge til kontoer funksjon dersom du svarte 3 på starten
                Brukere.legge_til_kontoer(svar_logg_inn_fødselsnummer)

            elif svar_start == "4": # kalle slett konto funksjonen dersom du svarte 4 på starten
                Brukere.slett_konto(svar_logg_inn_fødselsnummer)

            elif svar_start == "5": # kalle slett bruker funksjonen dersom du svarte 5 på starten
                Brukere.slett_bruker(svar_logg_inn_fødselsnummer)

        else:
            Operasjoner_felles.feilmelding()

    else:
        Operasjoner_felles.feilmelding()