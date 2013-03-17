


table = {
    'r': 0,
    'addi': 0b001000,
    'addiu': 0b001001,
    'andi': 0b001100,
    'beq': 0b000100,
    'bgez': 0b000001,
    'bgezal': 0b000001,
    'bgtz': 0b000111,
    'blez': 0b000110,
    'bltz': 0b000001,
    'bltzal': 0b000001,
    'bne': 0b000101,
    'divu': 0b000000,
    'j': 0b000010,
    'jal': 0b000011,
    'lb': 0b100000,
    'lui': 0b001111,
    'lw': 0b100011,
    'ori': 0b001101,
    'sb': 0b101000,
    'slti': 0b001010,
    'sltiu': 0b001010,
    'sw': 0b101011,
    'xori': 0b001110,
}


# encode a name to a number
def encode(name):
    return table[name]

