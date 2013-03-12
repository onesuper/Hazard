
class Singals(object):
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



r = Singals(True, False, False, True, False, False, False, True, False)
lw = Signals(False, True, True, True, True, False, False, False, False)
sw = Signals(NULL, True, NULL, False, False, True, False, False, False)
beq = Signals(NULL, False, NULL, False, False, False, True, False, True)
    
