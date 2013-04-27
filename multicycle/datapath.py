
from alu import ALU
from instruction import Instruction
from controls import Control
from registers import Registers
from memory import Memory
from utils import sign_extend, mux, mux4, AND, OR, Add, alu_control
from fsm import next_state


class Datapath(object):

    def __init__(self,PC=0x00400000):
        self.memory = Memory()
        self.PC = PC
        self.alu = ALU()
        self.registers = Registers()
        self.control = Control()
        self.cycle = 0
        self.state = 0   # aka state register
        self.IR = 0
        self.A = 0  
        self.B = 0
        self.ALUOut = 0
        self.MemData = 0


    # in each step, cycle plus 1
    def step(self, Debug = ()):


        # current state and enabled signals depend on the state register
        # and the opcode in IR
        (self.state, signals) = next_state(self.state, Instruction(self.IR).op())
        if 'fsm' in Debug: print "@state: {0}".format(self.state)



        
        # ALU
        self.alu.A = mux(signals.ALUSrcA, self.A, self.PC)
        self.alu.B = mux4(signals.ALUSrcB, [self.B,
                                            4,
                                            sign_extend(Instruction(self.IR).imm()),
                                            sign_extend(Instruction(self.IR).imm() << 2)])

        self.alu.control = alu_control(signals.ALUOp, Instruction(self.IR).funct())
        self.alu.calculate()

        self.ALUOut = self.alu.result
        if 'ALUOut' in Debug: print "ALUOut: {0}".format(hex(self.ALUOut))


        # next PC
        if (signals.PCWriteCond and self.alu.Zero) or signals.PCWrite:
            self.PC = mux4(signals.PCSource, [self.alu.result,
                                              self.ALUOut,                                          
                                              Instruction(self.IR).target() << 2 + self.PC & 0xf0000000])



        # Intruction memory
        Address = mux(signals.IorD, self.ALUOut, self.PC)

        if signals.MemWrite:
            self.memory.setWord(Address, WriteData)
        if signals.MemRead:
            self.MemData = self.IR = self.memory.getWord(self.PC)
            if 'IR' in Debug: print Instruction(self.IR)
                
            

        self.A = self.registers[Instruction(self.IR).rs()]
        self.B = self.registers[Instruction(self.IR).rt()] 
        if 'rs' in Debug: print "A: {0}".format(self.A)
        if 'rt' in Debug: print "B: {0}".format(self.B)               
        

        if signals.RegWrite:
            self.registers[mux(signals.RegDst,
                               Instruction(self.IR).rt(),
                               Instruction(self.IR).rd())] = mux(signals.MemtoReg,
                                                                 self.MemData,
                                                                 self.ALUOut) 




        self.cycle += 1

        if 'pc' in Debug: print "next PC: {0}".format(hex(self.PC))
        if 'cycle' in Debug: print "cycle: {0}".format(self.cycle)

        if len(Debug): print "=========================="
