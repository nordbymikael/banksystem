import os
import sys
sys.path.append(os.getcwd())
import Operasjoner_felles
import Brukere
import Sjekking
import mysqlconnector

def poststed_finnes_ikke (svar_opprett_bruker_postnummer):
    # du blir varslet om at poststedet ditt ikke ble funnet i databasen
    svar_opprett_bruker_poststed = input("\nDu fikk til å legge postnummer til den nye brukeren din, men vi fant ikke poststedet til postnummeret i vår database.\nVennligst skriv inn poststedet ditt (format: Flateby): ").capitalize()
    
    if Sjekking.spesielle_tegn("alle tegn", svar_opprett_bruker_poststed) == False and len(svar_opprett_bruker_poststed) in range(1, 256): # kontrollerer at formatet er gyldig
        mysqlconnector.mycursor.execute(f"INSERT INTO POSTSTED (POSTNUMMER, POSTSTED) VALUES (\"{svar_opprett_bruker_postnummer}\", \"{svar_opprett_bruker_poststed}\")")
        mysqlconnector.mydb.commit()
    
    else:
        Operasjoner_felles.feilmelding()
