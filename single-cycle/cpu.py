
from control import Control
from instruction import Instruction
from memory import Memory




class CPU(object):

    # R-type instructions including add, sub, and, slt
    R = Control(True, False, False, True, False, False, False, True, False)
    lw = Control(False, True, True, True, True, False, False, False, False)
    sw = Control(NULL, True, NULL, False, False, True, False, False, False)
    beq = Control(NULL, False, NULL, False, False, False, True, False, True)

    def __init__(self):
        self.memory = Memory()
        self.pc = self.memory.text_segment
        self.cycle = 0
        self.registers = [0] * 32


    def step(self):
        inst = Instruction(self.memory.getWord(self.pc))
        self.cycle += 1
        
