

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

    def address(self):   # 16-bit address for beq... 
        return self.bits & 0xffff

    def address2(self):  # 26-bit address for j...
        return self.bits & 0x08000000

    def _ld(self):
        label = ['op', 'rs', 'rt', 'address']
        group = [str(self.op()), str(self.rs()), str(self.rt()), str(self.address())]
        return '\t|'.join(label) + '\n' + '\t|'.join(group)

    def _r(self):
        return '[  ' + str(self.op()) + '  ][  ' + str(self.rs()) + '  ][  ' + str(self.rt()) + '  ][  ' + str(self.rd()) + '  ][  ' + str(self.shamt()) + '  ][  ' + str(self.funct()) + '  ]'

    def __str__(self):
        return str(bin(self.bits))
    

    def well(self):
        if self.op() == 0:  # r-type
            return self._r()
        elif self.op() == 35: # w
            return self._ld()
        elif self.op() == 43:  
            return self._ld()
        else:
            return bin(self.bits)


    def meaning(self):
        if self.op() == 0:  # r-type
            return 
        elif self.op() == 35:  #lw
            return '${0} = MEM[${1} + {2}'.format(self.rt(), self.rs(), self.address())
        elif self.op() == 43:  
            return self.ld()
        else:
            return bin(self.bits)
