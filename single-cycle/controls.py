
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
        
        

