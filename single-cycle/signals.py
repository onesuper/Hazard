
from utils import boolize

class Signal(object):
    def __init__(self, RegDst=False, ALUSrc=False, MemtoReg=False, RegWrite=False, MemRead=False, MemWrite=False, Branch=False, ALUOp1=False, ALUOp0=False, Jump=False):
        self.RegDst = RegDst
        self.ALUSrc = ALUSrc
        self.MemtoReg = MemtoReg
        self.RegWrite = RegWrite
        self.MemRead = MemRead
        self.MemWrite = MemWrite
        self.Branch = Branch
        self.ALUOp1 = ALUOp1
        self.ALUOp0 = ALUOp0
        self.Jump = Jump

    def __repr__(self):
        s = vars(self)
        # display the enabled signals
        return str([k for k in s.keys() if s[k]])

# None = we don't care that signal
r = Signal(RegDst=True, RegWrite=True, ALUOp1=True)
lw = Signal(ALUSrc=True, MemtoReg=True, RegWrite=True, MemRead=True)
sw = Signal(ALUSrc=True, MemWrite=True)
beq = Signal(Branch=True, ALUOp0=True)
addi = Signal(ALUSrc=True, RegWrite=True)
j = Signal(Jump=True)    
