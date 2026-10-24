# from binDec import bin_to_dec

def dec_to_duodec(aconv):
    if aconv == 0:
        return 0

    caracteres = "0123456789AB"
    resultat = ""

    while aconv > 0:
        reste = aconv%12
        resultat = caracteres[reste] + resultat #on inverse
        aconv //= 12

    return resultat

def duo_to_dec(aconv):
    if aconv == 0:
        return 0

    return int(aconv, 12)