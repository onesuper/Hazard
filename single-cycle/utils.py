
# 16bit -> 32bit
def sign_extend(bits):
    if bits & 0x8000:   # [16] is 1
        return bits | 0xffff0000
    else:
        return bits



# 2-way multiplexer
def mux(control, a, b):
    return a if control else b
    


def AND(a, b):
    return a and b


def OR(a, b):
    return a or b


def Add(A, B):
    return A+B

def boolize(b):
    if b == True: return '1'
    elif b == False: return '0'
    else: return 'x' 


def alu_control(ALUOp1, ALUOp0, funct):
    if not ALUOp1 and not ALUOp0:
        return 0b0010
    elif ALUOp0:
        return 0b0110
    elif ALUOp1 and (funct & 0b1111) == 0b0000:
        return 0b0010
    elif ALUOp1 and (funct & 0b1111) == 0b0010:
        return 0b0110
    elif ALUOp1 and (funct & 0b1111) == 0b0100:
        return 0b0000
    elif ALUOp1 and (funct & 0b1111) == 0b0101:
        return 0b0001
    elif ALUOp1 and (funct & 0b1111) == 0b1010:
        return 0b0111
    else:
        from exception import ControlException
        raise ControlException('ALU control unknown')
        
        
