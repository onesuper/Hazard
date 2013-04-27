

from exe import Exe
from datapath import Datapath
from lazy import addi, add, sub, lw, sw, and_, or_, beq, slt, j

exe = Exe()
exe.data_section = [77, 99]  # by word
exe.text_section = [addi('$t0', '$zero', 15),         #0x00400000
                    addi('$t1', '$zero', 12),
                    add('$t2', '$t0', '$t1'), #27
                    sub('$t3', '$t0', '$t1'),  #3
                    lw('$t4', '$gp', 0),
                    lw('$t5', '$gp', 4),
                    sw('$t2', '$gp', 8),     #27 in the data
                    and_('$t6', '$t1', '$t2'),
                    or_('$t7', '$t1', '$t2'), 
                    #beq('$s0', '$s1', -2), 
                    slt('$s1', '$t2', '$t3'),
                    slt('$s1', '$t3', '$t2'),
                    j(0x100000),
                    ]


d = Datapath()
d.memory.load(exe)



d.step(Debug=('fsm', 'pc', 'IR', 'cycle'))
d.step(Debug=('fsm', 'rs', 'rt', 'pc', 'cycle', 'ALUOut'))
d.step(Debug=('fsm', 'pc', 'cycle'))
d.step(Debug=('fsm', 'pc', 'cycle'))
d.step(Debug=('fsm', 'pc', 'cycle'))



print d.memory.show_data()
