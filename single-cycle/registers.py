

# the register file


class Registers(object):
    
    def __init__(self):
        self.registers = [0] * 32  # 32 registers in tota


    def __setitem__(self, write_reg, write_data):        
        registers[write_reg] = write_data 

    def __getitem__(self, read_reg):
        return self.registers[read_reg]

    def __repr__(self):
        group = ['$zero: ' + str(self.registers[0]),
                 '$at:' + str(self.registers[1]),
                 '$v0-$v1: ' + str(self.registers[2:4]),
                 '$a0-$a3: ' + str(self.registers[4:8]),
                 '$t0-$t7: ' + str(self.registers[8:16]),
                 '$s0-$s7: ' + str(self.registers[16:24]),
                 '$t8-$t9: ' + str(self.registers[24:26]),
                 '$k0-$k1: ' + str(self.registers[26:28]),
                 '$gp: ' + str(self.registers[28]) +
                 '  $sp:' + str(self.registers[29]) +
                 '  $fp: ' + str(self.registers[30]) +
                 '  $ra: ' + str(self.registers[31])]
        return '\n'.join(group)
