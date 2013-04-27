
# 16bit -> 32bit
def sign_extend(bits):
    return bits



# 2-way multiplexer
def mux(control, a, b):
    return a if control else b
    

def mux4(control, l):
    return l[control]



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


def alu_control(ALUOp, funct):
    if ALUOp == 0:
        return 0b0010
    elif ALUOp == 1:
        return 0b0110
    elif ALUOp == 2 and (funct & 0b1111) == 0b0000:
        return 0b0010
    elif ALUOp == 2 and (funct & 0b1111) == 0b0010:
        return 0b0110
    elif ALUOp == 2 and (funct & 0b1111) == 0b0100:
        return 0b0000
    elif ALUOp == 2 and (funct & 0b1111) == 0b0101:
        return 0b0001
    elif ALUOp == 2 and (funct & 0b1111) == 0b1010:
        return 0b0111
    else:
        from exception import ControlException
        raise ControlException('ALU control unknown')
        
        
