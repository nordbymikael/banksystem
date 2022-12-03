import mysql.connector
import sys
import os
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


mydb = mysql.connector.connect(
  host="localhost",
  port =3306,
  user="root",
  password="root",
  database="banksystem"
)

mycursor = mydb.cursor()

def opprett_bruker ():
    global svar_opprett_bruker_fornavn # global på alle for at de skal kunne brukes senere i funksjonen som lagrer alt i MySQL databasen
    svar_opprett_bruker_fornavn = input("\nDu har begynt å opprette din konto.\nVennligst skriv ditt fornavn: ").capitalize() # capitalize() for at f.eks. mIKhaiL skal bli gjort om til stor forbokstav og resten små

    if spesielletegn.sjekk_string_for_spesielle_tegn("alle tegn", svar_opprett_bruker_fornavn) == False and len(svar_opprett_bruker_fornavn) in range(1, 256): # sjekke om fornavn har ingen tall og om lengden er gyldig for MySQL (max 255 tegn)
        global svar_opprett_bruker_etternavn
        svar_opprett_bruker_etternavn = input("\nVennligst skriv ditt etternavn: ").capitalize() # capitalize() samme grunn som fornavn

        if sjekk_string_for_spesielle_tegn("alle tegn", svar_opprett_bruker_etternavn) == False and len(svar_opprett_bruker_etternavn) in range(1, 256): # samme sjekk som fornavn
            global svar_opprett_bruker_fødselsnummer
            svar_opprett_bruker_fødselsnummer = input("\nVennligst skriv ditt fødselsnummer (format: 11 sifre): ")

            if svar_opprett_bruker_fødselsnummer.isdigit() == True and len(svar_opprett_bruker_fødselsnummer) == 11 and fødselsnummer_sjekk_om_finnes(svar_opprett_bruker_fødselsnummer) == False: # sjekke om hele fødselsnummer er tall og er 11 lang, + sjekke om den finnes fra før 
                global svar_opprett_bruker_postnummer
                svar_opprett_bruker_postnummer = input("\nVennligst skriv inn ditt postnummer (format: 4 sifre): ")

                if svar_opprett_bruker_postnummer.isdigit() == True and len(svar_opprett_bruker_postnummer) == 4 and poststed_sjekk_om_finnes(svar_opprett_bruker_postnummer) == False: # sjekke lengden til postnummer (4 sifre) + sjekk om hele er int + sjekk om poststed er definert for dette postnummeret
                    poststed_finnes_ikke() # dersom poststedet ikke er definert for postnummeret: si ifra til brukeren og definer
                    opprett_bruker_etter_poststed() # gå videre i oppretting av brukeren
                    
                elif svar_opprett_bruker_postnummer.isdigit() == True and len(svar_opprett_bruker_postnummer) == 4 and poststed_sjekk_om_finnes(svar_opprett_bruker_postnummer) == True: # dersom poststedet ble funnet
                    opprett_bruker_etter_poststed() # gå videre i oppretting av brukeren

                else:
                    feilmelding()

            else:
                feilmelding()

        else:
            feilmelding()
            
    else:
        feilmelding()

def opprett_bruker_etter_poststed ():
    global svar_opprett_bruker_gatenavn
    svar_opprett_bruker_gatenavn = input("\nVennligst skriv inn gatenavnet du bor på (format: Eksempelveien (bare bokstaver; ikke Eksempelveien 1 e.l.)): ").title() # title() for at alle ord skal få stor forbokstav

    if sjekk_string_for_spesielle_tegn("alle tegn for adresser", svar_opprett_bruker_gatenavn) == False and len(svar_opprett_bruker_gatenavn) in range(1, 256): # sjekk om inneholder spesielle tegn og tall, men sjekker ikke for ' og annet, + sjekk lengde 1-255
        global svar_opprett_bruker_husnummer
        svar_opprett_bruker_husnummer = input("\nVennligst skriv inn husnummeret ditt (format: 1 (bare tall; ikke 1a)): ")
        
        if svar_opprett_bruker_husnummer.isdigit() == True and len(svar_opprett_bruker_husnummer) in range(1, 256): # sjekke om hele er tall og sjekke lengden
            global svar_opprett_bruker_telefonnummer
            svar_opprett_bruker_telefonnummer = input("\nVennligst skriv inn ditt telefonnummer (format: 8 sammensatte sifre (ikke +47 på starten)): ")

            if svar_opprett_bruker_telefonnummer.isdigit() and len(svar_opprett_bruker_telefonnummer) == 8: # sjekke om hele er tall og sjekke at lengden er 8 sifre (tlf nummer)
                global svar_opprett_bruker_epostadresse
                svar_opprett_bruker_epostadresse = input("\nVennligst skriv inn din e-postadresse (format: eksempel@eksempel.eksempel (med @ og domene)): ")
                
                if "@" in svar_opprett_bruker_epostadresse and "." in svar_opprett_bruker_epostadresse: # sjekke om e-postadressen har @ og .
                    global svar_opprett_bruker_pinkode
                    svar_opprett_bruker_pinkode = input("\nVennligst skriv inn en pinkode for brukeren din (4 eller 6 sifre): ")

                    if svar_opprett_bruker_pinkode.isdigit() == True and len(svar_opprett_bruker_pinkode) in range(4, 8, 2): # sjekke om hele pinkoden er tall og sjekke om lengden er 4 eller 6 sifre (range(4, 8, 2) hopper over 2 for hver verdi)
                        # print under printer ut all informasjon som du skrev når du laget brukeren, slik at du kan kontrollere at du skrev alt riktig
                        print(f"\nDu har nesten opprettet brukeren din.\nBrukeren din har følgende informasjon:\nFornavn: {svar_opprett_bruker_fornavn}\nEtternavn: {svar_opprett_bruker_etternavn}\nFødselsnummer: {svar_opprett_bruker_fødselsnummer}\nPostnummer: {svar_opprett_bruker_postnummer}\nGatenavn: {svar_opprett_bruker_gatenavn}\nHusnummer: {svar_opprett_bruker_husnummer}\nTelefonnummer: {svar_opprett_bruker_telefonnummer}\nE-postadresse: {svar_opprett_bruker_epostadresse}\nPinkode: {svar_opprett_bruker_pinkode}")
                        svar_bekreft = input("\033[1mSkriv Ja\033[0m for å opprette brukeren med følgende informasjon, \033[1meller skriv alt mulig annet\033[0m for å avbryte: ").capitalize()
                        
                        if svar_bekreft == "Ja": # bekreftelse på at du skrev alt riktig
                            lagre_opprettet_bruker()
                            mycursor.execute(f"SELECT KONTONUMMER FROM KONTOER WHERE FØDSELSNUMMER = {svar_opprett_bruker_fødselsnummer}") # spørring som velger kontonummeret på valgt fødselsnummer
                            myresult = mycursor.fetchall()
                            print(f"\n\033[1mDu har nå opprettet din bruker!\033[0m\nKontoen \033[1m{legge_til_nuller(myresult[0][0], 1)} ble automatisk opprettet\033[0m for brukeren din.\nVi overfører deg til første valgmulighet for at du kan logge inn på kontoen din.")
                        
                        else:
                            print("\n\033[1mDu har avbrutt opprettingen av kontoen din.\nVennligst start på nytt eller ta andre valg.\033[0m")

                    else:
                        feilmelding()

            else:
                feilmelding()

        else:
            feilmelding()

    else:
        feilmelding()
