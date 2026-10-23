def dec_to_hexa(aconv:int):
    if aconv == 0:
        return 0

    caracteres = "0123456789ABCDEF"
    resultat = ""

    while aconv > 0:
        reste = aconv%16
        resultat = caracteres[reste] + resultat
        aconv //= 16

    return resultat