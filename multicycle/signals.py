
from utils import boolize

class Signal(object):
    def __init__(self, RegDst=False, ALUSrcA=False, RegWrite=False, MemtoReg=False, MemRead=False, MemWrite=False, IorD=False, IRWrite=False, PCWrite=False, PCWriteCond=False, ALUOp=0, ALUSrcB=0, PCSource=0):
        self.RegDst = RegDst
        self.ALUSrcA = ALUSrcA
        self.RegWrite = RegWrite
        self.MemtoReg = MemtoReg
        self.MemRead = MemRead
        self.MemWrite = MemWrite
        self.IorD = IorD
        self.IRWrite = IRWrite
        self.PCWrite = PCWrite
        self.PCWriteCond = PCWriteCond

        # two bits
        self.ALUOp = ALUOp
        self.ALUSrcB = ALUSrcB
        self.PCSource = PCSource

        

    def __repr__(self):
        s = vars(self)
        # display the enabled signals
        return str([(k, s[k]) for k in s.keys() if s[k]])



