def string_er_float (string): # prøver å gjøre om stringen som vi skrev til en float
    try: # prøve å gjøre den om til en flaot
        float(string)
    except ValueError:
        return False # returnere False dersom ikke hele stringen kan bli gjort om til float (vi får value error dersom dette skjer)
    return True # returnere True dersom hele stringen kan bli gjort om til float
