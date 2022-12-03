import mysql.connector
import Brukere
import Operasjoner_felles
import Sjekking

mydb = mysql.connector.connect(
  host="localhost",
  port =3306,
  user="root",
  password="root",
  database="banksystem"
)

mycursor = mydb.cursor()

def logget_inn_på_brukeren ():
    while True:
        # startmelding
        print(f"\n\n\n################################################################################################\n\nVelkommen til Mikael bank.\nDu har logget inn på kontoen din med kontonummeret {logg_inn.svar_logg_inn_kontonummer}.\nDu har nå følgende valgmuligheter:\n1: Sjekke saldo.\n2: Inntak.\n3: Uttak.\n4: Overføring.\n5: Vise all personlig informasjon som banken har lagret om deg.\n6: Sjekk all historikk som banken har lagret om kontoen din.\n\033[1mTrykk på Enter\033[0m for å logge ut av brukeren.\n")
        global svar_logget_inn_start
        svar_logget_inn_start = input("Vennligs velg en av valgmulighetene ovenfor: ")

        if svar_logget_inn_start == "1": # sjekk saldo
            sjekk_saldo.sjekk_saldo(logg_inn.svar_logg_inn_kontonummer)

        elif svar_logget_inn_start == "2": # inntak (videre på funksjonen blir du overført til inntak)
            inntak_og_uttak.inntak_og_uttak("sette inn på", logg_inn.svar_logg_inn_kontonummer, "satt inn", "på")

        elif svar_logget_inn_start == "3": # uttak (videre på funksjonen blir du overført til uttak)
            inntak_og_uttak.inntak_og_uttak("ta ut fra", logg_inn.svar_logg_inn_kontonummer, "tatt ut", "fra")

        elif svar_logget_inn_start == "4": # overføring/transaksjon
            overføring.overføring(logg_inn.svar_logg_inn_kontonummer)

        elif svar_logget_inn_start == "5": # personopplysninger som banken vet om deg
            print_personopplysninger.personopplysninger_om_deg(logg_inn.svar_logg_inn_fødselsnummer, logg_inn.svar_logg_inn_kontonummer)

        elif svar_logget_inn_start == "6": # sjekk historikk for saldo, inntak, uttak og transaksjoner
            sjekk_historikk.sjekk_historikk_start(logg_inn.svar_logg_inn_kontonummer)

        elif svar_logget_inn_start == "": # gå over til while True loopen på starten
            break

        else:
            feilmelding.feilmelding()

def start ():
    while True:
        svar_start = input("################################################################################################\n\n\033[1mVelkommen til Mikhails bank.\033[0m\n\nHer kan du få full funksjonalitet tilgjengelig veldig fort.\n\nAlt du trenger er å logge inn på brukeren din og velge kontoen som du vil bruke, eller opprette en ny bruker.\nDu kan også legge til flere kontoer til en eksisterende bruker.\n\n\033[1mSkriv 1\033[0m for å opprette en ny bruker.\n\033[1mSkriv 2\033[0m for å logge inn på en eksisterende bruker.\n\033[1mSkriv 3\033[0m for å legge til kontoer på brukeren din.\n\033[1mSkriv 4\033[0m for å slette en konto på en eksisterende bruker.\n\033[1mSkriv 5\033[0m for å slette en bruker.\n\033[1mTrykk på Enter\033[0m for å avslutte programmet.\n") # startmelding

        if svar_start == "1":
            Brukere.opprett_bruker.opprett_bruker() # opprett bruker

        elif svar_start == "":
            break # dersom du har skrevet en tom string så stoppes loopen. denne kommer før neste elif fordi dersom denne (elif svar_start == "") kommer etter, så prøver Python å gjøre om en tom string til float og vi får en feil.

        elif spesielletegn.spesielle_tegn("alle tegn unntatt tall", svar_start) == False:

            if float(svar_start) in range(2, 6):
                logg_inn.logg_inn() # logg inn for å gjøre alt fra valg 2 til 5 og deretter (når du har logget inn) er det if og elif statements som sjekker hvor du skal gå videre. pga. sikerhet må man først logge inn
                
            else:
                feilmelding.feilmelding() # feilmelding dersom du ikke gjorde et av stegene ovenfor

        else:
            feilmelding.feilmelding() # feilmelding dersom du ikke gjorde et av stegene ovenfor

start()