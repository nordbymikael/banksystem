import os
import sys
sys.path.append(os.getcwd())
import Operasjoner_felles
import Brukere
import Sjekking
import mysqlconnector

def sjekk_historikk_start (kontonummer): # funksjonen med valg for hvilken type historikk du vil sjekke for kontoen din
    global svar_sjekk_historikk # jeg gjorde variabelet globalt for at vi skal få mulighet til å sjekke om vi definerte dette variabelet som "4" i neste funksjon. dette trengs for å printe kontonummeret til brukeren som vi overførte penger til med nuller på starten.
    svar_sjekk_historikk = input("\nDu har begynt å sjekke historikken på kontoen din.\n\033[1mSkriv 1\033[0m for å sjekke historikk om saldo.\n\033[1mSkriv 2\033[0m for å sjekke historikk om inntak.\n\033[1mSkriv 3\033[0m for å sjekke historikk om uttak.\n\033[1mSkriv 4\033[0m for histotikk om sendte transaksjoner.\n")

    if svar_sjekk_historikk == "1": # vi kaller funksjonen og vi setter inn det vi har definert i parameter inn i funksjonen
        sjekk_historikk_prosess(kontonummer, "sjekk av saldo", "SALDO", ["Kontonummer", "Saldo", "Tidspunkt (åååå-mm-dd)"], "saldo", "sjekket saldoen på kontoen")

    elif svar_sjekk_historikk == "2": # vi kaller funksjonen og vi setter inn det vi har definert i parameter inn i funksjonen
        sjekk_historikk_prosess(kontonummer, "inntak", "INNTAK", ["Kontonummer", "Saldo før", "Saldo etter", "Inntak sum", "Tidspunkt (åååå-mm-dd)"], "inntak", "satt inn penger på kontoen")

    elif svar_sjekk_historikk == "3": # vi kaller funksjonen og vi setter inn det vi har definert i parameter inn i funksjonen
        sjekk_historikk_prosess(kontonummer, "uttak", "UTTAK", ["Kontonummer", "Saldo før", "Saldo etter", "Uttak sum", "Tidspunkt (åååå-mm-dd)"], "uttak", "tatt ut penger fra kontoen")

    elif svar_sjekk_historikk == "4": # vi kaller funksjonen og vi setter inn det vi har definert i parameter inn i funksjonen
        sjekk_historikk_prosess(kontonummer, "transaksjoner/overføringer", "TRANSAKSJONER", ["Kontonummer", "Sendt til kontonummer", "Saldo før", "Saldo etter", "Transaksjon sum", "Tidspunkt (åååå-mm-dd)"], "transaksnoner/overføringer", "overført penger til andre kontoer")

    else:
        Operasjoner_felles.feilmelding()

def sjekk_historikk_prosess (kontonummer, hva_som_sjekkes, tabellnavn, liste_med_meldinger, ingen_historikk_for, du_har_totalt_ganger):    
    print(f"Historikk {hva_som_sjekkes} for kontonummeret {kontonummer}:") # henter det som sjekkes fra parameter. det kan være for eksempel "sjekk av saldo" eller "inntak". kontonummeret er kontonummeret vi har logget oss inn på og dette hentes også fra parameter. vi får for eksempel outputen "Historikk saldo som sjekkes for kontonummeret 00000000001".
    mysqlconnector.mycursor.execute(f"SELECT COUNT(*) FROM HISTORIKK_{tabellnavn} WHERE KONTONUMMER = {kontonummer}") # deretter har vi en spørring som velger antallet (count) til all historikk på en av historikktabellene (hentes også fra parameter), der den første kolonnen i raden er kontoen vår. dersom vi sjekker historikk for saldo, så skriver et variabel fra parameter at vi sjekker tabellen HISTORIKK_{her er variabelet}, altså HISTORIKK_SALDO
    myresult = mysqlconnector.mycursor.fetchall()

    if myresult[0][0] != 0: # dersom vi ikke fikk resultater, så får vi en melding om at vi ikke fikk resultater for typen historikk som vi har valgt på kontoen vår (se else:). dersom resultater finnes (count telte ikke 0 men hva som helst annet, f.eks. 1 eller 30)
    
        for y in range(myresult[0][0]): # for loop som kjører like mange ganger som vi fikk resultater (like mange rader som ble funnet med vårt kontonummer). dersom vi fikk opp 10 resultater/rader på historikken, så kjører denne for loopen 10 ganger.
            mysqlconnector.mycursor.execute(f"SELECT * FROM HISTORIKK_{tabellnavn} WHERE KONTONUMMER = {kontonummer}") # denne spørringen velger alle rader fra tabellen med historikktypen som vi sjekker. tabellnavn og kontonummer hentes fra parameter. denne spørringen velger ikke antallet rader med vårt kontonummer, men velger alt i alle radene med vårt kontonummer.
            myresult = mysqlconnector.mycursor.fetchall()
            i = 0 # tilbakestiller i tilbake til 0 når for loopen inne i denne for loopen er ferdig. 0 er den første plassen i en liste. derfor starter vi med 0. neste for loop stoppes av seg selv, når den er ferdig med å gjøre en operasjon med siste plass i listen/raden som loopen går gjennom.
            
            for x in myresult[y]: # hver plass/kolonne (x) i hver liste/rad fra myresult[y]. myresult er en tuple med lister, og disse listene er radene som vi fikk fra spørringen. y er derimot en variabel som blir definert av den første for loopen. dersom den kjører for eksmepel 5 ganger, så endrer den verdien til y for hver gang den kjører. for hver gang den kjører, så endres verdien f.eks. fra 0 til 4 dersom loopen kjører 5 ganger. dette gir oss muligheten til å fjøre ting for neste liste/rad i myresult hver gang den første for loopen kjører på nytt. y starter fra 0.
                
                if i == 0: # dersom i er 0 så printer for loopen den første plassen i raden. det er alltid kontonummeret. dette kontonummeret printes uten nuller på starten, dersom vi ikke bruker "legge til nuller" funksjonen
                    print(f"\n{liste_med_meldinger[i]}: {Operasjoner_felles.legge_til_nuller(x, 1)}") # legger til nuller på første plass i raden fra spørringen (kontonummeret)
                    i += 1 # når if statement er ferdig, så går den ikke videre til neste elif og else statements, men den går videre under sin if statement. derfor må hver if/elif/else statement legge til 1 til i, fordi de går ikke tilbake. dersom jeg ikke hadde endret på i, så hadde ikke vi gått over til neste ting som skal printes fra listen som vi definerte i parameter, og vi hadde for eksempel fått opp kontonummer to eller flere ganger på rad. derfor adderer jeg 1 til i. dette gjelder for alle neste if/elif/else statements

                elif i == 1 and svar_sjekk_historikk == "4": # dersom vi valgte å se historikk for transaksjon, så har vi to kontonummere. det andre står på andre plass (1) og vil ikke få nuller på starten uten at vi sier at den skal også ha nuller på starten.
                    print(f"{liste_med_meldinger[i]}: {Operasjoner_felles.legge_til_nuller(x, 1)}") # legger til nuller på andre plass i raden fra spørringen (kontonummeret vi overførte penger til) dersom vi valgte historikk for transaksjoner.
                    i += 1

                else:
                    print(f"{liste_med_meldinger[i]}: {x}") # dersom vår plass i listen ikke er på et kontonummer, så printer vi bare plassen fra raden i tabellen, uten å legge til 0. foran kommer alltid plass i fra listen med alle kolonner som vi har i tabellen vi valgte.
                    i += 1

        mysqlconnector.mycursor.execute(f"SELECT COUNT(*) FROM HISTORIKK_{tabellnavn} WHERE KONTONUMMER = {kontonummer}") # samme linje som linje 502
        myresult = mysqlconnector.mycursor.fetchall()
        print(f"\nDu har totalt {du_har_totalt_ganger} {myresult[0][0]} ganger.") # når vi fikk opp alle resultatene, så får vi opp en oppsummering som sier hvor mange ganger vi har gjennomført en operasjon. operasjonstypen hentes fra parameter, og myresult[0][0] hentes fra spørringen som er 2 linjer tidligere (count(*) teller alle rader som ble funnet)
    
    else: # her er meldingen jeg skrev om i "if myresult[0][0] != 0". denne henter definerete variabler fra parameter og skriver inn f.eks. "Denne kontoen (00000000001) har ingen historikk for saldo"
        print(f"\nDenne kontoen ({kontonummer}) har ingen historikk for {ingen_historikk_for}.")
