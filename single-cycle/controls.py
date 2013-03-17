
from exception import ControlException
from signals import r, lw, sw, beq, addi
from encoder import encode

class Control(object):

    def to_signal(self, intruction):
        if intruction.op() == encode('r'):
            return r
        elif intruction.op() == encode('lw'):
            return lw
        elif intruction.op() == encode('sw'):
            return sw
        elif intruction.op() == encode('beq'):
            return beq
        elif intruction.op() == encode('addi'):
            return addi
        else:
            raise ControlException('the opcode cannot be translated into a valid signal')
        
        

