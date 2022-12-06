import os
import sys
sys.path.append(os.getcwd())
import mysqlconnector

def poststed_hent ():
    postnr = input() # skrive inn postnummer
    mysqlconnector.mycursor.execute(f"SELECT POSTSTED FROM POSTSTED WHERE POSTNUMMER = \"{postnr}\"") # jeg setter inn postnummeret som jeg definerte in i spørringen

    myresult = mysqlconnector.mycursor.fetchall()
    print(myresult[0][0]) # myresult er en liste som inneholder lister (som er cellene i tabellen). for at vi skal få printet ut bare poststedet (uten parenteser, komma og anførselstegn), så må vi printe ut det eneste resultatet (listen) som vi fikk fra spørringen og deretter printer jeg ut det eneste som er i den listen (stringen)
