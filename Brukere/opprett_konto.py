def legge_til_kontoer (fødselsnummer): # legger til kontoer
    mycursor.execute(f"INSERT INTO KONTOER (FØDSELSNUMMER, SALDO) VALUES (\"{fødselsnummer}\", 0.00)") #legger til en konto med valgt fødselsnummer som hentes fra parameter
    mydb.commit()
    mycursor.execute(f"SELECT KONTONUMMER FROM KONTOER WHERE FØDSELSNUMMER = \"{fødselsnummer}\"") # spørring for kontonummer
    myresult = mycursor.fetchall()
    konto_som_brukes = myresult[-1][-1] # velger det siste kontonummeret som er på brukeren din
    print(f"Du har lagt til en ny konto til brukeren din.\nDenne har kontonummeret {legge_til_nuller(konto_som_brukes, 1)}") # varsler deg om kontonummeret til din nye bruker
