def fødselsnummer_sjekk_om_finnes (fødslesnummer):
    mycursor.execute(f"SELECT FØDSELSNUMMER FROM KUNDEINFO WHERE FØDSELSNUMMER = \"{fødslesnummer}\"") # jeg henter fødselsnummeret som jeg definerte i parameter og kjører en spørring som sjekker om fødselsnummeret er definert i KUNDEINFO tabellen
    myresult = mycursor.fetchall() # setter sammen alle resultater som jeg fikk fra spørringen og returnerer en liste med tuples

    if myresult == []:
        return False # returnerer False dersom fødselsnummeret ikke finnes i KUNDEINFO tabellen. dette trengs for å kontrollere at fødselsnummeret som vi skriver inn på f.eks. logg inn finnes i tabellen. dette trengs også for at nye brukere ikke kan bruke et allerede eksisterernde fødselsnummer på sin konto.
    else:
        return True # returnerer True dersom fødselsnummeret finnes i tabellen KUNDEINFO
