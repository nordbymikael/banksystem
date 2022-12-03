def spesielle_tegn (type_sjekk, string):
    spesielle_tegn = ["1234567890{}[]()<>\\/=~+-*%&,._!?\"'`´¨^@#¤§|$£", "{}[]()<>\\/=~+-*%&,._!?\"'`´¨^@#¤§|$£", "{}[]()<>\\/=~+-*%_!?^@#¤§|$£1234567890"]

    if type_sjekk == "alle tegn":
        return spesielle_tegn_loop(spesielle_tegn[0], string)
    elif type_sjekk == "alle tegn unntatt tall":
        return spesielle_tegn_loop(spesielle_tegn[1], string)
    elif type_sjekk == "alle tegn for adresser":
        return spesielle_tegn_loop(spesielle_tegn[2], string)

def spesielle_tegn_loop (spesielle_tegn, tekst): 
    for i in spesielle_tegn:
        if i in tekst:
            return True
    return False
