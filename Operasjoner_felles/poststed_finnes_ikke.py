

def poststed_finnes_ikke ():
    # du blir varslet om at poststedet ditt ikke ble funnet i databasen
    svar_opprett_bruker_poststed = input("\nDu fikk til å legge postnummer til den nye brukeren din, men vi fant ikke poststedet til postnummeret i vår database.\nVennligst skriv inn poststedet ditt (format: Flateby): ").capitalize()
    
    if spesielle_tegn("alle tegn", svar_opprett_bruker_poststed) == False and len(svar_opprett_bruker_poststed) in range(1, 256): # kontrollerer at formatet er gyldig
        hovedprogram.mycursor.execute(f"INSERT INTO POSTSTED (POSTNUMMER, POSTSTED) VALUES (\"{svar_opprett_bruker_postnummer}\", \"{svar_opprett_bruker_poststed}\")")
        mydb.commit()
    
    else:
        feilmelding()
