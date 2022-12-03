def legge_til_nuller (kontonummer, antall_kontonummer): # legger til nuller til kontonummer
    nuller = 11 - len(str(kontonummer)) # definerer at nullene som skal legges til på starten er 11 stk - lengden av kontonummeret som ikke er 0
    melding = "" # definerer en tom melding som det skal legges til nuller på
    for i in range(nuller): 
        melding += "0" # legge til "0" i stringen "nuller" ganger
    melding += str(kontonummer) # meldingen har nuller i seg, den trenger bare å bli lagt til kontonummeret uten nuller
    
    if antall_kontonummer == 1:
        return melding # returnerer meldingen med kontonummeret med nuller
    elif antall_kontonummer == 2:
        print(melding) # denne legger til nummer til flere kontonummere fordi denne har ikke return, men print. return stopper en loop, til og med dersom den ikke er ferdig. med return printes derfor bare et kontonummer.
