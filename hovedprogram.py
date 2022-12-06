import Brukere
import Operasjoner_felles
import Sjekking

def start ():
    while True:
        svar_start = input("################################################################################################\n\n\033[1mVelkommen til Mikaels bank.\033[0m\n\nHer kan du få full funksjonalitet og alt tilgjengelig veldig fort.\n\nAlt du trenger er å logge inn på brukeren din og velge kontoen som du vil bruke, eller opprette en ny bruker.\nDu kan også legge til flere kontoer på en eksisterende bruker.\n\n\033[1mSkriv 1\033[0m for å opprette en ny bruker.\n\033[1mSkriv 2\033[0m for å logge inn på en eksisterende bruker.\n\033[1mSkriv 3\033[0m for å legge til kontoer på brukeren din.\n\033[1mSkriv 4\033[0m for å slette en konto på en eksisterende bruker.\n\033[1mSkriv 5\033[0m for å slette en bruker.\n\033[1mTrykk på Enter\033[0m for å avslutte programmet.\n") # startmelding

        if svar_start == "1":
            Brukere.opprett_bruker() # opprett bruker

        elif svar_start == "":
            break # dersom du har skrevet en tom string så stoppes loopen. denne kommer før neste elif fordi dersom denne (elif svar_start == "") kommer etter, så prøver Python å gjøre om en tom string til float og vi får en feil.

        elif Sjekking.spesielle_tegn("alle tegn unntatt tall", svar_start) == False:

            if Sjekking.string_er_float(svar_start) == True and float(svar_start) in range(2, 6):
                Brukere.logg_inn(svar_start) # logg inn for å gjøre alt fra valg 2 til 5 og deretter (når du har logget inn) er det if og elif statements som sjekker hvor du skal gå videre. pga. sikerhet må man først logge inn
                
            else:
                Operasjoner_felles.feilmelding() # feilmelding dersom du ikke gjorde et av stegene ovenfor

        else:
            Operasjoner_felles.feilmelding() # feilmelding dersom du ikke gjorde et av stegene ovenfor

start()
