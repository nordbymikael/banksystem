import os
import sys
sys.path.append(os.getcwd())
import Operasjoner_felles
import Brukere

def logget_inn_på_brukeren (svar_logg_inn_kontonummer, svar_logg_inn_fødselsnummer):
    while True:
        # startmelding
        print(f"\n\n\n################################################################################################\n\nVelkommen til Mikael bank.\nDu har logget inn på kontoen din med kontonummeret {svar_logg_inn_kontonummer}.\nDu har nå følgende valgmuligheter:\n1: Sjekke saldo.\n2: Inntak.\n3: Uttak.\n4: Overføring.\n5: Vise all personlig informasjon som banken har lagret om deg.\n6: Sjekk all historikk som banken har lagret om kontoen din.\n\033[1mTrykk på Enter\033[0m for å logge ut av brukeren.\n")
        global svar_logget_inn_start
        svar_logget_inn_start = input("Vennligs velg en av valgmulighetene ovenfor: ")

        if svar_logget_inn_start == "1": # sjekk saldo
            Brukere.sjekk_saldo(svar_logg_inn_kontonummer)

        elif svar_logget_inn_start == "2": # inntak (videre på funksjonen blir du overført til inntak)
            Brukere.inntak_og_uttak("sette inn på", svar_logg_inn_kontonummer, "satt inn", "på", svar_logget_inn_start)

        elif svar_logget_inn_start == "3": # uttak (videre på funksjonen blir du overført til uttak)
            Brukere.inntak_og_uttak("ta ut fra", svar_logg_inn_kontonummer, "tatt ut", "fra", svar_logget_inn_start)

        elif svar_logget_inn_start == "4": # overføring/transaksjon
            Brukere.overføring(svar_logg_inn_kontonummer)

        elif svar_logget_inn_start == "5": # personopplysninger som banken vet om deg
            Brukere.personopplysninger_om_deg(svar_logg_inn_fødselsnummer, svar_logg_inn_kontonummer)

        elif svar_logget_inn_start == "6": # sjekk historikk for saldo, inntak, uttak og transaksjoner
            Brukere.sjekk_historikk_start(svar_logg_inn_kontonummer)

        elif svar_logget_inn_start == "": # gå over til while True loopen på starten
            break

        else:
            Operasjoner_felles.feilmelding()