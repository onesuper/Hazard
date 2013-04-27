
from alu import ALU
from instruction import Instruction
from controls import Control
from registers import Registers
from memory import Memory
from utils import sign_extend, mux, AND, Add, alu_control



class Datapath(object):

    def __init__(self,pc=0x00400000):
        self.memory = Memory()
        self.pc = pc
        self.alu = ALU()
        self.registers = Registers()
        self.control = Control()
        self.cycle = 0

    def step(self, Debug = ()):
    
        # fetch a word from memory, and make it an instruction
        inst = Instruction(self.memory.getWord(self.pc))
        if 'inst' in Debug:
            print inst


        # read the ALU operators from registers ANYWAY
        Read_data1 = self.registers[inst.rs()]
        Read_data2 = self.registers[inst.rt()]
        if 'Read data' in Debug:
            print "Read data 1: {0}".format(Read_data1)
            print "Read data 2: {0}".format(Read_data2)

        
        # translate the opcode to control signal 
        signal = self.control.to_signal(inst)
        if 'signal' in Debug:
            print signal


        # do everything in the serial code
        # ALU work
        self.alu.A = Read_data1
        self.alu.B = mux(signal.ALUSrc, sign_extend(inst.imm()), Read_data2)
        alu_control_value = alu_control(signal.ALUOp1, signal.ALUOp0, inst.funct())
        self.alu.work(alu_control_value)  # main work!
        ALU_result = self.alu.result

        if 'ALU control' in Debug:
            print  'ALU control: {0}'.format(bin(alu_control_value))

        if 'ALU' in Debug:
            print "ALU in1: {0}".format(self.alu.A)
            print "ALU in2: {0}".format(self.alu.B)
            print "ALU result: {0}".format(self.alu.result)
            print "ALU Zero: {0}".format(self.alu.Zero) 



        addr = ALU_result
            
        # read memory or not
        if signal.MemRead:
            Read_data = self.memory.getWord(addr)
            if 'Memory read' in Debug:
                print "Read MEM[{0}]: {1}".format(addr, Read_data)
        else:
            Read_data = None


        # write memory or not
        if signal.MemWrite:
            self.memory.setWord(addr, Read_data2)
            if 'Memory write' in Debug:
                print "MEM[{0}] = {1}".format(addr, Read_data2)


        # RegDst is used to choose a reg to write
        WriteRegister = mux(signal.RegDst, inst.rd(), inst.rt())
        
        # write register or not
        if signal.RegWrite:
            # MemtoReg is used to choose the value to write
            self.registers[WriteRegister] = mux(signal.MemtoReg, Read_data, ALU_result)
            if 'Register write' in Debug:
                print "REG[{0}] = {1}".format(WriteRegister, self.registers[WriteRegister])
                      
        # update pc to pc+4 or branch to another place
        mux4_result = mux(AND(self.alu.Zero, signal.Branch), 
                          Add(self.pc + 4, sign_extend(inst.imm()) << 2),
                          self.pc + 4)


        jump_target = (inst.target() << 2) | ((self.pc+4) & 0xf0000000)
        self.pc = mux(signal.Jump, jump_target, mux4_result)

        if 'pc' in Debug:
            print "next pc: {0:x}".format(self.pc) 

        if 'Reg' in Debug:
            print self.registers

        self.cycle += 1


      
