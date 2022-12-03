def pinkode_sjekk_om_riktig (fødselsnummer, pinkode):
    mycursor.execute(f"SELECT PINKODE FROM KUNDEINFO WHERE FØDSELSNUMMER = \"{fødselsnummer}\"") # spørring som finner pinkoden på fødslesnummeret som vi hentet fra parameter
    myresult = mycursor.fetchall() # setter sammen alle resultater som jeg fikk fra spørringen og returnerer en liste med tuples
    egentlig_resultat = myresult[0][0] # tar ut pinkoden fra tuple og liste

    if egentlig_resultat == pinkode:
        return True # returnere True dersom pinkoden som vi skrev og hentet fra parameter stemmer med den som står i tabellen
    else:
        return False # returnere False dersom pinkodene er annerledes
