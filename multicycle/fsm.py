
from signals import Signal
from encoder import encode


def next_state(state, opcode):
    
    # fetch instruction
    if state == 0:
        return (1, Signal(MemRead=True, ALUSrcB=1, PCWrite=True))
    # decode/fetch register value
    elif state == 1:
        s = Signal(ALUSrcB=3)
        if opcode == encode('lw') or opcode == encode('sw'):
            return (2, s)
        elif opcode == encode('r'):
            return (6, s)
        elif opcode == encode('beq'):
            return (8, s)
        elif opcode == encode('j'):
            return (9, s)
        elif opcode == encode('addi'):
            return (12, s)
        else:
            # that should be replaced
            raise Exception('opcode err: {0}'.format(opcode))
    # calculate address
    elif state == 2:
        s = Signal(ALUSrcA=True, ALUSrcB=2)
        if opcode == encode('lw'):
            return(3, s)
        elif opcode == encode('sw'):
            return(5, s)
        else:
            pass # you can never get here
    # read memory
    elif state == 3:
        return (4, Signal(MemRead=True, IorD=True))
    # memory read(end)
    elif state == 4:
        return (0, Signal(RegDst=True, RegWrite=True, MemtoReg=True))
    # write memory
    elif state == 5:
        return (0, Signal(MemWrite=True, IorD=True))
    # execute
    elif state == 6:
        return (7, Signal(ALUSrcA=True, ALUOp=2))
    # R(end)
    elif state == 7:
        return (0, Signal(RegDst=True, RegWrite=True))
    # branch(end)
    elif state == 8:
        return (0, Signal(ALUSrcA=True, ALUOp=1, PCWriteCond=True, PCSource=1))
    # jump(end)
    elif state == 9:
        return (0, Signal(PCWrite=True, PCSource=2))
    # addi
    elif state == 12:
        pass
    else:
        raise Exception('No such state!!!')
