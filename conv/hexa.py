def dec_to_hexa(aconv):
    if aconv == 0:
        return 0

    caracteres = "0123456789ABCDEF"
    resultat = ""

    while aconv > 0:
        reste = aconv%16
        resultat = caracteres[reste] + resultat
        aconv //= 16

    return resultat

def hexa_to_dec(aconv):
    if aconv == 0:
        return 0

    return int(aconv, 16)