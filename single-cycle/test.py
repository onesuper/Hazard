

from executable import EXE
from datapath import Datapath


exe = EXE([1, 2], # data: 1, 2
          [0b10001100000010000000000000000000,  # lw $t(8), offset($s(0))
           0b10001100000010010000000000000001,  # lw st(9), offset($s(0))
          #0b100011ssssstttttiiiiiiiiiiiiiiii  
           0b00000001000010010101000000100000]  # add $d(10), $s(8), $t(9)
          #0b000000ssssstttttddddd00000100000
          #0b12345678123456781234567812345678
          )


datapath = Datapath()
datapath.load(exe)

datapath.step()
