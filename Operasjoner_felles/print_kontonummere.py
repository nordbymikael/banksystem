def kontonummere_på_valgt_fødselsnummer (fødselsnummer): # printer ut alle kontonummere på valgt fødselsnummer (oppgitt i parameter)
    mycursor.execute(f"SELECT KONTONUMMER FROM KONTOER WHERE FØDSELSNUMMER = \"{fødselsnummer}\"")
    myresult = mycursor.fetchall()

    for x in myresult: # kaller legg til nuller funksjonen for hvert funnet kontonummer og printer ut hvert kontonummer som ble funnet
        legge_til_nuller(x[0], 2)
