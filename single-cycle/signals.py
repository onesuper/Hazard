
from utils import boolize

class Signals(object):
    def __init__(self, RegDst, ALUSrc, MemtoReg, RegWrite, MemRead, MemWrite, Branch, ALUOp1, ALUOp0):
        self.RegDst = RegDst
        self.ALUSrc = ALUSrc
        self.MemtoReg = MemtoReg
        self.RegWrite = RegWrite
        self.MemRead = MemRead
        self.MemWrite = MemWrite
        self.Branch = Branch
        self.ALUOp1 = ALUOp1
        self.ALUOp0 = ALUOp0

    def __repr__(self):
        group = ['RegDst: ' + boolize(self.RegDst),
                 'ALUSrc: ' + boolize(self.ALUSrc),
                 'MemtoReg: ' + boolize(self.MemtoReg),
                 'RegWrite: ' + boolize(self.RegWrite),
                 'MemRead: ' + boolize(self.MemRead),
                 'MemWrite: ' + boolize(self.MemWrite),
                 'Branch: ' + boolize(self.Branch),
                 'ALUOp1: ' + boolize(self.ALUOp1),
                 'ALUOp0: ' + boolize(self.ALUOp0)]
        return '\n'.join(group)

r = Signals(True, False, False, True, False, False, False, True, False)
lw = Signals(False, True, True, True, True, False, False, False, False)
sw = Signals(None, True, None, False, False, True, False, False, False)
beq = Signals(None, False, None, False, False, False, True, False, True)
    
