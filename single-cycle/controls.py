
from exception import ControlException
from signals import r, lw, sw, beq


class Control(object):

  
    def to_signal(self, intruction):
        if intruction.op() == 0b000000:
            return r
        elif intruction.op() == 0b100011:
            return lw
        elif intruction.op() == 0b101011:
            return sw
        elif intruction.op() == 0b000100:
            return beq
        else:
            raise ControlException('the opcode cannot be translated into a valid signal')
        
        
class ALUControl(object):
    def work(self, ALUOp1, ALUOp0, funct):
        if not ALUOp1 and not ALUOp00:
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
            raise ControlException('the ALU control')
        
        
