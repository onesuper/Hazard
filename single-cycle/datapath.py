
from instruction import Instruction
from controls import Control, ALUControl
from regester import Registers
from memory import Memory
from alu import ALU
from utiles import sign_extends, mux, OR, Add

class Datapath(object):

    def __init__(self, memory):
        self.memory = memory
        self.pc = memory.text_segment()
        self.alu = ALU()
        self.registers = Registers()
        self.control = Control()
        self.alu_control = ALUControl()
        self.cycle = 0

    def step(self):
        # fetch a word from memory, and make it an instruction
        inst = Instruction(self.memory.getWord(self.pc))

        # read the ALU operators from registers ANYWAY
        reg_data1 = registers[inst.rs()]
        reg_data2 = registers[inst.rt()]
        
        # translate the opcode to control signal 
        signal = self.control.to_signal(inst)

        # do everything in the serial code        
        # ALU work
        alu.A = reg_data1
        alu.B = mux(singal.ALUSrc,
                    sign_extends(inst.address()),
                    reg_data2)
        result_from_ALU = alu.work(alu_control(signal.ALUOp1,
                                               signal.ALUOp0,
                                               inst.funct()))

        # read memory or not
        if signal.MemRead:
            result_from_memory = memory.getWord(result_from_ALU)

        # write memory or not
        if signal.MemWrite:
            memory.setWord(result_from_ALU, reg_data2)

        # write register or not
        if signal.RegWrite:
            registers[mux(signal.RegDst,
                          inst.rt(),
                          inst.rd()] 
                      = mux(singal.MemtoReg,
                            result_from_memory,
                            result_from_ALU))
                      
        # update pc to pc+4 or branch to another place
        pc = mux(OR(alu.Zero, signal.Branch), 
                 ADD(pc + 4, sign_extends(inst.address()) << 2),
                 pc + 4)
            

        self.cycle += 1
