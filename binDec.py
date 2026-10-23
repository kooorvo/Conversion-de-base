def dec_to_bin(aconv:int):
    conv = bin(aconv)
    print(conv.split("b")[1])

def bin_to_dec(aconv):
    return int(aconv, 2)