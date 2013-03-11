

class Instruction(object):
    def __init__(self, bits):
        self.bits = bits

    def op(self):
        return self.bits >> 26

    def rs(self):
        return (self.bits & 0x3e00000) >> 21

    def rt(self):
        return (self.bits & 0x1f0000) >> 16

    def rd(self):
        return (self.bits & 0xf800) >> 11 

    def shamt(self):
        return (self.bits & 0x7c0) >> 6

    def funct(self):
        return self.bits & 0x3f

    def address(self):
        return self.bits & 0xffff
