
from exception import ALUException

class ALU(object):
    def __init__(self):
        self.result, self.A, self.B = 0, 0, 0
        self.Zero = False
        
        
    def work(self, control):
        
        # set result
        if control == 0b0000:
            self.result = self.A and self.B
        elif control == 0b0001:
            self.result =  self.A or self.B
        elif control == 0b0010:
            self.result = self.A + self.B
        elif control == 0b0110:
            self.result = self.A - self.B
        elif control == 0b0111:
            if self.A < self.B: self.Zero = True
        elif control == 0b1100:
            self.result = self.A ^ self.B
        else: 
            raise ALUException('the ALU control code cannot be translated into a valid behavior')
        
        # set zero according to result
        self.Zero = (self.result == 0)



