

# the register file


class Registers(object):
    
    def __init__(self):
        self.registers = [0] * 32  # 32 registers in tota


    def __setitem__(self, write_reg, write_data):        
        registers[write_reg] = write_data 

    def __getitem__(self, read_reg):
        return self.registers[read_reg]
