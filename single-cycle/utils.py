
# 16bit -> 32bit
def sign_extends(bits):
    if bits & 0x8000:   # [16] is 1
        return bits | 0xffff0000
    else:
        return bits



# 2-way multiplexer
def mux(control, a, b):
    return a if control else return b
    


def AND(a, b):
    return a and b


def OR(a, b):
    return a or b


def Add(A, B):
    return A+B
