def lagre_opprettet_bruker (): # lagrer brukeren som du opprettet og lager en konto for brukeren
    mycursor.execute(f"INSERT INTO KUNDEINFO (FØDSELSNUMMER, FORNAVN, ETTERNAVN, POSTNUMMER, GATENAVN, HUSNUMMER, TELEFONNUMMER, EPOSTADRESSE, PINKODE) VALUES (\"{svar_opprett_bruker_fødselsnummer}\", \"{svar_opprett_bruker_fornavn}\", \"{svar_opprett_bruker_etternavn}\", \"{svar_opprett_bruker_postnummer}\", \"{svar_opprett_bruker_gatenavn}\", {int(svar_opprett_bruker_husnummer)}, \"{svar_opprett_bruker_telefonnummer}\", \"{svar_opprett_bruker_epostadresse}\", \"{svar_opprett_bruker_pinkode}\")")
    mycursor.execute(f"INSERT INTO KONTOER (FØDSELSNUMMER, SALDO) VALUES (\"{svar_opprett_bruker_fødselsnummer}\", 0.00)") # legge til saldo 0
    mydb.commit()
