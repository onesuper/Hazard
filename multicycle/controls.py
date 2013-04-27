
from exception import ControlException
#from signals import r, lw, sw, beq, addi, j
from encoder import encode

# decode the opcode to an associated signal

class Control(object):

    def to_signal(self, instruction):
        if instruction.op() == encode('r'):
            return r
        elif instruction.op() == encode('lw'):
            return lw
        elif instruction.op() == encode('sw'):
            return sw
        elif instruction.op() == encode('beq'):
            return beq
        elif instruction.op() == encode('addi'):
            return addi
        elif instruction.op() == encode('j'):
            return j
        else:
            raise ControlException('the opcode cannot be translated into a valid signal')
        
        

