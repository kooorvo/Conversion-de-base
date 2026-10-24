def dec_to_bin(aconv):
    conv = bin(aconv)
    return (conv.split("b")[1])

def bin_to_dec(aconv):
    return int(aconv, 2)