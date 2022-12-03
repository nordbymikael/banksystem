def personopplysninger_om_deg (fødselsnummer, kontonummer): # printe personopplysninger
    mycursor.execute(f"SELECT KUNDEINFO.* FROM KONTOER INNER JOIN KUNDEINFO ON KONTOER.FØDSELSNUMMER = KUNDEINFO.FØDSELSNUMMER WHERE KONTOER.FØDSELSNUMMER = {fødselsnummer} AND KONTOER.KONTONUMMER = {kontonummer}")
    myresult = mycursor.fetchall()
    liste_med_meldinger = ["Fødselsnummer", "Fornavn", "Etternavn", "Postnummer", "Poststed", "Gatenavn", "Husnummer", "Telefonnummer", "E-postadresse"]
    i = 0
    for x in myresult[0]:
        print(f"{liste_med_meldinger[i]}: {x}")
        i += 1

        if i == 4:
            mycursor.execute(f"SELECT POSTSTED FROM POSTSTED WHERE POSTNUMMER = {myresult[0][3]}")
            myresult = mycursor.fetchall()
            print(f"{liste_med_meldinger[i]}: {myresult[0][0]}")
            i += 1
        elif i == 9:
            break
