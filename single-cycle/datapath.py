
from alu import ALU
from instruction import Instruction
from controls import Control
from registers import Registers
from utils import sign_extends, mux, OR, Add, alu_control



class Datapath(object):

    def __init__(self, memory):
        self.memory = memory
        self.pc = memory.text_segment
        self.alu = ALU()
        self.registers = Registers()
        self.control = Control()
        self.cycle = 0

    def step(self):

        print 'pc: ' + str(hex(self.pc))
        print self.registers
        
        # fetch a word from memory, and make it an instruction
        inst = Instruction(self.memory.getWord(self.pc))
        print 'instructions: ' + str(inst)
        print inst.well()
        print inst.meaning()

        # read the ALU operators from registers ANYWAY
        reg_data1 = self.registers[inst.rs()]
        reg_data2 = self.registers[inst.rt()]
        print 'register read data 1: ' + str(reg_data1)
        print 'register read data 2: ' + str(reg_data2)
        
        # translate the opcode to control signal 
        signal = self.control.to_signal(inst)
        print signal

        # do everything in the serial code
        # ALU work
        self.alu.A = reg_data1
        self.alu.B = mux(signal.ALUSrc,
                    sign_extends(inst.address()),
                    reg_data2)
        print 'ALU A: ' + str(self.alu.A)
        print 'ALU B: ' + str(self.alu.B)

        alu_control_value = alu_control(signal.ALUOp1, signal.ALUOp0, inst.funct())
        print 'alu control value: ' + str(bin(alu_control_value))

        self.alu.work(alu_control_value)  # main work!
        ALU_result = self.alu.result
        print 'ALU result: ' + str(ALU_result)


        # read memory or not
        if signal.MemRead:
            memory_read_data = self.memory.getWord(ALU_result)

        # write memory or not
        if signal.MemWrite:
            memory.setWord(ALU_result, reg_data2)

        # write register or not
        if signal.RegWrite:
            registers[mux(signal.RegDst,
                          inst.rt(),
                          inst.rd())] = mux(singal.MemtoReg,
                                            memory_read_data,
                                            ALU_result)
                      
        # update pc to pc+4 or branch to another place
        pc = mux(OR(alu.Zero, signal.Branch), 
                 ADD(pc + 4, sign_extends(inst.address()) << 2),
                 pc + 4)
            

        self.cycle += 1
